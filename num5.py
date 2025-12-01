import pandas as pd

dtf = pd.read_csv('titanic.csv')
print(dtf['Age'].median())
