import pandas as pd

player_id = 6

df = pd.read_csv('fifa19.csv')
df_outfield = df

variables = df_outfield[['Name','Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle']]

  
def distance_to_point(player1):
    squared_distance =0
    for val in range(1,len(variables.columns)):
        squared_distance += (variables.iat[player_id, val]-variables.iat[player1, val])**2
    return squared_distance**0.5


player_distances = []
for i in range(10000):
    if i != player_id:
        player_distances.append([distance_to_point(i), variables.iat[i,0]])

    

player_distances.sort()
    

print(f"The most similar players to {variables.iat[player_id,0]} are: \n")

for num in range(5):
    print(f"{num+1}. {player_distances[num][1]}")