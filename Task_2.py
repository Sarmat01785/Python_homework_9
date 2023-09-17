"""
                              Задача 42: 
Узнать какая максимальная households в зоне минимального значения population.
"""

import pandas as pd


data = pd.read_csv('california_housing_train.csv')

min_population = data['population'].min()

print(min_population)

filtered_data = data[data['population'] == min_population]

max_households = filtered_data['households'].max()

print(f"Максимальное количество домохозяйств в зоне с минимальным значением населения: {max_households}")

