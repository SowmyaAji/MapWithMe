import folium
import os
import json
import pandas as pd


health_plans = os.path.join('data', 'geozips.csv')

data = pd.read_csv(health_plans)
data['LocRate'] = data['city'].map(
    str) + " " + data['state'] + " " + data['rate']

# Make an empty map
m = folium.Map(location=[48, -102], zoom_start=5)

# I can add marker one by one on the map
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['latitude'], data.iloc[i]['longitude']],
                  popup=data.iloc[i]['LocRate']).add_to(m)

# Save it as html
m.save('health_plans.html')
