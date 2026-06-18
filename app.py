import streamlit as st 

generos = {
    'Trap' : {
        'Veigh' : 'https://www.youtube.com/watch?v=dkWyAlBUY20&list=RDdkWyAlBUY20&start_radio=1',
        'Teto' : 'https://www.youtube.com/watch?v=lxNS0yOZr1Q&list=RDlxNS0yOZr1Q&start_radio=1'
    },
    'Sertanejo' : {
        'Gustavo Lima' : 'https://www.youtube.com/watch?v=Uo7U7ruedic&list=PLG6ju-QvABa1NlvjmRC48ASsmEKzw6YM1',
        'Mari Fernandes' : 'https://www.youtube.com/watch?v=AxfqpsumkqM'
    },  
    'Pagode' : {
        'Péricles' : 'https://www.youtube.com/watch?v=T3Y6RRSDm4o&list=RDT3Y6RRSDm4o&start_radio=1',
        'Tiaguinho' : 'https://www.youtube.com/watch?v=qUqc_cYejX0'
    },
    'Eletronica' : {
        'Alok' : 'https://www.youtube.com/watch?v=JVpTp8IHdEg',
        'Calvin Harris' : 'https://www.youtube.com/watch?v=ebXbLfLACGM'
    }
}

st.sidebar.title('DJ NEY')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)
video, sobre = st.tabs(['Video', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Veigh':
     st.markdown('''
         Veigh (12 de setembro de 2001), nome artístico de Thiago Veigh da Silva, nasceu em Itapevi (SP) e se tornou um dos principais nomes do trap brasileiro. Suas músicas retratam experiências pessoais, conquistas e a realidade da periferia. O artista acumula mais de 4,6 bilhões de reproduções no Spotify e cerca de 1,4 bilhão de visualizações no YouTube
         ''')
     st.image('veigh.png')
     

    elif artista == 'Teto':
        st.markdown('''
        Teto (19 de outubro de 2001), nome artístico de Clériton Sávio Santos Silva, nasceu em Jacobina (BA) e ganhou destaque no trap nacional com suas letras melódicas e sucessos como "M4" e "Fim de Semana no Rio". O artista acumula mais de 2 bilhões de reproduções nas plataformas digitais.
        ''')
        st.image('teto.png')

    elif artista == 'Gustavo Lima':
        st.markdown('''
        Gusttavo Lima (3 de setembro de 1989), nome artístico de Nivaldo Batista Lima, nasceu em Presidente Olegário (MG) e é um dos maiores nomes do sertanejo brasileiro. Conhecido por hits como "Balada" e "Bloqueado", o cantor soma bilhões de reproduções e visualizações nas plataformas digitais.
        ''')
        st.image('gustavo.png')

    elif artista == 'Mari Fernandes':
        st.markdown('''
        Mari Fernandes (19 de fevereiro de 2001), nasceu em Alto Santo (CE) e se destacou no piseiro e forró. Com músicas como "Comunicação Falhou" e "Parada Louca", a cantora acumula centenas de milhões de reproduções nas plataformas digitais.
        ''')
        st.image('fernandes.png')

    elif artista == 'Péricles':
        st.markdown('''
        Péricles (22 de junho de 1969), nasceu em Santo André (SP) e se tornou um dos maiores nomes do pagode brasileiro. Ex-vocalista do Exaltasamba, o cantor possui uma carreira consolidada com milhões de ouvintes e visualizações.
        ''')
        st.image('pericles.png')

    elif artista == 'Tiaguinho':
        st.markdown('''
        Thiaguinho (11 de março de 1983), nome artístico de Thiago André Barbosa, nasceu em Presidente Prudente (SP). Ex-integrante do Exaltasamba, é um dos principais nomes do pagode brasileiro e acumula bilhões de reproduções nas plataformas digitais.
        ''')
        st.image('tiaguinho.png')

    elif artista == 'Alok':
        st.markdown('''
        Alok (26 de agosto de 1991), nome artístico de Alok Achkar Peres Petrillo, nasceu em Goiânia (GO) e é um dos DJs mais famosos do mundo. Com sucessos como "Hear Me Now" e "Deep Down", acumula bilhões de reproduções nas plataformas digitais.
        ''')
        st.image('alok.png')

    elif artista == 'Calvin Harris':
        st.markdown('''
        Calvin Harris (17 de janeiro de 1984), nome artístico de Adam Richard Wiles, nasceu em Dumfries, Escócia. Considerado um dos maiores DJs e produtores musicais do mundo, possui inúmeros sucessos e mais de 20 bilhões de reproduções em suas músicas.
        ''')
        st.image('calvin.png')
