import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- 1. CONFIGURAÇÃO DA CHAVE DE API DA OPENAI ---
api_key = "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" 

os.environ["OPENAI_API_KEY"] = api_key


# --- 2. CARREGAR O BANCO DE DADOS VETORIAL JÁ EXISTENTE ---
db_path = "./chroma_db_sem_duplicidade"
embeddings = OpenAIEmbeddings()

if not os.path.exists(db_path):
    print(f"ERRO: O diretório do banco de dados '{db_path}' não foi encontrado.")
    print("Você precisa executar o script 'rag.py' completo (versão limpa) pelo menos uma vez.")
    exit()

print(f"Carregando banco de dados vetorial de '{db_path}'...")
db = Chroma(persist_directory=db_path, embedding_function=embeddings)
print("Banco de dados carregado com sucesso.")


# --- 3. CRIAR O SISTEMA DE BUSCA E O CHATBOT ---
retriever = db.as_retriever(search_kwargs={"k": 10}) # Aumentamos o 'k' para buscar mais contexto
llm = OpenAI(temperature=0)
prompt_template = """
Use o contexto a seguir para responder a pergunta de forma clara e concisa.
Se a informação não estiver no contexto, diga que não encontrou dados para responder.

Contexto:
{context}

Pergunta: {question}
Resposta útil em português:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever,
    return_source_documents=False, # Não precisamos ver os documentos fonte no teste
    chain_type_kwargs={"prompt": PROMPT}
)
print("\nSistema RAG pronto para iniciar os testes!")


# --- 4. LISTA DE PERGUNTAS PARA O TESTE AUTOMATIZADO ---
lista_de_perguntas = [
    # Testes de Recuperação Simples
    "Qual o faturamento anual da empresa CNPJ_00001?",
    "Qual o momento de vida da empresa CNPJ_00010?",
    
    # Testes de Ranking e Ordenação
    "Quais são as 5 empresas com o maior faturamento anual? Liste o CNPJ e o valor.",
    "Quais são as 3 empresas com o menor saldo em conta? Liste o CNPJ e o saldo.",
    
    # Testes de Filtragem com Condição Única
    "Liste 3 empresas que estão no momento de vida 'Expansão'.",
    "Quantas empresas estão na fase de 'Declínio'?",
    
    # Testes de Filtragem com Múltiplas Condições
    "Existe alguma empresa em 'Maturidade' com faturamento anual superior a 15 milhões de reais?",
    "Liste empresas do setor de 'Cultivo de soja' que estão no momento de vida 'Maturidade'.",
    "Qual empresa em fase de 'Início' teve o maior volume total recebido?",
    
    # Testes de Relação (Pagamentos vs. Recebimentos)
    "Liste duas empresas cujo total pago foi significativamente maior que o total recebido.",
    "Existe alguma empresa que não registrou pagamentos mas teve recebimentos?"
]

print(f"\n--- INICIANDO BATERIA DE {len(lista_de_perguntas)} TESTES ---")

# --- 5. EXECUTAR E IMPRIMIR OS RESULTADOS ---
for i, pergunta in enumerate(lista_de_perguntas):
    print(f"\n[Teste {i+1}/{len(lista_de_perguntas)}]")
    print(f"Pergunta: {pergunta}")
    
    try:
        resultado = qa_chain.invoke({"query": pergunta})
        print("Resposta da IA:")
        # Adiciona um pequeno recuo para facilitar a leitura da resposta
        print(f"  -> {resultado['result'].strip()}") 
    except Exception as e:
        print(f"Ocorreu um erro ao processar esta pergunta: {e}")

print("\n--- BATERIA DE TESTES CONCLUÍDA ---")