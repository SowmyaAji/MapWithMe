import folium
import pandas as pd
import os
from folium.plugins import MarkerCluster

stores_data = os.path.join('data', 'store-locations.csv')
data = pd.read_csv(stores_data)
data['Store Address'] = data['Address'] +
data['City'] + data['State'] + data['Zip Code']

m = folium.Map(location=[48, -102], zoom_start=3, tiles='Stamen Terrain')
markerCluster = folium.plugins.MarkerCluster().add_to(m)

for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['Latitude'], data.iloc[i]
                   ['Longitude']],
                  tooltip=data.iloc[i]['Store Name'],
                  popup=data.iloc[i]['Store Address']).add_to(markerCluster)


m.save('stores.html')
