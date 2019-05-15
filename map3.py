import folium
import pandas as pd
import os


stores_data = os.path.join('data', 'store-locations.csv')
data = pd.read_csv(stores_data)

m = folium.Map(location=[20, 0], zoom_start=3)
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['Latitude'], data.iloc[i]
                   ['Longitude']], popup=data.iloc[i]["Store Name"]).add_to(m)


m.save('stores.html')
