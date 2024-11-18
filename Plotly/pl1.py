import plotly.graph_objs as go

# Создаем объект фигуры
fig = go.Figure()
# Данные для построения
x = [1974, 1987, 1999, 2012, 2022, 2046]
y = [4, 5, 6, 7, 8, 9]
# Собираем точки и объединяем их линиями
fig.add_trace(go.Scatter(x=x, y=y))
# Настройки окна
fig.update_layout(legend_orientation="h",
                  title="The number of the world's population by year",
                  xaxis_title="year",
                  yaxis_title="population",
                  margin=dict(l=0, r=0, t=30, b=0))
fig.show()





