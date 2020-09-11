import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

def read_csv(file):
    df = pd.read_csv(file)
    return df
    
file = read_csv('fifa19.csv')
file = file[(file['Position']=='CB') | (file['Position']=='LB')]

print(file.columns)
file = file[:13000]
#file['PositionOvr'] = file['Position'].apply(lambda x: 'GK' if x=='GK' else 'Def' if (x=='RCB'or x=='LCB' or x=='CB' or x=='LB' or x=='RB' or x=='LWB' or x=='RWB') else 'Mid' if (x=='LM' or x=='RM' or x=='CAM' or x=='LAM' or x=='RAM' or x=='CM' or x=='LCM' or x=='RCM' or x=='CDM' or x=='LDM' or x=='RDM') else 'Fwd' if (x=='ST' or x=='CF' or x=='RW' or x=='LW' or x=='RF' or x=='LF' or x=='LS' or x=='RS') else 'haha' ) 
file = file.reset_index()

inputs = file[['Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle']]
outcome = file[['Overall']]
#plot_file = file[['Strength', 'SprintSpeed']]

#sns.pairplot(data=file, vars = ['StandingTackle','SlidingTackle', 'Agility'], kind='reg')

x_train, x_test, outcome_train, outcome_test = train_test_split(inputs,outcome,train_size=0.8, test_size=0.2)

model = LinearRegression()
model.fit(x_train, outcome_train)
prediction = model.predict(x_test)

plt.scatter(outcome_test, prediction)
plt.show()
print(model.coef_)
print(model.score(x_test,outcome_test))
