import folium
import pandas

#Loads data from Volcanoes.txt into a DataFrame
data = pandas.read_csv("UdemyCourse\WebMap\Volcanoes.txt")

#Creates lat, long, elev, and name lists from the data frame
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#Changes color of the icon based on the elevation of the volcano
def colorPicker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red' 

#HTML to be used to perform a google search on the volcano name
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#Location is based off longitude/latitude coordinates
map = folium.Map(location=[42.3601, -71.0589], zoom_start=10, tiles="Stamen Terrain")

#Creates a feature group for the volcano data
fgv = folium.FeatureGroup(name="Volcano Map")

#Creates a feature group for the popuilation data
fgp = folium.FeatureGroup(name="Population")

#Adds markers to the feature group
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (name, name, el), width = 200, height = 100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=folium.Popup(iframe),
        fill_color = colorPicker(el), color = 'grey', fill_opacity = 0.7))

#Adds and colors polygons for different countries based on their populations
fgp.add_child(folium.GeoJson(data=open('UdemyCourse\WebMap\world.json', 'r', encoding='utf-8-sig').read(), 
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if  10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#Adds the feature groups to the map
map.add_child(fgv)
map.add_child(fgp)

#Adds layer control feature to the map
map.add_child(folium.LayerControl())

#Creates the map file
map.save("Map1.html")

