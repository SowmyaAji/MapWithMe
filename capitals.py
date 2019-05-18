import folium
import pandas as pd
import re

url = 'capitals.json'
data = pd.read_json(url, orient='columns')

data['CountryCap'] = data['Capital'].map(str) + ", " + data['Country']


def dmstring(s):
    st1 = s.split(".")
    deg = st1[0]
    sec = st1[1]
    hem = sec[-1]
    min = sec[:-1]
    dd = float(deg) + float(min)/60
    if hem == 'S' or hem == 'W':
        dd *= -1
    return dd


data['Latitude'] = data['Latitude'].apply(dmstring)
data['Longitude'] = data['Longitude'].apply(dmstring)


m = folium.Map(location=[20, 0], zoom_start=3, tiles='Stamen Terrain')
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
                  popup=data.iloc[i]['CountryCap'],
                  icon=folium.Icon(color='green', icon='leaf')
                  ).add_to(m)
m.save('capitals.html')
