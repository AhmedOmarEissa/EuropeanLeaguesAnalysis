import pandas as pd
arpy = pd.read_csv('arpy.csv')

df = pd.DataFrame()
for i  in range(22,31):
    x = arpy[arpy['age'] == i].sort_values('average_rating_yearly', ascending = False).head(10).reset_index()
    df = df.append(x.reset_index())
df.pivot(index='age', columns='player_name', values='level_0').plot()
