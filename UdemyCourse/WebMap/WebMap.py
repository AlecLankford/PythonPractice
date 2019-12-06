import folium
import pandas

#Loads data from Volcanoes.txt into a DataFrame
data = pandas.read_csv("UdemyCourse\WebMap\Volcanoes.txt")

#Creates latitude and longitude lists from the data frame
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Location is based off longitude/latitude coordinates
map = folium.Map(location=[42.3601, -71.0589], zoom_start=10, tiles="Stamen Terrain")

#Creates a feature group
fg = folium.FeatureGroup(name="My Map")

#Adds markers to the feature group
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " meters", icon=folium.Icon(color='green')))

#Adds the feature group to the map
map.add_child(fg)

#Creates the map file
map.save("Map1.html")

