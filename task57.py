import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# print(df.head())

# print(df[df["housing_median_age"] < 20][["total_bedrooms", "total_rooms"]])

print(df[df["population"] < 501][["median_house_value"]])









