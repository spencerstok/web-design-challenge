import pandas as pd

df = pd.read_csv("cities.csv")

df.to_html("data.html")
