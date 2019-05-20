import folium
import pandas as pd
import json


url = "cary-trees.json"
data = pd.read_json(url, orient='columns')
data['LocName'] = data['Name'].map(str) + ", " + data['Location Name']


def get_lat(arr):
    return arr[0]


def get_long(arr):
    return arr[1]


data['latitude'] = data['geo_point_2d'].apply(get_lat)
data['longitude'] = data['geo_point_2d'].apply(get_long)


m = folium.Map(location=[35.791538, -78.781120],
               zoom_start=12)

for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['latitude'], data.iloc[i]['longitude']],
                  tooltip=data.iloc[i]['LocName'],
                  icon=folium.Icon(color='green', icon='leaf')).add_to(m)

m.save('carytrees.html')
