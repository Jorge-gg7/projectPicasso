import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import streamlit as st

class metric:
    def __init__(self, attribute):
        self._attribute = attribute

    def metric_glossary(self):
        if self._attribute == 'Shooting 👟':
            st.markdown(
                """
                <style>
                u {
                    text-decoration: underline;
                    text-decoration-color: #DA291C;
                }
                m {
                    font-size: 15px;
                    }
            </style>
            <u>**Goals (Gls):**</u>
            *<m> Goals scored or allowed. </m>*
            
            ---
            <u>**Shots (Sh):**</u>
            *<m> Total shots not including penalty kicks. </m>*
            
            ---
            <u>**Shots on Target% (SoT%):**</u>
            *<m> Percentage of shots that are on target </m>*
                
            *<m> Minimum .395 shots per squad game to qualify as a leader </m>*
                
            *<m>Note: Shots on target do not include penalty kicks </m>*
            
            ---
            <u>**Shots on Target per 90 (SoT/90):**</u>
            *<m> Shots on target divided by 90 minutes </m>*
            
            *<m> Minimum 30 minutes played per squad game to qualify as a leader</m>*
            
            *<m>Note: Shots on target do not include penalty kicks </m>*
            
            ---
            <u>**Goals per Shot (G/Sh):**</u>
            *<m> Goals per shot </m>*
            
            *<m> Minimum .395 shots per squad game to qualify as a leader</m>*
            
            ---
            <u>**Average Shot Distance (Dist):**</u>
            *<m> Average distance, in yards, from goal of all shots taken </m>*
            
            *<m> Minimum .395 shots per squad game to qualify as a leader</m>*
            
            *<m>Note: Does not include penalty kicks </m>*
            
            ---
            <u>**Penalty Kick Goals (PK):**</u>
            *<m> Penalty Kicks Made </m>*
            
            ---
            <u>**Expected Goals (xG):**</u>
            *<m> xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted). </m>*
            
            *<m> Provided by Opta.</m>*
            
            ---
            <u>**Non-Penalty Expected Goals (npxG):**</u>
            *<m> Similar to Expected Goals but does not include penalty shootouts. </m>*
            
            *<m> Provided by Opta.</m>*
            
            ---
            <u>**Non-Penalty Expected Goals per shot (npxG/Sh):**</u>
            *<m> Non-Penalty Expected Goals divided by shots taken.</m>*
            
            *<m> Provided by Opta.</m>*
            
            ---
            <u>**Goals minus Expected Goals (G-xG):**</u>
            *<m> xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted). </m>*
            
            *<m> Provided by Opta.</m>*
            
            ---
            <u>**Non-Penalty Goals minus Non-Penalty Expected Goals (np : G-xG):**</u>
            *<m> xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted). </m>*
            
            *<m> Provided by Opta.</m>*
            """,
            unsafe_allow_html=True)
        elif self._attribute == 'Passing ⚽':
            st.markdown(
                """
                <style>
                u {
                    text-decoration: underline;
                    text-decoration-color: #DA291C;
                }
                m {
                    font-size: 15px;
                    }
            </style>
            <u>**Assists (Ast):**</u>
            *<m> Final pass or cross before a goal is scored. Includes unintentional passes, deflections and touches on 
            the final pass by an opposing player. </m>*
            
            ---
            <u>**Passes Completed % (Cmp%):**</u>
            *<m> Passes completed divided by passes attempted. </m>*

            ---
            <u>**Passes Attempted (Att)**</u>
            *<m> Number of passes attempted including failed or deflected passes. </m>*
            
            ---
            <u>**Total Progressive Distance Passed (PrgDist_Pass):**</u>
            *<m> Total distance, in yards, that completed passes have traveled towards the opponent's goal. </m>*
            
            <m> Note: Passes away from opponent's goal are counted as zero progressive yards. </m>
            
            ---
            <u>**Total Distance Passed (TotDist_Pass):**</u>
            *<m> Total distance, in yards, that completed passes have traveled in any direction. </m>*
            
            ---
            <u>**Short Passes Attempted (Att_Shrt):**</u>
            *<m> Passes attempted between 5 and 15 yards. </m>*
            
            ---
            <u>**Medium Passes Attempted (Att_Med):**</u>
            *<m> Passes attempted between 15 and 30 yards. </m>*
            
            ---
            <u>**Long Passes Attempted (Att_Long):**</u>
            *<m> Passes attempted longer than 30 yards. </m>*
            
            ---
            <u>**Short Passes Completion % (Cmp%_Shrt):**</u>
            *<m> Passes completion rate between 5 and 15 yards. </m>*
            
            *<m> Minimum 30 minutes played per squad game to qualify as a leader </m>*
            
            ---
            <u>**Medium Passes Attempted (Cmp%_Med):**</u>
            *<m> Passes completion rate between 15 and 30 yards. </m>*
            
            *<m> Minimum 30 minutes played per squad game to qualify as a leader </m>*
            
            ---
            <u>**Long Passes Attempted (Cmp%_Long):**</u>
            *<m> Passes completion rate longer than 30 yards. </m>*
            
            *<m> Minimum 30 minutes played per squad game to qualify as a leader </m>*
            
            ---
            <u>**Expected Assists Goals (xAG):**</u>
            *<m> xG which follows a pass that assists a shot. </m>*
            
            *<m> Provided by Opta. </m>*
            
            ---
            <u>**Expected Assists (xA):**</u>
            *<m> The likelihood each completed pass becomes a goal assists given the pass type, phase of play, 
            location and distance.</m>*
            
            *<m> Provided by Opta. </m>*
            
            <m>Minimum 30 minutes played per squad game to qualify as a leader.</m>
            
            ---
            <u>**Key Passes (KP):**</u>
            *<m> Passes that directly lead to a shot (assisted shots). </m>*
            
            ---
            <u>**Passes into Final Third (1/3_Pass):**</u>
            *<m> Completed passes that enter the 1/3 of the pitch closest to the goal
                Not including set pieces. </m>*
            
            ---
            <u>**Passes into Penalty Area (PPA):**</u>
            *<m> Completed passes into the 18-yard box
                Not including set pieces. </m>*
            
            ---
            <u>**Crosses into Penalty Area (CrsPA):**</u>
            *<m> Completed crosses into the 18-yard box
                Not including set pieces. </m>*
            
            ---
            <u>**Progressive Passes (PrgP):**</u>
            *<m> Completed passes that move the ball towards the opponent's goal line at least 10 yards from its 
            furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the 
            defending 40% of the pitch.
            """
            ,unsafe_allow_html=True)
        elif self._attribute == 'Pass Types 🛒':
            st.markdown("""
            <style>
                u {
                    text-decoration: underline;
                    text-decoration-color: #DA291C;
                }
                m {
                    font-size: 15px;
                    }
            </style>
            <u>**Passes Attempted (Att)**</u>
            *<m> Number of passes completed by another player receiving the pass. </m>*
            
            ---
            <u>**Passes Attempted (Att)**</u>
            *<m> Number of passes attempted including failed or deflected passes. </m>*
            
            ---
            <u>**Passes Completed % (Cmp%):**</u>
            *<m> Passes completed divided by passes attempted. </m>*

            ---
            <u>**Live Ball Passes (Live_Pass):**</u>
            *<m> Number of passes when the ball is in play and in bounds of the field. </m>*

            ---
            <u>**Dead Ball Passes (Dead):**</u>
            *<m> Number of passes from free kicks, corner kicks, kick offs, throw-ins and goal kicks. </m>*

            ---
            <u>**Freekick Passes (FK_Pass):**</u>
            *<m> Number of passes from free kicks. </m>*
            
            ---
            <u>**Through Ball Passes (TB):**</u>
            *<m> Completed pass sent between back defenders into open spaces. </m>*
            
            ---
            <u>**Switches (Sw):**</u>
            *<m> Passes that travel more than 40 yards of the width of the pitch. </m>*
            
            ---
            <u>**Crosses (Crs):**</u>
            *<m> Passes from the wide end of the pitch to the middle of the pitch. </m>*
            
            ---
            <u>**Throw Ins (TI):**</u>
            *<m> Passes from either outer widths of the pitch by a throw. </m>*
            
            ---
            <u>**Corner Kicks (CK):**</u>
            *<m> Passes from the corner of the pitch after an out of bounds ball to the back of the pitch. </m>*
            
            ---
            <u>**Inswing Corner Kicks (In):**</u>
            *<m> Corner Kicks that curves outwards and then towards the goal. </m>*
            
            ---
            <u>**Outswing Corner Kicks (Out):**</u>
            *<m> Corner Kicks that curve inwards and then away from the goal. </m>*
            
            ---
            <u>**Straight Corner Kicks (Str):**</u>
            *<m> Corner Kicks that are delivered into the penalty box with no curve. </m>*
            
            ---
            <u>**Others:**</u>
            *<m> Corner kicks that include short passes, edge of the box corner kicks and failed corner kicks that went
             behind the goal resulting in a goal kick for the opposing team.</m>*
             
            ---
            <u>**Offside Passes (Off):**</u>
            
            *<m> Passes that result in an offside (A player is in an offside position if: any part of the head, body or 
            feet is in the opponents' half (excluding the halfway line) and. any part of the head, body or feet is 
            nearer to the opponents' goal line than both the ball and the second-last opponent. </m>*
            
            ---
            <u>**Block passes (Blocks):**</u>
            *<m> Blocked by the opponent who was standing it the path. </m>*
            """,
                        unsafe_allow_html=True)
        elif self._attribute == 'Shot-Creating Actions 😎':
            st.markdown("""
                        <style>
                            u {
                                text-decoration: underline;
                                text-decoration-color: #DA291C;
                            }
                            m {
                                font-size: 15px;
                                }
                        </style>
                        <u>**Shot-Creating Actions (SCA)**</u>
                        <m>*The two offensive actions directly leading to a shot, such as passes, take-ons and drawing 
                        fouls.*</m>
                        
                        <m>Note: A single player can receive credit for multiple actions and the shot-taker can also
                         receive credit. </m>

                        ---
                        <u>**Shot-Creating Actions per 90 (SCA90)**</u>
                        <m>*Shot-Creating Actions divided by 90 minutes.*</m>
                        
                        <m>Minimum 30 minutes played per squad game to qualify as leader. </m>

                        ---
                        <u>**Live Passes (PassLive_SCA)**</u>
                        <m>*Completed live-ball passes that lead to a shot attempt.*</m>

                        ---
                        <u>**Dead Passes (PassDead_SCA)**</u>
                        <m>*Completed dead-ball passes that lead to a shot attempt.*</m>
                        
                        <m>Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks. </m>

                        ---
                        <u>**Take Ons (TO_SCA)**</u>
                        <m>*Successful take ons that lead to a shot attempt.*</m>

                        ---
                        <u>**Shots (Sh_SCA)**</u>
                        <m>*Shots that lead to another shot attempt.*</m>

                        ---
                        <u>**Fouls (Fld_SCA)**</u>
                        <m>*Fouls drawn that lead to a shot attempt.*</m>

                        ---
                        <u>**Defensive Action (Def_SCA)**</u>
                        <m>*Defensive actions like tackles that lead to a shot attempt.*</m>

                        ---
                        """, unsafe_allow_html=True)
        elif self._attribute == 'Goal-Creating Actions 🫡':
            st.markdown("""
                                    <style>
                                        u {
                                            text-decoration: underline;
                                            text-decoration-color: #DA291C;
                                        }
                                        m {
                                            font-size: 15px;
                                            }
                                    </style>
                                    <u>**Goal-Creating Actions (GCA)**</u>
                                    <m>*The two offensive actions directly leading to a goal, such as passes, take-ons and drawing 
                                    fouls.*</m>

                                    <m>Note: A single player can receive credit for multiple actions and the shot-taker can also
                                     receive credit. </m>

                                    ---
                                    <u>**Goal-Creating Actions per 90 (GCA90)**</u>
                                    <m>*Goal-Creating Actions divided by 90 minutes.*</m>

                                    <m>Minimum 30 minutes played per squad game to qualify as leader. </m>

                                    ---
                                    <u>**Live Passes (PassLive_GCA)**</u>
                                    <m>*Completed live-ball passes that lead to a goal.*</m>

                                    ---
                                    <u>**Dead Passes (PassDead_GCA)**</u>
                                    <m>*Completed dead-ball passes that lead to a goal.*</m>

                                    <m>Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks. </m>

                                    ---
                                    <u>**Take Ons (TO_GCA)**</u>
                                    <m>*Successful take ons that lead to a goal.*</m>

                                    ---
                                    <u>**Shots (Sh_GCA)**</u>
                                    <m>*Shots that lead to another goal.*</m>

                                    ---
                                    <u>**Fouls (Fld_GCA)**</u>
                                    <m>*Fouls drawn that lead to a goal.*</m>

                                    ---
                                    <u>**Defensive Action (Def_GCA)**</u>
                                    <m>*Defensive actions like tackles that lead to a goal.*</m>

                                    ---
                                    """, unsafe_allow_html=True)
        else:
            st.markdown("OTW")