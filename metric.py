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
            *<m> Shots on target per 90 minutes </m>*
            
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
            
            
            """,
            unsafe_allow_html=True)
        else:
            st.markdown("OTW")