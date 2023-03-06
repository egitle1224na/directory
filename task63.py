# import random

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

from sklearn.preprocessing import OneHotEncoder

x = [[0, "human"], [1, "robot"]]

y = OneHotEncoder().fit_transform(x).toarray()

print(y)