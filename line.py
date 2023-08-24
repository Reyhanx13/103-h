import pandas as pd

import plotly.express as px 

df=pd.read_csv("Videogames.csv")

fig = px.scatter(df, x="Platform(s)", y="Developer",color="Videogame")
fig.show()