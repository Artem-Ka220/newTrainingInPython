# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

label_encoder = LabelEncoder()
encoded_data = data.apply(label_encoder.fit_transform)
print(encoded_data)