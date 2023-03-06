# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import functions1 as f1

st.set_page_config(layout="wide")
dataset1 = pd.read_csv('data/data_2022_2023.csv')
dataset2 = pd.read_csv('data/data_2021_2022.csv')
dataset3 = pd.read_csv('data/df_2022_2023_gk.csv')
dataset4 = pd.read_csv('data/df_2021_2022_gk.csv')

st.sidebar.markdown("# Player Select")

x = f1.dataFunc1('Marcus Rashford', 'Shooting', dataset1, dataset2, dataset3, dataset4)

row0_spacer1, row0_1, row_spacer2 = st.columns((.1, 1, 5))
with row0_1:
    st.image('images/Logo.png')

x.display()
