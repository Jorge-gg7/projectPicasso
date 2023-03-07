import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


class dataFunc1:
    def __init__(self, name, attribute, dataset1, dataset2, dataset3, dataset4):
        """Used to create a new data set from the given user input
        :param name: Name of the player
        :param attribute: Attribute of the player like Shooting and Goalkeeping that the user is interested
        :param dataset1: First dataset used to extract data - 2022/23 dataset
        :param dataset2: Second dataset used to extract data - 2021/22 dataset
        :param dataset3: Third dataset used to extract data - 2022/23 gk dataset
        :param dataset4: Fourth dataset used to extract data - 2021/22 gk dataset
        """
        self._name = name
        self._attribute = attribute
        self._dataset1 = dataset1
        self._dataset2 = dataset2
        self._dataset3 = dataset3
        self._dataset4 = dataset4

    def display(self):
        df = self._dataset1.loc[self._dataset1['Player'] == str(self._name)]

        row0_spacer1, row0_1, row0_2, row0_3, row0_spacer2 = st.columns((.05,.5, 1,1,.05))
        with row0_1:
            st.image('images/' + self._name + '.png', use_column_width=True)
        with row0_2:
            st.markdown("Name:")
            st.markdown("Nationality:")
            st.markdown("Position:")
            st.markdown("Age:")
            st.markdown("Matches Played:")
            st.markdown("Games Started:")
        with row0_3:
            st.markdown("           " + str(df.iloc[0]["Player"]))
            st.markdown("           " + str(df.iloc[0]["Nation"]))
            st.markdown("           " + str(df.iloc[0]["Pos"]))
            st.markdown("           " + str(df.iloc[0]["Age"]))
            st.markdown("           " + str(df.iloc[0]["MP"]))
            st.markdown("           " + str(df.iloc[0]["Starts"]))

    def filter_data(self):
        att = {'Shooting 👟': ['Gls', 'Sh', 'SoT%', 'SoT/90', 'Dist', 'PK', 'PKatt', 'xG', 'npXG', 'npxG/Sh', 'G-xG',
                            'np:G-xG'],
               'Passing ⚽': ['Att', 'Cmp%', 'TotDist_Pass', 'PrgDist_Pass', 'Att_Shrt', 'Cmp%_Shrt', 'Att_Med',
                           'Cmp%_Med', 'Att_Long', 'Cmp%_Long', 'Ast', 'xAG', 'xA', 'KP', '1/3_Pass', 'PPA', 'CrsPA',
                           'PrgP'],
               'Pass Types 🛒': ['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'In', 'Out', 'Str', 'Off',
                              'Blocks'],
               'Shot-Creating Actions 😎': ['SCA', 'SCA90', 'PassLive_SCA', 'PassDead_SCA', 'TO_SCA', 'Sh_SCA', 'Fld_SCA',
                                        'Def_SCA'],
               'Goal-Creating Actions 🫡': ['GCA', 'GCA90', 'PassLive_GCA', 'PassDead_GCA', 'TO_GCA', 'Sh_GCA', 'Fld_GCA',
                                        'Def_GCA'],
               'Defensive Actions 💪': ['Tkl', 'TklW', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls', 'Att_Chl', 'Tkl%',
                                     'Lost', 'Blocks_Def', 'Blocks_Sh', 'Pass', 'Int', 'Clr', 'Err'],
               'Possession 👻': ['Touches', 'Def Pen', 'Def 3rd_Tch', 'Mid 3rd_Tch', 'Att 3rd_Tch', 'Att Pen', 'Live_Tch',
                              'Att_TakeOns', 'Succ', 'Succ%', 'Tkld', 'Tkld%', 'Carries', 'TotDist_Carr',
                              'PrgDist_Carr', 'PrgC', '1/3_Carr', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR'],
               'Team Success with & without 🎇': ['MP', 'Min', 'Min%', 'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub',
                                               'unSub', 'PPM', 'onG', 'onGA', '+/-', '+/-90', 'On-Off', 'onxG', 'onxGA',
                                               'xG+/-', 'xG+/-90', 'On-Off_xG'],
               'Miscellaneous 🏆': ['CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Offsd', 'PKwon', 'PKcon', 'OG', 'Recov',
                                 'Won_AD', 'Lost_AD', 'Won%']}
        df1 = self._dataset1.loc[self._dataset1['Player'] == str(self._name)]
        df1 = df1.loc[:, att[self._attribute]]
        df2 = self._dataset2.loc[self._dataset2['Player'] == str(self._name)]
        df2 = df2.loc[:, att[self._attribute]]

    # def data_visuals(self):
    #
    # def data_visuals_gk(self):
