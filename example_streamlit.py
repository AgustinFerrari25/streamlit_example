import streamlit as st
import pandas as pd

st.header("Ejemplo de uso de Streamlit")

st.write("Mi nombre es *Agustin*")

df=pd.DataFrame({'primera columna':[1,2,3,4,5],
                'segunda columna':[10,20,30,40,50]}
                )

st.write(df)


st.write("----------------------------------------------------")
if st.button("hola"):
    st.write("buen dia")
else:
    st.write("chau")

number=st.slider("edad:", min_value=0, max_value=100, value=None, step=2, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

options=('Dog', 'Cat', 'Mouse')
radio=st.radio("Pick one", options, index=0, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False, captions=None, label_visibility="visible")


if radio=='Dog':
    st.write("El perro, llamado perro doméstico o can, y en algunos lugares coloquialmente llamado chucho, tuso, choco, entre otros; es un mamífero carnívoro de la familia de los cánidos, que constituye una especie del género Canis")
elif radio=='Cat':
    st.write("El gato doméstico llamado más comúnmente gato, y de forma coloquial minino, michino, y algunos nombres más, es un mamífero carnívoro de la familia Felidae. El nombre actual en muchas lenguas proviene del latín vulgar catus")
elif radio=='Mouse':
    st.write("Mus es un género de roedores miomorfos de la familia Muridae que incluye la mayoría de los roedores llamados comúnmente ratones, si bien el nombre de ratón se usa para varias especies más pertenecientes a otros géneros. También se les conoce con el nombre de pericotes, lauchas o mineros")




