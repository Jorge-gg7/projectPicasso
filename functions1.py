import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image


class dataFunc1:
    def __init__(self, name, attribute, dataset1, dataset2, dataset3, dataset4, dataset5):
        """Used to create a new data set from the given user input
        :param name: Name of the player
        :param attribute: Attribute of the player like Shooting and Goalkeeping that the user is interested
        :param dataset1: First dataset used to extract data - 2022/23 dataset
        :param dataset2: Second dataset used to extract data - 2021/22 dataset
        :param dataset3: Third dataset used to extract data - 2022/23 gk dataset
        :param dataset4: Fourth dataset used to extract data - 2021/22 gk dataset
        :param dataset5: Fifth dataset used to extract data - 2022/23 new signings dataset
        """
        self._name = name
        self._attribute = attribute
        self._dataset1 = dataset1
        self._dataset2 = dataset2
        self._dataset3 = dataset3
        self._dataset4 = dataset4
        self._dataset5 = dataset5

    def display(self):
        df = self._dataset1.loc[self._dataset1['Player'] == str(self._name)].reset_index(drop=True)

        row0_spacer1, row0_1, row0_2, row0_3, row0_4, row0_spacer2 = st.columns((.05, .5, .5, .5, 1.25, .05))
        with row0_1:
            st.image('images/' + self._name + '.png', width=170)
        with row0_2:
            st.markdown("##### Name:")
            st.markdown("##### Nationality:")
            st.markdown("##### Position:")
            st.markdown("##### Age:")
            st.markdown("##### Matches Played:")
            st.markdown("##### Games Started:")
        with row0_3:
            st.markdown("#####           " + str(df.iloc[0]["Player"]))
            st.markdown("#####           " + str(df.iloc[0]["Nation"]))
            st.markdown("#####           " + str(df.iloc[0]["Pos"]))
            st.markdown("#####           " + str(df.iloc[0]["Age"]))
            st.markdown("#####           " + str(df.iloc[0]["MP"]))
            st.markdown("#####           " + str(df.iloc[0]["Starts"]))
        with row0_4:
            df.at[0, 'SoT%'] = df.at[0, 'SoT%'] / 100
            df['Dribbling'] = (df.at[0, 'Succ%'] + df.at[0, 'Tkld%']) / 200
            df.at[0, 'Tkl%'] = df.at[0, 'Tkl%'] / 100
            df.at[0, 'Succ%'] = df.at[0, 'Succ%'] / 100
            df.at[0, 'Cmp%'] = df.at[0, 'Cmp%'] / 100
            dff = pd.melt(df, id_vars='Player', value_vars=['SoT%', 'Cmp%', 'Dribbling', 'Tkl%', 'Succ%'],
                          var_name='Attributes', value_name='Rating')
            dff.replace(['SoT%', 'Cmp%', 'Tkl%', 'Succ%'], ['Shooting', 'Passing', 'Defending', 'Possession'],
                        inplace=True)
            fig = px.line_polar(dff, r='Rating', theta='Attributes', line_close=True, height=221, width=400,
                                color_discrete_sequence=['orange'], range_r=[0, 1])
            fig.update_traces(fill='toself')
            fig.update_layout(margin=dict(t=20, b=0), font_size=12, plot_bgcolor='#0e1117', font_color="grey")
            st.plotly_chart(fig, use_container_width=True, theme='streamlit')

    def filter_data(self):
        ### Defining what data is in what attribute
        att = {'Shooting 👟': ['Player', 'Gls', 'Sh', 'SoT%', 'SoT/90', 'G/Sh', 'Dist', 'PK', 'xG', 'npxG',
                              'npxG/Sh', 'G-xG', 'np:G-xG'],
               'Passing ⚽': ['Player', 'Att', 'Cmp%', 'TotDist_Pass', 'PrgDist_Pass', 'Att_Shrt', 'Cmp%_Shrt',
                             'Att_Med', 'Cmp%_Med', 'Att_Long', 'Cmp%_Long', 'Ast', 'xAG', 'xA', 'KP', '1/3_Pass',
                             'PPA',
                             'CrsPA', 'PrgP'],
               'Pass Types 🛒': ['Player', 'Att', 'Cmp', 'Cmp%', 'Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs', 'TI',
                                'CK', 'In', 'Out', 'Str', 'Off', 'Blocks'],
               'Shot-Creating Actions 😎': ['Player', 'SCA', 'SCA90', 'PassLive_SCA', 'PassDead_SCA', 'TO_SCA', 'Sh_SCA',
                                           'Fld_SCA', 'Def_SCA'],
               'Goal-Creating Actions 🫡': ['Player', 'GCA', 'GCA90', 'PassLive_GCA', 'PassDead_GCA', 'TO_GCA', 'Sh_GCA',
                                           'Fld_GCA', 'Def_GCA'],
               'Defensive Actions 💪': ['Player', 'Tkl', 'TklW', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls',
                                       'Att_Chl', 'Tkl_Chl', 'Lost', 'Blocks_Def', 'Blocks_Sh', 'Pass', 'Int', 'Clr',
                                       'Err'],
               'Possession 👻': ['Player', 'Touches', 'Def Pen', 'Def 3rd_Tch', 'Mid 3rd_Tch', 'Att 3rd_Tch', 'Att Pen',
                                'Live_Tch', 'Att_TakeOns', 'Succ', 'Succ%', 'Tkld', 'Tkld%', 'Carries', 'TotDist_Carr',
                                'PrgDist_Carr', 'PrgC', '1/3_Carr', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR'],
               'Team Success with & without 🎇': ['Player', 'MP', 'Min', 'Min%', 'Starts', 'Mn/Start', 'Compl', 'Subs',
                                                 'Mn/Sub', 'unSub', 'PPM', 'onG', 'onGA', '+/-', '+/-90', 'On-Off',
                                                 'onxG', 'onxGA', 'xG+/-', 'xG+/-90', 'On-Off_xG'],
               'Miscellaneous 🏆': ['Player', 'CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Offsd', 'PKwon', 'PKcon', 'OG',
                                   'Recov', 'Won_AD', 'Lost_AD', 'Won%'],
               'Advanced Goalkeeping 🥅': ['Player', 'GA', 'PKA', 'FK', 'CK', 'OG', 'PSxG', 'PSxG/SoT', 'PSxG+/-', '/90',
                                          'Cmp', 'Att_Launch', 'Cmp%', 'Att_Pass', 'Thr', 'Launch%_Pass', 'AvgLen_Pass',
                                          'Att_GKicks', 'Launch%_GKicks', 'AvgLen_GKicks', 'Opp', 'Stp', 'Stp%', '#OPA',
                                          '#OPA/90', 'AvgDist']}
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
        """

        :param df1: Filtered dataframe of dataset1
        :param df2: Filtered dataframe of dataset2
        :return:
        """
        if self._attribute == 'Shooting 👟':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, .05))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_spacer2, row1_2, row1_3, row1_spacer3 = st.columns((.1, 1.5, 1.5, .8, 1.7, .1))
            with row1_1:
                stat = ['Goals', 'Shots', 'Shots on Target%', 'Shots on Target per 90', 'Goals per Shot', 'Average'
                                                                                                          ' Shot Distance',
                        'Penalty Kick Goals']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row1_2:
                if see == "Goals":
                    diff1 = round(df1.iloc[0]["Gls"] - df2.iloc[0]["Gls"], 2)
                    st.metric("Goals", df1.iloc[0]["Gls"], diff1)
                elif see == "Shots":
                    diff1 = round(df1.iloc[0]["Sh"] - df2.iloc[0]["Sh"], 2)
                    st.metric("Shots", df1.iloc[0]["Sh"], diff1)
                elif see == "Shots on Target%":
                    diff1 = round(df1.iloc[0]["SoT%"] - df2.iloc[0]["SoT%"], 2)
                    st.metric("Shots on Target%", str(df1.iloc[0]["SoT%"]) + " %", str(diff1) + " %")
                elif see == "Shots on Target per 90":
                    diff1 = round(df1.iloc[0]["SoT/90"] - df2.iloc[0]["SoT/90"], 2)
                    st.metric("SoT/90", df1.iloc[0]["SoT/90"], diff1)
                elif see == "Goals per Shot":
                    diff1 = round(df1.iloc[0]["G/Sh"] - df2.iloc[0]["G/Sh"], 2)
                    st.metric("Goals Per Shot", df1.iloc[0]["G/Sh"], diff1)
                elif see == "Average Shot Distance":
                    diff1 = round(df1.iloc[0]["Dist"] - df2.iloc[0]["Dist"], 2)
                    st.metric("Avg Shot Dist.", str(df1.iloc[0]["Dist"]) + " yrd", str(diff1) + "yrd")
                elif see == "Penalty Kick Goals":
                    diff1 = round(df1.iloc[0]["PK"] - df2.iloc[0]["PK"], 2)
                    st.metric("Penalty Goals", df1.iloc[0]["PK"], diff1)
            with row1_3:
                if see == 'Goals':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Gls"] - (self._dataset1["Gls"].sum() + self._dataset5["Gls"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Shots":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Sh"] - (self._dataset1["Sh"].sum() + self._dataset5["Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Shots on Target%":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["SoT%"] - self._dataset1["SoT%"].mean(), 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Shots on Target per 90":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["SoT/90"] - (self._dataset1["SoT/90"].sum() +
                                                           self._dataset5["SoT/90"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Goals per Shot":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["G/Sh"] - (self._dataset1["G/Sh"].sum() + self._dataset5["G/Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Average Shot Distance":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Dist"] - (self._dataset1["Dist"].sum() + self._dataset5["Dist"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Penalty Kick Goals":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PK"] - (self._dataset1["PK"].sum() + self._dataset5["PK"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
            with row1_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")

            row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 5, .1))
            with row2_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == 'Goals':
                    dff1['Gls_Rank'] = dff1['Gls'].rank(ascending=False)
                    dff1 = dff1.sort_values("Gls_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Gls'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Goals")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Shots':
                    dff1['Sh_Rank'] = dff1['Sh'].rank(ascending=False)
                    dff1 = dff1.sort_values("Sh_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Sh'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Shots Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Shots")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Shots on Target%':
                    dff1['SoT%_Rank'] = dff1['SoT%'].rank(ascending=False)
                    dff1 = dff1.sort_values("SoT%_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['SoT%'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Shots on Target % Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="SoT %")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Shots on Target per 90':
                    dff1['SoT/90_Rank'] = dff1['SoT/90'].rank(ascending=False)
                    dff1 = dff1.sort_values("SoT/90_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['SoT/90'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Shots on Target per 90 Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="SoT/90")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Goals per Shot':
                    dff1['G/Sh_Rank'] = dff1['G/Sh'].rank(ascending=False)
                    dff1 = dff1.sort_values("G/Sh_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['G/Sh'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Goals per Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Goals/Shot")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Average Shot Distance':
                    dff1['Dist_Rank'] = dff1['Dist'].rank(ascending=False)
                    dff1 = dff1.sort_values("Dist_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Dist'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Avg Shot Distance Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Distance (yrds)")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Penalty Kick Goals':
                    dff1['PK_Rank'] = dff1['PK'].rank(ascending=False)
                    dff1 = dff1.sort_values("PK_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PK'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Penalty Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Penalty Goals")
                    st.plotly_chart(fig, use_container_width=True)

            row3_spacer1, row3_1, row3_spacer2 = st.columns((.05, 3.2, .05))
            with row3_1:
                st.markdown("##### Expected Results     -    :green[↑]/:red[↓] from previous season")

            row4_spacer1, row4_1, row4_spacer2, row4_2, row4_3, row4_spacer3 = st.columns((.1, 2, 1, .8, 1.5, .1))
            with row4_1:
                stat = ['Expected Goals', 'Non-Penalty Expected Goals', 'Non-Penalty Expected Goals per Shot',
                        'Goals minus Expected Goals', 'Non-Penalty Expected Goals minus Expected Goals']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row4_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")
            with row4_2:
                if see == "Expected Goals":
                    diff1 = round(df1.iloc[0]["xG"] - df2.iloc[0]["xG"], 2)
                    st.metric("Expected Goals", df1.iloc[0]["xG"], diff1)
                elif see == "Non-Penalty Expected Goals":
                    diff1 = round(df1.iloc[0]["npxG"] - df2.iloc[0]["npxG"], 2)
                    st.metric("Non-Pen xG", df1.iloc[0]["npxG"], diff1)
                elif see == "Non-Penalty Expected Goals per Shot":
                    diff1 = round(df1.iloc[0]["npxG/Sh"] - df2.iloc[0]["npxG/Sh"], 2)
                    st.metric("Non-Pen xG/Sh", str(df1.iloc[0]["npxG/Sh"]), str(diff1))
                elif see == "Goals minus Expected Goals":
                    diff1 = round(df1.iloc[0]["G-xG"] - df2.iloc[0]["G-xG"], 2)
                    st.metric("G - xG", df1.iloc[0]["G-xG"], diff1)
                elif see == "Non-Penalty Expected Goals minus Expected Goals":
                    diff1 = round(df1.iloc[0]["np:G-xG"] - df2.iloc[0]["np:G-xG"], 2)
                    st.metric("Non-Pen xG - xG", df1.iloc[0]["G/Sh"], diff1)
            with row4_3:
                if see == 'Expected Goals':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["xG"] - (self._dataset1["xG"].sum() + self._dataset5["xG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Non-Penalty Expected Goals':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["npxG"] - (self._dataset1["npxG"].sum() + self._dataset5["npxG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == "Non-Penalty Expected Goals per Shot":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["npxG/Sh"] - (
                            self._dataset1["npxG/Sh"].sum() + self._dataset5["npxG/Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more expected accuracy than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less expected accuracy than team average this season." % diff1)
                elif see == "Goals minus Expected Goals":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["G-xG"] - (self._dataset1["G-xG"].sum() + self._dataset5["G-xG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Non-Penalty Expected Goals minus Expected Goals':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["np:G-xG"] - (
                            self._dataset1["np:G-xG"].sum() + self._dataset5["np:G-xG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row5_spacer1, row5_1, row5_spacer2 = st.columns((.05, 5, .05))
            with row5_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == "Expected Goals":
                    dff1['xG_Rank'] = dff1['xG'].rank(ascending=False)
                    dff1 = dff1.sort_values("xG_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['xG'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Expected Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Expected Goals")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Non-Penalty Expected Goals":
                    dff1['npxG_Rank'] = dff1['npxG'].rank(ascending=False)
                    dff1 = dff1.sort_values("npxG_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['npxG'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Non-Penalty Expected Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Non-Pen Expected Goals")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Non-Penalty Expected Goals per Shot":
                    dff1['npxG/Sh_Rank'] = dff1['npxG/Sh'].rank(ascending=False)
                    dff1 = dff1.sort_values("npxG/Sh_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['npxG/Sh'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Non-Penalty Expected Goals per Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Non-Pen Expected Goals/Shot")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Goals minus Expected Goals":
                    dff1['G-xG_Rank'] = dff1['G-xG'].rank(ascending=False)
                    dff1 = dff1.sort_values("G-xG_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['G-xG'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Goals - Expected Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Goals - Expected Goals")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Non-Penalty Expected Goals minus Expected Goals":
                    dff1['np:G-xG_Rank'] = dff1['np:G-xG'].rank(ascending=False)
                    dff1 = dff1.sort_values("np:G-xG_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['np:G-xG'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Non-Penalty Expected Goals - Expected Goals Ranking',
                                      title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="npxG - xG")
                    st.plotly_chart(fig, use_container_width=True)

        elif self._attribute == 'Passing ⚽':

            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, .05))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_spacer2 = st.columns((.1, 1.35, 1.75, 1.2, 2, 0.1))
            with row1_1:
                diff1 = round(df1.iloc[0]["Ast"] - df2.iloc[0]["Ast"], 2)
                st.metric("Assists", str(df1.iloc[0]["Ast"]), diff1)
                diff1 = round(df1.iloc[0]["Att"] - df2.iloc[0]["Att"], 2)
                st.metric("Passess Attempted", str(df1.iloc[0]["Att"]), diff1)
                diff1 = round(df1.iloc[0]["TotDist_Pass"] - df2.iloc[0]["TotDist_Pass"], 2)
                st.metric("Total Distance Passed", str(df1.iloc[0]["TotDist_Pass"]) + " yrds", str(diff1) + " yrds")
            with row1_2:
                st.markdown("## ")
                diff1 = round(df1.iloc[0]["Ast"] - (self._dataset1["Ast"].sum() + self._dataset5["Ast"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                st.markdown("## ")
                st.markdown("### ")
                diff1 = round(df1.iloc[0]["Att"] - (self._dataset1["Att"].sum() + self._dataset5["Att"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                st.markdown("### ")
                st.markdown("### ")
                diff1 = round(df1.iloc[0]["TotDist_Pass"] - (
                        self._dataset1["TotDist_Pass"].sum() + self._dataset5["TotDist_Pass"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
            with row1_3:
                diff1 = round(df1.iloc[0]["Cmp%"] - df2.iloc[0]["Cmp%"], 2)
                st.metric("Passess Completed %", str(df1.iloc[0]["Cmp%"]) + " %", diff1)
                diff1 = round(df1.iloc[0]["PrgDist_Pass"] - df2.iloc[0]["PrgDist_Pass"], 2)
                st.metric("Total Progressive Distance Passed", str(df1.iloc[0]["PrgDist_Pass"]) + " yrds", str(diff1) +
                          " yrds")
            with row1_4:
                st.markdown("## ")
                diff1 = round(df1.iloc[0]["Cmp%"] - (self._dataset1["Cmp%"].sum() + self._dataset5["Cmp%"].sum()) / 26,
                              2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                st.markdown("# ")
                st.markdown("##### ")
                diff1 = round(df1.iloc[0]["PrgDist_Pass"] - (
                        self._dataset1["PrgDist_Pass"].sum() + self._dataset5["PrgDist_Pass"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] yards further than team average this seaosn." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] yards nearer than team average this season." % diff1)

            row2_spacer1, row2_1, row2_2, row2_spacer2 = st.columns((.1, 3, 3, .1))
            with row2_1:
                dff = df1.loc[:, ['Player', 'Att_Shrt', 'Att_Med', 'Att_Long']]
                dff = dff.replace(self._name, str(self._name) + " 2022/23")
                dff2 = df2.loc[:, ['Player', 'Att_Shrt', 'Att_Med', 'Att_Long']]
                dff2 = dff2.replace(self._name, str(self._name) + " 2021/22")
                dff = dff.append(dff2, ignore_index=True)

                dff_avg1 = pd.concat([self._dataset1, self._dataset5]).reset_index(drop=True)
                dff_avg1.loc['Average 2022/23'] = dff_avg1.mean()
                dff_avg1 = dff_avg1.loc['Average 2022/23', ['Player', 'Att_Shrt', 'Att_Med', 'Att_Long']]
                dff = dff.append(dff_avg1, ignore_index=True)
                dff = dff.fillna("Team Average 2022/23")

                dff_avg2 = self._dataset2.reset_index()
                dff_avg2.loc['Average 2021/22'] = dff_avg2.mean()
                dff_avg2 = dff_avg2.loc['Average 2021/22', ['Player', 'Att_Shrt', 'Att_Med', 'Att_Long']]
                dff = dff.append(dff_avg2, ignore_index=True)
                dff = dff.fillna("Team Average 2021/22")

                fig = px.bar(dff, x='Player', y=['Att_Shrt', 'Att_Med',
                                                 'Att_Long'], labels={'value': 'Number of Pass Attempts',
                                                                      'variable': 'Variable'}, title='Attempted Passes')
                new_names = {'Att_Shrt': 'Short Pass Atmpt', 'Att_Med': 'Medium Pass Atmpt',
                             'Att_Long': 'Long Pass Atmpt'}
                fig.for_each_trace(lambda t: t.update(name=new_names[t.name],
                                                      legendgroup=new_names[t.name],
                                                      hovertemplate=t.hovertemplate.replace(t.name, new_names[t.name])
                                                      ))
                fig.update_layout(barmode='group', height=450, legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1,
                    xanchor="right",
                    x=1
                ))
                st.plotly_chart(fig, use_container_width=True, width=500)
            with row2_2:
                dff = df1.loc[:, ['Player', 'Cmp%_Shrt', 'Cmp%_Med', 'Cmp%_Long']]
                dff = dff.replace(self._name, str(self._name) + " 2022/23")
                dff2 = df2.loc[:, ['Player', 'Cmp%_Shrt', 'Cmp%_Med', 'Cmp%_Long']]
                dff2 = dff2.replace(self._name, str(self._name) + " 2021/22")
                dff = dff.append(dff2, ignore_index=True)

                dff_avg1 = pd.concat([self._dataset1, self._dataset5]).reset_index(drop=True)
                dff_avg1.loc['Average 2022/23'] = dff_avg1.mean()
                dff_avg1 = dff_avg1.loc['Average 2022/23', ['Player', 'Cmp%_Shrt', 'Cmp%_Med', 'Cmp%_Long']]
                dff = dff.append(dff_avg1, ignore_index=True)
                dff = dff.fillna("Team Average 2022/23")

                dff_avg2 = self._dataset2.reset_index()
                dff_avg2.loc['Average 2021/22'] = dff_avg2.mean()
                dff_avg2 = dff_avg2.loc['Average 2021/22', ['Player', 'Cmp%_Shrt', 'Cmp%_Med', 'Cmp%_Long']]
                dff = dff.append(dff_avg2, ignore_index=True)
                dff = dff.fillna("Team Average 2021/22")

                fig = px.bar(dff, x='Player', y=['Player', 'Cmp%_Shrt', 'Cmp%_Med', 'Cmp%_Long'], labels={'value': '%',
                                                                                                          'variable': 'Variable'},
                             title='Pass Completion Rate %')
                new_names = {'Cmp%_Shrt': 'Pass Completion % Short', 'Cmp%_Med': 'Pass Completion % Medium',
                             'Cmp%_Long': 'Pass Completion % Long'}
                fig.for_each_trace(lambda t: t.update(name=new_names[t.name],
                                                      legendgroup=new_names[t.name],
                                                      hovertemplate=t.hovertemplate.replace(t.name, new_names[t.name])
                                                      ))
                fig.update_layout(barmode='group', legend=dict(
                    orientation="v",
                    yanchor="bottom",
                    y=1,
                    xanchor="right",
                    x=1
                ))
                st.plotly_chart(fig, use_container_width=True, width=500)

            row3_spacer1, row3_1, row3_spacer2, row3_2, row3_3, row3_spacer3 = st.columns((.1, 1.5, 1.3, 1, 1.7, .1))
            with row3_1:
                stat = ['Expected Assists Goals', 'Expected Assists', 'Key Passes', 'Passes into Final Third',
                        'Passes into Penalty Area', 'Crosses into Penalty Area', 'Progressive Passes']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row3_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")
            with row3_2:
                if see == 'Expected Assists Goals':
                    diff1 = round(df1.iloc[0]["xAG"] - df2.iloc[0]["xAG"], 2)
                    st.metric("Exp Assisted Goals", df1.iloc[0]["xAG"], diff1)
                elif see == 'Expected Assists':
                    diff1 = round(df1.iloc[0]["xA"] - df2.iloc[0]["xA"], 2)
                    st.metric("Exp Assists", df1.iloc[0]["xA"], diff1)
                elif see == 'Key Passes':
                    diff1 = round(df1.iloc[0]["KP"] - df2.iloc[0]["KP"], 2)
                    st.metric("Key Passes", df1.iloc[0]["KP"], diff1)
                elif see == 'Passes into Final Third':
                    diff1 = round(df1.iloc[0]["1/3_Pass"] - df2.iloc[0]["1/3_Pass"], 2)
                    st.metric("1/3 Pass", df1.iloc[0]["1/3_Pass"], diff1)
                elif see == 'Passes into Penalty Area':
                    diff1 = round(df1.iloc[0]["PPA"] - df2.iloc[0]["PPA"], 2)
                    st.metric("Passes into Pen", df1.iloc[0]["PPA"], diff1)
                elif see == 'Crosses into Penalty Area':
                    diff1 = round(df1.iloc[0]["CrsPA"] - df2.iloc[0]["CrsPA"], 2)
                    st.metric("Crosses into Pen", df1.iloc[0]["CrsPA"], diff1)
                elif see == 'Progressive Passes':
                    diff1 = round(df1.iloc[0]["PrgP"] - df2.iloc[0]["PrgP"], 2)
                    st.metric("Prgsv Pass", df1.iloc[0]["PrgP"], diff1)
            with row3_3:
                if see == 'Expected Assists Goals':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["xAG"] - (self._dataset1["xAG"].sum() + self._dataset5["xAG"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Expected Assists':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["xA"] - (self._dataset1["xA"].sum() + self._dataset5["xA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Key Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["KP"] - (self._dataset1["KP"].sum() + self._dataset5["KP"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Passes into Final Third':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["1/3_Pass"] - (
                            self._dataset1["1/3_Pass"].sum() + self._dataset5["1/3_Pass"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Passes into Penalty Area':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PPA"] - (self._dataset1["PPA"].sum() + self._dataset5["PPA"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Crosses into Penalty Area':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["CrsPA"] - (self._dataset1["CrsPA"].sum() + self._dataset5["CrsPA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Progressive Passes':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["PrgP"] - (self._dataset1["PrgP"].sum() + self._dataset5["PrgP"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row4_spacer1, row4_1, row4_spacer2 = st.columns((.1, 3.2, .1))
            with row4_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == 'Expected Assists Goals':
                    dff1['xAG_Rank'] = dff1['xAG'].rank(ascending=False)
                    dff1 = dff1.sort_values("xAG_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['xAG'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Expected Assists Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Expected Assists Goals")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Expected Assists":
                    dff1['xA_Rank'] = dff1['xA'].rank(ascending=False)
                    dff1 = dff1.sort_values("xA_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['xA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Expected Assists Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Expected Assists")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Key Passes':
                    dff1['KP_Rank'] = dff1['KP'].rank(ascending=False)
                    dff1 = dff1.sort_values("KP_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['KP'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Key Passes Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Key Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Passes into Final Third':
                    dff1['1/3_Rank'] = dff1['1/3_Pass'].rank(ascending=False)
                    dff1 = dff1.sort_values("1/3_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['1/3_Pass'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Final Third Passes Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Final Third Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Passes into Penalty Area":
                    dff1['PPA_Rank'] = dff1['PPA'].rank(ascending=False)
                    dff1 = dff1.sort_values("PPA_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PPA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Passes into Penalty Area Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes into Penalty Area")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Crosses into Penalty Area':
                    dff1['CrsPA_Rank'] = dff1['CrsPA'].rank(ascending=False)
                    dff1 = dff1.sort_values("CrsPA_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['CrsPA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Crosses into Penalty Area Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Crosses into Penalty Area")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Progressive Passes':
                    dff1['PrgP_Rank'] = dff1['PrgP'].rank(ascending=False)
                    dff1 = dff1.sort_values("PrgP_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PrgP'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Progressive Passess Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Progressive Passes")
                    st.plotly_chart(fig, use_container_width=True)

        elif self._attribute == 'Pass Types 🛒':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, 5))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_2, row1_3, row1_spacer2 = st.columns((.05, 2, 2, 5, 2))
            with row1_1:
                diff1 = round(df1.iloc[0]["Att"] - df2.iloc[0]["Att"], 2)
                st.metric("Attempted Passes", df1.iloc[0]["Att"], diff1)
            with row1_2:
                diff1 = round(df1.iloc[0]["Cmp"] - df2.iloc[0]["Cmp"], 2)
                st.metric("Completed Passes", df1.iloc[0]["Cmp"], diff1)
            with row1_3:
                diff1 = round(df1.iloc[0]["Cmp%"] - df2.iloc[0]["Cmp%"], 2)
                st.metric("Completed Passes %", str(df1.iloc[0]["Cmp%"]) + " %", str(diff1) + " %")
            with row1_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")

            row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .01))
            with row2_1:
                dff1 = df1
                dff1.replace(str(self._name), str(self._name) + " 2022/23", inplace=True)
                dff2 = df2
                dff2.replace(str(self._name), str(self._name) + " 2021/22", inplace=True)
                dff = pd.concat([dff1, dff2], ignore_index=True)

                dff = pd.melt(dff, id_vars=['Player'], value_vars=['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs',
                                                                   'TI', 'CK'], var_name='Statistic',
                              value_name='Amount of Passes')
                dff.replace(['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs', 'TI', 'CK'],
                            ['Live Pass', 'Dead Pass', 'Freekick Pass', 'Through Balls', 'Switches', 'Crosses',
                             'Throw Ins', 'Corner Kicks'], inplace=True)

                fig = px.bar(dff, x='Statistic', y='Amount of Passes', color='Player')
                fig.update_layout(barmode='group', title='Pass Types')
                st.plotly_chart(fig, use_container_width=True)

            row3_spacer1, row3_1, row3_2, row3_3, row3_spacer2 = st.columns((.1, 4, 2, 2, .1))
            with row3_1:
                dff1 = df1
                dff1['Others'] = dff1['CK'] - dff1['In'] - dff1['Out'] - dff1['Str']
                dff1 = pd.melt(dff1, id_vars='Player', value_vars=['CK', 'In', 'Out', 'Str', 'Others'],
                               var_name='Statistic',
                               value_name='Amount of Passes')

                dff2 = df2
                dff2['Others'] = dff2['CK'] - dff2['In'] - dff2['Out'] - dff2['Str']
                dff2 = pd.melt(dff2, id_vars='Player', value_vars=['CK', 'In', 'Out', 'Str', 'Others'],
                               var_name='Statistic', value_name='Amount of Passes')

                dff = pd.concat([dff1, dff2], ignore_index=True)
                dff.replace(['CK', 'In', 'Out', 'Str'], ['Corner Kicks', 'In-Swing Corner', 'Out-Swing Corner',
                                                         'Straight'], inplace=True)
                fig = px.bar(dff, x='Statistic', y='Amount of Passes', color='Player')
                fig.update_layout(legend=dict(orientation='h', yanchor="top", y=1.05, xanchor="right", x=1), barmode=
                'group', title='Corner Kick Statistics')
                st.plotly_chart(fig, use_container_width=True)

            with row3_2:
                diff1 = round(df1.iloc[0]['Off'] - df2.iloc[0]['Off'], 2)
                st.markdown("### Pass Outcomes")
                st.metric('Offside Passes', df1.iloc[0]['Off'], diff1)
            with row3_3:
                diff1 = round(df1.iloc[0]['Blocks'] - df2.iloc[0]['Blocks'], 2)
                st.markdown("## ")
                st.markdown("#### ")
                st.metric('Blocked Passes', df1.iloc[0]['Blocks'], diff1)

        elif self._attribute == 'Shot-Creating Actions 😎':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, 5))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_spacer2 = st.columns((.05, 1, 2, 1, 2, .05))
            with row1_1:
                diff = round(df1.iloc[0]['SCA'] - df2.iloc[0]['SCA'], 2)
                st.metric('Shot Creating Actions', df1.iloc[0]['SCA'], diff)
                st.markdown(" ")
                st.metric('Example Stat', 'Value', '↑/↓ from prev season')
            with row1_2:
                st.markdown("# ")
                diff1 = round(df1.iloc[0]["SCA"] - (self._dataset1["SCA"].sum() + self._dataset5["SCA"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
            with row1_3:
                diff = round(df1.iloc[0]['SCA90'] - df2.iloc[0]['SCA90'], 2)
                st.metric('SCA per 90', df1.iloc[0]['SCA90'], diff)
            with row1_4:
                st.markdown("# ")
                diff1 = round(
                    df1.iloc[0]["SCA90"] - (self._dataset1["SCA90"].sum() + self._dataset5["SCA90"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row2_spacer1, row2_1, row2_2, row2_spacer2 = st.columns((.05, 5, 5, .05))
            with row2_1:
                dff1 = pd.melt(df1, id_vars='Player', value_vars=["PassLive_SCA", 'PassDead_SCA', 'TO_SCA', 'Sh_SCA',
                                                                  'Fld_SCA', 'Def_SCA'], var_name='SCA', value_name=
                               'Actions')
                dff1.replace(["PassLive_SCA", 'PassDead_SCA', 'TO_SCA', 'Sh_SCA', 'Fld_SCA', 'Def_SCA'],
                             ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions'],
                             inplace=True)
                fig = px.pie(dff1, values='Actions', names='SCA',
                             title='% of Different Shot Creating Actions Created by'
                                   ' Player in 2022/23 Season')
                fig.update_layout(margin=dict(t=30, b=20), height=350, title_font_size=14)
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                st.plotly_chart(fig, use_container_width=True)
            with row2_2:
                dff1 = pd.melt(df2, id_vars='Player', value_vars=["PassLive_SCA", 'PassDead_SCA', 'TO_SCA', 'Sh_SCA',
                                                                  'Fld_SCA', 'Def_SCA'], var_name='SCA', value_name=
                               'Actions')
                dff1.replace(["PassLive_SCA", 'PassDead_SCA', 'TO_SCA', 'Sh_SCA', 'Fld_SCA', 'Def_SCA'],
                             ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions'],
                             inplace=True)
                fig = px.pie(dff1, values='Actions', names='SCA',
                             title='% of Different Shot Creating Actions Created by'
                                   ' Player in 2021/22 Season')
                fig.update_layout(margin=dict(t=30, b=20), height=350, title_font_size=14)
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                st.plotly_chart(fig, use_container_width=True)

            row3_spacer1, row3_1, row3_spacer2, row3_2, row3_3, row3_spacer3 = st.columns((.1, 1.5, 1.3, 1, 1.7, .1))
            with row3_1:
                stat = ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row3_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")
            with row3_2:
                if see == 'Live Passes':
                    diff1 = round(df1.iloc[0]["PassLive_SCA"] - df2.iloc[0]["PassLive_SCA"], 2)
                    st.metric("Live Passes to Shot", df1.iloc[0]["PassLive_SCA"], diff1)
                elif see == 'Dead Passes':
                    diff1 = round(df1.iloc[0]["PassDead_SCA"] - df2.iloc[0]["PassDead_SCA"], 2)
                    st.metric("Dead Passes to Shot", df1.iloc[0]["PassDead_SCA"], diff1)
                elif see == 'Take-Ons':
                    diff1 = round(df1.iloc[0]["TO_SCA"] - df2.iloc[0]["TO_SCA"], 2)
                    st.metric("Take-Ons to Shot", df1.iloc[0]["TO_SCA"], diff1)
                elif see == 'Shots':
                    diff1 = round(df1.iloc[0]["Sh_SCA"] - df2.iloc[0]["Sh_SCA"], 2)
                    st.metric("Shots Leading to Shot", df1.iloc[0]["Sh_SCA"], diff1)
                elif see == 'Fouls Drawn':
                    diff1 = round(df1.iloc[0]["Fld_SCA"] - df2.iloc[0]["Fld_SCA"], 2)
                    st.metric("Fouls Drawn to Shot", df1.iloc[0]["Fld_SCA"], diff1)
                elif see == 'Defensive Actions':
                    diff1 = round(df1.iloc[0]["Def_SCA"] - df2.iloc[0]["Def_SCA"], 2)
                    st.metric("Defensive Actions to Shot", df1.iloc[0]["Def_SCA"], diff1)
            with row3_3:
                if see == 'Live Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PassLive_SCA"] - (
                            self._dataset1["PassLive_SCA"].sum() + self._dataset5["PassLive_SCA"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Dead Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PassDead_SCA"] - (
                            self._dataset1["PassDead_SCA"].sum() + self._dataset5["PassDead_SCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Take-Ons':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["TO_SCA"] - (self._dataset1["TO_SCA"].sum() + self._dataset5["TO_SCA"].sum()) / 26,
                        2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Fouls Drawn':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Fld_SCA"] - (
                            self._dataset1["Fld_SCA"].sum() + self._dataset5["Fld_SCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Shots':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Sh_SCA"] - (self._dataset1["Sh_SCA"].sum() + self._dataset5["Sh_SCA"].sum()) / 26,
                        2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Defensive Actions':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Def_SCA"] - (
                                self._dataset1["Def_SCA"].sum() + self._dataset5["Def_SCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row4_spacer1, row4_1, row4_spacer2 = st.columns((.1, 3.2, .1))
            with row4_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == 'Live Passes':
                    dff1['LivePass_Rank'] = dff1['PassLive_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("LivePass_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PassLive_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Live Passes leading to Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Dead Passes":
                    dff1['DP_Rank'] = dff1['PassDead_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("DP_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PassDead_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Dead Passes leading to Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Take-Ons':
                    dff1['TO_Rank'] = dff1['TO_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("TO_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['TO_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Take-ons leading to Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Shots':
                    dff1['Sh_Rank'] = dff1['Sh_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("Sh_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Sh_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Shots leading to other Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Shots")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Fouls Drawn":
                    dff1['F_Rank'] = dff1['Fld_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("F_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Fld_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Fouls Drawn leading to Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Fouls Drawn")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Defensive Actions':
                    dff1['D_Rank'] = dff1['Def_SCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("D_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Def_SCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Defensive Actions leading to Shot Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Defensive Actions")
                    st.plotly_chart(fig, use_container_width=True)

        elif self._attribute == 'Goal-Creating Actions 🫡':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, 5))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_spacer2 = st.columns((.05, 1, 2, 1, 2, .05))
            with row1_1:
                diff = round(df1.iloc[0]['GCA'] - df2.iloc[0]['GCA'], 2)
                st.metric('Goal Creating Actions', df1.iloc[0]['GCA'], diff)
                st.markdown(" ")
                st.metric('Example Stat', 'Value', '↑/↓ from prev season')
            with row1_2:
                st.markdown("# ")
                diff1 = round(df1.iloc[0]["GCA"] - (self._dataset1["GCA"].sum() + self._dataset5["GCA"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
            with row1_3:
                diff = round(df1.iloc[0]['GCA90'] - df2.iloc[0]['GCA90'], 2)
                st.metric('GCA per 90', df1.iloc[0]['GCA90'], diff)
            with row1_4:
                st.markdown("# ")
                diff1 = round(
                    df1.iloc[0]["GCA90"] - (self._dataset1["GCA90"].sum() + self._dataset5["GCA90"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row2_spacer1, row2_1, row2_2, row2_spacer2 = st.columns((.05, 5, 5, .05))
            with row2_1:
                dff1 = pd.melt(df1, id_vars='Player', value_vars=["PassLive_GCA", 'PassDead_GCA', 'TO_GCA', 'Sh_GCA',
                                                                  'Fld_GCA', 'Def_GCA'], var_name='GCA', value_name=
                               'Actions')
                dff1.replace(["PassLive_GCA", 'PassDead_GCA', 'TO_GCA', 'Sh_GCA', 'Fld_GCA', 'Def_GCA'],
                             ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions'],
                             inplace=True)
                fig = px.pie(dff1, values='Actions', names='GCA',
                             title='% of Different Goal Creating Actions Created by'
                                   ' Player in 2022/23 Season')
                fig.update_layout(margin=dict(t=30, b=20), height=350, title_font_size=14)
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                st.plotly_chart(fig, use_container_width=True)
            with row2_2:
                dff1 = pd.melt(df2, id_vars='Player', value_vars=["PassLive_GCA", 'PassDead_GCA', 'TO_GCA', 'Sh_GCA',
                                                                  'Fld_GCA', 'Def_GCA'], var_name='GCA', value_name=
                               'Actions')
                dff1.replace(["PassLive_GCA", 'PassDead_GCA', 'TO_GCA', 'Sh_GCA', 'Fld_GCA', 'Def_GCA'],
                             ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions'],
                             inplace=True)
                fig = px.pie(dff1, values='Actions', names='GCA',
                             title='% of Different Goal Creating Actions Created by'
                                   ' Player in 2021/22 Season')
                fig.update_layout(margin=dict(t=30, b=20), height=350, title_font_size=14)
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                st.plotly_chart(fig, use_container_width=True)

            row3_spacer1, row3_1, row3_spacer2, row3_2, row3_3, row3_spacer3 = st.columns((.1, 1.5, 1.3, 1, 1.7, .1))
            with row3_1:
                stat = ['Live Passes', 'Dead Passes', 'Take-Ons', 'Shots', 'Fouls Drawn', 'Defensive Actions']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row3_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")
            with row3_2:
                if see == 'Live Passes':
                    diff1 = round(df1.iloc[0]["PassLive_GCA"] - df2.iloc[0]["PassLive_GCA"], 2)
                    st.metric("Live Passes to Shot", df1.iloc[0]["PassLive_GCA"], diff1)
                elif see == 'Dead Passes':
                    diff1 = round(df1.iloc[0]["PassDead_GCA"] - df2.iloc[0]["PassDead_GCA"], 2)
                    st.metric("Dead Passes to Shot", df1.iloc[0]["PassDead_GCA"], diff1)
                elif see == 'Take-Ons':
                    diff1 = round(df1.iloc[0]["TO_GCA"] - df2.iloc[0]["TO_GCA"], 2)
                    st.metric("Take-Ons to Shot", df1.iloc[0]["TO_GCA"], diff1)
                elif see == 'Shots':
                    diff1 = round(df1.iloc[0]["Sh_GCA"] - df2.iloc[0]["Sh_GCA"], 2)
                    st.metric("Shots Leading to Shot", df1.iloc[0]["Sh_GCA"], diff1)
                elif see == 'Fouls Drawn':
                    diff1 = round(df1.iloc[0]["Fld_GCA"] - df2.iloc[0]["Fld_GCA"], 2)
                    st.metric("Fouls Drawn to Shot", df1.iloc[0]["Fld_GCA"], diff1)
                elif see == 'Defensive Actions':
                    diff1 = round(df1.iloc[0]["Def_GCA"] - df2.iloc[0]["Def_GCA"], 2)
                    st.metric("Defensive Actions to Shot", df1.iloc[0]["Def_GCA"], diff1)
            with row3_3:
                if see == 'Live Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PassLive_GCA"] - (
                            self._dataset1["PassLive_GCA"].sum() + self._dataset5["PassLive_GCA"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Dead Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PassDead_GCA"] - (
                            self._dataset1["PassDead_GCA"].sum() + self._dataset5["PassDead_GCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Take-Ons':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["TO_GCA"] - (self._dataset1["TO_GCA"].sum() + self._dataset5["TO_GCA"].sum()) / 26,
                        2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Fouls Drawn':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Fld_GCA"] - (
                            self._dataset1["Fld_GCA"].sum() + self._dataset5["Fld_GCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Shots':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Sh_GCA"] - (self._dataset1["Sh_GCA"].sum() + self._dataset5["Sh_GCA"].sum()) / 26,
                        2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Defensive Actions':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Def_GCA"] - (
                                self._dataset1["Def_GCA"].sum() + self._dataset5["Def_GCA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row4_spacer1, row4_1, row4_spacer2 = st.columns((.1, 3.2, .1))
            with row4_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == 'Live Passes':
                    dff1['LivePass_Rank'] = dff1['PassLive_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("LivePass_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PassLive_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Live Passes leading to Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Dead Passes":
                    dff1['DP_Rank'] = dff1['PassDead_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("DP_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PassDead_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Dead Passes leading to Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Take-Ons':
                    dff1['TO_Rank'] = dff1['TO_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("TO_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['TO_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Take-ons leading to Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Shots':
                    dff1['Sh_Rank'] = dff1['Sh_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("Sh_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Sh_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Shots leading to other Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Shots")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == "Fouls Drawn":
                    dff1['F_Rank'] = dff1['Fld_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("F_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Fld_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Fouls Drawn leading to Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Fouls Drawn")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Defensive Actions':
                    dff1['D_Rank'] = dff1['Def_GCA'].rank(ascending=False)
                    dff1 = dff1.sort_values("D_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Def_GCA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Defensive Actions leading to Goals Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Defensive Actions")
                    st.plotly_chart(fig, use_container_width=True)

        elif self._attribute == 'Defensive Actions 💪':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, 5))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")

            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_spacer2 = st.columns((.05, 1.3, 1.3, 1, 1.5, .05))
            with row1_1:
                df1 = df1.replace(str(self._name), str(self._name) + " 2022/23")
                df2 = df2.replace(str(self._name), str(self._name) + " 2021/22")
                nums = [100] * 6
                dff = pd.concat([df1, df2], ignore_index=True)
                dff = pd.melt(dff, id_vars='Player', value_vars=['Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls'],
                              var_name=
                              'Tackle Location', value_name='Tackles')
                dff = dff.replace(['Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls'], ['Defensive Third Tackles',
                                                                                     'Middle Third Tackles',
                                                                                     'Attacking Third Tackles'])
                dff['Height'] = nums
                img = Image.open("images/FootballField.png")
                fig = px.bar(dff, x='Player', y='Height', color='Tackle Location',
                             hover_data={'Height': False,
                                         'Tackles': True}, text='Tackles')
                fig.update_layout(height=590, title='Tackles on each 1/3 of the Field',
                                  showlegend=False, hoverlabel=dict(bgcolor='Black',
                                                                    font_size=15),
                                  margin=dict())
                fig.update_traces(width=1)
                fig.update_yaxes(visible=False)
                fig.add_layout_image(
                    dict(
                        source=img,
                        xref="x domain",
                        yref="y",
                        x=0,
                        y=300,
                        sizex=1,
                        sizey=300,
                        sizing='stretch',
                        layer='above',
                        opacity=0.3
                    ))
                fig.add_shape(
                    type='line', xref='x', yref='y', x0=.5, x1=.5, y0=0, y1=300, line_color='red'
                )
                st.plotly_chart(fig, use_container_width=True)
            with row1_2:
                dff = pd.DataFrame(columns=['Player', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls'])
                dff_avg1 = pd.concat([self._dataset1, self._dataset5]).reset_index(drop=True)
                dff_avg1.loc['Average 2022/23'] = round(dff_avg1.mean(), 2)
                dff_avg1 = dff_avg1.loc['Average 2022/23', ['Player', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls']]
                dff_avg1 = dff_avg1.fillna("Team Average 2022/23")

                dff_avg2 = self._dataset2.reset_index(drop=True)
                dff_avg2.loc['Average 2021/22'] = round(dff_avg2.mean(), 2)
                dff_avg2 = dff_avg2.loc['Average 2021/22', ['Player', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls']]
                dff_avg2 = dff_avg2.fillna("Team Average 2021/22")

                nums = [100] * 6
                dff = dff.append([dff_avg1, dff_avg2], ignore_index=True)
                dff = pd.melt(dff, id_vars='Player', value_vars=['Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls'],
                              var_name=
                              'Tackle Location', value_name='Tackles')
                dff = dff.replace(['Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls'], ['Defensive Third Tackles',
                                                                                     'Middle Third Tackles',
                                                                                     'Attacking Third Tackles'])
                dff['Height'] = nums
                img = Image.open("images/FootballField.png")
                fig = px.bar(dff, x='Player', y='Height', color='Tackle Location',
                             hover_data={'Height': False,
                                         'Tackles': True}, text='Tackles')
                fig.update_layout(height=590,
                                  showlegend=False, hoverlabel=dict(bgcolor='Black',
                                                                    font_size=15),
                                  margin=dict())
                fig.update_traces(width=1)
                fig.update_yaxes(visible=False)
                fig.add_layout_image(
                    dict(
                        source=img,
                        xref="x domain",
                        yref="y",
                        x=0,
                        y=300,
                        sizex=1,
                        sizey=300,
                        sizing='stretch',
                        layer='above',
                        opacity=0.3
                    ))
                fig.add_shape(
                    type='line', xref='x', yref='y', x0=.5, x1=.5, y0=0, y1=300, line_color='red'
                )
                st.plotly_chart(fig, use_container_width=True)
            with row1_3:
                diff = df1.iloc[0]['Tkl'] - df2.iloc[0]['Tkl']
                st.metric('Total Tackles', df1.iloc[0]['Tkl'], diff)
                diff = df1.iloc[0]['TklW'] - df2.iloc[0]['TklW']
                st.metric('Total Tackles Won', df1.iloc[0]['TklW'], diff)
                diff = round(df1.iloc[0]['Int'] - df2.iloc[0]['Int'], 2)
                st.metric('Interceptions', str(df1.iloc[0]['Int']), str(diff))
                diff = round(df1.iloc[0]['Clr'] - df2.iloc[0]['Clr'], 2)
                st.metric('Clearances', str(df1.iloc[0]['Clr']), str(diff))
                diff = round(df1.iloc[0]['Err'] - df2.iloc[0]['Err'], 2)
                st.metric('Errors', str(df1.iloc[0]['Err']), str(diff))
            with row1_4:
                dff = pd.concat([self._dataset1, self._dataset5], ignore_index=True)
                dff['Tkl_Rank'] = dff['Tkl'].rank(ascending=False, method='max')
                dff['TklW_Rank'] = dff['TklW'].rank(ascending=False, method='max')
                dff['Int_Rank'] = dff['Int'].rank(ascending=False, method='max')
                dff['Clr_Rank'] = dff['Clr'].rank(ascending=False, method='max')
                dff['Err_Rank'] = dff['Err'].rank(ascending=False, method='max')
                st.markdown("# ")
                st.markdown("##### Rank " + str(
                    dff[dff['Player'] == self._name]['Tkl_Rank'].item()) + " in the team this season.")
                st.markdown("# ")
                st.markdown("## ")
                st.markdown("##### Rank " + str(
                    dff[dff['Player'] == self._name]['TklW_Rank'].item()) + " in the team this season.")
                st.markdown("# ")
                st.markdown("## ")
                st.markdown("##### Rank " + str(
                    dff[dff['Player'] == self._name]['Int_Rank'].item()) + " in the team this season.")
                st.markdown("# ")
                st.markdown("## ")
                st.markdown("##### Rank " + str(
                    dff[dff['Player'] == self._name]['Clr_Rank'].item()) + " in the team this season.")
                st.markdown("# ")
                st.markdown("## ")
                st.markdown("##### Rank " + str(
                    dff[dff['Player'] == self._name]['Err_Rank'].item()) + " in the team this season.")

            row2_spacer1, row2_1, row2_2, row2_spacer2 = st.columns((.05, 3, 3, .05))
            with row2_1:
                dff1 = pd.melt(df1, id_vars='Player', value_vars=['Tkl_Chl', 'Lost'], var_name='Challenges Won/Lost',
                               value_name='Tackles')
                dff1 = dff1.replace([str(self._name), 'Tkl_Chl'], [str(self._name) + " 2022/23", 'Won'])
                fig1 = px.pie(dff1, values='Tackles', names='Challenges Won/Lost',
                              color_discrete_sequence=px.colors.sequential.RdBu,
                              title='Challenges Win-Lost % in 2022/23 Season')
                fig1.update_layout(margin=dict(t=30, b=20), height=350)
                fig1.update_traces(textposition='inside', textinfo='percent+label+value')

                dff2 = pd.melt(df2, id_vars='Player', value_vars=['Tkl_Chl', 'Lost'], var_name='Challenges Won/Lost',
                               value_name='Tackles')
                dff2 = dff2.replace([str(self._name), 'Tkl_Chl'], [str(self._name) + " 2021/22", 'Won'])
                fig2 = px.pie(dff2, values='Tackles', names='Challenges Won/Lost',
                              color_discrete_sequence=px.colors.sequential.RdBu,
                              title='Challenges Win-Lost % in 2021/22 Season')
                fig2.update_layout(margin=dict(t=30, b=20), height=350)
                fig2.update_traces(textposition='inside', textinfo='percent+label+value')

                st.plotly_chart(fig1, use_container_width=True)
                st.plotly_chart(fig2, use_container_width=True)
            with row2_2:
                dff1 = pd.melt(df1, id_vars='Player', value_vars=['Blocks_Sh', 'Pass'], var_name='Ball Movement Type',
                               value_name='Blocks')
                dff1 = dff1.replace([str(self._name), 'Blocks_Sh', 'Pass'],
                                    [str(self._name) + " 2022/23", 'Shots blocked',
                                     'Passes Blocked'])
                fig1 = px.pie(dff1, values='Blocks', names='Ball Movement Type',
                              color_discrete_sequence=px.colors.sequential.RdBu,
                              title='Ball Movement Blocked by Player in 2022/23 Season')
                fig1.update_layout(margin=dict(t=30, b=20), height=350)
                fig1.update_traces(textposition='inside', textinfo='percent+label+value')

                dff2 = pd.melt(df2, id_vars='Player', value_vars=['Blocks_Sh', 'Pass'], var_name='Ball Movement Type',
                               value_name='Blocks')
                dff2 = dff2.replace([str(self._name), 'Blocks_Sh', 'Pass'],
                                    [str(self._name) + " 2021/22", 'Shots blocked',
                                     'Passes Blocked'])
                fig2 = px.pie(dff2, values='Blocks', names='Ball Movement Type',
                              color_discrete_sequence=px.colors.sequential.RdBu,
                              title='Ball Movement Blocked by Player in 2021/22 Season')
                fig2.update_layout(margin=dict(t=30, b=20), height=350)
                fig2.update_traces(textposition='inside', textinfo='percent+label+value')

                st.plotly_chart(fig1, use_container_width=True)
                st.plotly_chart(fig2, use_container_width=True)

        elif self._attribute == 'Possession 👻':
            row0_spacer1, row0_1, row0_spacer2 = st.columns((.05, 3.2, .05))
            with row0_1:
                st.markdown("##### Actual Statistics - :green[↑]/:red[↓] from previous season")
                st.markdown("#### Touches")

            row1_spacer1, row1_1, row1_2, row1_3, row1_4, row1_spacer2 = st.columns((.1, 1, 2, 1, 2, .05))
            with row1_1:
                diff = round(df1.iloc[0]['Touches'] - df2.iloc[0]['Touches'], 2)
                st.metric('Total Touches', df1.iloc[0]['Touches'], diff)
            with row1_2:
                st.markdown("# ")
                diff1 = round(
                    df1.iloc[0]["Touches"] - (self._dataset1["Touches"].sum() + self._dataset5["Touches"].sum()) / 26,
                    2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
            with row1_3:
                diff = round(df1.iloc[0]['Live_Tch'] - df2.iloc[0]['Live_Tch'], 2)
                st.metric('Total Live Touches', df1.iloc[0]['Live_Tch'], diff)
            with row1_4:
                st.markdown("# ")
                diff1 = round(
                    df1.iloc[0]["Live_Tch"] - (
                            self._dataset1["Live_Tch"].sum() + self._dataset5["Live_Tch"].sum()) / 26,
                    2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average this season.")
                else:
                    st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row2_spacer1, row2_1, row2_2, row2_3, row2_spacer2 = st.columns((.05, 2.45, 6, 2.45, .05))
            with row2_1:
                diff = round(df1.iloc[0]["Att Pen"] - (
                        self._dataset1["Att Pen"].sum() + self._dataset5["Att Pen"].sum()) / 26, 2)
                st.markdown("## ")
                st.markdown("## ")
                st.markdown("###### Attacking Penalty Box Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("## ")
                diff = round(df1.iloc[0]["Att 3rd_Tch"] - (
                        self._dataset1["Att 3rd_Tch"].sum() + self._dataset5["Att 3rd_Tch"].sum()) / 26, 2)
                st.markdown("###### Attacking Third Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("# ")
                st.markdown("###### ")
                diff = round(df1.iloc[0]["Mid 3rd_Tch"] - (
                        self._dataset1["Mid 3rd_Tch"].sum() + self._dataset5["Mid 3rd_Tch"].sum()) / 26, 2)
                st.markdown("###### Middle Third Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("## ")
                st.markdown("### ")
                diff = round(df1.iloc[0]["Def 3rd_Tch"] - (
                        self._dataset1["Def 3rd_Tch"].sum() + self._dataset5["Def 3rd_Tch"].sum()) / 26, 2)
                st.markdown("###### Defensive Third Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("# ")
                diff = round(df1.iloc[0]["Def Pen"] - (
                        self._dataset1["Def Pen"].sum() + self._dataset5["Def Pen"].sum()) / 26, 2)
                st.markdown("###### Defensive Penalty Box Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
            with row2_2:
                df1 = df1.replace(str(self._name), str(self._name) + " 2022/23")
                df2 = df2.replace(str(self._name), str(self._name) + " 2021/22")

                x = [2, 3, 1, 4, 1, 4, 1, 4, 2, 3]
                y = [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]

                dff = pd.concat([df1, df2], ignore_index=True)
                dff = pd.melt(dff, id_vars='Player', value_vars=['Def Pen', 'Def 3rd_Tch', 'Mid 3rd_Tch', 'Att 3rd_Tch',
                                                                 'Att Pen'], value_name='Touches', var_name='Areas')
                dff['x'] = x
                dff['Area'] = y

                dff.replace(['Def Pen', 'Def 3rd_Tch', 'Mid 3rd_Tch', 'Att 3rd_Tch', 'Att Pen'],
                            ['Defensive Penalty Box', 'Defensive Third', 'Middle Third', 'Attacking Third',
                             'Attacking Penalty Box'], inplace=True)

                img = Image.open("images/FootballField.png")
                fig = px.scatter(dff, x='x', y='Area', size='Touches', color='Areas', hover_name='Player',
                                 hover_data={'x': False, 'Area': False, 'Player': False, 'Touches': True},
                                 title='Touches by Player in Different Parts of the Field in the '
                                       '2022/23 and 2021/22 Season',
                                 color_discrete_sequence=px.colors.sequential.RdBu,
                                 size_max=30)
                fig.update_layout(height=750, margin=dict(t=50, b=0), title_font_size=14, legend=dict(
                    yanchor="bottom",
                    y=.815,
                    xanchor="right",
                    x=1,
                    bgcolor="Green",
                    bordercolor="White",
                    borderwidth=2
                ))
                fig.update_xaxes(range=[0, 5], visible=False)
                fig.update_yaxes(range=[0, 10], visible=True, showticklabels=False)
                fig.update_traces(mode='markers', marker=dict(sizemode='area',
                                                              line_width=2))
                fig.add_layout_image(
                    dict(
                        source=img,
                        xref="x",
                        yref="y",
                        x=0,
                        y=10,
                        sizex=5,
                        sizey=10,
                        sizing='stretch',
                        layer='below',
                        opacity=.8
                    ))
                st.plotly_chart(fig, use_container_width=True)
            with row2_3:
                diff = round(df2.iloc[0]["Att Pen"] - (
                    self._dataset2["Att Pen"].mean()), 2)
                st.markdown("## ")
                st.markdown("## ")
                st.markdown("###### Attacking Penalty Box Touches in 2021/22 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("## ")
                diff = round(df2.iloc[0]["Att 3rd_Tch"] - (
                    self._dataset2["Att 3rd_Tch"].mean()), 2)
                st.markdown("###### Attacking Third Touches in 2021/22 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("# ")
                st.markdown("###### ")
                diff = round(df2.iloc[0]["Mid 3rd_Tch"] - (
                    self._dataset2["Mid 3rd_Tch"].mean()), 2)
                st.markdown("###### Middle Third Touches in 2021/22 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("## ")
                st.markdown("### ")
                diff = round(df1.iloc[0]["Def 3rd_Tch"] - (
                    self._dataset2["Def 3rd_Tch"].mean()), 2)
                st.markdown("###### Defensive Third Touches in 2022/23 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)
                st.markdown("# ")
                diff = round(df1.iloc[0]["Def Pen"] - (
                    self._dataset2["Def Pen"].mean()), 2)
                st.markdown("###### Defensive Penalty Box Touches in 2021/22 Season")
                if diff > 0:
                    st.markdown("###### :green[↑ %a] more than team average this season." % diff)
                elif diff == 0:
                    st.markdown("###### Similar to team average this season.")
                else:
                    st.markdown("###### :red[↓ %a] less than team average this season." % diff)

            row3_spacer1, row3_1, row3_spacer2 = st.columns((.05, 3.2, .05))
            with row3_1:
                st.markdown("#### Take-Ons")

            row4_spacer1, row4_1, row4_2, row4_3, row4_spacer2 = st.columns((.05, 4, 1, 4, .05))
            with row4_1:
                dff = df1
                dff['Unsucc'] = dff.iloc[0]['Att_TakeOns'] - dff.iloc[0]['Succ']
                dff = pd.melt(dff, id_vars='Player', value_vars=['Succ', 'Unsucc'], var_name='Take-Ons',
                              value_name='Win / Loss')
                dff.replace(['Succ', 'Unsucc'], ['Successful Take-Ons', 'Unsuccessful Take-Ons'], inplace=True)

                fig = px.pie(dff, values='Win / Loss', names='Take-Ons',
                             color_discrete_sequence=px.colors.sequential.RdBu,
                             title='Take-Ons Win-Loss % in the 2022/23 Season')
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                fig.update_layout(margin=dict(t=40, b=20), legend=dict(xanchor="right", x=0))
                st.plotly_chart(fig, use_container_width=True)
            with row4_2:
                st.metric("Total Take-Ons", df1.iloc[0]['Att_TakeOns'])
            with row4_3:
                dff = df1
                dff['Tkld_U'] = dff.iloc[0]['Att_TakeOns'] - dff.iloc[0]['Tkld']
                dff = pd.melt(dff, id_vars='Player', value_vars=['Tkld', 'Tkld_U'], var_name='Take-Ons',
                              value_name='Win / Loss')
                dff.replace(['Tkld', 'Tkld_U'], ['Tackled During Take-Ons', 'Untackled Take-Ons'], inplace=True)

                fig = px.pie(dff, values='Win / Loss', names='Take-Ons',
                             color_discrete_sequence=px.colors.sequential.RdBu,
                             title='Tackled During Take-Ons % in the 2022/23 Season')
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                fig.update_layout(margin=dict(t=40, b=20))
                st.plotly_chart(fig, use_container_width=True)

            row5_spacer1, row5_1, row5_2, row5_3, row5_spacer2 = st.columns((.05, 4, 1, 4, .05))
            with row5_1:
                dff = df2
                dff['Unsucc'] = dff.iloc[0]['Att_TakeOns'] - dff.iloc[0]['Succ']
                dff = pd.melt(dff, id_vars='Player', value_vars=['Succ', 'Unsucc'], var_name='Take-Ons',
                              value_name='Win / Loss')
                dff.replace(['Succ', 'Unsucc'], ['Successful Take-Ons', 'Unsuccessful Take-Ons'], inplace=True)

                fig = px.pie(dff, values='Win / Loss', names='Take-Ons',
                             color_discrete_sequence=px.colors.sequential.RdBu,
                             title='Take-Ons Win-Loss % in the 2021/22 Season')
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                fig.update_layout(margin=dict(t=40, b=20), legend=dict(xanchor="right", x=0))
                st.plotly_chart(fig, use_container_width=True)
            with row5_2:
                st.metric("Total Take-Ons", df2.iloc[0]['Att_TakeOns'])
            with row5_3:
                dff = df2
                dff['Tkld_U'] = dff.iloc[0]['Att_TakeOns'] - dff.iloc[0]['Tkld']
                dff = pd.melt(dff, id_vars='Player', value_vars=['Tkld', 'Tkld_U'], var_name='Take-Ons',
                              value_name='Win / Loss')
                dff.replace(['Tkld', 'Tkld_U'], ['Tackled During Take-Ons', 'Untackled Take-Ons'], inplace=True)

                fig = px.pie(dff, values='Win / Loss', names='Take-Ons',
                             color_discrete_sequence=px.colors.sequential.RdBu,
                             title='Tackled During Take-Ons % in the 2021/22 Season')
                fig.update_traces(textposition='inside', textinfo='percent+label+value')
                fig.update_layout(margin=dict(t=40, b=20))
                st.plotly_chart(fig, use_container_width=True)

            row6_spacer1, row6_1, row6_spacer2 = st.columns((.05, 3.2, .05))
            with row6_1:
                st.markdown("#### Carries & Receiving Passes")

            row7_spacer1, row7_1, row7_spacer2, row7_2, row7_3, row7_spacer3 = st.columns((.1, 1.5, 1.3, 1.2, 1.7, .1))
            with row7_1:
                stat = ['Total Carries', 'Total Distance Carried', 'Total Progressive Distance Carried', 'Total '
                                                                                                         'Progressive Carries',
                        'Carries into the Final Third', 'Carries into Attacking Penalty Area',
                        'Miscontrols', 'Dispossessed', 'Passes Received', 'Progressive Passes Received']
                see = st.selectbox("Select the stat that you want to see! 👋", stat)
            with row7_spacer2:
                st.metric("Example Stat", "Value", "↑/↓ from prev season")
            with row7_2:
                if see == 'Total Carries':
                    diff1 = round(df1.iloc[0]["Carries"] - df2.iloc[0]["Carries"], 2)
                    st.metric("Total Carries", df1.iloc[0]["Carries"], diff1)
                elif see == 'Total Distance Carried':
                    diff1 = round(df1.iloc[0]["TotDist_Carr"] - df2.iloc[0]["TotDist_Carr"], 2)
                    st.metric("Total Distance Carried", str(df1.iloc[0]["TotDist_Carr"]) + " yrds",
                              str(diff1) + " yrds")
                elif see == 'Total Progressive Distance Carried':
                    diff1 = round(df1.iloc[0]["PrgDist_Carr"] - df2.iloc[0]["PrgDist_Carr"], 2)
                    st.metric("Total Prog Distance Carried", str(df1.iloc[0]["PrgDist_Carr"]) + " yrds",
                              str(diff1) + " yrds")
                elif see == 'Total Progressive Carries':
                    diff1 = round(df1.iloc[0]["PrgC"] - df2.iloc[0]["PrgC"], 2)
                    st.metric("Total Progressive Carries", df1.iloc[0]["PrgC"], diff1)
                elif see == 'Carries into the Final Third':
                    diff1 = round(df1.iloc[0]["1/3_Carr"] - df2.iloc[0]["1/3_Carr"], 2)
                    st.metric("Carries into Final 1/3", df1.iloc[0]["1/3_Carr"], diff1)
                elif see == 'Carries into Attacking Penalty Area':
                    diff1 = round(df1.iloc[0]["CPA"] - df2.iloc[0]["CPA"], 2)
                    st.metric("Carries into Attacking Pen.", df1.iloc[0]["CPA"], diff1)
                elif see == 'Miscontrols':
                    diff1 = round(df1.iloc[0]["Mis"] - df2.iloc[0]["Mis"], 2)
                    st.metric("Miscontrols", df1.iloc[0]["Mis"], diff1)
                elif see == 'Dispossessed':
                    diff1 = round(df1.iloc[0]["Dis"] - df2.iloc[0]["Dis"], 2)
                    st.metric("Dispossessed", df1.iloc[0]["Dis"], diff1)
                elif see == 'Passes Received':
                    diff1 = round(df1.iloc[0]["Rec"] - df2.iloc[0]["Rec"], 2)
                    st.metric("Passes Received", df1.iloc[0]["Rec"], diff1)
                elif see == 'Progressive Passes Received':
                    diff1 = round(df1.iloc[0]["PrgR"] - df2.iloc[0]["PrgR"], 2)
                    st.metric("Prog. Passes Received", df1.iloc[0]["PrgR"], diff1)
            with row7_3:
                if see == 'Total Carries':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Carries"] - (
                                self._dataset1["Carries"].sum() + self._dataset5["Carries"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Total Distance Carried':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["TotDist_Carr"] - (
                                self._dataset1["TotDist_Carr"].sum() + self._dataset5["TotDist_Carr"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] yards more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] yards less than team average this season." % diff1)
                elif see == 'Total Progressive Distance Carried':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PrgDist_Carr"] - (
                                self._dataset1["PrgDist_Carr"].sum() + self._dataset5["PrgDist_Carr"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] yards more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] yards less than team average this season." % diff1)
                elif see == 'Total Progressive Carries':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["PrgC"] - (self._dataset1["PrgC"].sum() + self._dataset5["PrgC"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Carries into the Final Third':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["1/3_Carr"] - (
                                self._dataset1["1/3_Carr"].sum() + self._dataset5["1/3_Carr"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Carries into Attacking Penalty Area':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["CPA"] - (self._dataset1["CPA"].sum() + self._dataset5["CPA"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Miscontrols':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Mis"] - (self._dataset1["Mis"].sum() + self._dataset5["Mis"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Dispossessed':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Dis"] - (self._dataset1["Dis"].sum() + self._dataset5["Dis"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Passes Received':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Rec"] - (self._dataset1["Rec"].sum() + self._dataset5["Rec"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)
                elif see == 'Progressive Passes Received':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["PrgR"] - (self._dataset1["PrgR"].sum() + self._dataset5["PrgR"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average this season." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average this season.")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average this season." % diff1)

            row8_spacer1, row8_1, row8_spacer2 = st.columns((.1, 3.2, .1))
            with row8_1:
                dff1 = self._dataset1
                dff1 = pd.concat([dff1, self._dataset5]).reset_index(drop=True)
                if see == 'Total Carries':
                    dff1['Carr_Rank'] = dff1['Carries'].rank(ascending=False)
                    dff1 = dff1.sort_values("Carr_Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Carries'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Total Carries Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Carries")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Total Distance Carried':
                    dff1['Rank'] = dff1['TotDist_Carr'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['TotDist_Carr'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Total Distance Carries Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Yards")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Total Progressive Distance Carried':
                    dff1['Rank'] = dff1['PrgDist_Carr'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PrgDist_Carr'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Total Progressive Distance Carries Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Yards")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Total Progressive Carries':
                    dff1['Rank'] = dff1['PrgC'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PrgC'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Total Distance Carries Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Progressive Carries")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Carries into the Final Third':
                    dff1['Rank'] = dff1['1/3_Carr'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['1/3_Carr'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Carries into the Final Third Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Carries")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Carries into Attacking Penalty Area':
                    dff1['Rank'] = dff1['CPA'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['CPA'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Carries into Attacking Penalty Area Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Carries")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Miscontrols':
                    dff1['Rank'] = dff1['Mis'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Mis'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Miscontrols Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Miscontrols")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Dispossessed':
                    dff1['Rank'] = dff1['Dis'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Dis'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Dispossession Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Dispossessed")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Passes Received':
                    dff1['Rank'] = dff1['Rec'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['Rec'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Passes Received Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes Received")
                    st.plotly_chart(fig, use_container_width=True)
                elif see == 'Progressive Passes Received':
                    dff1['Rank'] = dff1['PrgR'].rank(ascending=False)
                    dff1 = dff1.sort_values("Rank")
                    dff1 = dff1.reset_index(drop=True)
                    index = dff1[dff1['Player'] == self._name].index.values[0]
                    colours = ['lightslategrey', ] * 26
                    colours[index] = '#DA291C'
                    x = dff1['Player'].values.tolist()
                    y = dff1['PrgR'].values.tolist()
                    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colours)])
                    fig.update_layout(title_text='Progressive Passes Received Ranking', title_font_size=30)
                    fig.update_xaxes(title_text="Player")
                    fig.update_yaxes(title_text="Passes Received")
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown("# WORK IN PROGRESS")
    # def data_visuals_gk(self, df1, df2):
