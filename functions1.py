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
        df1 = self._dataset2.loc[self._dataset2['Player'] == str(self._name)]

        row0_spacer1, row0_1, row0_2, row0_3, row0_spacer2 = st.columns((.05, .5, 1, 1, .05))
        with row0_1:
            st.image('images/' + self._name + '.png', use_column_width=True)
        with row0_2:
            st.markdown("##### Name:")
            st.markdown("##### Nationality:")
            st.markdown("##### Position:")
            st.markdown("##### Age:")
            st.markdown("##### Matches Played:")
            st.markdown("##### Games Started:")
        with row0_3:
            st.markdown("           " + str(df.iloc[0]["Player"]))
            st.markdown("           " + str(df.iloc[0]["Nation"]))
            st.markdown("           " + str(df.iloc[0]["Pos"]))
            st.markdown("           " + str(df.iloc[0]["Age"]))
            st.markdown("           " + str(df.iloc[0]["MP"]))
            st.markdown("           " + str(df.iloc[0]["Starts"]))

    def filter_data(self):
        ### Defining what data is in what attribute
        att = {'Shooting 👟': ['Gls', 'Sh', 'SoT%', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'PK', 'PKatt', 'xG', 'npxG',
                              'npxG/Sh', 'G-xG', 'np:G-xG'],
               'Passing ⚽': ['Att', 'Cmp%', 'TotDist_Pass', 'PrgDist_Pass', 'Att_Shrt', 'Cmp%_Shrt', 'Att_Med',
                             'Cmp%_Med', 'Att_Long', 'Cmp%_Long', 'Ast', 'xAG', 'xA', 'KP', '1/3_Pass', 'PPA', 'CrsPA',
                             'PrgP'],
               'Pass Types 🛒': ['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'In', 'Out', 'Str',
                                'Off',
                                'Blocks'],
               'Shot-Creating Actions 😎': ['SCA', 'SCA90', 'PassLive_SCA', 'PassDead_SCA', 'TO_SCA', 'Sh_SCA',
                                           'Fld_SCA',
                                           'Def_SCA'],
               'Goal-Creating Actions 🫡': ['GCA', 'GCA90', 'PassLive_GCA', 'PassDead_GCA', 'TO_GCA', 'Sh_GCA',
                                           'Fld_GCA',
                                           'Def_GCA'],
               'Defensive Actions 💪': ['Tkl', 'TklW', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls', 'Att_Chl', 'Tkl%',
                                       'Lost', 'Blocks_Def', 'Blocks_Sh', 'Pass', 'Int', 'Clr', 'Err'],
               'Possession 👻': ['Touches', 'Def Pen', 'Def 3rd_Tch', 'Mid 3rd_Tch', 'Att 3rd_Tch', 'Att Pen',
                                'Live_Tch',
                                'Att_TakeOns', 'Succ', 'Succ%', 'Tkld', 'Tkld%', 'Carries', 'TotDist_Carr',
                                'PrgDist_Carr', 'PrgC', '1/3_Carr', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR'],
               'Team Success with & without 🎇': ['MP', 'Min', 'Min%', 'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub',
                                                 'unSub', 'PPM', 'onG', 'onGA', '+/-', '+/-90', 'On-Off', 'onxG',
                                                 'onxGA',
                                                 'xG+/-', 'xG+/-90', 'On-Off_xG'],
               'Miscellaneous 🏆': ['CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Offsd', 'PKwon', 'PKcon', 'OG', 'Recov',
                                   'Won_AD', 'Lost_AD', 'Won%'],
               'Advanced Goalkeeping 🥅': ['GA',
                                          'PKA', 'FK', 'CK', 'OG', 'PSxG', 'PSxG/SoT', 'PSxG+/-', '/90', 'Cmp',
                                          'Att_Launch', 'Cmp%', 'Att_Pass',
                                          'Thr', 'Launch%_Pass', 'AvgLen_Pass', 'Att_GKicks', 'Launch%_GKicks',
                                          'AvgLen_GKicks', 'Opp', 'Stp', 'Stp%', '#OPA', '#OPA/90', 'AvgDist']}
        ### Filtering data based off the attribute. However, if the attribute is Advanced Goalkeeping, only DdG has
        ### data and other players will have an empty dataset.
        if self._attribute == 'Advanced Goalkeeping 🥅':
            if self._name == 'David de Gea':
                df1 = self._dataset3.loc[self._dataset3['Player'] == str(self._name)]
                df1 = df1.loc[:, att[self._attribute]]
                df2 = self._dataset3.loc[self._dataset4['Player'] == str(self._name)]
                df2 = df2.loc[:, att[self._attribute]]
            else:
                df1 = pd.DataFrame(columns=att['Advanced Goalkeeping 🥅'])
                df2 = pd.DataFrame(columns=att['Advanced Goalkeeping 🥅'])
        else:
            df1 = self._dataset1.loc[self._dataset1['Player'] == str(self._name)]
            df1 = df1.loc[:, att[self._attribute]]
            df2 = self._dataset2.loc[self._dataset2['Player'] == str(self._name)]
            df2 = df2.loc[:, att[self._attribute]]

        return df1, df2

    def data_visuals(self, df1, df2):
        if self._attribute == 'Shooting 👟':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, .05))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")
            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_5, row1_spacer2 = st.columns((.1, 1, 1, 1, 1, 1, .1))
            with row1_1:
                st.markdown("#### Goals")
                st.markdown("##  " + str(df1.iloc[0]["Gls"]))
                diff1 = round(df1.iloc[0]["Gls"] - df2.iloc[0]["Gls"],2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row1_2:
                st.markdown("#### Shots")
                st.markdown("##  " + str(df1.iloc[0]["Sh"]))
                diff1 = round(df1.iloc[0]["Sh"] - df2.iloc[0]["Sh"],2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row1_3:
                st.markdown("#### SoT%")
                st.markdown("##  " + str(df1.iloc[0]["SoT%"]))
                diff1 = round(df1.iloc[0]["SoT%"] - df2.iloc[0]["SoT%"],2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row1_4:
                st.markdown("#### SoT/90")
                st.markdown("##  " + str(df1.iloc[0]["SoT/90"]))
                diff1 = round(df1.iloc[0]["SoT/90"] - df2.iloc[0]["SoT/90"],2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row1_5:
                st.markdown("#### Goals/Shot")
                st.markdown("##  " + str(df1.iloc[0]["G/Sh"]))
                diff1 = round(df1.iloc[0]["G/Sh"] - df2.iloc[0]["G/Sh"], 2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            row2_spacer1, row2_1, row2_2, row2_3, row2_4, row2_spacer2 = st.columns((.5,1,1,1,1,.5))
            with row2_1:
                st.markdown("#### Goals/SoT")
                st.markdown("##  " + str(df1.iloc[0]["G/SoT"]))
                diff1 = round(df1.iloc[0]["G/SoT"] - df2.iloc[0]["G/SoT"], 2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row2_2:
                st.markdown("#### Shot Dist")
                st.markdown("##  " + str(df1.iloc[0]["Dist"]))
                diff1 = round(df1.iloc[0]["Dist"] - df2.iloc[0]["Dist"], 2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row2_3:
                st.markdown("#### PK")
                st.markdown("##  " + str(df1.iloc[0]["PK"]))
                diff1 = round(df1.iloc[0]["PK"] - df2.iloc[0]["PK"], 2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            with row2_4:
                st.markdown("#### PKatt")
                st.markdown("##  " + str(df1.iloc[0]["PKatt"]))
                diff1 = round(df1.iloc[0]["PKatt"] - df2.iloc[0]["PKatt"], 2)
                if diff1 > 0:
                    st.markdown(":green[↑ %a]" % diff1)
                elif diff1 == 0:
                    st.markdown(diff1)
                else:
                    st.markdown(":red[↓ %a]" % diff1)
            row3_spacer1, row3_1, row3_spacer2 = st.columns((.05, 3.2, .05))
            with row3_1:
                st.markdown("##### Expected Results     -    :green[↑]/:red[↓] from previous season")
    # def data_visuals_gk(self, df1, df2):
