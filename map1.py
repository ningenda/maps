import folium

map= folium.Map(location=[25.618444,85.122278],zoom_start=10,tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")
for coordinates in [[25.6,85.1],[25.1,85.6]]:
    map.add_child(folium.Marker(location=coordinates,popup="Hi I am a marker",icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
