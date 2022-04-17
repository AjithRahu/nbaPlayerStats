import sys
import time
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.static import teams 
from nba_api.stats.endpoints import playergamelog






'''
COMMAND LINE ARGUMENTS:

FILE(FULL PATH) FIRSTNAME LASTNAME TEAMABBREVIATION

'''

#print("Number of arguments:", len(sys.argv), "arguments.")
#print("Argument List:", str(sys.argv))

#Get full list of NBA Players
player_dict = players.get_players()


first_name = str(sys.argv[1])
last_name = str(sys.argv[2])
team_against_input = str(sys.argv[3])

print("NBA Player: {} {}".format(str(sys.argv[1]), str(sys.argv[2])))




# Find requested player by full name.
# Use ternary operator or write function 
# Names are case sensitive
###### TODO: NEED TO CHECK IF INPUT PLAYER NAME AND TEAM NAME EXISTS
player = [player for player in player_dict if player['full_name'] == "{} {}".format(str(sys.argv[1]), str(sys.argv[2]))][0]
player_id = player['id']

print(player)
print(player_id)



# Team ID
teams = teams.get_teams()
team_against = [x for x in teams if x['abbreviation'] == team_against_input][0]
print(team_against['full_name'])




#Call the API endpoint passing in lebron's ID & which season 
gamelog_player = playergamelog.PlayerGameLog(player_id=player_id, season = '2021')

#Converts gamelog object into a pandas dataframe
#can also convert to JSON or dictionary  
df_player_games = gamelog_player.get_data_frames()
df_player_games = df_player_games[0]
df_player_games_seven = df_player_games.head(7)


print(df_player_games_seven)

print("Last Seven Games: ", df_player_games_seven["FG3_PCT"].mean())

print("Last Seven Games 3PM: ",df_player_games_seven["FG3M"].mean())

print("Season: ",df_player_games["FG3_PCT"].mean())

print("Season 3PM: ",df_player_games["FG3M"].mean())



######## TODO: Need to make arguments to check if the argument even exists
df_player_games_team = df_player_games[df_player_games["MATCHUP"].str.contains(team_against['abbreviation'])]
print(df_player_games_team)

