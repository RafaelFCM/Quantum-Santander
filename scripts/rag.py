import pandas as pd
import os
import time # Importamos a biblioteca time
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DataFrameLoader
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- 1. CONFIGURAÇÃO DA CHAVE DE API DA OPENAI ---
api_key = "" 

os.environ["OPENAI_API_KEY"] = api_key

# --- 2. CARREGAR A BASE DE DADOS ANALÍTICA ---
try:
    df_analitico = pd.read_csv('../data/Base_Analitica_PJ_Versao_final.csv', delimiter=';')
    print("Base analítica 'Base_Analitica_PJ_Versao_final.csv' carregada com sucesso.")
except FileNotFoundError:
    print("Erro: O arquivo 'Base_Analitica_PJ_Versao_final.csv' não foi encontrado.")
    exit()

df_analitico['texto_empresa'] = df_analitico.apply(
    lambda row: f"A empresa com ID {row['ID']} tem faturamento anual de {row.get('VL_FATU', 0):.2f} reais, "
                f"saldo em conta de {row.get('VL_SLDO', 0):.2f} reais, foi aberta em {row.get('DT_ABRT', 'N/A')} "
                f"e está no momento de vida '{row.get('MOMENTO_VIDA', 'N/A')}'. "
                f"O total recebido foi {row.get('VL_TOTAL_RECEBIDO', 0):.2f} e o total pago foi {row.get('VL_TOTAL_PAGO', 0):.2f}.",
    axis=1
)

# --- 3. PREPARAR OS DOCUMENTOS PARA O LANGCHAIN ---
loader = DataFrameLoader(df_analitico, page_content_column='texto_empresa')
documentos = loader.load()
print(f"\n{len(documentos)} documentos foram criados (1 por empresa).")

# --- 4. CRIAR A BASE DE DADOS VETORIAL (ChromaDB) EM LOTES ---
print("\nIniciando a criação do banco de dados vetorial em lotes...")
embeddings = OpenAIEmbeddings()
db_path = "./chroma_db_sem_duplicidade"
batch_size = 1000 # Definimos o tamanho do lote

# Aponta para o diretório e cria o cliente Chroma
db = Chroma(persist_directory=db_path, embedding_function=embeddings)

# Itera sobre os documentos em lotes
for i in range(0, len(documentos), batch_size):
    lote = documentos[i:i + batch_size]
    
    # Extrai os textos e metadados do lote de documentos
    textos_lote = [doc.page_content for doc in lote]
    metadados_lote = [doc.metadata for doc in lote]
    
    # Adiciona o lote ao ChromaDB
    db.add_texts(texts=textos_lote, metadatas=metadados_lote)
    
    print(f"  - Lote de {len(lote)} documentos ({i+len(lote)} de {len(documentos)}) processado.")
    time.sleep(1) # Pequena pausa para não sobrecarregar a API

# Persiste o banco de dados em disco
db.persist()
print("\nBanco de dados vetorial criado e salvo com sucesso em './chroma_db_sem_duplicidade'.")

# --- 5. CRIAR O SISTEMA DE BUSCA E O CHATBOT ---
retriever = db.as_retriever(search_kwargs={"k": 5})
llm = OpenAI(temperature=0)
prompt_template = """
Use o contexto a seguir para responder a pergunta no final.
Se você não sabe a resposta, apenas diga que não sabe.

{context}

Pergunta: {question}
Resposta útil em português:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever,
    return_source_documents=True, chain_type_kwargs={"prompt": PROMPT}
)
print("\nSistema RAG pronto para receber perguntas!")

# --- 6. FAZER PERGUNTAS AO SISTEMA ---
pergunta1 = "Quais são as 3 empresas com maior faturamento anual?"
pergunta2 = "Existe alguma empresa em fase de 'Expansão' que tenha pago mais de 4 milhões?"
pergunta3 = "Liste as empresas que estão no momento de vida de 'Declínio' e mostre seus faturamentos."

for i, pergunta in enumerate([pergunta1, pergunta2, pergunta3]):
    print(f"\n--- Processando Pergunta {i+1}: {pergunta} ---")
    resultado = qa_chain.invoke({"query": pergunta})
    print("\nResposta Gerada:")
    print(resultado["result"])