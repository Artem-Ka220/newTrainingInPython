# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

import pandas as pd

avg = pd.read_csv('california_housing_train.csv')

avg = (avg[avg['population'] < 500]['median_house_value'].mean())
