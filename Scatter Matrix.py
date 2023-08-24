import pandas as pd

import plotly.express as px 

df=pd.read_csv("Cars.csv")

fig = px.line(df, x="Model Year", y="Car Name")
fig.show()