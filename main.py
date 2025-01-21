import pandas as pd
import folium

df = pd.read_table("data/cleaned-data.csv", sep=",")

sampled_data = df.sample(1000)

m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

for i in range(0,len(sampled_data)):
    folium.Marker(
      location=[sampled_data.iloc[i]['lat'], sampled_data.iloc[i]['long']],
      popup=sampled_data.iloc[i]['id'],
   ).add_to(m)
    