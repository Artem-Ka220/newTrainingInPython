# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы
import pandas as pd                            # подключить библиотеку к программе as(alias) - псевдоним.

from pandas import read_csv

df = pd.read_csv('sample_data/california_housing_train.csv') # Прочтем файл .csv(он находится в Google Colab)

print(df.shape)
print(df.dtypes) # тип данных столбцов
print(df.info) # вывод информации о DataFrame (df) в консоль. Информация о структуре данных, количестве строк и столбцов, типах данных и других характеристиках DataFrame.
print(df.describe()) # вывод основных статистических характеристик числовых столбцов DataFrame (df). 
