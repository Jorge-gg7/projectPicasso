# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd


st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

pd.read_csv('data/data_2022_2023.csv')
