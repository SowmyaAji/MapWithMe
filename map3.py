import folium
import pandas as pd
import os
from folium.plugins import MarkerCluster

stores_data = os.path.join('data', 'store-locations.csv')
data = pd.read_csv(stores_data)
data['Store Address'] = data['Address'].map(
    str) + " " + data['City'] + " " + data['State'] + " " + data['Zip Code']


m = folium.Map(location=[48, -102], zoom_start=3, tiles='Stamen Terrain')
markerCluster = folium.plugins.MarkerCluster().add_to(m)

for i in range(0, len(data)):
    folium.CircleMarker([data.iloc[i]['Latitude'], data.iloc[i]
                         ['Longitude']],
                        radius=10,
                        tooltip=data.iloc[i]['Store Name'],
                        popup=data.iloc[i]['Store Address'],
                        color="#ff0000",
                        fill=True,
                        fill_color="#ff0000").add_to(markerCluster)


m.save('stores.html')
