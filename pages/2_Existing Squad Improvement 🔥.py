# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import functions1 as f1
import metric as mg

st.set_page_config(layout="wide")
dataset1 = pd.read_csv('data/data_2022_2023.csv', index_col='Unnamed: 0')
dataset2 = pd.read_csv('data/data_2021_2022.csv', index_col='Unnamed: 0')
dataset3 = pd.read_csv('data/df_2022_2023_gk.csv', index_col='Unnamed: 0')
dataset4 = pd.read_csv('data/df_2021_2022_gk.csv', index_col='Unnamed: 0')
dataset5 = pd.read_csv('data/df_2022_2023_new_signings.csv', index_col='Unnamed: 0')

### Sidebar customisation and input values
st.sidebar.markdown("#  How does this work?")
st.sidebar.markdown("First, select the player you want to analyse. Then select the attribute like Shooting or"
                    " Possession that you want to analyse about the player. The website will then generate helpful "
                    "visuals that analyses our raw data.")
st.sidebar.markdown("# Player Select")
name_list = dataset1["Player"].tolist()
player = st.sidebar.selectbox('Select the player that you want to analyse', name_list)
att_list = ['Shooting 👟', 'Passing ⚽', 'Pass Types 🛒', 'Shot-Creating Actions 😎', 'Goal-Creating Actions 🫡',
            'Defensive Actions 💪', 'Possession 👻', 'Team Success with & without 🎇', 'Advanced Goalkeeping 🥅',
            'Miscellaneous 🏆']
attribute = st.sidebar.selectbox('Select the attribute that you want to analyse', att_list)
drop_gloss = st.sidebar.expander("Metric Glossary")
with drop_gloss:
    m = mg.metric(attribute)
    m.metric_glossary()

x = f1.dataFunc1(player, attribute, dataset1, dataset2, dataset3, dataset4, dataset5)

row0_spacer1, row0_1, row0_2, row0_spacer2 = st.columns((.1, 1, 5, .1))
with row0_1:
    st.image('images/Logo.png')
with row0_2:
    st.title("Existing Squad Improvements 🔥")

row3_spacer1, row3_1, row3_spacer2 = st.columns((.05, 3.2, .05))
with row3_1:
    st.markdown("This page analyses the statistics of the current players who were also part of the Manchester "
                "United squad in the 2021/22 season. This page will compare statistics of the player of your choice "
                "from this season against the "
                "statistics from the previous season. In some instances, some statistics "
                "will be compared against team averages from the current 2022/23 season.")

row1_spacer1, row1_1, row1_spacer2 = st.columns((.05, 3.2, .05))
with row1_1:
    st.markdown("### Basic Information")

x.display()

row2_spacer1, row2_1, row2_spacer2 = st.columns((.05, 3.2, .05))
with row2_1:
    st.markdown("### Analysis")

df1, df2 = x.filter_data()

if attribute == "Advanced Goalkeeping 🥅":
    if player == "David de Gea":
        x.data_visuals_gk(df1,df2)
    else:
        st.header("NO DATA FOR PLAYER")
elif attribute == 'Shooting 👟' or 'Goal-Creating Actions 🫡':
    if player == "David de Gea":
        st.header("NO DATA FOR PLAYER")
    else:
        x.data_visuals(df1,df2)
else:
    x.data_visuals(df1,df2)
