import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())


def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams':teams
    }

    return team_dict


def teamvsteamAPI(team1, team2):
    temp_df = matches[(matches['Team1']==team1) & (matches['Team2']==team2) | 
    (matches['Team1']==team2) & (matches['Team2']==team1)]

    total_matches = temp_df.shape[0]

    matches_team1_won = temp_df['WinningTeam'].value_counts()[team1]
    matches_team2_won = temp_df['WinningTeam'].value_counts()[team2]

    draws = total_matches -(matches_team1_won + matches_team2_won)

    response = {
        'total matches' : str(total_matches),
         team1: str(matches_team1_won),
         team2: str(matches_team2_won),
         'draws':str(draws)
    }

    return response