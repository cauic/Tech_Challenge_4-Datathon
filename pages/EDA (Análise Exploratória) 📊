import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Carregar o dataset
df = pd.read_csv('PEDE_PASSOS_DATASET_FIAP.csv', sep=';')

# Título da página
st.header(":orange[Análise Exploratória de Dados]", divider="blue")

# Seção: Exibição do Dataset e Resumo
st.markdown('### Base de Dados')
st.write('Esta base de dados contém informações de desempenho de alunos em diversas métricas (como INDE) durante os anos de 2020, 2021 e 2022. O objetivo desta análise é explorar as variações e padrões desses dados ao longo dos anos, e identificar valores anômalos ou padrões interessantes que possam ser observados.')

# Exibir as primeiras linhas do dataset
st.dataframe(df.head())

# Seção: Dados Nulos
st.markdown('### Dados Nulos')
nulos = pd.DataFrame(df.isnull().sum(), columns=['Quantidade de Nulos'])
nulos['Percentual de Nulos (%)'] = (nulos['Quantidade de Nulos'] / len(df) * 100).round(2)
st.write(nulos)

# Explicação sobre os dados nulos
st.markdown('Os dados nulos podem ocorrer porque esta é uma série temporal. Alguns alunos podem não ter participado em determinados anos, o que justifica a ausência de dados nas colunas de anos específicos. Isso é comum quando estamos lidando com informações que se estendem por vários períodos.')

# Gráfico de barras para visualizar a quantidade de dados nulos
nulos_plot = pd.DataFrame({'Colunas': df.columns, 'Nulos': df.isnull().sum().values})
fig_nulos = px.bar(nulos_plot, x='Colunas', y='Nulos', title='Quantidade de Dados Nulos por Coluna')
fig_nulos.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig_nulos)

# Seção: Resumo Estatístico
st.markdown('### Resumo Estatístico')
resumo_estatistico = df.describe().T
st.write(resumo_estatistico)

# Seção: Tipos de Dados
st.markdown('### Tipos de Dados')
tipos_dados = pd.DataFrame(df.dtypes, columns=['Tipo de Dado'])
st.write(tipos_dados)

# Boxplot para as três colunas INDE
st.markdown('### Boxplot para Variáveis INDE')

# Filtrando as colunas INDE
inde_columns = ['INDE_2020', 'INDE_2021', 'INDE_2022']
df_inde = df[inde_columns]

# Converter as colunas INDE para numéricas, forçando erros a serem convertidos para NaN
for col in inde_columns:
    df_inde[col] = pd.to_numeric(df_inde[col], errors='coerce')

# Verificar se as colunas estão presentes no dataframe
if all(col in df.columns for col in inde_columns):
    # Criar o boxplot com Plotly
    df_melted = df_inde.melt(var_name="Ano", value_name="INDE")
    fig_inde = px.box(df_melted, x="Ano", y="INDE", points="all", title="Distribuição de INDE por Ano")
    st.plotly_chart(fig_inde)

    st.markdown('O boxplot acima exibe a distribuição das variáveis INDE para os anos de 2020, 2021 e 2022. Isso ajuda a visualizar como os alunos se comportaram ao longo dos anos, identificando possíveis outliers e variações no desempenho.')




# Função para detectar outliers e calcular limites
def detectar_outliers(df_col):
    # Converter valores para numéricos e remover valores NaN
    df_col_clean = pd.to_numeric(df_col, errors='coerce').dropna()

    # Se a coluna estiver vazia após a conversão, retornar None
    if df_col_clean.empty:
        return None, None, None

    # Calcular limites
    limite_superior = round(df_col_clean.mean() + 3 * df_col_clean.std(), 2)
    limite_inferior = round(df_col_clean.mean() - 3 * df_col_clean.std(), 2)

    # Identificar outliers
    outliers = df_col_clean[(df_col_clean > limite_superior) | (df_col_clean < limite_inferior)]
    return outliers, limite_inferior, limite_superior

# Detectar e exibir outliers para cada INDE (2020, 2021, 2022)
inde_columns = ['INDE_2020', 'INDE_2021', 'INDE_2022']

for col in inde_columns:
    st.markdown(f'### Outliers em {col}')
    outliers, limite_inferior, limite_superior = detectar_outliers(df[col])

    # Verificar se houve um erro na conversão dos dados (coluna vazia ou inválida)
    if outliers is None:
        st.write(f'Os dados na coluna {col} estão vazios ou não numéricos. Não foi possível calcular os outliers.')
    else:
        # Exibir os limites
        st.write(f"Limite Inferior: {limite_inferior}, Limite Superior: {limite_superior}")

        # Verificar se há outliers
        if not outliers.empty:
            # Filtrar o dataset para os alunos com outliers
            outliers_detalhes = df[df[col].isin(outliers)]

            # Verificar se o DataFrame de outliers está vazio antes de exibir
            if not outliers_detalhes.empty:
                # Exibir o nome, valor do INDE e demais variáveis
                st.write(outliers_detalhes[['NOME', col] + [c for c in df.columns if c != 'NOME' and c != col]])
            else:
                st.write(f'Nenhum outlier detectado em {col}.')
        else:
            st.write(f'Nenhum outlier detectado em {col}.')
