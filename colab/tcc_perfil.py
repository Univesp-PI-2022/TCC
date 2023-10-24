from pysus.online_data.sinasc import download
from pysus.online_data import parquets_to_dataframe
from pysus.online_data import SINAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from unidecode import unidecode
import unicodedata

#from pandas_profiling import ProfileReport

df = pd.read_csv('/Users/walterjr/Downloads/violencia_2009_2021_tratado_novo.csv', encoding='utf-8')
df_visao = df.head(10)
df_filtrado = df[df['LES_AUTOP'] == 'Não']
df_filtrado_visao = df_filtrado.head(10)

# Perfil

df_perfil = df_filtrado[['CS_RACA', 'CS_ESCOL_N','LOCAL_OCOR']].describe()

raca_counts = df_filtrado['CS_RACA'].value_counts()
escolaridade_counts = df_filtrado['CS_ESCOL_N'].value_counts()
local_counts = df_filtrado['LOCAL_OCOR'].value_counts()



# testes

import matplotlib.pyplot as plt
import seaborn as sns

# Definir a ordem desejada para as categorias
ordem_raca = df_filtrado['CS_RACA'].value_counts().index
ordem_escolaridade = df_filtrado['CS_ESCOL_N'].value_counts().index
ordem_local = df_filtrado['LOCAL_OCOR'].value_counts().index

# Gráfico de barras para raça
plt.figure(figsize=(12, 10))
sns.countplot(data=df_filtrado, x='CS_RACA', order=ordem_raca)
plt.title('Distribuição de Raça')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus
plt.show()

# Gráfico de barras para escolaridade
plt.figure(figsize=(12, 10))
sns.countplot(data=df_filtrado, x='CS_ESCOL_N', order=ordem_escolaridade)
plt.title('Distribuição de Escolaridade')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus
plt.show()

# Gráfico de barras para local de ocor
plt.figure(figsize=(12, 10))
sns.countplot(data=df_filtrado, x='LOCAL_OCOR', order=ordem_local)
plt.title('Distribuição de LOCAL DA OCORRÊNCIA')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus
plt.show()