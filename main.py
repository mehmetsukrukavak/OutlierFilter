import pandas as pd

data_set = pd.read_csv("outlier_ornek_veriseti.csv", sep=";")

print(data_set)

Q1 = data_set.boy.quantile(0.25)
Q3 = data_set.boy.quantile(0.75)

IQR_value = Q3 - Q1

alt_limit = Q1 - 1.5 * IQR_value
ust_limit = Q3 + 1.5 * IQR_value

data_set_outlier_filtrelenmis = data_set[(data_set.boy > alt_limit) & (data_set.boy < ust_limit)]
print(data_set_outlier_filtrelenmis)