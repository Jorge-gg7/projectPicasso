import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


class dataFunc1:
    def __init__(self, name, attribute, dataset1, dataset2, dataset3, dataset4):
        """Used to create a new data set from the given user input
        :param name: Name of the player
        :param attribute: Attribute of the player like Shooting and Goalkeeping that the user is interested
        :param dataset1: First dataset used to extract data - 2022/23 dataset
        :param dataset2: Second dataset used to extract data - 2021/22 dataset
        :param dataset3: Third dataset used to extract data - 2022/23 gk dataset
        :param dataset4: Fourth dataset used to extract data - 2021/22 gk dataset
        """
        self._name = name
        self._attribute = attribute
        self._dataset1 = dataset1
        self._dataset2 = dataset2
        self._dataset3 = dataset3
        self._dataset4 = dataset4

    def filter_data(self):
        att = {'Shooting': ['Gls', 'Sh', 'SoT%', 'SoT/90', 'Dist', 'PK', 'PKatt', 'xG', 'npXG', 'npxG/Sh', 'G-xG',
                             'np:G-xG'],
                'Passing': ['Att', 'Cmp%', 'TotDist_Pass', 'PrgDist_Pass', 'Att_Shrt', 'Cmp%_Shrt', 'Att_Med',
                            'Cmp%_Med', 'Att_Long', 'Cmp%_Long', 'Ast', 'xAG', 'xA', 'KP', '1/3_Pass', 'PPA', 'CrsPA',
                            'PrgP'],
                'Pass Types': '',
                'Shot-Creating Action': '',
                'Goal-Creating Action': '',
                'Defensive Actions': '',
                'Possession': '',
                'Team Success with & without': '',
                'Miscellaneous': ''}
        df1 = self._dataset1.loc[self._dataset1['Player'] == str(self._name)]
        df1 = df1.loc[:, att[self._attribute]]
        df2 = self._dataset2.loc[self._dataset2['Player'] == str(self._name)]
        df1 = df2.loc[:, att[self._attribute]]

    def data_visuals(self):

    def data_visuals_gk(self):
