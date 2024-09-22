import streamlit as st
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, accuracy_score
from imblearn.over_sampling import SMOTE

# Título do aplicativo
st.header(":orange[Modelo - Gradient Boosting]", divider="blue")
st.write("Predição de Alunos em Risco de Desempenho Acadêmico")
# Descrição
st.write("")
st.write("")
st.write("""
    ### O que significa estar em "Risco"?
    Nesta aplicação, utilizamos um modelo de **Gradient Boosting** para prever se um aluno está em risco de ter um desempenho acadêmico 
    insatisfatório, sendo classificado na categoria de **Quartzo** — conhecida como a pedra de menor desempenho no contexto educacional.
    
    Os alunos são avaliados em várias disciplinas e índices acadêmicos, como as notas de Português, Matemática, Inglês, 
    além de indicadores como o **Índice de Engajamento Geral (IEG)** e o **Índice de Aproveitamento Acadêmico (IAA)**.

    ### O que é a Pedra Quartzo?
    A **Pedra Quartzo** representa o nível mais crítico de desempenho acadêmico entre as classificações. Estar na **pedra Quartzo** significa que o aluno
    está com grandes dificuldades e precisa de acompanhamento mais próximo para evitar a reprovação ou abandono escolar.
    
    O modelo visa ajudar a identificar esses alunos em risco com base nas informações fornecidas, permitindo que intervenções sejam realizadas a tempo.
""")

# Função para coletar entradas do usuário
def coletar_entradas_usuario():
    nota_port = st.number_input("Nota de Português", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    nota_mat = st.number_input("Nota de Matemática", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    nota_ing = st.number_input("Nota de Inglês", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    ano_ingresso = st.number_input("Ano de Ingresso", min_value=2000, max_value=2024, value=2020)
    ieg = st.number_input("Índice IEG", min_value=0.0, max_value=5.0, value=5.0, step=0.1)
    iaa = st.number_input("Índice IAA", min_value=0.0, max_value=5.0, value=5.0, step=0.1)
    
    # Criar um dicionário com os valores
    dados_usuario = {
        'IEG_2022': [ieg],
        'IAA_2022': [iaa],
        'ANO_INGRESSO_2022': [ano_ingresso],
        'NOTA_PORT_2022': [nota_port],
        'NOTA_MAT_2022': [nota_mat],
        'NOTA_ING_2022': [nota_ing]
    }
    
    return pd.DataFrame(dados_usuario)

# Carregar o dataset e preparar os dados
@st.cache_data
def carregar_dados():
    data = pd.read_csv('PEDE_PASSOS_DATASET_FIAP.csv', sep=';')
    data = data[['PEDRA_2022', 'IEG_2022', 'IAA_2022', 'ANO_INGRESSO_2022', 'NOTA_PORT_2022', 'NOTA_MAT_2022', 'NOTA_ING_2022']]
    data['RISCO'] = data['PEDRA_2022'].apply(lambda x: 1 if x == 'Quartzo' else 0)
    data = data.drop(columns=['PEDRA_2022'])
    data.fillna(data.median(), inplace=True)
    return data

# Treinar o modelo de Gradient Boosting
@st.cache_resource
def treinar_modelo():
    data = carregar_dados()
    X = data.drop(columns=['RISCO'])
    y = data['RISCO']
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Aplicar SMOTE para balancear as classes
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
    
    # Treinar o modelo
    model_gb = GradientBoostingClassifier(learning_rate=0.1, max_depth=3, n_estimators=200, random_state=42)
    model_gb.fit(X_train_balanced, y_train_balanced)
    
    # Calcular a acurácia e o recall no conjunto de teste
    y_pred_test = model_gb.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred_test)
    recall = recall_score(y_test, y_pred_test)
    
    return model_gb, acuracia, recall

# Carregar o modelo treinado, acurácia e recall
modelo_gb, acuracia_modelo, recall_modelo = treinar_modelo()

# Coletar as entradas do usuário
dados_usuario = coletar_entradas_usuario()

# Prever o risco
if st.button("Prever Risco"):
    st.write("Dados fornecidos pelo usuário:")
    st.write(dados_usuario)

    predicao = modelo_gb.predict(dados_usuario)
    probabilidade = modelo_gb.predict_proba(dados_usuario)[0][1]  # Probabilidade do aluno estar em risco
    
    if predicao[0] == 1:
        st.error(f"O aluno está em risco!")
    else:
        st.success(f"O aluno não está em risco.")

# Exibir a acurácia e recall como cartões fixos
col1, col2 = st.columns(2)
with col1:
    st.metric("Acurácia Global do Modelo", f"{acuracia_modelo * 100:.2f}%")
with col2:
    st.metric("Recall Global do Modelo", f"{recall_modelo * 100:.2f}%")

# Explicação sobre a escolha da métrica Recall
st.write("""
    ### Métricas de Avaliação
    A **Acurácia** indica a porcentagem de previsões corretas do modelo, enquanto o **Recall** mede a capacidade
    do modelo de identificar corretamente os alunos que estão em risco. No contexto educacional, o **Recall** é particularmente importante, 
    pois queremos garantir que a maioria dos alunos que realmente estão em risco sejam identificados para que intervenções possam ser feitas a tempo.
""")
