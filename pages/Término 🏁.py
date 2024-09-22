import streamlit as st
import base64

# Função para exibir links de imagem com base64
def get_image_download_link(img_path, link, width):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f'<a href="{link}" target="_blank"><img src="data:image/jpeg;base64,{encoded_string}" alt="Link Image" style="width:{width}px;"></a>'

# Função para renderizar a conclusão do projeto
def render_conclusao():
    st.header(":orange[Conclusão]", divider="blue")
    
    st.write("""
    Este projeto propôs a criação de um modelo de machine learning para **identificação de alunos em risco**, utilizando um conjunto de dados composto por notas acadêmicas e indicadores de desempenho, como o **Índice de Engajamento Geral (IEG)** e o **Índice de Aproveitamento Acadêmico (IAA)**. O principal objetivo foi desenvolver uma ferramenta que permita identificar de forma proativa os alunos que estão mais propensos a enfrentar dificuldades acadêmicas, especialmente os classificados na **Pedra Quartzo**, que representa o nível mais crítico de desempenho.

    O modelo selecionado, **Gradient Boosting**, mostrou um desempenho sólido, especialmente nas métricas de **recall** e **acurácia**, sendo capaz de identificar corretamente a maioria dos alunos em risco, permitindo que intervenções educacionais possam ser planejadas de maneira mais precisa. O uso de técnicas como **SMOTE** para balancear as classes foi crucial para melhorar a capacidade do modelo de lidar com o desbalanceamento natural dos dados, onde o número de alunos em risco era significativamente menor que o de alunos sem risco.
    
    ### Como esse modelo pode ajudar a Passos Mágicos
    
    O modelo de predição desenvolvido pode ser uma **ferramenta estratégica** fundamental para a **Passos Mágicos**, auxiliando em diversas frentes:
    
    1. **Identificação Antecipada de Alunos em Risco**:
       O modelo pode ser integrado ao sistema educacional da instituição, permitindo que professores e administradores recebam alertas sobre alunos que estão com maior probabilidade de enfrentar dificuldades acadêmicas. Ao identificar esses alunos precocemente, a escola pode tomar ações proativas, como oferecer **suporte personalizado**, reforços ou orientação pedagógica focada.
    
    2. **Apoio na Tomada de Decisão**:
       Os dados e previsões gerados pelo modelo podem fornecer **insights valiosos** para a equipe administrativa da Passos Mágicos. Isso pode ajudar na alocação eficiente de recursos, garantindo que as **intervenções sejam direcionadas** para os alunos que mais precisam de apoio. Além disso, a análise dos padrões de risco pode ser usada para **ajustar o currículo** ou estratégias de ensino para aumentar o engajamento dos alunos em disciplinas onde o risco é mais elevado.
    
    3. **Acompanhamento e Evolução do Desempenho**:
       Através do monitoramento contínuo, a **Passos Mágicos** pode avaliar se as intervenções educacionais estão surtindo efeito e ajustar suas estratégias com base nos resultados obtidos. O modelo pode ser atualizado regularmente com novos dados para refletir o progresso dos alunos, criando um **ciclo contínuo de melhoria** no processo educacional.
    
    4. **Diminuição da Evasão Escolar**:
       Ao intervir de maneira precoce, a instituição pode não apenas melhorar o desempenho acadêmico dos alunos, mas também reduzir significativamente a taxa de **abandono escolar**. Ao identificar alunos em risco antes que eles cheguem a um ponto crítico, é possível fornecer **apoio emocional e acadêmico** necessário para que esses estudantes permaneçam na escola e superem as dificuldades.
    
    ### O Futuro
    
    Com a aplicação do modelo de predição de risco, a **Passos Mágicos** tem a oportunidade de transformar seus processos educacionais, movendo-se de uma abordagem reativa para uma abordagem **proativa** e baseada em dados. Ao adotar tecnologias de machine learning no acompanhamento de seus alunos, a instituição pode reforçar seu compromisso com o sucesso educacional, garantindo que cada aluno receba a atenção necessária para **alcançar todo o seu potencial**.
    """)

# Função para renderizar o passo a passo do projeto
def render_referencias():
    st.header(":orange[Sobre o Projeto]", divider="blue")
    st.header(':violet[Pipeline de Análise de Dados e Machine Learning]')
    st.image('passos_magicos_pipeline.drawio.png', caption='Pipeline de Dados', use_column_width=True)
    st.markdown('')
    st.write("""
    ### 1. Coleta de Dados
    O primeiro passo foi coletar as informações dos alunos, como notas de diversas disciplinas e índices de desempenho acadêmico. 
    Esses dados foram disponibilizados em um formato de planilha (CSV).

    ### 2. Limpeza e Tratamento dos Dados
    Realizamos a limpeza dos dados, incluindo a remoção de valores ausentes e duplicados, além de ajustes no tipo de dados. 
    Também eliminamos colunas desnecessárias para focar nas informações mais relevantes para o modelo.

    ### 3. Análise Exploratória de Dados (EDA)
    Antes de construir o modelo, fizemos uma análise exploratória para entender a distribuição das notas, o comportamento dos alunos em risco (Quartzo), 
    e identificar possíveis padrões.

    ### 4. Balanceamento dos Dados
    Como a quantidade de alunos em risco era menor que os outros, aplicamos a técnica de oversampling com **SMOTE** para balancear o conjunto de treino e melhorar o desempenho do modelo.

    ### 5. Construção do Modelo
    Testamos alguns modelos, ajustando seus hiperparâmetros. O algoritmo **Gradient Boosting** foi o que apresentou o melhor desempenho, especialmente no recall — importante para identificar a maioria dos alunos em risco.

    ### 6. Avaliação do Modelo
    O modelo foi avaliado usando métricas como **acurácia** e **recall**, sendo o **recall** a métrica mais relevante neste caso, 
    pois queríamos garantir que a maioria dos alunos em risco fossem corretamente identificados.

    ### 7. Aplicação Interativa com Streamlit
    Finalmente, integramos o modelo em uma aplicação interativa com **Streamlit**, permitindo que o usuário insira os dados dos alunos 
    e obtenha previsões sobre o risco acadêmico em tempo real.
    """)
    st.markdown('')

# Criar as abas
abas = st.tabs(["📊 Conclusão", "🔧 Passo a Passo do Projeto"])

# Exibir o conteúdo de cada aba
with abas[0]:
    render_conclusao()

with abas[1]:
    render_referencias()
