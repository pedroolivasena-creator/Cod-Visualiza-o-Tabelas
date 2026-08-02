# Cod-Visualiza-o-Tabelas
# Documentação do Código – Dashboard Interativo de Estatísticas de E-commerce

## 1. Objetivo

Este projeto tem como objetivo desenvolver um **dashboard interativo** utilizando as bibliotecas **Dash**, **Plotly Express** e **Pandas** para realizar a análise exploratória de um conjunto de dados de um e-commerce. O sistema permite visualizar informações estatísticas por meio de diferentes gráficos, facilitando a interpretação dos dados e auxiliando na tomada de decisões.

---

# 2. Tecnologias Utilizadas

* **Python** – Linguagem de programação utilizada no desenvolvimento.
* **Pandas** – Responsável pela leitura e manipulação dos dados.
* **Plotly Express** – Utilizado para a criação de gráficos interativos.
* **Dash** – Framework utilizado para transformar os gráficos em uma aplicação web interativa.

---

# 3. Estrutura do Código

O código está dividido em seis partes principais:

1. Importação das bibliotecas;
2. Leitura do conjunto de dados;
3. Criação dos gráficos;
4. Construção do layout da aplicação;
5. Organização visual do dashboard;
6. Execução do servidor.

---

# 4. Importação das Bibliotecas

```python
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
```

Nesta etapa são importadas as bibliotecas necessárias para o funcionamento da aplicação.

**Pandas (pd)**

Responsável pela leitura do arquivo CSV e pela manipulação dos dados.

**Plotly Express (px)**

Utilizado para construir gráficos interativos de maneira simples.

**Dash**

Framework responsável pela criação da interface web.

* `Dash` inicializa a aplicação.
* `dcc` (Dash Core Components) exibe os gráficos.
* `html` cria os elementos visuais da página.

---

# 5. Leitura dos Dados

```python
df = pd.read_csv(
    r"C:/Users/Usuario/PycharmProjects/PythonProject/ecommerce_estatistica.csv"
)
```

O arquivo CSV é carregado para um DataFrame chamado **df**, que armazenará todas as informações do conjunto de dados.

Esse DataFrame será utilizado por todos os gráficos da aplicação.

---

# 6. Inicialização da Aplicação

```python
app = Dash(__name__)
```

Esta instrução cria a aplicação Dash responsável por hospedar o dashboard.

---

# 7. Desenvolvimento dos Gráficos

## 7.1 Histograma

```python
fig_hist = px.histogram(...)
```

### Objetivo

Apresentar a distribuição dos preços dos produtos.

### Variável utilizada

* Preço

### Informações obtidas

* Frequência dos preços;
* Concentração dos produtos;
* Possíveis valores extremos.

---

## 7.2 Gráfico de Dispersão

```python
fig_scatter = px.scatter(...)
```

### Objetivo

Analisar a relação entre:

* Preço;
* Quantidade vendida.

Cada ponto representa um produto do conjunto de dados.

As diferentes marcas são identificadas por cores distintas.

Esse gráfico permite verificar se produtos mais caros tendem a vender mais ou menos.

---

## 7.3 Heatmap de Correlação

```python
corr = df[['Desconto','Preço','Desconto_MinMax']].corr()
```

É calculada uma matriz de correlação entre as variáveis numéricas.

Posteriormente:

```python
fig_heat = px.imshow(...)
```

gera o mapa de calor.

### Objetivo

Visualizar o grau de relacionamento entre as variáveis.

Valores próximos de:

* **1** → Correlação positiva forte;
* **0** → Pouca ou nenhuma correlação;
* **−1** → Correlação negativa forte.

---

## 7.4 Gráfico de Barras

```python
marcas = (
    df["Marca"]
    .value_counts()
    .reset_index()
)
```

Conta a quantidade de produtos existentes para cada marca.

Depois:

```python
fig_bar = px.bar(...)
```

gera o gráfico.

### Objetivo

Comparar a quantidade de produtos cadastrados por marca.

---

## 7.5 Gráfico de Pizza

```python
avaliacoes = (
    df["N_Avaliações"]
    .value_counts()
    .head(10)
)
```

Seleciona as dez maiores ocorrências do número de avaliações.

Posteriormente:

```python
fig_pie = px.pie(...)
```

gera o gráfico de pizza.

### Objetivo

Mostrar a participação percentual dos dez grupos de avaliações mais frequentes.

---

## 7.6 Gráfico de Densidade

```python
fig_kde = px.density_contour(...)
```

Cria um gráfico de densidade baseado na variável **Marca_Cod**.

### Objetivo

Identificar regiões onde existe maior concentração dos registros.

Quanto mais intensa a coloração, maior a densidade de observações.

---

## 7.7 CountPlot

Primeiramente é realizado um agrupamento:

```python
df.groupby(["Temporada","Marca_Cod"])
```

Depois é criado o gráfico de barras.

### Objetivo

Comparar a quantidade de produtos por temporada, separados por marca.

Esse gráfico auxilia na análise da distribuição das marcas ao longo das diferentes temporadas.

---

# 8. Construção do Layout

O layout é definido utilizando componentes HTML do Dash.

```python
app.layout = html.Div([
```

Todo o conteúdo da aplicação fica dentro desse contêiner principal.

O título é criado utilizando:

```python
html.H1()
```

Os gráficos são inseridos através de:

```python
dcc.Graph()
```

Cada gráfico recebe uma figura criada anteriormente.

---

# 9. Organização Visual

Os gráficos são organizados utilizando CSS Grid.

```python
"display": "grid"
```

e

```python
"gridTemplateColumns": "50% 50%"
```

Essa configuração posiciona dois gráficos por linha.

A organização final é:

* Histograma | Dispersão
* Heatmap | Barras
* Pizza | Densidade
* CountPlot

Essa estrutura melhora a visualização e facilita a comparação entre os diferentes gráficos.

---

# 10. Execução da Aplicação

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Quando o arquivo é executado, o servidor local do Dash é iniciado.

O dashboard fica disponível no navegador por meio do endereço:

```
http://127.0.0.1:8050/
```

O parâmetro `debug=True` permite atualizar automaticamente a aplicação sempre que o código é modificado.

---

# 11. Resultados Esperados

Ao executar o programa, é exibido um dashboard interativo contendo sete gráficos que possibilitam analisar:

* Distribuição dos preços;
* Relação entre preço e quantidade vendida;
* Correlação entre preço e desconto;
* Quantidade de produtos por marca;
* Distribuição das avaliações dos produtos;
* Concentração dos registros por marca;
* Distribuição das marcas em diferentes temporadas.

Todas as visualizações são interativas, permitindo ampliar, mover, selecionar áreas específicas e visualizar informações detalhadas ao passar o cursor sobre os gráficos.

---

# 12. Conclusão

O dashboard desenvolvido oferece uma interface intuitiva para análise exploratória dos dados do e-commerce. A combinação das bibliotecas Pandas, Plotly Express e Dash possibilita a construção de uma aplicação web dinâmica, na qual diferentes aspectos do conjunto de dados podem ser analisados de forma rápida e visual.

A estrutura modular do código facilita futuras expansões, como a inclusão de filtros, indicadores (KPIs), novos gráficos e integração com bancos de dados, tornando a aplicação adequada para projetos de Business Intelligence e análise de dados.

