# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import functions1 as f1

st.set_page_config(layout="wide")
dataset1 = pd.read_csv('data/data_2022_2023.csv')
dataset2 = pd.read_csv('data/data_2021_2022.csv')
dataset3 = pd.read_csv('data/df_2022_2023_gk.csv')
dataset4 = pd.read_csv('data/df_2021_2022_gk.csv')

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
    st.markdown("**")

x = f1.dataFunc1(player, attribute, dataset1, dataset2, dataset3, dataset4)

row0_spacer1, row0_1, row0_2, row0_spacer2 = st.columns((.1, 1, 5,.1))
with row0_1:
    st.image('images/Logo.png')
with row0_2:
    st.title("Existing Squad Improvements 🔥")

row1_spacer1, row1_1, row1_spacer2 = st.columns((.05, 3.2, .05))
with row1_1:
    st.markdown("### Basic Information")

x.display()

row2_spacer1, row2_1, row2_spacer2 = st.columns((.05, 3.2, .05))
with row2_1:
    st.markdown("### Analysis")