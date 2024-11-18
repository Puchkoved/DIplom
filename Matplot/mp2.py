import matplotlib.pyplot as plt
import numpy as np
# Генерация случайного набора чисел
data = np.random.randn(1000)
# Построение гистограммы
plt.hist(data,#Значения
         color='skyblue',#Цвет столбца
         edgecolor='black')#Цвет оконтовки столбца
# Оформление
plt.xlabel('Значение')
plt.ylabel('Количество')
plt.title('Гистограмма')
plt.show()