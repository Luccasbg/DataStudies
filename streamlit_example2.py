# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:48:46 2022

@author: Luccas
"""

import pandas as pd
import streamlit as st

df = pd.read_csv('covid-variants.csv')

variante = list(df['variant'].unique())
pais = list(df['location'].unique())

df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

st.selectbox('Escolha o país', ['Todos'] + pais)
st.selectbox('Escolha a variante', ['Todas'] + variante)


