# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import functions1 as f1
import plotly_express as px

st.set_page_config(layout="wide")
dataset1 = pd.read_csv('data/data_2022_2023.csv', index_col='Unnamed: 0')
dataset2 = pd.read_csv('data/data_2021_2022.csv', index_col='Unnamed: 0')
dataset3 = pd.read_csv('data/df_2022_2023_gk.csv', index_col='Unnamed: 0')
dataset4 = pd.read_csv('data/df_2021_2022_gk.csv', index_col='Unnamed: 0')

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
    if attribute == 'Shooting 👟':
        st.markdown("""
            <style>
                u {
                    text-decoration: underline;
                    text-decoration-color: #fa4d00;
                    }
                m {
                    font-size: 14px;
                    }
                </style>
            <u>**Actual Stats**</u>
            
            **Gls -- Goals**
            
            <m>Goals scored or allowed</m>
            
            ---
            
            **Sh -- Shots Total**
            
            Shots Total
            Does not include penalty kicks
        """,
                    unsafe_allow_html=True)

x = f1.dataFunc1(player, attribute, dataset1, dataset2, dataset3, dataset4)

row0_spacer1, row0_1, row0_2, row0_spacer2 = st.columns((.1, 1, 5,.1))
with row0_1:
    st.image('images/Logo.png')
with row0_2:
    st.title("Existing Squad Improvements 🔥")

row3_spacer1, row3_1, row3_spacer2 = st.columns((.05, 3.2, .05))
with row3_1:
    st.markdown("This page analyses the statistics of the current players who were also part of the Manchester"
                "United squad in the 2021/22 season. This page will compare statistics from this season against the "
                "statistics from the previous season of your choice of player. In some instances, some statistics "
                "will be compared against team averages.")

row1_spacer1, row1_1, row1_spacer2 = st.columns((.05, 3.2, .05))
with row1_1:
    st.markdown("### Basic Information")

x.display()

row2_spacer1, row2_1, row2_spacer2 = st.columns((.05, 3.2, .05))
with row2_1:
    st.markdown("### Analysis")

df1, df2 = x.filter_data()
x.data_visuals(df1 ,df2)

# if attribute == Adv GK
#   if player == DdG
#       x.data_visuals_gk(df1,df2)
#   else
#       warning message
# elif attribute == Shooting or GCA
#   if player == DdG
#       warning message
#   else
#       x.data_visuals(df1,df2)
# else:
#   x.data_visuals(df1,df2)