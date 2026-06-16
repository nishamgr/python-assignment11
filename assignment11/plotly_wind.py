import plotly.express as px
import plotly.data as pldata
import pandas as pd

#load dataset
df = pldata.wind(return_type='pandas')

#printing first 10 rows
print("The first 10 rows: ")
print(df.head(10))

#printing last 10 rows
print("Last 10 rows: ")
print(df.tail(10))

#converts strenght col to float
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

#scatter plot
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Strength Vs. Frequency by Direction"
)

#savs to HTML
fig.write_html("wind.html")

print("Plot saved at wind.html")