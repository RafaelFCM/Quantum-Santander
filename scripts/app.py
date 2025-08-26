from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

# --- Importações do RAG e Grafo ---
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import networkx as nx
from pyvis.network import Network
import tempfile

# =====================================================================================
# CONFIGURAÇÕES PRINCIPAIS - EDITE AQUI
# =====================================================================================

# Coloque o nome EXATO da sua pasta do Chroma DB aqui.
CHROMA_DB_DIRECTORY = "chroma_db_sem_duplicidade" # <--- USE O NOME QUE VOCÊ CRIOU

# Insira sua chave de API da OpenAI aqui
OPENAI_API_KEY = "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"

# =====================================================================================
# INICIALIZAÇÃO E CARREGAMENTO DE DADOS
# =====================================================================================

app = Flask(__name__)
CORS(app)

# --- Carregar Dados ---
try:
    df_analitico = pd.read_csv('../data/Base_Analitica_PJ.csv', delimiter=';')
    df_transacoes = pd.read_csv('../data/Base 2 - Transacoes.csv', delimiter=';')
    
    print("Bases de dados carregadas com sucesso.")
except FileNotFoundError as e:
    print(f"ERRO CRÍTICO: Arquivo não encontrado - {e}.")
    df_analitico = pd.DataFrame()
    df_transacoes = pd.DataFrame()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
qa_chain = None

if OPENAI_API_KEY != "SUA_CHAVE_API_AQUI" and os.path.exists(f"./{CHROMA_DB_DIRECTORY}"):
    try:
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory=f"./{CHROMA_DB_DIRECTORY}", embedding_function=embeddings)
        retriever = db.as_retriever()
        llm = OpenAI(temperature=0.5, model_name="gpt-3.5-turbo-instruct") # Usando um modelo mais robusto para análise
        prompt_template = "Contexto: {context}\nPergunta: {question}\nResposta útil em português:"
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, chain_type_kwargs={"prompt": PROMPT})
        print("--> SUCESSO: Sistema RAG carregado e pronto para uso.")
    except Exception as e:
        print(f"--> ERRO ao carregar sistema RAG: {e}")
else:
    print("--> AVISO: Sistema RAG não foi carregado.")

# =====================================================================================
# API ENDPOINTS
# =====================================================================================

# ... [Endpoints antigos continuam aqui] ...
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(df_analitico['ID'].unique().tolist()) if not df_analitico.empty else (jsonify({"erro": "Dados não carregados"}), 500)

@app.route('/api/cliente/<string:cnpj>', methods=['GET'])
def get_dados_cliente(cnpj):
    if not df_analitico.empty:
        dados = df_analitico[df_analitico['ID'] == cnpj]
        return jsonify(dados.to_dict(orient='records')[0]) if not dados.empty else (jsonify({"erro": "Cliente não encontrado"}), 404)
    return jsonify({"erro": "Dados não carregados"}), 500

@app.route('/api/rag/ask', methods=['POST'])
def ask_rag():
    if not qa_chain: return jsonify({"erro": "Sistema RAG não está disponível"}), 503
    pergunta = request.json.get('pergunta')
    if not pergunta: return jsonify({"erro": "Nenhuma pergunta fornecida"}), 400
    try:
        resultado = qa_chain.invoke({"query": pergunta})
        return jsonify({"resposta": resultado['result']})
    except Exception as e: return jsonify({"erro": f"Erro ao processar a pergunta: {e}"}), 500

@app.route('/api/network_graph/<string:cnpj>', methods=['GET'])
def get_network_graph(cnpj):
    if df_transacoes.empty: return "<h4>Dados de transações não carregados.</h4>", 500
    # ... [código do grafo continua o mesmo] ...
    transacoes_empresa = df_transacoes[(df_transacoes['ID_PGTO'] == cnpj) | (df_transacoes['ID_RCBE'] == cnpj)].head(50)
    if transacoes_empresa.empty: return "<h4>Nenhuma transação encontrada.</h4>", 200
    mapeamento_momento_vida = df_analitico.set_index('ID')['MOMENTO_VIDA'].to_dict()
    cores_map = {'Início': '#3498db', 'Expansão': '#2ecc71', 'Maturidade': '#f1c40f', 'Declínio': '#e74c3c'}
    G = nx.from_pandas_edgelist(transacoes_empresa, 'ID_PGTO', 'ID_RCBE', ['VL'], create_using=nx.DiGraph())
    net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    for node in G.nodes():
        momento = mapeamento_momento_vida.get(node, 'Não definido')
        cor = cores_map.get(momento, '#95a5a6')
        net.add_node(node, label=node, title=f"Momento de Vida: {momento}", color=cor)
    for source, target, data in G.edges(data=True):
        valor_int = int(data['VL'])
        net.add_edge(source, target, value=valor_int / 100000, title=f"Valor: R$ {valor_int:,}")
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.html', encoding='utf-8') as tmp:
        net.save_graph(tmp.name)
        tmp.seek(0)
        html_content = tmp.read()
    os.remove(tmp.name)
    return html_content, 200, {'Content-Type': 'text/html'}


# --- NOVO ENDPOINT PARA VISÃO GLOBAL ---
@app.route('/api/global_insights', methods=['GET'])
def get_global_insights():
    if df_analitico.empty: return jsonify({"erro": "Dados não carregados"}), 500
    
    dist_momento_vida = df_analitico['MOMENTO_VIDA'].value_counts().to_dict()
    top_5_setores = df_analitico['DS_CNAE'].value_counts().nlargest(5).to_dict()

    return jsonify({
        'distribuicao_vida': {'labels': list(dist_momento_vida.keys()), 'data': list(dist_momento_vida.values())},
        'top_setores': {'labels': list(top_5_setores.keys()), 'data': list(top_5_setores.values())}
    })

# --- NOVO ENDPOINT PARA ANÁLISE DE CRÉDITO COM IA ---
@app.route('/api/credit_analysis/<string:cnpj>', methods=['GET'])
def get_credit_analysis(cnpj):
    if not qa_chain: return jsonify({"analise": "Sistema de IA não disponível."}), 503
    
    # Coleta de dados
    cliente_data = df_analitico[df_analitico['ID'] == cnpj].to_dict(orient='records')[0]
    
    # Prompt estruturado para a IA
    prompt = f"""
    Você é um analista de crédito sênior do Banco Santander. Sua tarefa é avaliar o risco de conceder um empréstimo para o cliente a seguir.
    Baseie sua análise exclusivamente nos dados fornecidos, focando em estabilidade, crescimento e fluxo de caixa.

    **DADOS DO CLIENTE:**
    - **CNPJ:** {cliente_data['ID']}
    - **Faturamento Anual:** R$ {cliente_data['VL_FATU']:,}
    - **Saldo em Conta (última referência):** R$ {cliente_data['VL_SLDO']:,}
    - **Momento de Vida da Empresa:** {cliente_data['MOMENTO_VIDA']} (Idade: {cliente_data['IDADE_ANOS']} anos)
    - **Setor (CNAE):** {cliente_data['DS_CNAE']}
    - **Total Recebido em Transações:** R$ {cliente_data['VL_TOTAL_RECEBIDO']:,}
    - **Total Pago em Transações:** R$ {cliente_data['VL_TOTAL_PAGO']:,}

    **SUA ANÁLISE:**
    Com base em tudo isso, forneça uma análise concisa em 3 seções, usando tags HTML <p>, <strong> e <ul><li> para formatação:
    1. **Recomendação e Risco:** (Ex: Recomendação Favorável com Risco Baixo, Recomendação Cautelosa com Risco Moderado, etc.)
    2. **Pontos Positivos (Prós):** (Liste 2 a 3 pontos fortes em formato de lista)
    3. **Pontos de Atenção (Contras/Riscos):** (Liste 2 a 3 pontos de atenção em formato de lista)
    """
    
    try:
        resultado = qa_chain.invoke({"query": prompt})
        return jsonify({"analise": resultado['result']})
    except Exception as e:
        return jsonify({"analise": f"Ocorreu um erro ao gerar a análise: {e}"}), 500


# --- Função principal para rodar o servidor ---
if __name__ == '__main__':
    app.run(debug=True)