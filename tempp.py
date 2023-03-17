import pandas as pd

data = pd.read_csv("data/df_2022_2023_gk.csv")
data1 = pd.read_csv("data/df_2022_2023_gk.csv")
# att = {'Shooting': ['Gls', 'Sh', 'SoT'], 'Passing': ['Dist', 'Fk']}
#
# df = data.loc[data['Player'] == 'Bruno Fernandes']
# df = df.loc[:, att['Shooting']]
#
# print(df)
# print(type(df))

# column_names = list(data.columns.values)
# col_names = list(data1.columns.values)
# print(column_names)
# print(col_names)

df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
print(df)