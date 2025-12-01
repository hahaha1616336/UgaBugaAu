import pandas as pd
dtf = pd.read_csv('titanic.csv')

print(f"{dtf[dtf['Survived'] == 1]['Age'].mean():.2f} {dtf[dtf['Survived'] == 0]['Age'].mean():.2f}")
