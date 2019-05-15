import folium
import os
import json

# Create map object
m = folium.Map(location=[42.3701, -71.0589], zoom_start=12)

# Global tooltip
tooltip = "Click for More Info"

# Create custom marker icon
logoIcon = folium.features.CustomIcon('smiley1.png', icon_size=(50, 50))


# Create markers, popup and tooltip
folium.Marker([42.363600, -71.099500], popup="<strong>Location One</strong>",
              tooltip=tooltip).add_to(m),

# change marker icon
folium.Marker([42.333600, -71.109500], popup="<strong>Location Two</strong>",
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

# change marker color
folium.Marker([42.377120, -71.062400], popup="<strong>Location Three</strong>",
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),

# change marker color and icon
folium.Marker([42.374150, -71.122410], popup="<strong>Location Four</strong>",
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),

# custom marker usage
folium.Marker([42.375140, -71.032450], popup="<strong>Location Five</strong>",
              tooltip=tooltip,
              icon=logoIcon).add_to(m),

# circle marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup="Random birthplace",
    color="#428bca",
    fill=True,
    fill_color="428bca",
).add_to(m),


# Generate map
m.save('map.html')
