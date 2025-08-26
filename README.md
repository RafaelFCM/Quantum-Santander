# Solução Analítica de Fluxo de Caixa para Clientes PJ

## Visão Geral do Projeto

Esta é uma ferramenta analítica integrada, desenvolvida como um  **portal digital interativo** , para capacitar analistas a entenderem o fluxo de caixa de empresas clientes (PJ) de forma profunda e intuitiva. A solução utiliza tecnologias avançadas de Inteligência Artificial para processar dados transacionais e cadastrais, gerando insights valiosos, classificações automáticas e visualizações de rede que revelam as conexões financeiras entre as entidades.

O projeto evoluiu de scripts individuais para uma aplicação web completa com uma arquitetura cliente-servidor. O  **back-end (cérebro)** , construído em Python com Flask, serve os dados e a lógica de IA através de uma API. O **front-end (rosto)** é um dashboard interativo em HTML/JavaScript que consome essa API, proporcionando uma experiência de usuário rica e centralizada para análise de dados, exploração de redes financeiras e interação com um assistente de IA.

## Como Usar a Solução

Siga os passos abaixo para configurar e executar o portal de análise em sua máquina local.

### Pré-requisitos

* **Python:** Certifique-se de ter o Python 3.8 ou superior instalado.
* **Chave de API:** Você precisará de uma chave de API da OpenAI para a funcionalidade do assistente de IA.
* **Navegador Web:** Um navegador moderno como Chrome, Firefox ou Edge.
* **Editor de Código:** Recomenda-se o uso do VS Code com a extensão **Live Server** para uma melhor experiência de desenvolvimento do front-end.

---

### Passo 1: Setup do Ambiente

1. **Prepare a Pasta do Projeto**
   * Coloque todos os arquivos (`.py`, `.csv`, `.html`, etc.) em uma única pasta.
2. **Crie e Ative um Ambiente Virtual (`venv`)**
   * Abra um terminal na pasta do projeto e execute:
     **Bash**

     ```
     # No Windows
     python -m venv venv
     # No macOS/Linux
     python3 -m venv venv
     ```
   * Ative o ambiente:
     **Bash**

     ```
     # No Windows
     .\venv\Scripts\activate
     # No macOS/Linux
     source venv/bin/activate
     ```
3. **Instale as Dependências**
   * Crie um arquivo chamado `requirements.txt` na sua pasta com o seguinte conteúdo:
     **Plaintext**

     ```
     pandas
     networkx
     pyvis
     langchain
     langchain-chroma
     langchain-openai
     openai
     Flask
     Flask-Cors
     ```
   * Agora, instale todas as bibliotecas de uma vez:
     **Bash**

     ```
     pip install -r requirements.txt
     ```

---

### Passo 2: Preparação dos Dados (Execução Única)

Antes de iniciar o portal, você precisa processar os dados brutos e criar a base de conhecimento da IA. **Estes scripts só precisam ser executados uma vez.**

1. **Limpeza e Enriquecimento dos Dados**
   * Execute o script para gerar a base analítica limpa:
     **Bash**

     ```
     python analise_classificacao_clientes_cruz.py
     ```
   * Isso criará o arquivo `Base_Analitica_PJ_Versao_final.csv` formatado corretamente.
2. **Criação da Base de Conhecimento da IA (RAG)**
   * Abra o arquivo `rag.py` e insira sua chave de API da OpenAI.
   * Execute o script para criar a base de dados vetorial:
     **Bash**

     ```
     python rag.py
     ```
   * Isso criará a pasta `chroma_db_sem_duplicidade`, que funciona como a "memória" da IA.

---

### Passo 3: Execução do Portal Digital

O portal funciona com duas partes rodando simultaneamente: o back-end e o front-end.

1. **Inicie o Servidor Back-End**
   * Abra o arquivo `app.py` e configure as duas variáveis no topo:

     * `CHROMA_DB_DIRECTORY`: Verifique se o nome da pasta (`chroma_db` ou `chroma_db_sem_duplicidade`) está correto.
     * `OPENAI_API_KEY`: Insira sua chave de API da OpenAI.
   * No seu terminal, inicie o servidor Flask:
     **Bash**

     ```
     python app.py
     ```
   * O terminal mostrará que o servidor está rodando em `http://127.0.0.1:5000`. **Deixe este terminal aberto.**
2. **Abra a Interface Front-End**
   * No seu editor de código (VS Code), clique com o botão direito no arquivo `index.html`.
   * Selecione  **"Open with Live Server"** .
   * Seu navegador abrirá automaticamente o dashboard, geralmente em um endereço como `http://127.0.0.1:5500`.

### O Que Esperar do Portal

Ao abrir o `index.html` no navegador, você terá acesso a um dashboard completo e interativo:

* **Seleção de Cliente:** Um menu suspenso no topo permite que você escolha uma empresa específica para análise.
* **Dashboard Dinâmico:** Ao selecionar um cliente, a tela se atualiza mostrando:
  * **KPIs:** Faturamento, Saldo em Conta e Momento de Vida.
  * **Rede de Relacionamento:** Um grafo interativo focado nas conexões daquela empresa, com legendas e informações detalhadas ao passar o mouse.
* **Assistente de IA:** Na parte inferior, uma caixa de texto permite que você faça perguntas em linguagem natural sobre todo o portfólio de clientes e receba respostas geradas pela IA em tempo real.
