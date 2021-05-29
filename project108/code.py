import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"], show_hist=False,)
fig.show()