import seaborn as sns
import matplotlib.pyplot as pl
import pandas as pd

# Данные
x_y = {'year': [1974, 1987, 1999, 2012, 2022, 2046], 'people': [4, 5, 6, 7, 8, 9]}
# Создаем датафрейм
dframe = pd.DataFrame(x_y)
# Строим график
sns.lineplot(x='year', y='people', data=dframe) # Строим график
pl.show()
