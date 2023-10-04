import streamlit as stimport 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as graphvizst
from dotenv import dotenv_values,load_dotenv
import os
import seaborn as sns

ENV = dotenv_values(".env")
load_dotenv(override=False)

#Cargar el dataset
df = pd.read_csv(os.environ['DATASETS_PATH']+'/diabetes.csv')
df

var = 'Pregnancies'
var_title = 'Numero de Embarazos'

# Ajustes de la figura de Matplotlib
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(11, 4), sharex=True)

# Plotea el histograma
sns.histplot(data=df[var], ax=ax[0], kde=False)
ax[0].set_xlabel(var_title)
ax[0].set_ylabel('Frecuencia')

# Plotea la curva de densidad
sns.kdeplot(data=df[var], ax=ax[1], fill=True)
ax[1].set_xlabel(var_title)
ax[1].set_ylabel('Densidad')

fig.suptitle('Análisis Univariado de la ' + var_title)

plt.tight_layout()
st.pyplot(fig)

#--------------------
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

#Line chart
df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)

#Bar Chart
df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)

#area_chart
df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)

#pairplot
df= pd.DataFrame(np.random.randn(500, 3),    columns=['x', 'y','z'])
c = alt.Chart(df).mark_circle().encode(
    x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z']
    )
st.altair_chart(c, use_container_width=True)

#Diagram
st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

#maps
df = pd.DataFrame(np.random.randn(500, 2) + [23.634501, -102.552784],columns=['lat', 'lon'])
st.map(df)

