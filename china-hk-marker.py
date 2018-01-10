import folium
#guangdong
map=folium.Map(location=[23.3790, 113.7633],tiles="Mapbox Bright",max_zoom=6)
#hong kong
map.add_child(folium.Marker(location=[22.3964, 114.1095], popup="Here! I am from Hong Kong!", icon=folium.Icon(color='green')))

map.save("china-hk.html")
