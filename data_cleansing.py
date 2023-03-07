import pandas as pd

pd.set_option('display.max_columns', None)

######################################        First Dataset        ####################################################

### Getting the raw data by web scraping
url_link1 = 'https://fbref.com/en/squads/19538871/2022-2023/all_comps/Manchester-United-Stats-All-Competitions'
df_unclean_2022_2023 = pd.read_html(url_link1, header=1)

### Start building the new data frame for Mancheter United 2022-2023 Season
df_2022_2023 = df_unclean_2022_2023[16]
df_2022_2023.drop('Matches', axis=1, inplace=True)

for i in range(21, 46, 5):
    colu = ['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age']
    dff = df_unclean_2022_2023[i]
    dff.drop(columns=colu, axis=1, inplace=True)
    df_2022_2023 = df_2022_2023.join(dff, how="outer", rsuffix='_%a' % i)

### From the website, the Playing Time table has more players than the other tables. So to delete the additional players,
### I filtered all the players with NaN
df_pt_2023 = df_unclean_2022_2023[46]
df_pt_2023.drop(columns=['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age'], axis=1, inplace=True)
df_pt_2023 = df_pt_2023.loc[df_pt_2023["MP"] != 0]
df_2022_2023 = df_2022_2023.join(df_pt_2023, how="outer", rsuffix='_pt')

### Dropping repeat columns and renaming similar naming columns
df_2022_2023.drop(columns=["Cmp_26", "Att_26"], inplace=True)

renaming = {'Cmp.1': 'Cmp_Shrt', 'Att.1': 'Att_Shrt', 'Cmp%.1': 'Cmp%_Shrt',
            'Cmp.2': 'Cmp_Med', 'Att.2': 'Att_Med', 'Cmp%.2': 'Cmp%_Med',
            'Cmp.3': 'Cmp_Long', 'Att.3': 'Att_Long', 'Cmp%.3': 'Cmp%_Long',
            'FK_26': 'FK_Pass',
            'PassLive': 'PassLive_SCA', 'PassDead': 'PassDead_SCA', 'TO': 'TO_SCA', 'Sh_31': 'Sh_SCA', 'Fld': 'Fld_SCA',
            'Def': 'Def_SCA',
            'PassLive.1': 'PassLive_GCA', 'PassDead.1': 'PassDead_GCA', 'TO.1': 'TO_GCA', 'Sh.1': 'Sh_GCA',
            'Fld.1': 'Fld_GCA',
            'Def.1': 'Def_GCA',
            'Tkl.1': 'Tkl_Chl', 'Att_36': 'Att_Chl', 'Blocks_36': 'Blocks_Def', 'Sh_36': 'Blocks_Sh',
            'Def 3rd': 'Def 3rd_Tkls', 'Mid 3rd': 'Mid 3rd_Tkls', 'Att 3rd': 'Att 3rd_Tkls',
            'Live': 'Live_Pass',
            'Def 3rd_41': 'Def 3rd_Tch', 'Mid 3rd_41': 'Mid 3rd_Tch', 'Att 3rd_41': 'Att 3rd_Tch',
            'Live_41': 'Live_Tch', 'Att_41': 'Att_TakeOns',
            'TotDist': 'TotDist_Pass', 'PrgDist': 'PrgDist_Pass',
            'TotDist_41': 'TotDist_Carr', 'PrgDist_41': 'PrgDist_Carr',
            '1/3_41': '1/3_Carr', '1/3': '1/3_Pass', 'On-Off.1': 'On-Off_xG'}
df_2022_2023.rename(columns=renaming, inplace=True)

### Joining last dataset to the main dataset and editing any repeat columns
df_misc_2023 = df_unclean_2022_2023[51]
df_misc_2023.drop(columns=['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age'], axis=1, inplace=True)
df_2022_2023 = df_2022_2023.join(df_misc_2023, how="outer", rsuffix='_ms')
df_2022_2023.drop(columns=['Crs_ms', 'Int_ms', 'TklW_ms'], inplace=True)
renaming1 = {'Off_ms': 'Offsd', 'Won': 'Won_AD', 'Lost_ms': 'Lost_AD'}
df_2022_2023.rename(columns=renaming1, inplace=True)

df_2022_2023.dropna(subset=['Cmp%'], inplace=True)
df_2022_2023.fillna(0, inplace=True)

### Taking out new players from the main dataframe and adding it into a new data frame.
new_players = ['Casemiro', 'Lisandro Martínez', 'Tyrell Malacia',
               'Marcel Sabitzer', 'Wout Weghorst', 'Antony',
               'Christian Eriksen', 'Kobbie Mainoo']

df_2022_2023_new = df_2022_2023.loc[df_2022_2023["Player"].isin(new_players)].reset_index(drop=True)
df_2022_2023 = df_2022_2023[~df_2022_2023["Player"].isin(new_players)].reset_index(drop=True)

### Additional GK stats in a new data frame, since DDG has played most of Manchester United matches this season in all
### competitions, I decided to delete the other goalkeepers.
df_gk_2022_2023 = df_unclean_2022_2023[11]
df_gk_2022_2023.dropna(subset=['FK'], inplace=True)
df_gk_2022_2023.drop(columns=['Matches'], inplace=True)
renaming2 = {'Att': 'Att_Launch', 'Att.1': 'Att_Pass', 'Att.2': 'Att_GKicks', 'AvgLen': 'AvgLen_Pass', 'AvgLen.1':
             'AvgLen_GKicks', 'Launch%': 'Launch%_Pass', 'Launch%.1': 'Launch%_GKicks'}
df_gk_2022_2023.rename(columns=renaming2, inplace=True)

df_2022_2023.to_csv('./data/data_2022_2023.csv', index=True)
df_gk_2022_2023.to_csv('./data/df_2022_2023_gk.csv', index=True)
df_2022_2023_new.to_csv('./data/df_2022_2023_new_signings.csv', index=True)

######################################        Second Dataset        ####################################################
url_link2 = 'https://fbref.com/en/squads/19538871/2021-2022/all_comps/Manchester-United-Stats-All-Competitions'
df_unclean_2021_2022 = pd.read_html(url_link2, header=1)

df_2021_2022 = df_unclean_2021_2022[16]
df_2021_2022.drop('Matches', axis=1, inplace=True)

for i in range(21, 52, 5):
    colu = ['Player', 'Nation', 'Pos', '90s', 'Matches', 'Age']
    dff = df_unclean_2021_2022[i]
    dff.drop(columns=colu, axis=1, inplace=True)
    df_2021_2022 = df_2021_2022.join(dff, how="outer", rsuffix='_%a' % i)

df_2021_2022 = df_2021_2022[df_2021_2022['Player'].notna()]
df_2021_2022.fillna(0, inplace=True)
df_2021_2022.rename(columns=renaming, inplace=True)
df_2021_2022.rename(columns=renaming1, inplace=True)

df_gk_2021_2022 = df_unclean_2021_2022[11]
df_gk_2021_2022.drop(df_gk_2021_2022[df_gk_2021_2022['90s']<5].index, inplace=True)
df_gk_2021_2022.drop('Matches', axis=1, inplace=True)
df_gk_2021_2022.rename(columns=renaming2, inplace=True)

df_2021_2022.to_csv('./data/data_2021_2022.csv', index=True)
df_gk_2021_2022.to_csv('./data/df_2021_2022_gk.csv', index=True)