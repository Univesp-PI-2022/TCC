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

df_visao_filtrado = df_filtrado.head(10)

df_pop = pd.read_csv('/Users/walterjr/Downloads/ibge_cnv_popsvsbr205141187_3_174_108.csv', encoding='utf-8',sep=',')
df_pop = df_pop.dropna(axis=0)
# http://tabnet.datasus.gov.br/cgi/tabcgi.exe?ibge/cnv/reprojpopuf.def


ocorrencias_por_ano_estado = df_filtrado.groupby(['NU_ANO', 'SG_UF'])['DT_OCOR'].count()
grupos_por_ano = ocorrencias_por_ano_estado.groupby('NU_ANO')

dataframes_por_ano = {}  # Dicionário para armazenar os DataFrames por ano

for ano, grupo in grupos_por_ano:
    dataframes_por_ano[ano] = grupo.copy()  # Cria uma cópia do grupo e armazena no dicionário

df_2017 = dataframes_por_ano[2017]
df_2018 = dataframes_por_ano[2018]
df_2019 = dataframes_por_ano[2019]

df_2020 = dataframes_por_ano[2020]
df_2021 = dataframes_por_ano[2021]

df_2017 = df_2017.to_frame()
df_2018 = df_2018.to_frame()
df_2019 = df_2019.to_frame()
df_2020 = df_2020.to_frame()
df_2021 = df_2021.to_frame()

df_2017 = df_2017.reset_index()
df_2018 = df_2018.reset_index()
df_2019 = df_2019.reset_index()
df_2020 = df_2020.reset_index()
df_2021 = df_2021.reset_index()

anos = ['2017', '2018','2019','2020','2021']

# Dicionário para armazenar os DataFrames separados
dataframes_por_ano_pop = {}

# Loop para criar DataFrames separados para cada ano
for ano in anos:
    # Seleciona as colunas específicas para o ano atual
    colunas_selecionadas = ['Unidade da Federação', ano]
    df_ano = df_pop[colunas_selecionadas]
    
    # Define o ano como chave no dicionário de DataFrames
    dataframes_por_ano_pop[ano] = df_ano

df_pop_2017 = dataframes_por_ano_pop['2017']
df_pop_2018 = dataframes_por_ano_pop['2018']
df_pop_2019 = dataframes_por_ano_pop['2019']
df_pop_2020 = dataframes_por_ano_pop['2020']
df_pop_2021 = dataframes_por_ano_pop['2021']

df_pop_2017['Unidade da Federação'] = df_pop_2017['Unidade da Federação'].str[3:]
       
df_pop_2018['Unidade da Federação'] = df_pop_2018['Unidade da Federação'].str[3:]
       
df_pop_2019['Unidade da Federação'] = df_pop_2019['Unidade da Federação'].str[3:]
              
df_pop_2020['Unidade da Federação'] = df_pop_2020['Unidade da Federação'].str[3:]
              
df_pop_2021['Unidade da Federação'] = df_pop_2021['Unidade da Federação'].str[3:]
              
       
df_pop_2017 = df_pop_2017.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2018 = df_pop_2018.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2019 = df_pop_2019.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2020 = df_pop_2020.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2021 = df_pop_2021.sort_values(by='Unidade da Federação', ascending=True)

df_pop_2017 = df_pop_2017.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2018 = df_pop_2018.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2019 = df_pop_2019.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2020 = df_pop_2020.sort_values(by='Unidade da Federação', ascending=True)
df_pop_2021 = df_pop_2021.sort_values(by='Unidade da Federação', ascending=True)

df_pop_2017 = df_pop_2017.reset_index()
df_pop_2018 = df_pop_2018.reset_index()
df_pop_2019 = df_pop_2019.reset_index()
df_pop_2020 = df_pop_2020.reset_index()
df_pop_2021 = df_pop_2021.reset_index()





df_2017['resultado'] = (df_2017['DT_OCOR'] / df_pop_2017['2017'])*100000
df_2018['resultado'] = (df_2018['DT_OCOR'] / df_pop_2018['2018'])*100000
df_2019['resultado'] = (df_2019['DT_OCOR'] / df_pop_2019['2019'])*100000
df_2020['resultado'] = (df_2020['DT_OCOR'] / df_pop_2020['2020'])*100000
df_2021['resultado'] = (df_2021['DT_OCOR'] / df_pop_2021['2021'])*100000

agrupado2017 = df_2017.sort_values(by='resultado', ascending=False).reset_index()
agrupado2018 = df_2018.sort_values(by='resultado', ascending=False).reset_index()
agrupado2019 = df_2019.sort_values(by='resultado', ascending=False).reset_index()
agrupado2020 = df_2020.sort_values(by='resultado', ascending=False).reset_index()
agrupado2021 = df_2021.sort_values(by='resultado', ascending=False).reset_index()


# Gráficos


# Adicionar uma coluna 'Ano' para diferenciar os dados de 2020 e 2021
agrupado2017['Ano'] = 2017
agrupado2018['Ano'] = 2018
agrupado2019['Ano'] = 2019
agrupado2020['Ano'] = 2020
agrupado2021['Ano'] = 2021

# Concatenar os DataFrames em um único DataFrame
combined_data1 = pd.concat([agrupado2017,agrupado2018,agrupado2019])
combined_data2= pd.concat([agrupado2020,agrupado2021])



########### ordem de 2017 ok mas 18 e 19 nao
import pandas as pd
import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.io as pio


anos = [2017, 2018, 2019]
#combined_fig.update_layout(width=1500)  # Aumentar a largura do gráfico
#combined_fig.update_xaxes(range=[0, len(df_ano)])  # Definir os limites de exibição horizontal

# Criar uma lista para armazenar os gráficos individuais
figs = []

for ano in anos:
    # Filtrar o DataFrame para o ano atual
    df_ano = globals()[f'agrupado{ano}']
    
    # Ordenar o DataFrame pela coluna 'DT_OCOR' em ordem decrescente
    df_ano = df_ano.sort_values(by='resultado', ascending=False)
    
    # Criar o gráfico de barras para o ano atual
    fig = go.Figure(data=[go.Bar(x=df_ano['SG_UF'], y=df_ano['resultado'],
                                text=df_ano['resultado'], texttemplate='%{y}', textposition='outside')])
    
    fig.update_layout(xaxis_tickangle=45, xaxis_title='Estado', yaxis_title='Número de ocorrências para cada 100 mil habitantes',
                      title=f'Número de ocorrências por Estado - {ano}')
    
    figs.append(fig)

# Organizar os gráficos em uma única figura
combined_fig = sp.make_subplots(rows=1, cols=len(figs), subplot_titles=[str(ano) for ano in anos])

for i, fig in enumerate(figs):
    combined_fig.add_trace(fig.data[0], row=1, col=i + 1) 

combined_fig.update_layout(title='Número de ocorrências por Estado 2017-2019 para cada 100 mil habitantes')

# Exibir a figura
pio.show(combined_fig)

# Salvar a figura como HTML
pio.write_html(combined_fig, file='gráfico_interativo_por_estado_100k_2017-2019.html', auto_open=True)

# testes

anos = [2020,2021]
# combined_fig.update_layout(width=1500)  # Aumentar a largura do gráfico
# combined_fig.update_xaxes(range=[0, len(df_ano)])  # Definir os limites de exibição horizontal

# Criar uma lista para armazenar os gráficos individuais
figs = []

for ano in anos:
    # Filtrar o DataFrame para o ano atual
    df_ano = globals()[f'agrupado{ano}']
    
    # Ordenar o DataFrame pela coluna 'DT_OCOR' em ordem decrescente
    df_ano = df_ano.sort_values(by='resultado', ascending=False)
    
    # Criar o gráfico de barras para o ano atual
    fig = go.Figure(data=[go.Bar(x=df_ano['SG_UF'], y=df_ano['resultado'],
                                text=df_ano['resultado'], texttemplate='%{y}', textposition='outside')])
    
    fig.update_layout(xaxis_tickangle=45, xaxis_title='Estado', yaxis_title='Número de ocorrências',
                      title=f'Número de ocorrências por Estado - {ano}')
    
    figs.append(fig)

# Organizar os gráficos em uma única figura
combined_fig = sp.make_subplots(rows=1, cols=len(figs), subplot_titles=[str(ano) for ano in anos])

for i, fig in enumerate(figs):
    combined_fig.add_trace(fig.data[0], row=1, col=i + 1)

combined_fig.update_layout(title='Número de ocorrências por Estado 2020-2021 para cada 100 mil habitantes')

# Exibir a figura
pio.show(combined_fig)

# Salvar a figura como HTML
pio.write_html(combined_fig, file='gráfico_interativo_por_estado_100k_2020-2021.html', auto_open=True)

# testes


# # Exibir os gráficos
# for fig in figs:
#     pio.show(fig)


# # Salvar a figura como HTML
# pio.write_html(fig, file='grafico_interativo_por_estado_100k_2020-2021.html', auto_open=True)


