import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


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
            df['Dribbling'] = (df.at[0,'Succ%'] + df.at[0,'Tkld%']) / 200
            df.at[0, 'Tkl%'] = df.at[0,'Tkl%'] / 100
            df.at[0, 'Succ%'] = df.at[0, 'Succ%'] / 100
            df.at[0, 'Cmp%'] = df.at[0, 'Cmp%'] / 100
            dff = pd.melt(df, id_vars = 'Player', value_vars=['SoT%', 'Cmp%' , 'Dribbling', 'Tkl%', 'Succ%'],
                          var_name='Attributes', value_name='Rating')
            dff.replace(['SoT%', 'Cmp%', 'Tkl%', 'Succ%'], ['Shooting', 'Passing', 'Defending', 'Possession'], inplace=True)
            fig = px.line_polar(dff, r='Rating', theta='Attributes', line_close=True, height=221, width = 400,
                                color_discrete_sequence=['orange'])
            fig.update_traces(fill='toself')
            fig.update_layout(margin=dict(t=20,b=0), font_size = 11, plot_bgcolor='#0e1117')
            st.plotly_chart(fig, use_container_width=True, theme='streamlit')
            st.markdown("")

    def filter_data(self):
        ### Defining what data is in what attribute
        att = {'Shooting 👟': ['Player', 'Gls', 'Sh', 'SoT%', 'SoT/90', 'G/Sh', 'Dist', 'PK', 'xG', 'npxG',
                              'npxG/Sh', 'G-xG', 'np:G-xG'],
               'Passing ⚽': ['Player', 'Att', 'Cmp%', 'TotDist_Pass', 'PrgDist_Pass', 'Att_Shrt', 'Cmp%_Shrt',
                             'Att_Med', 'Cmp%_Med', 'Att_Long', 'Cmp%_Long', 'Ast', 'xAG', 'xA', 'KP', '1/3_Pass',
                             'PPA',
                             'CrsPA', 'PrgP'],
               'Pass Types 🛒': ['Player', 'Att', 'Cmp', 'Cmp%','Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs', 'TI',
                                'CK', 'In', 'Out', 'Str', 'Off', 'Blocks'],
               'Shot-Creating Actions 😎': ['Player', 'SCA', 'SCA90', 'PassLive_SCA', 'PassDead_SCA', 'TO_SCA', 'Sh_SCA',
                                           'Fld_SCA', 'Def_SCA'],
               'Goal-Creating Actions 🫡': ['Player', 'GCA', 'GCA90', 'PassLive_GCA', 'PassDead_GCA', 'TO_GCA', 'Sh_GCA',
                                           'Fld_GCA', 'Def_GCA'],
               'Defensive Actions 💪': ['Player', 'Tkl', 'TklW', 'Def 3rd_Tkls', 'Mid 3rd_Tkls', 'Att 3rd_Tkls',
                                       'Att_Chl', 'Tkl%', 'Lost', 'Blocks_Def', 'Blocks_Sh', 'Pass', 'Int', 'Clr',
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
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == "Shots":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["Sh"] - (self._dataset1["Sh"].sum() + self._dataset5["Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == "Shots on Target%":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["SoT%"] - self._dataset1["SoT%"].mean(), 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more accurate than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less accurate than team average." % diff1)
                elif see == "Shots on Target per 90":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["SoT/90"] - (self._dataset1["SoT/90"].sum() +
                                                           self._dataset5["SoT/90"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more accurate than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less accurate than team average." % diff1)
                elif see == "Goals per Shot":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["G/Sh"] - (self._dataset1["G/Sh"].sum() + self._dataset5["G/Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == "Average Shot Distance":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["Dist"] - (self._dataset1["Dist"].sum() + self._dataset5["Dist"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == "Penalty Kick Goals":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PK"] - (self._dataset1["PK"].sum() + self._dataset5["PK"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
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
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Non-Penalty Expected Goals':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["npxG"] - (self._dataset1["npxG"].sum() + self._dataset5["npxG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == "Non-Penalty Expected Goals per Shot":
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["npxG/Sh"] - (
                                self._dataset1["npxG/Sh"].sum() + self._dataset5["npxG/Sh"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more expected accuracy than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less expected accuracy than team average." % diff1)
                elif see == "Goals minus Expected Goals":
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["G-xG"] - (self._dataset1["G-xG"].sum() + self._dataset5["G-xG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Non-Penalty Expected Goals minus Expected Goals':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["np:G-xG"] - (
                                self._dataset1["np:G-xG"].sum() + self._dataset5["np:G-xG"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)

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
                    st.markdown("##### :green[↑ %a] more than team average." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average")
                else:
                    st.markdown("##### :red[↓ %a] less than team average." % diff1)
                st.markdown("## ")
                st.markdown("### ")
                diff1 = round(df1.iloc[0]["Att"] - (self._dataset1["Att"].sum() + self._dataset5["Att"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] more than team average." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average")
                else:
                    st.markdown("##### :red[↓ %a] less than team average." % diff1)
                st.markdown("### ")
                st.markdown("### ")
                diff1 = round(df1.iloc[0]["TotDist_Pass"] - (
                            self._dataset1["TotDist_Pass"].sum() + self._dataset5["TotDist_Pass"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] yards further than team average." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average")
                else:
                    st.markdown("##### :red[↓ %a] yards nearer than team average." % diff1)
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
                    st.markdown("##### :green[↑ %a] more than team average." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average")
                else:
                    st.markdown("##### :red[↓ %a] less than team average." % diff1)
                st.markdown("# ")
                st.markdown("##### ")
                diff1 = round(df1.iloc[0]["PrgDist_Pass"] - (
                            self._dataset1["PrgDist_Pass"].sum() + self._dataset5["PrgDist_Pass"].sum()) / 26, 2)
                if diff1 > 0:
                    st.markdown("##### :green[↑ %a] yards further than team average." % diff1)
                elif diff1 == 0:
                    st.markdown("##### Similar to team average")
                else:
                    st.markdown("##### :red[↓ %a] yards nearer than team average." % diff1)

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
                fig.update_layout(barmode='group', legend=dict(
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
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Expected Assists':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["xA"] - (self._dataset1["xA"].sum() + self._dataset5["xA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Key Passes':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["KP"] - (self._dataset1["KP"].sum() + self._dataset5["KP"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Passes into Final Third':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["1/3_Pass"] - (
                                self._dataset1["1/3_Pass"].sum() + self._dataset5["1/3_Pass"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Passes into Penalty Area':
                    st.markdown("## ")
                    diff1 = round(df1.iloc[0]["PPA"] - (self._dataset1["PPA"].sum() + self._dataset5["PPA"].sum()) / 26,
                                  2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Crosses into Penalty Area':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["CrsPA"] - (self._dataset1["CrsPA"].sum() + self._dataset5["CrsPA"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)
                elif see == 'Progressive Passes':
                    st.markdown("## ")
                    diff1 = round(
                        df1.iloc[0]["PrgP"] - (self._dataset1["PrgP"].sum() + self._dataset5["PrgP"].sum()) / 26, 2)
                    if diff1 > 0:
                        st.markdown("##### :green[↑ %a] more than team average." % diff1)
                    elif diff1 == 0:
                        st.markdown("##### Similar to team average")
                    else:
                        st.markdown("##### :red[↓ %a] less than team average." % diff1)

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

            row1_spacer1, row1_1, row1_2, row1_3, row1_spacer2 = st.columns((.05,2,2,5,2))
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

            row2_spacer1, row2_1, row2_spacer2 = st.columns((.1,3.2,.01))
            with row2_1:
                dff1 = df1
                dff1.replace(str(self._name), str(self._name) + " 2022/23", inplace=True)
                dff2 = df2
                dff2.replace(str(self._name), str(self._name) + " 2021/22", inplace=True)
                dff = pd.concat([dff1, dff2], ignore_index=True)

                dff = pd.melt(dff, id_vars=['Player'], value_vars=['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs',
                        'TI','CK'], var_name='Statistic', value_name ='Amount of Passes')
                dff.replace(['Live_Pass', 'Dead', 'FK_Pass', 'TB', 'Sw', 'Crs','TI','CK'],
                            ['Live Pass', 'Dead Pass', 'Freekick Pass', 'Through Balls', 'Switches', 'Crosses',
                             'Throw Ins', 'Corner Kicks'], inplace=True)

                fig = px.bar(dff, x='Statistic', y='Amount of Passes', color='Player')
                fig.update_layout(barmode='group', title='Pass Types')
                st.plotly_chart(fig, use_container_width=True)

            row3_spacer1, row3_1, row3_2, row3_3, row3_spacer2 = st.columns((.1,4,2,2,.1))
            with row3_1:
                dff1 = df1
                dff1['Others'] = dff1['CK'] - dff1['In'] - dff1['Out'] - dff1['Str']
                dff1 = pd.melt(dff1, id_vars='Player', value_vars=['CK', 'In', 'Out', 'Str', 'Others'], var_name='Statistic',
                               value_name='Amount of Passes')

                dff2 = df2
                dff2['Others'] = dff2['CK'] - dff2['In'] - dff2['Out'] - dff2['Str']
                dff2 = pd.melt(dff2, id_vars='Player', value_vars=['CK', 'In', 'Out', 'Str', 'Others'],
                               var_name='Statistic', value_name='Amount of Passes')

                dff = pd.concat([dff1, dff2], ignore_index=True)
                dff.replace(['CK', 'In', 'Out', 'Str'],['Corner Kicks', 'In-Swing Corner', 'Out-Swing Corner',
                                                        'Straight'], inplace=True)
                fig = px.bar(dff, x='Statistic', y='Amount of Passes', color='Player')
                fig.update_layout(legend=dict(orientation = 'h', yanchor="top", y=1.05, xanchor="right", x=1), barmode=
                                  'group', title='Corner Kick Statistics')
                st.plotly_chart(fig, use_container_width=True)

            with row3_2:
                diff1 = round(df1.iloc[0]['Off']-df2.iloc[0]['Off'],2)
                st.markdown("### Pass Outcomes")
                st.metric('Offside Passes', df1.iloc[0]['Off'], diff1)
            with row3_3:
                diff1 = round(df1.iloc[0]['Blocks'] - df2.iloc[0]['Blocks'], 2)
                st.markdown("## ")
                st.markdown("#### ")
                st.metric('Blocked Passes', df1.iloc[0]['Blocks'], diff1)

        elif self._attribute == 'Shot-Creating Actions 😎':
            st.markdown("")
        else:
            st.markdown("# WORK IN PROGRESS")
    # def data_visuals_gk(self, df1, df2):


