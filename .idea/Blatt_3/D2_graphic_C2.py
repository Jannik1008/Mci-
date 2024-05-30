import plotly.express as px
import numpy as np
import pandas as pd
import glob 
import os
import statsmodels.api as sm
#Excel einlesen
folder_path = r'.idea\Blatt_3\Daten_C2'
file_pattern = os.path.join(folder_path, '*.xlsx')
files = glob.glob(file_pattern)

all_data = []

for file in files:
    df = pd.read_excel(file)
    selected_columns = df[['id', 'mt']]
    all_data.append(selected_columns)

combined_df = pd.concat(all_data)

fig = px.scatter(combined_df, x='id', y='mt', title='C2 graph')

#Regressionsgerade berechnen
X = combined_df['id']
Y = combined_df['mt']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

# Extrahiere die Koeffizienten der Regressionsgeraden
intercept = model.params[0]
slope = model.params[1]
print(f"Regressionsgerade: Y = {intercept} + {slope} * X")

fig.add_traces(px.line(x=combined_df['id'], y = predictions, title='C2 graph').data)
fig.show()