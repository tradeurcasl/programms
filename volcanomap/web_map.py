import folium
import pandas

'''Read and export information about every volcanoe in txt file and adapting it for our using'''
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

'''Create a base-layer of map'''
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

'''Volcanoes markers'''
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
                                      fill_color=color_producer(el), fill=True, color='grey', fill_opacity=0.7))

'''different layer-zones for density of population'''
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('map.html')