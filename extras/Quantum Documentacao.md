**CHALLENGE SANTANDER 2025 - 4SI – FIAP **

**Nome e Descrição do Cliente \(Empresa\):** Santander 





**Nome do time e integrantes: **

Quantum 

• 

Alexandre Ilha de Vilhena RM88689 

• 

Bruno Norões de Magalhães RM82511 

• 

Erik Hoon Ko RM93599 

• 

Rafael Fiel Cruz Miranda RM94654 

• 

Luca Moraes Zaharic RM95794 





**Histórico de revisões deste documento: **

****

Versão 

Data 

\(0.0\) 

\(DD/MM/YYYY\) 

Autor 

Descrição \(O que fez no doc?\) 

1.0 

02/05/2025 

Equipe 

Criação inicial do documento de visão 

Quantum 

2.0 

17/05/2025 

Equipe 

Adição das seções de Documentação 

Quantum 

Técnica e Dashboard 

****

****

**Escopo \(o que o desafio abrange e contempla\)**: Desenvolvimento de uma solução analítica para análise de fluxo de caixa de pessoas jurídicas \(PJ\) 

• 

Implementação de crawler para coleta de dados públicos 

• 

Criação de sistema RAG com LLM para análise de dados 

• 

Desenvolvimento de grafos para mapeamento de redes financeiras 

• 

Criação de dashboard interativo para visualização dos resultados 

• 

Elaboração de documentação técnica detalhada da arquitetura da solução 

• 

Criação de protótipo não funcional navegável do dashboard **Não Escopo \(o que não será feito deve ser esclarecido para alinhar** **expectativas\)**: 

• 

Implementação de sistemas de pagamento 

• 

Integração direta com sistemas core do banco 

• 

Gestão de transações financeiras 

• 

Implementação de políticas de crédito 

• 

Funcionalidades completas de backend no protótipo do dashboard \(o protótipo é navegável e visual, mas não processa dados reais nem executa análises em tempo real\). 





**Oportunidades de Negócio identificadas \(alto nível - preliminares\): **

• 

Antecipação de necessidades de produtos financeiros para PJs 

• 

Melhoria substancial na prospecção e qualificação de clientes PJ através da identificação automática e precisa do seu perfil e momento de vida, permitindo ofertas de produtos e serviços mais direcionadas, oportunas e eficientes; 

• 

Mitigação proativa de riscos de crédito, operacionais e sistêmicos pela compreensão aprofundada das cadeias de valor, das interdependências financeiras das PJs e da saúde financeira da rede; 

• 

Criação de ofertas de produtos e serviços \(crédito, investimento, seguros, câmbio, etc.\) verdadeiramente personalizadas e contextuais, baseadas no estágio da “Cruz da PJ” e no momento de vida da empresa, aumentando a conversão e a satisfação do cliente; 

• 

Identificação de novas oportunidades de negócio e cross-sell/up-sell ao entender as necessidades não atendidas das PJs e de suas redes de relacionamento. 





**Posicionamento **

A solução ideal, materializada na plataforma Quantum, é uma ferramenta analítica integrada, projetada para capacitar o Santander a analisar e entender o fluxo de caixa de suas empresas clientes, utilizando tecnologias avançadas de IA e automação para fornecer insights valiosos e previsões precisas. 





**Descrição do problema **

• 

No contexto do Perfil PJ \(Desafio 1\), a plataforma permitirá a análise detalhada da “Cruz da PJ” \(recebimentos, pagamentos, investimentos, crédito\) e a classificação automática do momento de vida da empresa \(Início, Expansão, Maturidade, Declínio\), considerando fatores contextuais. Isso será viabilizado por um crawler inteligente para coleta de dados públicos. 

• 

Para as Cadeias de Valor \(Desafio 2\), a plataforma utilizará análise de SASNA para mapear as redes de relacionamento financeiro das PJs, identificando os elos mais importantes, a capacidade de pagamentos/recebimentos da rede e os riscos associados a essas redes, conforme solicitado no desafio. 

• 

Tecnologias de Suporte Fundamentais: A solução combinará um crawler inteligente para coleta de dados; um sistema RAG com LLM para extrair insights valiosos de dados não estruturados \(enriquecendo as análises dos desafios\); Social Network Analysis para o mapeamento e exploração de redes. 

O objetivo final é permitir recomendações proativas e personalizadas de produtos financeiros e uma gestão de riscos mais eficaz, ágil e informada. 





**Descrição e Visão Geral da solução \(inspiração, motivação, propósito\):** A solução nasce da necessidade de transformar dados em insights para o Santander, utilizando tecnologias de ponta. O propósito é criar uma plataforma que não apenas analise o fluxo de caixa das PJs, mas também entenda seu momento de vida, suas redes de relacionamento e antecipe suas necessidades, permitindo ao banco oferecer produtos mais adequados e gerenciar riscos de forma mais eficiente. 





**Regras e/ou Restrições a considerar:** 1. A solução só usará e contará com dados públicos e autorizados pelo Santander, incluindo relatórios institucionais, dados da CVM, B3 e informações disponíveis publicamente 

2. O desenvolvimento deve seguir as melhores práticas de segurança e privacidade de dados, garantindo conformidade com LGPD e regulamentações bancárias 

3. A solução deve ser escalável e capaz de processar grandes volumes de dados em tempo hábil, considerando o crescimento do número de PJs analisadas 4. O sistema deve ser modular e permitir fácil manutenção e atualização, com documentação clara e código bem estruturado 5. As tecnologias utilizadas devem ser de código aberto ou com licenças adequadas para uso comercial 

6. A solução deve ser desenvolvida considerando a integração futura com sistemas existentes do Santander 

7. O dashboard deve ser responsivo e acessível, permitindo visualização em diferentes dispositivos 

8. Os modelos de ML e análises devem ser explicáveis e auditáveis, permitindo compreensão das decisões tomadas 

**Relação de Requisitos Funcionais e Não funcionais da solução: **

****

Nº 

Nome 

Descrição 

RF001 Coleta de Dados 

Sistema deve coletar automaticamente 

dados públicos de PJs através de 

crawler 

RF002 Análise de Dados Não Estruturados Processamento e análise de dados não 

com LLM/RAG \(Análise de Perfil e 

estruturados usando RAG e LLM 

Momento de Vida da PJ\) 

RF003 Mapeamento e Análise de Cadeias 

Construção e análise de grafos de 

de Valor 

relacionamento financeiro 

RF004 Dashboard 

Visualização interativa dos resultados e insights 

RF005 Performance 

Processamento de grandes volumes de 

dados em tempo hábil 

RF006 Segurança 

Proteção e conformidade com LGPD e 

regulamentações bancárias 

RF007 Usabilidade 

Interface intuitiva e fácil de usar para analistas e gestores 

RF008 Escalabilidade 

Capacidade de crescer com o aumento 

do volume de dados e usuários 

RF009 Documentação Técnica da 

Elaboração de esquema/fluxograma e 

Arquitetura 

texto explicativo da arquitetura da 

solução 

RF010 Protótipo de Dashboard Navegável Criação de um protótipo não funcional 

do dashboard, com link de acesso e 

prints das telas 

****

****

**Tecnologias e linguagens previstas para desenvolver a solução: **

• 

LLM/RAG: OpenAI GPT 

• 

Visualização: Streamlit 

• 

Linguagens: Python, SQL 

• 

Banco de Dados: SQL-based \(implícito para armazenamento\) 

• 

Crawler: Python com bibliotecas de web scraping 

• 

Análise de Grafos: Python com bibliotecas relevantes \(ex: NetworkX\) **Benefícios previstos ou esperados com a solução: **

• 

Antecipação de necessidades de produtos financeiros para PJs 



• 

Maior assertividade e personalização na oferta de soluções financeiras \(crédito, investimento, pagamentos, recebimentos\) ao compreender profundamente o momento, as necessidades específicas e o contexto da empresa \(fatores do Desafio 1\); 

• 

Visão 360º e dinâmica das interconexões financeiras dos clientes PJ e de seus ecossistemas, permitindo uma gestão de portfólio mais estratégica, a identificação proativa de riscos \(incluindo riscos de contágio na rede\) e oportunidades \(alinhado ao Desafio 2\); 

• 

Aumento da fidelização dos clientes PJ através de um relacionamento mais proativo e baseado em insights gerados pela plataforma Quantum; 

• 

Otimização da alocação de recursos e da tomada de decisão estratégica do banco com base em análises de dados mais ricas e precisas sobre o segmento PJ. 





**Cronograma de execução: **

****

Atividade 

Maio Junho Julho Agosto Setembro Outubro Levantamento de Requisitos 

X 





Pesquisa de Tecnologias 

X 





Design da Arquitetura 



X 





Desenvolvimento do Crawler 



X 

X 

X 





Implementação RAG/LLM 



X 

X 

X 





Desenvolvimento de Grafos 



X 

X 

X 





Dashboard \(Desenvolvimento e 

X 



X 





Prototipagem\) 

Testes e Validação 





X 

X 



Documentação e Entrega 

X 





X 

****



**Arquitetura da Solução **

A arquitetura da solução Quantum foi concebida como um sistema integrado e robusto, projetado para transformar dados brutos em inteligência acionável para o Santander, com foco na análise aprofundada do fluxo de caixa e do perfil de Pessoas Jurídicas \(PJ\). O fluxograma da arquitetura ilustra visualmente os componentes chave e suas interconexões, que serão detalhados textualmente a seguir. 





O componente **Crawler**, desenvolvido em Python com apoio do **Selenium**, é o responsável por interagir com diversas fontes públicas de dados, incluindo relatórios de relação com investidores \(RI\), APIs e páginas web. Esse módulo automatizado é programado para navegar, localizar e extrair informações relevantes de forma robusta e flexível, adaptando-se a diferentes formatos e estruturas encontradas na internet. 

Uma vez coletados, os textos extraídos são imediatamente processados com **SBERT **

**\(Sentence-BERT\)**, gerando **embeddings vetoriais semânticos** que são armazenados no **ChromaDB**, um banco de dados vetorial altamente otimizado para buscas por similaridade. 

Esse armazenamento elimina a necessidade de um banco relacional intermediário, simplificando a arquitetura e permitindo que as informações estejam prontas para análises semânticas imediatas. 

O componente central da análise é o sistema de **RAG \(Retrieval-Augmented Generation\)**, integrado a **LLMs \(Large Language Models\)** como o **GPT da OpenAI**, operando em Python. Esse módulo consulta o ChromaDB para recuperar os vetores mais relevantes de acordo com a pergunta ou contexto, e em seguida utiliza o modelo de linguagem para interpretar e gerar insights textuais com base nas evidências encontradas. Além de responder a perguntas, o RAG também atua como um motor analítico, sugerindo correlações, destacando empresas críticas e identificando padrões financeiros. 

Complementando o RAG, o sistema inclui um **módulo de construção de grafos**, também desenvolvido em Python com **NetworkX**, que recebe instruções da RAG sobre quais entidades e relações devem ser representadas visualmente. Esse grafo destaca, por 

exemplo, empresas com alto risco, alta influência ou relevância estratégica. A estrutura e os elementos exibidos são definidos dinamicamente com base nos critérios de priorização sugeridos pelo modelo de linguagem, permitindo análises adaptativas e inteligentes. 

Todos os resultados — desde os textos interpretativos até os grafos personalizados — são apresentados em um **dashboard interativo desenvolvido com Streamlit**. Esse painel permite que analistas e gestores explorem os dados de forma intuitiva, realizem consultas em linguagem natural, visualizem as conexões mais relevantes e acompanhem a saúde e a influência das empresas ao longo do tempo. A interatividade possibilita filtros personalizados, simulações de impacto e análise profunda de perfis empresariais, apoiando decisões estratégicas com base em dados interpretados e visualmente acessíveis. 





**Possíveis Fontes de Dados Públicas **

Fontes Oficiais de Dados Financeiros e Corporativos: 

● B3 

● CVM \(Comissão de Valores Mobiliários\) 

● Seção de Relações com Investidores \(RI\) dos sites corporativos 

● Receita Federal 

● IBGE 

● Banco Central do Brasil 



Portais Financeiros e de Notícias: 

● InfoMoney 

● Valor Econômico 

● Investing.com 



APIs e Serviços de Dados: 

● Alpha Vantage 

● Quandl 

● API da B3 

● API do IBGE 



Dados Setoriais e Associações: 

● ABRAS \(Associação Brasileira de Supermercados\) 

● ABRASCE \(Associação Brasileira de Shopping Centers\) 

● ANFAVEA \(Associação Nacional dos Fabricantes de Veículos Automotores\) 

● ANP \(Agência Nacional do Petróleo\) 



**Dashboard: Protótipo Não Funcional Navegável** A equipe desenvolveu um protótipo não funcional e navegável do dashboard da solução Quantum. Este protótipo visa demonstrar a interface e as principais funcionalidades de visualização que seriam disponibilizadas aos usuários finais. 

• 

**Visão Geral PJ: **Apresenta uma análise simulada da “Cruz da PJ” 

\(recebimentos, pagamentos, investimentos, crédito\) para uma empresa exemplo. Inclui gráficos de barras para recebimentos e pagamentos, métricas de totais, e exemplos de fontes de receita e categorias de despesa. Também mostra exemplos de saldos de investimento e linhas de crédito utilizadas. 

• 

**Momento de Vida da Empresa: **Demonstra a classificação automática do momento de vida das empresas, com uma justificativa baseada em dados simulados e exemplos de fatores contextuais considerados \(crescimento da receita, investimento em P&D, número de funcionários, etc.\). 

• 

**Cadeias de Valor e Redes Financeiras: **Ilustra o mapeamento de relacionamentos financeiros das empresas, Grafo interativo de relacionamentos, Mapa de calor de conexões, Identificação de nós críticos, Análise de clusters e comunidades. 

• 

**Insights e Recomendações: **Apresenta exemplos de como o dashboard funcional geraria insights acionáveis e recomendações personalizadas de produtos e serviços financeiros, baseados nas análises das seções anteriores. 





# Document Outline

+ CHALLENGE SANTANDER 2025 - 4SI – FIAP  
+ Nome e Descrição do Cliente \(Empresa\):  
+ Nome do time e integrantes:  
+ Histórico de revisões deste documento:  
+ Não Escopo \(o que não será feito deve ser esclarecido para alinhar expectativas\):  
+ Oportunidades de Negócio identificadas \(alto nível - preliminares\):  
+ Posicionamento  
+ Descrição do problema  
+ Descrição e Visão Geral da solução \(inspiração, motivação, propósito\):  
+ Regras e/ou Restrições a considerar:  
+ Relação de Requisitos Funcionais e Não funcionais da solução:  
+ Benefícios previstos ou esperados com a solução:  
+ Cronograma de execução:  
+ Possíveis Fontes de Dados Públicas  
+ Dashboard: Protótipo Não Funcional Navegável



