import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
dataset1 = pd.read_csv('data/data_2022_2023.csv', index_col='Unnamed: 0')
dataset2 = pd.read_csv('data/data_2021_2022.csv', index_col='Unnamed: 0')
dataset3 = pd.read_csv('data/df_2022_2023_gk.csv', index_col='Unnamed: 0')
dataset4 = pd.read_csv('data/df_2021_2022_gk.csv', index_col='Unnamed: 0')
dataset5 = pd.read_csv('data/df_2022_2023_new_signings.csv', index_col='Unnamed: 0')

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
        "### Welcome to my MUFC Analyser! Please enjoy using my webapp I have developed that analyses "
        "Manchester United's incredible success in the 2022/23 season.")

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
with row1_1:
    st.markdown("#### Purpose of This Project")
    st.markdown("Ever since I was young, I was always a diehard Manchester United fan. I loved the spirit and "
                "history of the club and I have always loved the sport of football. After watching how Erik Ten Hag has"
                " revolutionised Manchester United, I wanted to create a project that could analyse how Erik Ten Hag's"
                " was able to massively improve the squad in such a short time. As somebody who knew how to code and"
                " have created webapps before, I wanted to pursue this project. During my journey of creating this"
                " web app, I was able to learn: ")
    st.markdown("* How to create databases by web scraping.")
    st.markdown("* How to manage large databases.")
    st.markdown("* How to create a webapp using Streamlit.")
    st.markdown("* How to create a responsive data visualisation webapp that could show specific "
                "data based on a user's input.")
    st.markdown(" ")
    st.markdown("Visit the [Github repository](https://github.com/Jorge-gg7/projectPicasso) here!")

row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .1))
with row2_1:
    see_data = st.expander("Background")
    with see_data:
        row4_spacer1, row4_1, row4_2, row4_spacer2 = st.columns((.2, 3.2, 2, .2))
        with row4_1:
            st.markdown("Sir Alex Ferguson is regarded as one of the greatest managers in the history of football and "
                        "is regarded the best manager Manchester United has ever had. He managed Manchester United from 1986 to"
                        " 2013, accumulating 38 club trophies throughout his career in Manchester United, the most of any"
                        " manager in the world. He was credited for valuing youth during his time with Manchester United, "
                        "particularly in the 1990s with the 'Class of '92' that included the likes of David Beckham and Paul "
                        "Scholes, who contributed to making the club one of the richest and most successful in the world."
                        "After his departure in 2013, filling in his shoes seemed like an impossible task to do. The pressure "
                        "that the next manager to do the same was immense as they needed to both be tactically adaptable whilst"
                        " also upholding Manchester United's identity of attacking football and intense winning mentality. And "
                        "this really was the case. ")
        with row4_2:
            st.image('images/SAF.png')

        row5_spacer1, row5_1, row5_spacer2 = st.columns((.1, 3.2, .1))
        with row5_1:
            st.markdown(
                " Sir Alex Ferguson appointed David "
                "Moyes, a fellow Scotsman, after his retirement since he had found success in the Premier League in the"
                " 2012-13 season where he finished 6th with Everton in the Premier League."
                " Although he brought on the likes of Maruoane Fellaini from Everton and Juan Mata from Chelsea, "
                "he managed to finish 7th in the Premier and winning 0 trophies, the first time in decades for "
                "Manchester United. Not only that, the players that he bought could not adjust to Manchester United's "
                "playstyle and they were big and expensive flops by the end of the season."
                "After just 10 months, David Moyes was sacked due to extremely poor results.")
            st.markdown(
                "This was a recurring trend after Sir Alex's departure where great managers bring in their ideologies "
                "into Manchester United, buying extremely expensive players that are not needed and then getting "
                "undesirable results which leads to them getting sacked after a season or 2. This was the case for the "
                "likes of Louis van Gaal and Jose Mourinho where they had brought in their ideologies of defensive "
                "football (the total opposite of Manchester United's identity) and were supplied with players at "
                " ridiculous prices and also do not fit into "
                "their own systems like Angel Di Maria, Alexis Sanchez and most notably Paul Pogba. Many fans have "
                "since then blamed various parties for the downfall of Manchester United  "
                "where many have blamed the lack of funding from the Glazers, the largest shareholders of "
                "Manchester United, and the poor recruitment of both players and managers from their ex-CEO Ed "
                "Woodward ")

        row6_spacer1, row6_1, row6_2, row6_spacer2 = st.columns((.2, 2, 3.2, .2))
        with row6_1:
            st.image('images/OGS.png')
        with row6_2:
            st.markdown(
                "Things started to slowly change when Ole Gunnar Solskjaer was hired as their caretaker manager in the "
                "2018-2019 season."
                "Manchester United's results started to improve"
                " and The United identity started to show more and more after each game. "
                "Many hailed Solskjaer to be the next Sir Alex Ferguson due to his  "
                "ex-Manchester United player status and his knowledge of  "
                "Manchester United's true identity under Sir Alex Ferguson. "
                "After a few games, Manchester United signed Solskjaer as their manager and "
                "things started to reveal itself after a few 'honeymoon' months. Results started to "
                "worsen and Solskjaer's lack in adapting his tactics to different teams showed more and more after "
                "each match they play. When the new season came, Manchester United showed a glimpse of promise after"
                " signing the likes of Aaron Wan-Bissaka, Harry Maguire and Bruno Fernandes. These were great signings"
                " compared to the previous season signings and it was definitely the right step forward. ")

        row7_spacer1, row7_1, row7_spacer2 = st.columns((.1, 3.5, .1))
        with row7_1:
            st.markdown("During his first 2 full season at Manchester United, Solskjaer managed to finish 3rd and 2nd "
            "respectively and managed to reach a semi-final and final stage respectively in the Europa League in "
            "both years as well. During these 2 years, there were ofcourse great matches that proved that "
            "Solskjaer's effect on the squad was truly sensational like the Champions League match against PSG. "
            "However, during most of the season, fans were unhappy that the results that Manchester United have were"
            " always an uncertainty where Manchester United could beat the champions Manchester City 2-1 on one day "
            " and then lose to 1-0 to a relegation zone team the next week. Moreover, many fans have observed that "
            "Solskjaer was tactically unadaptable as he only knew how to do counter attacking football with the "
            "likes of his pacey wingers' Marcus Rashford and Mason Greenwood. This was very apparent during his "
            "last season at United. Eventhough the club made an impulsive Cristiano Ronaldo signing, the fans knew"
            "that Solskjaer's sacking was imminent because of this problem. After 12 games into the season"
            " he was ultimately sacked for poor results.")
            st.markdown(
                "During the rest of the 2021-22 season under Ralf Ragnick, things weren't any better. Results were "
                "still extremely uncertain even against worse teams and the everlasting problems brought on by the "
                "Glazers and senior management were clearer than before after Ragnick's explosive press conference. "
                "Fans started to protest against the Glazers and Ed Woodward, stating that the club was underfunded, "
                "the United identity has long been forgotten and the fans were not being heard. Fans even broke into "
                "Old Trafford before the Liverpool game to stage a protest against the Glazers and their "
                "mismanagement and call for some action. In the next season, the Glazers had finally listened to their "
                "fans.")

        row8_spacer1, row8_1, row8_2, row8_spacer2 = st.columns((.15, 3.2, 2, .15))
        with row8_1:
            st.markdown(
                "On 21 April 2022, Erik Ten Hag was was appointed as manager of Manchester United starting from the end "
                "of the 2021–22 season until June 2025, with the option of extending for a further year. Ten Hag is most "
                "notably known for managing the Dutch side Ajax to a semi-final in the Champions League by winning against "
                "defending champions Real Madrid 4-1. Ten Hag's is also well known for his managing style where he much like"
                "Sir Alex Ferguson, he values youth greatly and enforces a 'I am the boss' mentality towards his players. "
                "Fans were excited to hear that Ten Hag will be joining Manchester United knowing what he can bring to the "
                "club. The club further supported him by signing players from his previous club like Lisandro Martinez"
                " and Antony and further expanded the squad's depth by signing the likes of Tyrell Malacia and Christian"
                " Eriksen. However, after his first few games as manager, fans started to speculate if this was just "
                "another fluke. His first 2 Premier League games ended in a loss")
        with row8_2:
            st.image('images/ETH.png')

        row9_spacer1, row9_1, row9_spacer2 = st.columns((.1, 3.5, .1))
        with row9_1:
            st.markdown(" against weaker sides and this prompted many analysts and pundits to doubt Ten"
                        " Hag even more. However, things quickly changed after his"
                        " next game against arch rivals, Liverpool, at home who were also struggling in form but "
                        "were the clear favourites out of the two. Ten Hag made some changes within his squad and "
                        "adapted his tactics to Liverpool's tactics and in the end Manchester United won 2-1. "
                        "From that point on, things started to look much better for Ten Hag and his squad. "
                        "Manchester United started winning more and more, beating League leaders Arsenal and other "
                        "Top 6 contenders and also qualifying for the Round of 16 of the Europa League. Even though Ten"
                        " Hag had to deal with some internal issues like the Cristiano Ronaldo interview and Jadon "
                        "Sancho's drop in form, everyone applauded how Ten Hag dealt with the situations stating that"
                        " his man management is like no other. Overall, Ten Hag has been doing an insane amount of"
                        " work to put his squad where they belong and I believe that this is not the end for him." )

row10_spacer1, row10_1, row10_spacer2 = st.columns((.1, 3.2, .1))
with row10_1:
    st.markdown("#### How do I use this webapp?")
    st.markdown("This webapp contains 2 parts, the Analysis on the Improvement of Players that are still with "
                "Manchester United from the previous 2021/2022 season and the Analysis on the New Signings Impact on "
                "the squad.")
    st.markdown("##### Existing Squad Improvement")
    st.markdown("For this analysis, the user inputs 2 different types of data to analyse. The first being the player "
                "and the next being the stat that the user is interested in. With that, the webapp will show how"
                " much the player has improved/deteriorate from last season under Ten Hag and how different he plays "
                "as well by comparing his stats from this season and last season. For example, **WORK IN PROGRESS**")
    #st.image()
    st.markdown("##### New Signings Impact")
    st.markdown("For this analysis, the user inputs 2 different types of data to analyse. The first being the player "
                "and the next being the stat that the user is interested in. With that, the webapp will show how "
                "this new signing has either improve/worsen the team by analysing his stats and comparing the team's "
                "stats from last season and this season. For example, **WORK IN PROGRESS**")
    #st.image()

row11_spacer1, row11_1, row11_spacer2 = st.columns((.1, 3.2, .1))
with row11_1:

    st.markdown("#### Select and click on the dropdown menu to see the different raw datasets!")
    input = st.radio(
        "Which dataset do you want to see?",
        ["Player Stats 2022/23", "Player Stats 2021/22", "New Signing Stats 2022/23",
         "Advanced Goalkeeper Stats 2022/23", "Advanced Goalkeeper Stats 2021/22"],
        horizontal=True
    )
    see_data1 = st.expander("Click here to see the dataset!")
    with see_data1:
        if input == "Player Stats 2022/23":
            st.dataframe(data=dataset1.reset_index(drop=True))
        elif input == "Player Stats 2021/22":
            st.dataframe(data=dataset2.reset_index(drop=True))
        elif input == "New Signing Stats 2022/23":
            st.dataframe(data=dataset5.reset_index(drop=True))
        elif input == "Advanced Goalkeeper Stats 2022/23":
            st.dataframe(data=dataset3.reset_index(drop=True))
        elif input == "Advanced Goalkeeper Stats 2021/22":
            st.dataframe(data=dataset4.reset_index(drop=True))

row12_spacer1, row12_1, row12_spacer2 = st.columns((.1, 3.2, .1))
with row12_1:
    notes = st.expander("Notes on the datasets ⁉️ : ")
    with notes:
        st.markdown("1. Players with 0 minutes in each season are not included in the dataset.")
        st.markdown("2. FA Cup and Carabao Cup statistics are unavailable, therefore the only goalkeeper that is "
                    "included in the dataset is David De Gea .")
        st.markdown("3. Abbreviations are explained in the Existing Squad Improvement 🔥 and New Signings Impact page.")
        st.markdown("4. New signings include players that were newly signed in the 2022/23 season or players who were "
                    "promoted to the first team from the youth team.")
        st.markdown("5. All datasets were updated on 5/1/2024.")