import pandas as pd
import plotly.express as px
import streamlit as st
import locale

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

# Função para renderizar a subaba Tech Challenge 5
def render_tech_challenge_5():
    st.header(":orange[Tech Challenge 5 | Datathon]", divider="blue")
    st.markdown("## Iluminando Vidas: Um Projeto de Impacto Social")
    st.write("")
    st.markdown('### Objetivo') 
    st.markdown('Esse é um projeto da pós-graduação em Data Analytics pela FIAP.')
    st.markdown('Nosso objetivo é criar uma solução preditiva que demonstre o impacto da ONG Passos Mágicos na comunidade que atende.')
    st.markdown('Essa ONG, que atua há 31 anos em um município carente de São Paulo, busca transformar vidas por meio da educação. O desafio inclui análise e visualização de dados, machine learning e o deploy em produção.')
    st.markdown('### Autores')
    st.markdown('Laio Soares')
    st.markdown('Emerson Cauic')

# Função para renderizar a subaba Introdução
def render_introducao():
    st.header(":orange[Introdução]", divider="blue")
    st.markdown('O projeto "Iluminando Vidas" visa revelar e amplificar o impacto da ONG Passos Mágicos, que há mais de três décadas atua como farol de esperança para crianças e jovens em situação de vulnerabilidade.')
    st.markdown('Neste desafio, trabalharemos com dados educacionais e socioeconômicos dos estudantes atendidos pela ONG. A análise focará em identificar os resultados e benefícios proporcionados pela educação oferecida, utilizando técnicas avançadas de análise de dados e machine learning.')
    st.markdown('O resultado final será uma aplicação que ajude a ONG a ampliar o seu impacto social. ALém disso, será apresentada em um dashboard interativo e a solução preditiva será implementada via Streamlit.')

tab1, tab2 = st.tabs(["Tech Challenge 5", "Introdução"])
with tab1:
    render_tech_challenge_5()
with tab2:
    render_introducao()
