import streamlit as st
import pandas as pd
import matplotlib as plt

st.set_page_config(layout="wide")

row0_spacer1, row0_1, row0_2, row0_spacer2, row0_3, row0_spacer3 = st.columns((.1, 0.5, 1, .1, 1, .1))
with row0_1:
    st.image('images/Logo.png')
with row0_2:
    st.text("")
    st.title("MUFC Analyser")
with row0_3:
    st.text("")
    st.text("")
    st.subheader('Streamlit App by [Brandon Chew](https://www.linkedin.com/in/brandonc07/)')

row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown(
        "#### Welcome to my MUFC Analyser! Please enjoy using my very cool webapp that I have developed that analyses "
        "Manchester United's incredible success in the 2022/23 season.")
    st.markdown("#### Background")
    st.markdown("Sir Alex Ferguson is regarded as one of the greatest managers in the history of football and "
                "is regarded the best manager Manchester United has ever had. He managed Manchester United from 1986 to"
                " 2013, accumulating 38 club trophies throughout his career in Manchester United, the most of any"
                " manager in the world. He was credited for valuing youth during his time with Manchester United, "
                "particularly in the 1990s with the 'Class of '92' that included the likes of David Beckham and Paul "
                "Scholes, who contributed to making the club one of the richest and most successful in the world. ")
    st.markdown("After his departure in 2013, filling in his shoes seemed like an impossible task to do. The pressure "
                "that the next manager to do the same was immense as they needed to both be tactically adaptable whilst"
                " also upholding Manchester United's identity of attacking football and intense winning mentality. And "
                "this really was the case. Sir Alex Ferguson appointed David "
                "Moyes, a fellow Scotsman, after his retirement since he had found success in the Premier League in the"
                " 2012-13 season where he finished 6th with Everton in the Premier League."
                " Although he brought on the likes of Maruoane Fellaini from Everton and Juan Mata from Chelsea, "
                "he managed to finish 7th in the Premier and winning 0 trophies, the first time in decades for "
                "Manchester United. Not only that, the players that he bought could not adjust to Manchester United's "
                "playstyle and they were big and expensive flops by the end of the season."
                "After just 10 months, David Moyes was sacked due to extremely poor results.")
    st.markdown("This was a recurring trend after Sir Alex's departure where great managers bring in their ideologies "
                "into Manchester United, buying extremely expensive players that are not needed and then getting "
                "undesirable results which leads to them getting sacked after a season or 2. This was the case for the "
                "likes of Louis van Gaal and Jose Mourinho where they had brought in their ideologies of defensive "
                "football (the total opposite of Manchester United's identity) and bought players who do not fit into "
                "their own systems like Angel Di Maria, Alexis Sanchez and most notably Paul Pogba. ")
    st.markdown("#### Purpose of This Project")
