import pandas as pd
dtf = pd.read_csv("titanic.csv")


print(dtf.shape[0], dtf.shape[1], dtf.dtypes, dtf.isnull().sum(), len(dtf))
print(dtf["Age"].isnull().sum())
