# -*- coding: utf-8 -*-
"""ProvaEstatistica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emiYXop-r9oiqv24gyVuDEKQgv9CpRgL

###Importes e leitura do arquivo

---
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import seaborn as sn
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from scipy import stats

arqv = pd.read_csv('BDAgro.csv')
arqv

arqv.head()

arqv.tail()

"""Q1)  Calcule medidas de tendência central, como a média, mediana e moda. Calcule Medidas de
dispersão para entender a variabilidade dos dados. Isso pode incluir o desvio padrão, a variância
e a amplitude.

Número de Máquinas no campo:
"""

media = arqv['NMaquinas'].mean()
mediana = arqv['NMaquinas'].median()
quartil = arqv['NMaquinas'].quantile(q=0.25)
moda = arqv['NMaquinas'].mode()
desv_pad = arqv['NMaquinas'].std()
variancia = arqv['NMaquinas'].var()
amplitude = arqv['NMaquinas'].max() - arqv['NMaquinas'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Números de Trabalhadores:"""

media = arqv['NTrabalhadores'].mean()
mediana = arqv['NTrabalhadores'].median()
quartil = arqv['NTrabalhadores'].quantile(q=0.25)
moda = arqv['NTrabalhadores'].mode()
desv_pad = arqv['NTrabalhadores'].std()
variancia = arqv['NTrabalhadores'].var()
amplitude = arqv['NTrabalhadores'].max() - arqv['NTrabalhadores'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Espacamento do plantio:"""

media = arqv['Espacamen'].mean()
mediana = arqv['Espacamen'].median()
quartil = arqv['Espacamen'].quantile(q=0.25)
moda = arqv['Espacamen'].mode()
desv_pad = arqv['Espacamen'].std()
variancia = arqv['Espacamen'].var()
amplitude = arqv['Espacamen'].max() - arqv['Espacamen'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Peso médio da batata doce (gramas):"""

media = arqv['PsMedBd'].mean()
mediana = arqv['PsMedBd'].median()
quartil = arqv['PsMedBd'].quantile(q=0.25)
moda = arqv['PsMedBd'].mode()
desv_pad = arqv['PsMedBd'].std()
variancia = arqv['PsMedBd'].var()
amplitude = arqv['PsMedBd'].max() - arqv['PsMedBd'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Peso médio da batata inglesa (gramas):"""

media = arqv['PsMedBi'].mean()
mediana = arqv['PsMedBi'].median()
quartil = arqv['PsMedBi'].quantile(q=0.25)
moda = arqv['PsMedBi'].mode()
desv_pad = arqv['PsMedBi'].std()
variancia = arqv['PsMedBi'].var()
amplitude = arqv['PsMedBi'].max() - arqv['PsMedBi'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Teor de sólidos solúveis batata doce: a quantidade de açúcares e outros
compostos solúveis nos frutos, expressa em graus Brix.
"""

media = arqv['BrixBd'].mean()
mediana = arqv['BrixBd'].median()
quartil = arqv['BrixBd'].quantile(q=0.25)
moda = arqv['BrixBd'].mode()
desv_pad = arqv['BrixBd'].std()
variancia = arqv['BrixBd'].var()
amplitude = arqv['BrixBd'].max() - arqv['BrixBd'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Teor de sólidos solúveis batata inglesa: a quantidade de açúcares e outros
compostos solúveis nos frutos, expressa em graus Brix.
"""

media = arqv['BrixBi'].mean()
mediana = arqv['BrixBi'].median()
quartil = arqv['BrixBi'].quantile(q=0.25)
moda = arqv['BrixBi'].mode()
desv_pad = arqv['BrixBi'].std()
variancia = arqv['BrixBi'].var()
amplitude = arqv['BrixBi'].max() - arqv['BrixBi'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Temperatura:"""

media = arqv['temp'].mean()
mediana = arqv['temp'].median()
quartil = arqv['temp'].quantile(q=0.25)
moda = arqv['temp'].mode()
desv_pad = arqv['temp'].std()
variancia = arqv['temp'].var()
amplitude = arqv['temp'].max() - arqv['temp'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Umidade"""

media = arqv['umidade'].mean()
mediana = arqv['umidade'].median()
quartil = arqv['umidade'].quantile(q=0.25)
moda = arqv['umidade'].mode()
desv_pad = arqv['umidade'].std()
variancia = arqv['umidade'].var()
amplitude = arqv['umidade'].max() - arqv['umidade'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Precipitação (trimeste/mm)"""

media = arqv['prec'].mean()
mediana = arqv['prec'].median()
quartil = arqv['prec'].quantile(q=0.25)
moda = arqv['prec'].mode()
desv_pad = arqv['prec'].std()
variancia = arqv['prec'].var()
amplitude = arqv['prec'].max() - arqv['prec'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Producao total batata doce mensal (kg)"""

media = arqv['ProdBd'].mean()
mediana = arqv['ProdBd'].median()
quartil = arqv['ProdBd'].quantile(q=0.25)
moda = arqv['ProdBd'].mode()
desv_pad = arqv['ProdBd'].std()
variancia = arqv['ProdBd'].var()
amplitude = arqv['ProdBd'].max() - arqv['ProdBd'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Producao total batata inglesamensal (Kg)"""

media = arqv['ProdBi'].mean()
mediana = arqv['ProdBi'].median()
quartil = arqv['ProdBi'].quantile(q=0.25)
moda = arqv['ProdBi'].mode()
desv_pad = arqv['ProdBi'].std()
variancia = arqv['ProdBi'].var()
amplitude = arqv['ProdBi'].max() - arqv['ProdBi'].min()
coef_Variacao = desv_pad / media


print('Média: ', media)
print('Mediana: ', mediana)
print('Quartil: ', quartil)
print('Moda: ', moda)
print('Desvio Padrão: ', desv_pad)
print('Variância: ', variancia)
print('Amplitude: ', amplitude)
print('Coeficiente de Variacao: ', coef_Variacao)

"""Q2) Visualize cada variável com gráficos descritivos para visualizar os dados. Utilize histogramas, boxplots, entre outros. Os gráficos podem fornecer insights visuais sobre a distribuição, forma e
tendências dos dados

Número de Máquinas no campo:
"""

arqv['NMaquinas'].plot(kind = 'box')

arqv['NMaquinas'].hist();

"""Número de trabalhadores no campo"""

arqv['NTrabalhadores'].plot(kind = 'box')

arqv['NTrabalhadores'].hist();

"""Espacamento do plantio"""

arqv['Espacamen'].plot(kind = 'box')

arqv['Espacamen'].hist();

"""Peso médio da batata doce (gramas)"""

arqv['PsMedBd'].plot(kind = 'box')

arqv['PsMedBd'].hist();

"""Peso médio da batata inglesa (gramas)"""

arqv['PsMedBi'].plot(kind = 'box')

arqv['PsMedBi'].hist();

"""Teor de sólidos solúveis batata doce: a quantidade de açúcares e outros
compostos solúveis nos frutos, expressa em graus Brix
"""

arqv['BrixBd'].plot(kind = 'box')

arqv['BrixBd'].hist();

"""Teor de sólidos solúveis batata inglesa: a quantidade de açúcares e outros compostos solúveis nos frutos, expressa em graus Brix."""

arqv['BrixBi'].plot(kind = 'box')

arqv['BrixBi'].hist();

"""temperatura"""

arqv['temp'].plot(kind = 'box')

arqv['temp'].hist();

"""umidade"""

arqv['umidade'].plot(kind = 'box')

arqv['umidade'].hist();

"""precipitação (trimeste/mm)"""

arqv['prec'].plot(kind = 'box')

arqv['prec'].hist();

"""Producao total batata doce mensal (kg)"""

arqv['ProdBd'].plot(kind = 'box')

arqv['ProdBd'].hist();

"""Producao total batata inglesamensal (Kg)"""

arqv['ProdBi'].plot(kind = 'box')

arqv['ProdBi'].hist();

"""Q3) Identifique e analise valores atípicos ou discrepantes nos dados. Valores atípicos podemafetar
as medidas de tendência central e a interpretação dos resultados. Estes valores atípicos devemser os valores que estão fora do Intervalo de Confiança para média.

#Resposta: Analise do boxPlot de tempo e umidade

Q4)Visualize o cruzamento de variáveis mostrando o comportamento por UF das variaveis
agricolas e climáticas. Represente com gráficos descritivos para visualizar os dados. Utilize
gráficos de barras entre outros. (-qual a produção total e a media por UF, -qual a produção total
por tipo de cultivo, - qual a temperatura, umidade e precipitação total e media por UF
"""

arqv['UF'].hist();

producao_total_por_uf = arqv.groupby('UF')['ProdBd', 'ProdBi'].sum().sum(axis=1)

num_empresas_por_uf = arqv.groupby('UF').size()

# Calculando a média de produção por UF
producao_media_por_uf = producao_total_por_uf / num_empresas_por_uf
producao_total_por_cultivo = arqv.groupby('MetdCult')['ProdBd', 'ProdBi'].sum().sum(axis=1)
dados_por_uf = arqv.groupby('UF')['temp', 'umidade', 'prec'].agg(['sum', 'mean'])

print(dados_por_uf)

"""Q5) Identifique as correlacoes de Pearson entre todas as variáveis dependentes (producoes
agricolas) com as independentes.
"""

correlation = arqv.corr()

plot = sn.heatmap(correlation, annot = True, fmt=".1f", linewidths=.6)
plot

arqv.corr()

"""Q6) Aplique a regressão Multipla pra identificar a relacao das produções agricolas e as variáveis
climáticas. O método estatístico utilizado para modelar a relação entre uma variável dependente
e duas ou mais variáveis independentes. No Python, você pode realizar regressão múltipla
utilizando bibliotecas como o NumPy, o pandas e o scikit-learn
"""

#Variáveis independentes
X = arqv[['temp', 'umidade', 'prec', 'NTrabalhadores']]

# Variável dependente 'ProdBd'
y_prodbd = arqv['ProdBd']
modelo_prodbd = LinearRegression()
modelo_prodbd.fit(X, y_prodbd)

# Variável dependente 'ProdBi'
y_prodbi = arqv['ProdBi']
modelo_prodbi = LinearRegression()
modelo_prodbi.fit(X, y_prodbi)

# Coeficientes e termo independente para 'ProdBd'
coeficientes_prodbd = modelo_prodbd.coef_
termo_ind_prodbd = modelo_prodbd.intercept_

# Coeficientes e termo independente para 'ProdBi'
coeficientes_prodbi = modelo_prodbi.coef_
termo_ind_prodbi = modelo_prodbi.intercept_

# Imprimir coeficientes para cada variável independente
for i, column in enumerate(X.columns):
    print(f'Coeficiente para {column} em ProdBd: {coeficientes_prodbd[i]}')
    print(f'Coeficiente para {column} em ProdBi: {coeficientes_prodbi[i]}')

# Imprimir termo independente
print(f'Termo independente em ProdBd: {termo_ind_prodbd}')
print(f'Termo independente em ProdBi: {termo_ind_prodbi}')

"""Q7) Aplique os dois tipos de estatística de teste para realizar um teste de comparação de médias. Você pode utilizar diferentes métodos estatísticos, dependendo das características dos seus dados e do objetivo da comparação. Os dois métodos comuns: o teste t de Student (2 var independentes) e a análise de variância- ANOVA (mais de um var independentes). Escolha umadas variáveis independentes e aplique o teste"""

# Dados das amostras independentes
X = arqv[arqv['temp'] < 25]['ProdBd']
Y = arqv[arqv['temp'] >= 25]['ProdBd']

# Teste t de Student
t_statistic, p_value = stats.ttest_ind(X, Y)

# Imprimir os resultados
print("Teste t de Student:")
print("Estatística t:", t_statistic)
print("Valor de p:", p_value)

# Dados das variáveis independentes e dependente
VI1 = arqv['temp']
VI2 = arqv['umidade']
VI3 = arqv['prec']
VD = arqv['ProdBd']

# Teste ANOVA
f_statistic, p_value = stats.f_oneway(VI1, VI2, VI3, VD)

# Imprimir os resultados
print("Teste ANOVA:")
print("Estatística F:", f_statistic)
print("Valor de p:", p_value)

def regressao_multipla(dados):
    # Carregar os dados do banco de dados para um DataFrame do pandas

    # Separar as variáveis independentes (climáticas) da variável dependente (produção agrícola)
    X = arqv.iloc[:, 4:-2].values  # A partir da quarta coluna até a antepenúltima são as variáveis independentes
    y = arqv.iloc[:, -2:].values   # As duas últimas colunas são as variáveis dependentes


    # Criar o objeto de regressão linear
    regressor = LinearRegression()

    # Treinar o modelo de regressão múltipla
    regressor.fit(X, y)

    # Imprimir os coeficientes de regressão
    coeficientes = regressor.coef_
    print("Coeficientes de regressão:")
    for i, coef in enumerate(coeficientes):
        print(f"Variável {i+1}: {coef}")

    # Imprimir o coeficiente de intercepção
    intercepto = regressor.intercept_
    print(f"Coeficiente de intercepção: {intercepto}")

    # Realizar previsões
    previsoes = regressor.predict(X)
    print("Previsões:")
    for i, prev in enumerate(previsoes):
        print(f"Previsão {i+1}: {prev}")

# Exemplo de uso da função
regressao_multipla("arqv.csv")  # Substitua "dados.csv" pelo caminho ou nome do arquivo do banco de dados

arqv['temp'].plot(kind = 'box')

arqv['temp'].hist();

X = arqv[['temp', 'umidade', 'prec', 'NTrabalhadores']]

y_prodbd = arqv['ProdBd']
modelo_prodbd = LinearRegression()
modelo_prodbd.fit(X, y_prodbd)

y_prodbi = arqv['ProdBi']
modelo_prodbi = LinearRegression()
modelo_prodbi.fit(X, y_prodbi)

coeficientes_prodbd = modelo_prodbd.coef_
termo_ind_prodbd = modelo_prodbd.intercept_

coeficientes_prodbi = modelo_prodbi.coef_
termo_ind_prodbi = modelo_prodbi.intercept_

for i, column in enumerate(X.columns):
	print(f'Coeficiente para {column} em ProdBd: {coeficientes_prodbd[i]}')

	print(f'Coeficiente para {column} em ProdBi: {coeficientes_prodbi[i]}')

print(f'Termo independente em ProdBd: {termo_ind_prodbd}')

print(f'Termo independente em ProdBi: {termo_ind_prodbi}')

# Dados das amostras independentes
X = arqv[arqv['temp'] < 25]['ProdBd']
Y = arqv[arqv['temp'] >= 25]['ProdBd']

# Teste t de Student
t_statistic, p_value = stats.ttest_ind(X, Y)

# Imprimir os resultados
print("Teste t de Student:")
print("Estatística t:", t_statistic)
print("Valor de p:", p_value)

# Dados das variáveis independentes e dependente
VI1 = arqv['temp']
VI2 = arqv['umidade']
VI3 = arqv['prec']
VD = arqv['ProdBd']

# Teste ANOVA
f_statistic, p_value = stats.f_oneway(VI1, VI2, VI3, VD)

# Imprimir os resultados
print("Teste ANOVA:")
print("Estatística F:", f_statistic)
print("Valor de p:", p_value)