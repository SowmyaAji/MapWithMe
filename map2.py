import folium
import pandas as pd
import os

# access the json file of US states in the variable states
states = os.path.join('data', 'us-states.json')

# access the csv file of unemployment data in the variable unemployment_data
unemployment_data = os.path.join('data', 'us-unemployment.csv')

# read the unemployment data from the CSV file into the variable state_data using pandas as pd
state_data = pd.read_csv(unemployment_data)

# create different bins for the legend to show

bins = list(state_data['Unemployment'].quantile([0, 0.25, 0.5, 0.75, 1]))
# create map object
m = folium.Map([48, -102], zoom_start=3)
folium.Choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate %",
    bins=bins,
    reset=True
).add_to(m)


m.save('map2.html')
