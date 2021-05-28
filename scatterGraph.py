import plotly.express as px 
import pandas as pd 
df = pd.read_csv("Project.csv")
fig = px.scatter(df,x="date",y="cases",color="country", size="cases",size_max=60)
fig.show()