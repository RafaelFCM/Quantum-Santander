# import pandas as pd
# from datetime import datetime

# # --- Carregar os Dados ---
# # Garanta que os arquivos 'Base 1 - ID.csv' e 'Base 2 - Transacoes.csv' 
# # estejam na mesma pasta que este script.
# try:
#     df_id = pd.read_csv('../data/Base 1 - ID.csv', delimiter=';')
#     df_transacoes = pd.read_csv('../data/Base 2 - Transacoes.csv', delimiter=';')

#     print("Arquivos CSV carregados com sucesso!")

#     # --- Limpeza e Preparação dos Dados ---
#     # Converter as colunas de data para o formato datetime
#     df_id['DT_ABRT'] = pd.to_datetime(df_id['DT_ABRT'])
#     df_id['DT_REFE'] = pd.to_datetime(df_id['DT_REFE'])
#     df_transacoes['DT_REFE'] = pd.to_datetime(df_transacoes['DT_REFE'])

#     print("Colunas de data convertidas para datetime.")

#     # --- 1. Classificação do Momento de Vida da Empresa ---
#     print("Iniciando a classificação do momento de vida das empresas...")

#     # Usar a data de referência mais recente como "hoje" para cálculos de idade
#     data_referencia_max = df_id['DT_REFE'].max()

#     # Calcular a idade da empresa em anos
#     df_id['IDADE_ANOS'] = (data_referencia_max - df_id['DT_ABRT']).dt.days / 365.25

#     # Definir as faixas de idade para cada estágio
#     bins_idade = [0, 2, 5, 10, float('inf')]
#     labels_idade = ['Início', 'Expansão', 'Maturidade', 'Declínio']
#     df_id['MOMENTO_VIDA'] = pd.cut(df_id['IDADE_ANOS'], bins=bins_idade, labels=labels_idade, right=False)

#     print("Classificação do momento de vida concluída.")

#     # --- 2. Análise "Cruz da PJ" (Recebimentos e Pagamentos) ---
#     print("Calculando totais de recebimentos e pagamentos (Cruz da PJ)...")

#     # Calcular o total de recebimentos para cada empresa
#     df_recebimentos = df_transacoes.groupby('ID_RCBE')['VL'].sum().reset_index()
#     df_recebimentos.rename(columns={'ID_RCBE': 'ID', 'VL': 'VL_TOTAL_RECEBIDO'}, inplace=True)

#     # Calcular o total de pagamentos para cada empresa
#     df_pagamentos = df_transacoes.groupby('ID_PGTO')['VL'].sum().reset_index()
#     df_pagamentos.rename(columns={'ID_PGTO': 'ID', 'VL': 'VL_TOTAL_PAGO'}, inplace=True)

#     print("Cálculos da Cruz da PJ concluídos.")

#     # --- Unir todas as informações em um único DataFrame ---
#     print("Unindo as informações na base analítica final...")
#     df_analitico = pd.merge(df_id, df_recebimentos, on='ID', how='left')
#     df_analitico = pd.merge(df_analitico, df_pagamentos, on='ID', how='left')

#     # Preencher com 0s os valores de empresas que não tiveram recebimentos ou pagamentos
#     df_analitico['VL_TOTAL_RECEBIDO'].fillna(0, inplace=True)
#     df_analitico['VL_TOTAL_PAGO'].fillna(0, inplace=True)

#     # --- Salvar o resultado em um novo arquivo CSV ---
#     nome_arquivo_saida = '../data/Base_Analitica_PJ.csv'
#     df_analitico.to_csv(nome_arquivo_saida, index=False, sep=';')

#     print("\n--- Processo Concluído! ---")
#     print(f"O arquivo '{nome_arquivo_saida}' foi gerado em sua pasta de trabalho.")
    
#     # Exibir as primeiras linhas do resultado final no console
#     print("\n--- Amostra do Resultado Final (primeiras 5 linhas) ---")
#     print(df_analitico.head())


# except FileNotFoundError as e:
#     print(f"ERRO: Arquivo não encontrado. Verifique se os arquivos CSV estão na mesma pasta do script. Detalhes: {e}")
# except Exception as e:
#     print(f"Ocorreu um erro inesperado durante a execução: {e}")


# ======================= VERSÃO INTERMEDIÁRIA =======================


# import pandas as pd

# try:
#     print("Carregando arquivos...")
#     df_id = pd.read_csv('../data/Base 1 - ID.csv', delimiter=';')
#     df_transacoes = pd.read_csv('../data/Base 2 - Transacoes.csv', delimiter=';')

#     # --- NOVO PASSO: DE-DUPLICAÇÃO ---
#     print(f"Número de linhas antes da limpeza: {len(df_id)}")
    
#     # Converter DT_REFE para datetime para garantir a ordenação correta
#     df_id['DT_REFE'] = pd.to_datetime(df_id['DT_REFE'])
    
#     # Ordena os dados pela data de referência (do mais antigo para o mais novo)
#     df_id = df_id.sort_values('DT_REFE')
    
#     # Mantém apenas a última (a mais recente) ocorrência de cada ID
#     df_id_limpo = df_id.drop_duplicates(subset='ID', keep='last')
    
#     print(f"Número de linhas após a limpeza: {len(df_id_limpo)}")
#     # ------------------------------------

#     # Agora, o resto do script continua usando o df_id_limpo
#     df_id_limpo['DT_ABRT'] = pd.to_datetime(df_id_limpo['DT_ABRT'])
    
#     data_referencia_max = df_id_limpo['DT_REFE'].max()
#     df_id_limpo['IDADE_ANOS'] = (data_referencia_max - df_id_limpo['DT_ABRT']).dt.days / 365.25

#     bins_idade = [0, 2, 5, 10, float('inf')]
#     labels_idade = ['Início', 'Expansão', 'Maturidade', 'Declínio']
#     df_id_limpo['MOMENTO_VIDA'] = pd.cut(df_id_limpo['IDADE_ANOS'], bins=bins_idade, labels=labels_idade, right=False)

#     df_recebimentos = df_transacoes.groupby('ID_RCBE')['VL'].sum().reset_index()
#     df_recebimentos.rename(columns={'ID_RCBE': 'ID', 'VL': 'VL_TOTAL_RECEBIDO'}, inplace=True)

#     df_pagamentos = df_transacoes.groupby('ID_PGTO')['VL'].sum().reset_index()
#     df_pagamentos.rename(columns={'ID_PGTO': 'ID', 'VL': 'VL_TOTAL_PAGO'}, inplace=True)

#     df_analitico = pd.merge(df_id_limpo, df_recebimentos, on='ID', how='left')
#     df_analitico = pd.merge(df_analitico, df_pagamentos, on='ID', how='left')

#     df_analitico['VL_TOTAL_RECEBIDO'].fillna(0, inplace=True)
#     df_analitico['VL_TOTAL_PAGO'].fillna(0, inplace=True)

#     nome_arquivo_saida = '../data/Base_Analitica_PJ_sem_duplicidade.csv'
#     df_analitico.to_csv(nome_arquivo_saida, index=False, sep=';')

#     print(f"\nArquivo '{nome_arquivo_saida}' atualizado e limpo com sucesso!")

# except Exception as e:
#     print(f"Ocorreu um erro: {e}")







# ==================================== VERSÃO FINAL ====================================





import pandas as pd

try:
    print("Carregando arquivos...")
    df_id = pd.read_csv('../data/Base 1 - ID.csv', delimiter=';')
    df_transacoes = pd.read_csv('../data/Base 2 - Transacoes.csv', delimiter=';')

    # --- PASSO DE LIMPEZA: DE-DUPLICAÇÃO ---
    print(f"Número de linhas antes da limpeza: {len(df_id)}")
    
    df_id['DT_REFE'] = pd.to_datetime(df_id['DT_REFE'])
    df_id = df_id.sort_values('DT_REFE')
    df_id_limpo = df_id.drop_duplicates(subset='ID', keep='last').copy()
    
    print(f"Número de linhas após a limpeza: {len(df_id_limpo)}")
    # ------------------------------------

    # Continua o script usando o df_id_limpo
    df_id_limpo['DT_ABRT'] = pd.to_datetime(df_id_limpo['DT_ABRT'])
    
    data_referencia_max = df_id_limpo['DT_REFE'].max()
    
    # --- ALTERADO: IDADE_ANOS arredondada para o inteiro mais próximo ---
    df_id_limpo['IDADE_ANOS'] = ((data_referencia_max - df_id_limpo['DT_ABRT']).dt.days / 365.25).round(0).astype(int)

    bins_idade = [0, 2, 5, 10, float('inf')]
    labels_idade = ['Início', 'Expansão', 'Maturidade', 'Declínio']
    df_id_limpo['MOMENTO_VIDA'] = pd.cut(df_id_limpo['IDADE_ANOS'], bins=bins_idade, labels=labels_idade, right=False)

    df_recebimentos = df_transacoes.groupby('ID_RCBE')['VL'].sum().reset_index()
    df_recebimentos.rename(columns={'ID_RCBE': 'ID', 'VL': 'VL_TOTAL_RECEBIDO'}, inplace=True)

    df_pagamentos = df_transacoes.groupby('ID_PGTO')['VL'].sum().reset_index()
    df_pagamentos.rename(columns={'ID_PGTO': 'ID', 'VL': 'VL_TOTAL_PAGO'}, inplace=True)

    df_analitico = pd.merge(df_id_limpo, df_recebimentos, on='ID', how='left')
    df_analitico = pd.merge(df_analitico, df_pagamentos, on='ID', how='left')

    df_analitico['VL_TOTAL_RECEBIDO'].fillna(0, inplace=True)
    df_analitico['VL_TOTAL_PAGO'].fillna(0, inplace=True)

    # --- AJUSTE DOS TIPOS DE DADOS PARA INTEIRO ---
    print("Ajustando os tipos de dados para inteiro...")
    colunas_para_inteiro = ['VL_FATU', 'VL_SLDO', 'VL_TOTAL_RECEBIDO', 'VL_TOTAL_PAGO']
    
    for coluna in colunas_para_inteiro:
        df_analitico[coluna] = df_analitico[coluna].astype(int)
    # ----------------------------------------------------

    nome_arquivo_saida = '../data/Base_Analitica_PJ_Versao_final.csv'
    df_analitico.to_csv(nome_arquivo_saida, index=False, sep=';')

    print(f"\nArquivo '{nome_arquivo_saida}' atualizado com todos os tipos de dados corretos!")
    print("\nVisualização dos tipos de dados finais:")
    print(df_analitico.info())


except Exception as e:
    print(f"Ocorreu um erro: {e}")