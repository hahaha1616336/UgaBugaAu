import pandas as pd

dtf = pd.read_csv('titanic.csv')

print(f"{dtf[dtf['Pclass'] == 1]['Fare'].mean():.2f}")
print(f"{(dtf[dtf['Pclass'] == 3]['Survived'].sum() / dtf[dtf['Pclass'] == 3].shape[0] * 100):.2f}")
