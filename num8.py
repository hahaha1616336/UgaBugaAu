import pandas as pd

dtf = pd.read_csv('titanic.csv')
print(len(dtf[(dtf['Sex'] == 'female') & (dtf['Pclass'] == 1) & (dtf['Survived'] == 1)]))
print(len(dtf[(dtf['Age'] < 18) & (dtf['Parch'] == 0)]))
