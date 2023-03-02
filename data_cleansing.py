import pandas as pd

pd.set_option('display.max_columns', None)

url_link1 = 'https://fbref.com/en/squads/19538871/2022-2023/all_comps/Manchester-United-Stats-All-Competitions'
url_link2 = 'https://fbref.com/en/squads/19538871/2021-2022/all_comps/Manchester-United-Stats-All-Competitions'

df_unclean_2022_2023 = pd.read_html(url_link1, header=1)
df_unclean_2021_2022 = pd.read_html(url_link2, header=1)

df_2022_2023 = df_unclean_2022_2023[16]
df_2022_2023.drop('Matches', axis=1, inplace=True)

for i in range(21,46,5):
    colu = ['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age']
    dff = df_unclean_2022_2023[i]
    dff.drop(columns=colu, axis=1, inplace=True)
    df_2022_2023 = df_2022_2023.join(dff, how="outer", rsuffix='_%a'%i)

df_pt_2023 = df_unclean_2022_2023[46]
df_pt_2023.drop(columns=['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age'], axis=1, inplace=True)
df_pt_2023 = df_pt_2023.loc[df_pt_2023["MP"] != 0]
df_2022_2023 = df_2022_2023.join(df_pt_2023, how="outer", rsuffix='_pt')

df_2022_2023.drop(columns=["Cmp_26", "Att_26"], inplace=True)

renaming = {'Cmp.1': 'Cmp_Shrt', 'Att.1': 'Att_Shrt', 'Cmp%.1': 'Cmp%_Shrt',
            'Cmp.2': 'Cmp_Med', 'Att.2': 'Att_Med', 'Cmp%.2': 'Cmp%_Med',
            'Cmp.3': 'Cmp_Long', 'Att.3': 'Att_Long','Cmp%.3': 'Cmp%_Long',
            'FK_26': 'FK_Pass',
            'PassLive': 'PassLive_SCA', 'PassDead': 'PassDead_SCA', 'TO': 'TO_SCA', 'Sh_31': 'Sh_SCA', 'Fld': 'Fld_SCA',
            'Def': 'Def_GCA',
            'PassLive.1': 'PassLive_GCA', 'PassDead.1': 'PassDead_GCA', 'TO.1': 'TO_GCA', 'Sh.1': 'Sh_GCA', 'Fld.1': 'Fld_GCA',
            'Def.1': 'Def_GCA',
            'Tkl.1': 'Tkl_Chl', 'Att_36': 'Att_Chl', 'Blocks_36': 'Blocks_Def', 'Sh_36': 'Blocks_Sh',
            'Def 3rd': 'Def 3rd_Tkls', 'Mid 3rd': 'Mid 3rd_Tkls', 'Att 3rd': 'Att 3rd_Tkls',
            'Live': 'Live_Pass',
            'Def 3rd_41': 'Def 3rd_Tch', 'Mid 3rd_41': 'Mid 3rd_Tch', 'Att 3rd_41': 'Att 3rd_Tch',
            'Live_41': 'Live_Tch', 'Att_41': 'Att_TakeOns',
            'TotDist': 'TotDist_Pass', 'PrgDist': 'PrgDist_Pass',
            'TotDist_41': 'TotDist_Carr', 'PrgDist_41': 'PrgDist_Carr',
            '1/3_41': '1/3_Carr', '1/3': '1/3_Pass' }
df_2022_2023.rename(columns=renaming, inplace=True)

df_misc_2023 = df_unclean_2022_2023[51]
df_misc_2023.drop(columns=['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age'], axis=1, inplace=True)
df_2022_2023 = df_2022_2023.join(df_misc_2023, how="outer", rsuffix='_ms')
df_2022_2023.drop(columns=['Crs_ms', 'Int_ms', 'TklW_ms'], inplace=True)
renaming1 = {'Off_ms': 'Offsd', 'Won': 'Won_AD', 'Lost_ms': 'Lost_AD'}
df_2022_2023.rename(columns=renaming1, inplace=True)

df_2022_2023.dropna(subset=['Cmp%'],inplace=True)
df_2022_2023.fillna(0)

print(df_2022_2023)

df_gk_2022_2023 = df_unclean_2022_2023[11]
df_gk_2022_2023.fillna(0)
