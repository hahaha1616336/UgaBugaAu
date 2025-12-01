import pandas as pd

dtf = pd.read_csv("titanic.csv")

print(dtf[dtf["Survived"] == 1].shape[0])
print(f"{(dtf[dtf['Survived'] == 1].shape[0] / len(dtf)) * 100:.4f}")
print(f"{dtf[dtf['Sex'] == 'male']['Survived'].sum() * 100 / dtf[dtf['Sex'] == 'male'].shape[0]:.2f}")
print(f"{dtf[dtf['Sex'] == 'female']['Survived'].sum() * 100 / dtf[dtf['Sex'] == 'female'].shape[0]:.2f}")
