import pandas as pd
import sportsipy
from sportsipy.nfl.teams import Teams

try:
    teams = Teams('2021')
    df_team = pd.DataFrame([(i.name,i.abbreviation) for i in teams], columns = ['team','abbreviation'])
    
except:
    df_team = pd.DataFrame([(None,None)],columns = ['team','abbreviation'])

df_team.to_csv('teams_2021.csv',index = None)