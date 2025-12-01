import pandas as pd

dtf = pd.read_csv("titanic.csv")

print(dtf.describe())

for col in ('Survived', 'Pclass', 'Sex', 'Embarked'):
    print(dtf[col].value_counts())

print(dtf[dtf['Sex'] == 'male'].shape[0])
print(dtf[dtf['Pclass'] == 1].shape[0])
