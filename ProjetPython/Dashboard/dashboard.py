import streamlit as st
import pandas as pd
import plost 
#for plost documentation
#https://pypi.org/project/Plost/
#https://plost.streamlit.app/


#Importation css
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Création du menu déroulant et gestion des paramètres :

st.sidebar.header("CONSOMMATION DE DROGUE")
st.sidebar.subheader('Paramètres histogrammes')
hist_xaxis = st.sidebar.selectbox('Xaxis selon ', ('Age', 'Education_level')) 

st.sidebar.subheader('Donut chart parameter')
donut_axis = st.sidebar.selectbox('Select data', ('Sexe', 'Country','Ethnicity'))

st.sidebar.subheader('Boxplots parameter')
boxplot_yaxis = st.sidebar.selectbox('Select data', ('Neuroticism','Extraversionness','Openness','Agreability','Conscientiousness','Impulsiveness','Sensation_Seeking'))


# Row A
st.markdown('### DESCRIPTION DATASET')
col1, col2, col3 = st.columns(3)
col1.metric("Observations:", "1885", "Individus")
col2.metric("Features:", "13", "Var explicatives")
col3.metric("Targets :", "19", "Drogues")

#Import the dataset
df_drugs = pd.read_csv("df_drugs.csv")

#GRAPHICS row b
#data histo:
df_a=df_drugs[[hist_xaxis,"ID"]].groupby(hist_xaxis).count()
df_a.reset_index(inplace=True)
#data for pie plot
df_donut=df_drugs[[donut_axis,'ID']].groupby(donut_axis).count()
df_donut.reset_index(inplace=True)
c1,c2=st.columns(2)
with c1:
    texte="Histogramme de consommateurs selon "+hist_xaxis
    st.markdown('##### '+texte)
    plost.bar_chart(data=df_a,
     bar=hist_xaxis, 
     value="ID", 
     width=0, 
     height=0,
     color='#deef9f',
      use_container_width=True)
with c2:
    texte=' Distribution nombres consommateurs selon '+ donut_axis
    st.markdown('##### '+texte)
    plost.donut_chart(
        data=df_donut,
        theta='ID',
        color=donut_axis,
        legend='bottom', 
        use_container_width=True)

#GRAPHICS row c
c3,c4=st.columns(2)
#data
df_age=df_drugs[["Age","ID",boxplot_yaxis]].groupby(["Age",boxplot_yaxis]).count()
df_age.reset_index(inplace=True)

df_edL=df_drugs[["Education_level","ID",boxplot_yaxis]].groupby(["Education_level",boxplot_yaxis]).count()
df_edL.reset_index(inplace=True)

with c3:
    texte="Nombre de personnes par degré de "+ boxplot_yaxis + " par age"
    st.markdown('##### '+texte)
    plost.scatter_chart(
    data=df_age,
    x='Age',
    y=boxplot_yaxis,
    color='#9fefb8',
    size='ID',
    width=250,
    height=450)
with c4:
    texte="Nombre de personnes par degré de "+ boxplot_yaxis + " par niveau d'éducation"
    st.markdown('##### '+texte)
    plost.scatter_chart(
    data=df_edL,
    x='Education_level',
    y=boxplot_yaxis,
    color='#deef9f',
    size='ID',
    width=250,
    height=600)

   