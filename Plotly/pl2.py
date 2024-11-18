import numpy as np
import plotly.express as px

# Генерация случайных данных с нормальным распределением
data = np.random.normal(loc=0, scale=1, size=1000)

# Создание гистограммы с помощью Plotly
fig = px.histogram(data, nbins=30, title='Histogram of the Gaussian distribution')

# Отображение графика
fig.show()