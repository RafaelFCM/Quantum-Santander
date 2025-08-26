# Passo 4: Análise de Cadeias de Valor com Grafos
# Nesta etapa, vamos transformar os dados brutos de transações em uma visualização de rede (um grafo) interativa. Vamos enxergar de forma clara como o dinheiro flui entre as diferentes empresas.
# Nós (Círculos): Cada empresa será um nó no nosso grafo.
# Arestas (Linhas/Setas): Cada transação será uma seta que vai da empresa pagadora para a empresa recebedora.
# Insights: Com isso, podemos identificar empresas que são "hubs" financeiros (que se conectam com muitas outras), visualizar clusters de negócios e entender a cadeia de pagamentos.


import pandas as pd
import networkx as nx
from pyvis.network import Network

print("Iniciando o Passo 4: Análise de Grafos...")

# --- 1. CARREGAR OS DADOS NECESSÁRIOS ---
try:
    # Usamos a base de transações para as conexões
    df_transacoes = pd.read_csv('../data/Base 2 - Transacoes.csv', delimiter=';')
    # E a base analítica (limpa e sem duplicatas) para enriquecer os nós
    df_analitico = pd.read_csv('../data/Base_Analitica_PJ_Versao_final.csv', delimiter=';')
    print("Arquivos 'Base 2 - Transacoes.csv' e 'Base_Analitica_PJ_Versao_final.csv' carregados.")
except FileNotFoundError as e:
    print(f"ERRO: Arquivo não encontrado. {e}")
    print("Certifique-se de que os arquivos CSV estão na mesma pasta do script.")
    exit()

# --- 2. PREPARAR OS DADOS PARA O GRAFO ---
# Para não sobrecarregar a visualização, vamos usar uma amostra das transações.
# Em um projeto real, você poderia filtrar por um período, valor ou tipo de transação.
# Vamos pegar uma amostra maior para ter uma rede mais rica.
if len(df_transacoes) > 2000:
    df_amostra = df_transacoes.sample(n=2000, random_state=42)
else:
    df_amostra = df_transacoes

# Criar um mapeamento do ID da empresa para o seu 'Momento de Vida'
# Isso nos permitirá colorir os nós do grafo
mapeamento_momento_vida = df_analitico.set_index('ID')['MOMENTO_VIDA'].to_dict()

# --- 3. CONSTRUIR O GRAFO COM NETWORKX ---
G = nx.from_pandas_edgelist(
    df_amostra,
    source='ID_PGTO',
    target='ID_RCBE',
    edge_attr='VL', # O atributo da aresta será o valor da transação
    create_using=nx.DiGraph() # Grafo direcionado (seta indica o fluxo do dinheiro)
)

print(f"Grafo criado com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")

# --- 4. PREPARAR A VISUALIZAÇÃO INTERATIVA COM PYVIS ---
net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white", notebook=True, directed=True)

# Mapear os momentos de vida para cores para melhor visualização
cores_map = {
    'Início': '#3498db',     # Azul
    'Expansão': '#2ecc71',   # Verde
    'Maturidade': '#f1c40f', # Amarelo
    'Declínio': '#e74c3c'      # Vermelho
}

# Adicionar os nós (empresas) ao grafo visual
for node in G.nodes():
    momento = mapeamento_momento_vida.get(node, 'Não definido')
    cor = cores_map.get(momento, '#95a5a6') # Cor padrão cinza
    
    net.add_node(
        node,
        label=node,
        title=f"Momento de Vida: {momento}", # Tooltip ao passar o mouse
        color=cor
    )

# Adicionar as arestas (transações) ao grafo visual
for source, target, data in G.edges(data=True):
    valor = data['VL']
    valor_int = int(valor)
    net.add_edge(
        source,
        target,
        value=valor / 100000, # Escalonar o valor para a largura da aresta não ficar exagerada
        title=f"Valor: R$ {valor_int:,}" # Tooltip na aresta
    )

# --- 5. GERAR O ARQUIVO HTML ---
nome_arquivo_html = 'rede_financeira.html'
net.show_buttons(filter_=['physics'])
net.show(nome_arquivo_html)

print("\n--- Processo Concluído! ---")
print(f"O arquivo '{nome_arquivo_html}' foi gerado em sua pasta de trabalho.")
print("Abra este arquivo em seu navegador para ver o grafo interativo.")