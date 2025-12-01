import pandas as pd

dtf = pd.read_csv("titanic.csv")
dtf['FamilySize'] = dtf['SibSp'] + dtf['Parch'] + 1
print(dtf.loc[888, 'FamilySize'])
