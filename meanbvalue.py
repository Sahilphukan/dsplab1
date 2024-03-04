import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
mean_values =df.groupby('Weather').mean()
print(mean_values)