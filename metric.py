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
        elif self._attribute == 'Defensive Actions 💪':
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
                        <u>**Total Tackles (Tkl)**</u>
                        <m>*Number of players tackled.*</m>

                        ---
                        <u>**Total Tackles Won (TklW)**</u>
                        <m>*Tackles in which the tackler's team won possession of the ball.*</m>
                        
                        ---
                        <u>**Interceptions (Int)**</u>
                        <m>*Occurs when a player intercepts a pass of the opposing team.*</m>
                        
                        ---
                        <u>**Clearances (Clr)**</u>
                        <m>*Occurs when a player launches a ball towards the attacking penalty area from a defensive
                        area of the pitch.*</m>
                        
                        ---
                        <u>**Errors (Err)**</u>
                        <m>*Mistakes leading to an opponent's shot.*</m>
                        
                        ---
                        <u>**Defensive Third Tackles (Def 3rd_Tkls)**</u>
                        <m>*Tackles in the defensive area of the team's pitch.*</m>
                        
                        ---
                        <u>**Middle Third Tackles (Mid 3rd_Tkls)**</u>
                        <m>*Tackles in the middle area of the team's pitch.*</m>
                        
                        ---
                        <u>**Attacking Third Tackles (Att 3rd_Tkls)**</u>
                        <m>*Tackles in the attacking area of the team's pitch.*</m>
                        
                        ---
                        <u>**Challenges Won (Tkl_Chl)**</u>
                        <m>*Number of dribblers successfully tackled.*</m>
                        
                        ---
                        <u>**Challenges Lost (Lost)**</u>
                        <m>*Number of dribblers unsuccessful tackled.*</m>
                        
                        ---
                        <u>**Shots Blocked (Blocks_Sh)**</u>
                        <m>*Number of times blocking a shot by standing in its path.*</m>
                        
                        ---
                        <u>**Passes Blocked (Pass)**</u>
                        <m>*Number of times blocking a pass by standing in its path.*</m>
                        
            """, unsafe_allow_html=True)
        elif self._attribute == 'Possession 👻':
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
                        <u>**Total Touches (Touches)**</u>
                        <m>*Number of times a player touched the ball.*</m>
                        
                        <m>Note: Receiving a pass, then dribbling, then sending a pass counts as one touch.</m>
                        ---
                        <u>**Total Live Touches (Live_Tch)**</u>
                        <m>*Live-ball touches. Does not include corner kicks, free kicks, throw-ins, kick-offs, goal
                        kicks or penalty kicks.*</m>

                        ---
                        <u>**Defensive Penalty Box Touches (Def Pen)**</u>
                        <m>*Touches in the defensive penalty area (18-yard box).*</m>

                        ---
                        <u>**Defensive Third Touches (Def 3rd_Tch)**</u>
                        <m>*Touches in the defensive third of the pitch including the defensive penalty area.*</m>

                        ---
                        <u>**Middle Third Touches (Mid 3rd_Tch)**</u>
                        <m>*Touches in the middle third of the pitch.*</m>

                        ---
                        <u>**Attacking Third Touches (Att 3rd_Tch)**</u>
                        <m>*Touches in the attacking third of the pitch including the attacking penalty area.*</m>

                        ---
                        <u>**Attacking Penalty Box Touches (Att Pen)**</u>
                        <m>*Touches in the attacking penalty area (18-yard box).*</m>

                        ---
                        <u>**Successful Take-Ons (Succ)**</u>
                        <m>*Number of defenders taken on successfully, by dribbling past them.*</m>

                        ---
                        <u>**Unsuccessful Take-Ons **</u>
                        <m>*Number of defenders unsuccessfully taken on. Includes attempts where the dribblers retained 
                        possession but was unable to get past the defender.*</m>

                        ---
                        <u>**Tackled During Take-On (Tkld)**</u>
                        <m>*Number of times tackled by a defender during a take-on attempt. Does not mean that the 
                        take-on was unsuccessful.*</m>

                        ---
                        <u>**Untackled During Take-On**</u>
                        <m>*Number of times unchallenged while attempting a take-on.*</m>

                        ---
                        <u>**Total Carries (Carries)**</u>
                        <m>*Number of times the player controlled the ball with their feet.*</m>

                        ---
                        <u>**Total Distance Carried (TotDist)**</u>
                        <m>*Total distance, in yards, a player moved the ball while controlling it with their feet, 
                        in any direction.*</m>

                        ---
                        <u>**Total Progressive Distance Carried (PrgDist)**</u>
                        <m>*Total distance, in yards, a player moved the ball while controlling it with their feet 
                        towards the opponent's goal.*</m>

                        ---
                        <u>**Total Progressive Carries (PrgC)**</u>
                        <m>*Carries that move the ball towards the opponent's goal line at least 10 yards from its
                        furthest point in the last six passes, or any carry into the penalty area.*</m>
                        
                        <m>Excludes carries which end in the defending 50% of the pitch. </m>

                        ---
                        <u>**Carries into the Final Third (1/3_Carr)**</u>
                        <m>*Carries that enter the 1/3 of the pitch closest to the goal.*</m>

                        ---
                        <u>**Carries into Penalty Area (CPA)**</u>
                        <m>*Carries into the 18-yard box.*</m>

                        ---
                        <u>**Miscontrols (Mis)**</u>
                        <m>*Number of times a player failed when attempting to gain control of a ball.*</m>

                        ---
                        <u>**Dispossessed (Dis)**</u>
                        <m>*Number of times a player loses control of the ball after being tackled by an opposing 
                        player. Does not include attempted take-ons.*</m>

                        ---
                        <u>**Passes Received (Rec)**</u>
                        <m>*Number of times a player successfully received a pass.*</m>

                        ---
                        <u>**Progressive Passes Received (PrgR)**</u>
                        <m>*Completed passes that move the ball towards the opponent's goal line at least 10 yards from 
                        its furthest point in the last six passes, or any completed pass into the penalty area.*</m>

                        <m>Excludes passes from the defending 40% of the pitch. </m>
            """,unsafe_allow_html=True)
        elif self._attribute == 'Team Success with & without 🎇':
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
                        <u>**Total Matches Played (MP)**</u>
                        <m>*Total matches played by the player.*</m>

                        ---
                        <u>**Total Minutes Played (Min)**</u>
                        <m>*Total minutes played by the player.*</m>

                        ---
                        <u>**Minutes per Matches Played (Mn/MP)**</u>
                        <m>*Total Minutes divided by total matches played.*</m>

                        ---
                        <u>**Percentage of Squad Minutes Played (Min%)**</u>
                        <m>*Percentage of team's total minutes in which player was on the pitch. Player minutes divided
                        by team total minutes played.*</m>
                        
                        <m>Minimum 30 minutes played per squad game to qualify as leader.</m>
                        ---
                        <u>**Total Games Starts (Starts)**</u>
                        <m>*Game or games started by player.*</m>

                        ---
                        <u>**Minutes Per Start (Mn/Start)**</u>
                        <m>*Average minutes for every match started.*</m>

                        <m>Minimum 30 minutes played per squad game to qualify as a leader.</m>
                        ---
                        <u>**Completed Games from Start (Compl)**</u>
                        <m>*Number of completed games when the player started for the squad.*</m>

                        ---
                        <u>**Total Games as Substitute (Subs)**</u>
                        <m>*Game or games player did not start, so as a substitute.*</m>

                        ---
                        <u>**Minutes per Substitute (Mn/Sub)**</u>
                        <m>*Average minutes for every match as a substitute.*</m>

                        ---
                        <u>**Games as Unused Substitute (unSub)**</u>
                        <m>*Games that the player did not play and was only a substitute.*</m>

                        ---
                        <u>**Points Per Match (PPM)**</u>
                        <m>*Average number of points earned by the team from matches in which the player played.*</m>

                        <m>Minimum 30 minutes played per squad game to qualify as a leader. </m>
                        ---
                        <u>**Goals Scored by Team While on Pitch (onG)**</u>
                        <m>*Goals scored by the team while the player is on the pitch.*</m>

                        ---
                        <u>**Goals Conceded by Team While on Pitch (onGA)**</u>
                        <m>*Goals conceded by the team while the player is on the pitch.*</m>

                        ---
                        <u>**(+/-)**</u>
                        <m>*Plus/Minus. Goals scored minus goals conceded by the team while player was on the pitch.*</m>

                        ---
                        <u>**+/- per 90 (+/-90)**</u>
                        <m>*Plus/Minus divided by 90 minutes. Goals scored minus goals conceded by the team while player 
                        was on the pitch per 90 minutes played. *</m>

                        <m>Minimum 30 minutes played per squad game to qualify as leader.</m>
                        ---
                        <u>**(On-Off)**</u>
                        <m>*Net goals per 90 minutes by the team while the player was on the pitch minus net goals 
                        conceded per 90 minutes by the team while the player was off the pitch. *</m>

                        <m>Minimum 30 minutes played per squad game to qualify as leader.</m>
                        
                        ---
                        <u>**Expected Goals Scored by Team While on Pitch (onxG)**</u>
                        <m>*xG totals include penalty kicks, but do not include penalty shootouts 
                        (unless otherwise noted). *</m>
                        
                        ---
                        <u>**Expected Goals Conceded by Team While on Pitch (onxGA)**</u>
                        <m>*xG totals include penalty kicks, but do not include penalty shootouts 
                        (unless otherwise noted). *</m>
                        
                        ---
                        <u>**(xG+/-)**</u>
                        <m>*Expected goals scored minus expected goals conceded by the team while the player was on the 
                        pitch. *</m>
                        
                        ---
                        <u>**Expected +/- per 90 (xG+/-90)**</u>
                        <m>*Expected goals scored minus expected goals conceded by the team while the player was on the 
                        pitch per 90 minutes played. *</m>
                        
                        ---
                        <u>**Expected On-Off (On-Off_xG)**</u>
                        <m>*Net expected goals per 90 minutes by the team while the player was on the pitch minus net 
                        expected goals per 90 minutes by the team while the player was off the pitch. *</m>
                        
                        ---
            """, unsafe_allow_html=True)
        elif self._attribute == 'Miscellaneous 🏆':
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
                        <u>**Yellow Cards (CrdY)**</u>
                        <m>*Number of single yellow cards obtained in a match.*</m>

                        ---
                        <u>**Red Cards (CrdR)**</u>
                        <m>*Number of red cards obtained in a match.*</m>

                        ---
                        <u>**2 Yellow Cards (2CrdY)**</u>
                        <m>*Number of second yellow cards obtained in a match.*</m>

                        ---
                        <u>**Fouls Committed (Fls)**</u>
                        <m>*Number of fouls committed against an opponent in a match.*</m>

                        ---
                        <u>**Fouls Drawn (Fld)**</u>
                        <m>*Number of fouls drawn by an opponent in a match.*</m>

                        ---
                        <u>**Offsides (Ofsd)**</u>
                        <m>*Number of times the player is caught offside in a match.*</m>

                        ---
                        <u>**Penalty Kicks Won (PKwon)**</u>
                        <m>*Number of penalty kicks won by getting fouled in a match.*</m>

                        ---
                        <u>**Penalty Kicks Conceded (PKcon)**</u>
                        <m>*Number of penalty kicks given away to an opponent in a match.*</m>

                        ---
                        <u>**Own Goals (OG)**</u>
                        <m>*Number of own goals scored against the team.*</m>

                        ---
                        <u>**Ball Recoveries (Recov)**</u>
                        <m>*Number of loose balls recovered.*</m>

                        ---
                        <u>**Aeriel Duels Wins (Won_AD)**</u>
                        <m>*Number of aeriel duels won.*</m>

                        ---
                        <u>**Aeriel Duels Lost (Lost_AD)**</u>
                        <m>*Number of aeriel duels lost.*</m>

                        ---
            """, unsafe_allow_html=True)
        elif self._attribute == 'Advanced Goalkeeping 🥅':
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
                        <u>**Goals Against (GA)**</u>
                        <m>*Number of goals that were scored by the opposing team whilst the player was the goalkeeper.
                        *</m>

                        ---
                        <u>**Penalty Kicks Allowed (PKA)**</u>
                        <m>*Number of goals from Penalty Kicks
                        that were scored by the opposing team whilst the player was the goalkeeper.*</m>

                        ---
                        <u>**Free Kicks Goal Against (FK)**</u>
                        <m>*Number of goals from Free Kicks 
                        that were scored by the opposing team whilst the player was the goalkeeper.*</m>
                        
                        ---
                        <u>**Corner Kicks Goal Against (CK)**</u>
                        <m>*Number of goals from Corner Kicks
                        that were scored by the opposing team whilst the player was the goalkeeper.*</m>
                        
                        ---
                        <u>**Own Goals Against (OG)**</u>
                        <m>*Own goals scored against the goalkeeper.*</m>
                        
                        ---
                        <u>**Free Kicks Goal Against (FK)**</u>
                        <m>*Number of Free Kick goals 
                        that were scored by the opposing team whilst the player was the goal keeper.*</m>
                        
                        ---
                        <u>**Launch Passes [excluding Goal Kicks]**</u>
                        <m>*Passes that were longer than 40 yards during a live ball play.*</m>
                        
                        ---
                        <u>**Throw Passes [excluding Goal Kicks] (Thr)**</u>
                        <m>*Passes that were thrown during a live ball play.*</m>
                        
                        ---
                        <u>**Regular Passes [excluding Goal Kicks]**</u>
                        <m>*Passes that were shorter than 40 yards and were kicked during a live ball play.*</m>
                        
                        ---
                        <u>**Average Pass Length [excluding Goal Kicks] (AvgLen_Pass)**</u>
                        <m>*Average length of a live ball play pass in yards.*</m>
                        
                        ---
                        <u>**Total Passes Attempted [excluding Goal Kicks]**</u>
                        <m>*Total number of passes that were attempted (not necessarily successful) from a live ball
                        play.*</m>
                        
                        ---
                        <u>**Completed Launch Passes (Cmp)**</u>
                        <m>*Passes that were longer than 40 yards and were successfully received by a teammate 
                        in any sort of play (including Goal Kicks).*</m>
                        
                        ---
                        <u>**Incomplete Launch Passes**</u>
                        <m>*Passes that were longer than 40 yards to a teammate but was not received 
                        in any sort of play (including Goal Kicks).*</m>
                        
                        ---
                        <u>**Total Launches Attempted (Att_Launch)**</u>
                        <m>*Passes that were longer than 40 yards to a teammate in any sort of play (including Goal 
                        Kicks).*</m>
                        
                        ---
                        <u>**Short Pass Goal Kicks**</u>
                        <m>*Passes that were shorter than 40 yards and were passed from a Goal Kick.*
                        </m>
                        
                        ---
                        <u>**Launched Goal Kicks**</u>
                        <m>*Passes that were longer than 40 yards and were passed from a Goal Kick.*
                        </m>
                        
                        ---
                        <u>**Average Pass Length [Goal Kicks] (AvgLen_GKicks)**</u>
                        <m>*Average length of a Goal Kick pass in yards*</m>
                        
                        ---
                        <u>**Total Goal Kicks Attempted (Att_GKicks)**</u>
                        <m>*Total number of Goal Kicks that were attempted (not necessarily successful).*</m>
                        
                        ---
                        <u>**Crosses Challenged (Stp)**</u>
                        <m>*Number of crosses into the penalty area which were successfully stopped by the goalkeeper*</m>
                        
                        ---
                        <u>**Crosses Unchallenged**</u>
                        <m>*Number of crosses into the penalty area which the goalkeeper did not challenge or attempt
                        to stop by catching or deflecting the cross.*</m>
                        
                        ---
                        <u>**Total Crosses Faced (Opp)**</u>
                        <m>*Opponent's attempted crosses into the penalty area.*</m>
                        
                        ---
                        <u>**Average Pass Length [Goal Kicks] (AvgLen_GKicks)**</u>
                        <m>*Average length of a Goal Kick pass in yards.*</m>
                        
                        ---
                        <u>**Total Defensive Actions (#OPA)**</u>
                        <m>*Number of defensive actions outside of the penalty area. E.g. tackling defenders, clearing 
                        balls.*</m>
                        
                        ---
                        <u>**Total Defensive Actions/90 (#OPA/90)**</u>
                        <m>*Number of defensive actions outside of the penalty area per 90 minutes. E.g. tackling 
                        defenders, clearing balls.*</m>
                        
                        ---
                        <u>**Average Distance of Defensive Action from Goal (AvgDist)**</u>
                        <m>*Average distance from goal (in yards) of all defensive actions.*</m>
                        
                        ---
                        <u>**Post-Shot Expected Goals (PSxG)**</u>
                        <m>*PSxG is the expeceted goals based on how likely the goalkeeper is to save the shot. xG 
                        totals include penalty kicks, but do not include penalty shootouts.*</m>
                        
                        <m>Provided by Opta</m>
                        
                        ---
                        <u>**Post-Shot Expected Goals per Shot on Target (PSxG/SoT)**</u>
                        <m>*PSxG divided by Shots on Target (not including penalty kicks).*</m>
                        
                        <m>Provided by Opta</m>
                        
                        ---
                        <u>**Post-Shot Expected Goals Minus Goals Allowed(PSxG+/-)**</u>
                        <m>*PSxG minus PSxGA. Positive numbers suggest better luck or an above average ability to stop 
                        shots.*</m>
                        
                        <m>Provided by Opta</m>
                        
                        ---
                        <u>**Post-Shot Expected Goals Minus Goals Allowed per 90 (/90)**</u>
                        <m>*PSxG+/- divided by 90 minutes.*</m>
                        
                        <m>Provided by Opta</m>
            """, unsafe_allow_html=True)
        else:
            st.markdown("OTW")