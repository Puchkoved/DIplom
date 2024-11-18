import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Генерация случайных данных с нормальным распределением
data = np.random.normal(loc=0, scale=1, size=1000)

# Создание гистограммы с помощью Seaborn
sns.histplot(data, bins=30, kde=True)

# Настройка заголовка и меток
plt.title('Гистограмма распределения Гауса')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Отображение графика
plt.show()