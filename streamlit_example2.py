# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:48:46 2022

@author: Luccas
"""

import pandas as pd
import streamlit as st

df = pd.read_csv('covid-variants.csv') #lendo tabela excel

variantes = list(df['variant'].unique())
paises = list(df['location'].unique())

df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

pais = st.sidebar.selectbox('Escolha o país', ['Todos'] + paises)
variante = st.sidebar.selectbox('Escolha a variante', ['Todas'] + variantes)

if(pais != 'Todos'):
    st.header('Mostrando resultados de ' + pais)
    df = df[df['location'] == pais]
else:
    st.header('Mostrando resultados para todos os países')
    
if(variante != 'Todas'):
    st.subheader('Mostrando resultados para variante ' + variante)
    df = df[df['variant'] == variante]
    
else:
    st.subheader('Mostrando resultados para todas as variantes')
    
dfShow = df.groupby(by = ['date']).sum()

import plotly.express as px
fig = px.line(dfShow, x = dfShow.index, y = 'num_sequences')
fig.update_layout(title = 'casos diários de covid 19')
st.plotly_chart(fig, use_container_width= True)

