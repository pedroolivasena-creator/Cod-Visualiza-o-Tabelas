import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# ===============================
# Leitura dos dados
# ===============================
df = pd.read_csv(
    r"C:/Users/Usuario/PycharmProjects/PythonProject/ecommerce_estatistica.csv"
)

# ===============================
# Criação da aplicação
# ===============================
app = Dash(__name__)

# ===============================
# Gráfico 1 - Histograma
# ===============================
fig_hist = px.histogram(
    df,
    x="Preço",
    nbins=50,
    title="Histograma - Preços"
)

# ===============================
# Gráfico 2 - Dispersão
# ===============================
fig_scatter = px.scatter(
    df,
    x="Preço",
    y="Qtd_Vendidos",
    color="Marca",
    title="Relação das vendas baseadas no preço"
)

# ===============================
# Gráfico 3 - Heatmap
# ===============================
corr = df[['Desconto', 'Preço', 'Desconto_MinMax']].corr()

fig_heat = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlação entre Preço e Desconto"
)

# ===============================
# Gráfico 4 - Barras
# ===============================
marcas = (
    df["Marca"]
    .value_counts()
    .reset_index()
)

marcas.columns = ["Marca", "Quantidade"]

fig_bar = px.bar(
    marcas,
    x="Marca",
    y="Quantidade",
    color="Quantidade",
    title="Marcas e Quantidades"
)

# ===============================
# Gráfico 5 - Pizza
# ===============================
avaliacoes = (
    df["N_Avaliações"]
    .value_counts()
    .head(10)
    .reset_index()
)

avaliacoes.columns = ["Avaliações", "Quantidade"]

fig_pie = px.pie(
    avaliacoes,
    values="Quantidade",
    names="Avaliações",
    title="Top 10 números de avaliações"
)

# ===============================
# Gráfico 6 - Densidade
# ===============================
fig_kde = px.density_contour(
    df,
    x="Marca_Cod",
    title="Densidade das Marcas"
)

fig_kde.update_traces(contours_coloring="fill")

# ===============================
# Gráfico 7 - CountPlot
# ===============================
count = (
    df.groupby(["Temporada", "Marca_Cod"])
      .size()
      .reset_index(name="Quantidade")
)

fig_count = px.bar(
    count,
    x="Temporada",
    y="Quantidade",
    color="Marca_Cod",
    barmode="group",
    title="Temporadas por Marca"
)

# ===============================
# Layout
# ===============================
app.layout = html.Div([

    html.H1(
        "Dashboard de Estatísticas do E-commerce",
        style={
            "textAlign": "center"
        }
    ),

    html.Div([

        dcc.Graph(figure=fig_hist),

        dcc.Graph(figure=fig_scatter),

    ], style={
        "display": "grid",
        "gridTemplateColumns": "50% 50%"
    }),

    html.Div([

        dcc.Graph(figure=fig_heat),

        dcc.Graph(figure=fig_bar),

    ], style={
        "display": "grid",
        "gridTemplateColumns": "50% 50%"
    }),

    html.Div([

        dcc.Graph(figure=fig_pie),

        dcc.Graph(figure=fig_kde),

    ], style={
        "display": "grid",
        "gridTemplateColumns": "50% 50%"
    }),

    dcc.Graph(figure=fig_count)

])

# ===============================
# Executar
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
