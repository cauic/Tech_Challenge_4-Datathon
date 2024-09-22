
import streamlit as st
import streamlit.components.v1 as components
st.header(":orange[A Passos Mágicos]", divider="blue")




# Embed URL of the Power BI report
## Link para o site 

st.markdown("")


evento = st.selectbox("Selecione um evento:", [
    "Quem são",
    "O que fazem",
    "Impacto",
    "Apoie"
])

if evento == "Quem são":
    st.subheader(":red[Conhecendo a Passos Mágicos]", divider="blue")
    st.markdown('A Associação Passos Mágicos tem uma trajetória de 30 anos dedicada à transformação da vida de crianças e jovens de baixa renda em Embu-Guaçu. Fundada por Michelle Flues e Dimetri Ivanoff em 1992, a iniciativa começou em orfanatos locais e, em 2016, expandiu-se para um projeto social e educacional que oferece educação de qualidade, apoio psicológico e uma visão ampliada do mundo.')
    
    st.subheader(":violet[O que fazem]", divider="")
    st.markdown('A Associação oferece um programa educacional completo, que inclui aceleração do conhecimento, apoio psicopedagógico, e programas especiais como apadrinhamento e intercâmbio, visando integrar os alunos a diferentes culturas e ambientes.')

    st.subheader(":violet[Nossa história]", divider="")
    st.markdown('Desde 1992, a atuação da Passos Mágicos impacta centenas de crianças e jovens. Em 2023, mais de 1.100 crianças foram atendidas, com um crescente número de bolsistas e universitários beneficiados pelos programas oferecidos.')

    st.subheader(":violet[Nossa equipe]", divider="")
    st.markdown('A equipe da ONG é formada por profissionais comprometidos com a transformação educacional, atuando em áreas como psicologia, psicopedagogia, música, tecnologia, e mais, sempre priorizando a confiança e o desenvolvimento integral dos alunos.')

elif evento == "O que fazem":
    st.subheader(":red[Aceleração do Conhecimento]", divider="blue")
    st.markdown("""
    A Passos Mágicos oferece aulas de alfabetização, língua portuguesa e matemática para crianças e adolescentes de 7 a 17 anos, residentes em Embu-Guaçu. Os alunos são distribuídos em turmas de acordo com seu nível de conhecimento, determinado por uma prova de sondagem realizada no ingresso.
    
    Atualmente, 1.000 alunos efetivos estão distribuídos nas seguintes fases:
    - **Fase Alfabetização**: Destinada a alunos em fase de alfabetização ou com dificuldades na leitura e escrita. **20% dos alunos.**
    - **Fases 1 e 2**: Conteúdos do Ensino Fundamental 1, explorados em profundidade. **37% dos alunos.**
    - **Fases 3 e 4**: Conteúdos do Ensino Fundamental 2, com foco em aprofundamento. **24% dos alunos.**
    - **Fases 5 e 6**: Conteúdos para o Ensino Médio, com foco em jovens e adolescentes. **8% dos alunos.**
    - **Fases 7 e 8**: Preparação intensiva para vestibulandos e terceiranistas. **11% dos alunos.**
    """)

    st.markdown("""
    As aulas são estruturadas para desenvolver a criatividade e o interesse pelo conhecimento, com atividades que incluem leitura, escrita e projetos artísticos. Além disso, a ONG incentiva o desenvolvimento ético, promovendo um ambiente onde o aprendizado é compartilhado e voltado ao bem comum.
    """)

    st.subheader(":violet[Programas Educacionais]", divider="")
    st.markdown("""
    - **Programa Vem Ser**: Criado em parceria com a Rede Decisão, oferece plataformas de ensino para alunos do Ensino Médio e vestibulandos. Iniciativas incluem:
        - **Vem Ser Vestibular**: Focado na preparação para o Enem e vestibulares.
        - **Vem Ser Vestibulinho**: Preparação para alunos do 9º ano que desejam ingressar em escolas técnicas.
    
    - **Programa PAIDEIA**: Em 2019, através de uma parceria com a USP, adolescentes participaram de um curso intensivo de um ano na Escola Politécnica da USP. O programa abrangeu Sustentabilidade, Computação, e Programação. 
        - **40 alunos formados em 2019**
        - **22 alunos cursando em 2020**
    """)

    st.subheader(":violet[Assistência Psicológica]", divider="")
    st.markdown("""
    A Passos Mágicos entende que o suporte emocional é fundamental para o desempenho acadêmico. A ONG oferece acompanhamento psicológico tanto individual quanto coletivo, para alunos e seus responsáveis. Além dos atendimentos regulares, foram criados projetos específicos:
    
    - **Sacode a Poeira**: Focado na gestão do tempo e produtividade dos alunos.
    - **Eu no Comando**: Programa de orientação vocacional para vestibulandos indecisos.
    
    - **5000+ atendimentos psicológicos**
    - **800+ atendimentos psicopedagógicos**
    """)

    st.subheader(":violet[Ampliação da Visão de Mundo]", divider="")
    st.markdown("""
    A ONG promove a integração dos alunos com diversos elementos culturais através de visitas a museus, parques e eventos. Além disso, são oferecidas aulas de inglês para alunos a partir da fase 3, com oportunidades de participação em programas de intercâmbio. O objetivo é expandir a visão de mundo dos alunos e proporcionar contato com diferentes culturas.
    """)

if evento == "Impacto":
    st.subheader(":red[Indicadores de Impacto em 2023]", divider="blue")
    
    # Indicadores principais
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Pessoas Impactadas", value="4.400")
    with col2:
        st.metric(label="Alunos no Programa", value="1.100")

    # Distribuição dos alunos por fase com destaque
    st.markdown("---")  # Linha divisória
    st.markdown("### :blue[Distribuição dos Alunos por Fase]")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Alfabetização", value="20%")
    with col2:
        st.metric(label="Fases 1 e 2", value="37%")
    with col3:
        st.metric(label="Fases 3 e 4", value="24%")
    with col4:
        st.metric(label="Fases 5 e 6", value="8%")
    with col5:
        st.metric(label="Fases 7 e 8", value="11%")
    
    # Indicadores de Bolsistas e Universitários com destaque
    st.markdown("---")  # Linha divisória
    st.markdown("### :blue[Indicadores de Bolsistas e Universitários]")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Bolsistas em Escolas Particulares", value="98")
    with col2:
        st.metric(label="Universitários Atuais", value="103")
    with col3:
        st.metric(label="Universitários Formados", value="41")

elif evento == "Apoie":
    st.subheader(":red[Apadrinhando um aluno]", divider="blue")
    st.markdown("""
    Ao apadrinhar um aluno, a parceria é firmada diretamente com a instituição de ensino. O padrinho deve efetuar o pagamento diretamente à escola, garantindo que um de nossos alunos tenha acesso a uma educação de qualidade em uma das escolas particulares parceiras.
    
    - **Valor anual:** R$ 13.500
    - **Benefício:** Matrícula de um aluno em uma escola parceira
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #28a745; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Doar R$ 13.500 anuais</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":red[Contribuindo com nosso Programa de Aceleração]", divider="blue")
    st.markdown("""
    Ao contribuir com nosso Programa de Aceleração, você nos ajuda a promover educação de qualidade e o desenvolvimento de habilidades socioemocionais para crianças e jovens de baixa renda em situação de vulnerabilidade.
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero doar</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Doando itens para nossas campanhas]", divider="")
    st.markdown("""
    Você também pode contribuir com nossas campanhas anuais de arrecadação. Sua ajuda se transformará em momentos especiais para os alunos e suas famílias:
    
    - **Materiais escolares:** Doação de materiais para alunos bolsistas e em geral
    - **Páscoa Mágica:** Arrecadação de ovos de páscoa e chocolates
    - **Dia das Crianças:** Arrecadação de brinquedos
    - **Campanha do Agasalho:** Arrecadação de roupas de inverno
    - **Natal Mágico:** Arrecadação de roupas, calçados, brinquedos, e livros
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero contribuir</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Sendo voluntário em uma ação]", divider="")
    st.markdown("""
    Participe de nossas ações interagindo com os alunos, compartilhando experiências e conhecimento. Você também pode desenvolver uma ação voltada para a ampliação da visão de mundo dos alunos.
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero ser voluntário</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Participando dos nossos jantares]", divider="")
    st.markdown("""
    Mensalmente, promovemos jantares para apresentar a ONG e seus programas. Estes eventos são oportunidades para conhecer nosso trabalho e se tornar um parceiro. Fique atento aos convites via Instagram ou cadastre-se para recebê-los.
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero participar</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Criando seu 'Niver do Bem']", divider="")
    st.markdown("""
    Transforme sua comemoração de aniversário em uma festa solidária, trocando presentes por doações:
    
    - **Crie um evento:** Cadastre seu evento e indique uma instituição
    - **Divulgue:** Compartilhe o link do evento com seus convidados
    - **Multiplique a felicidade:** Convidados fazem as doações no site, e o dinheiro é repassado à instituição escolhida
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Criar evento</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Apoio ao programa de intercâmbio]", divider="")
    st.markdown("""
    Contribua para a integração dos alunos com diferentes ambientes e culturas, apoiando nosso programa de intercâmbio.
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero apoiar</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )

    st.subheader(":blue[Tornando-se uma empresa apoiadora]", divider="")
    st.markdown("""
    Como empresa, seu apoio é essencial para impactar muitas vidas. Além do financiamento, sua empresa pode conectar crianças e jovens com profissionais, contribuindo para um futuro melhor. Nossos focos de atuação incluem:
    
    - **ODS 1:** Erradicação da Pobreza
    - **ODS 4:** Educação de Qualidade
    - **ODS 5:** Igualdade de Gênero
    - **ODS 8:** Trabalho Decente
    - **ODS 10:** Redução das Desigualdades
    """)
    st.markdown(
        """
        <a href='https://api.whatsapp.com/send/?phone=5511982083282&text&type=phone_number&app_absent=0' 
        style='display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-align: center; 
        text-decoration: none; border-radius: 5px;'>Quero ser uma empresa parceira</a>
        <p style='font-size: 12px; color: gray; text-align: left;'>Este é um contato oficial da ONG Passos Mágicos.</p>
        """, 
        unsafe_allow_html=True
    )
