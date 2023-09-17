"""
                               Задача 40: 
Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""

import pandas as pd


data = pd.read_csv('california_housing_train.csv')


filtered_data = data[(data['population'] >= 0) & (data['population'] <=500)]

mean_price = filtered_data['median_house_value'].mean()

# print("Средняя стоимость дома, где кол-во людей от 0 до 500:", mean_price)
print(f"Средняя стоимость дома, где кол-во людей от 0 до 500: ${mean_price:.2f}")


# print(data)
# print(data.dtypes)

# print()
# print(data.shape)
# print(data.info())
# print(data.describe())