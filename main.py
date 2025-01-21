import pandas as pd

df = pd.read_csv("data/flickr_data2.csv", names=['id', 'user', 'lat', 'long', 'tags', 'title', 'date_taken_minute',
       'date_taken_hour', 'date_taken_day', 'date_taken_month',
       'date_taken_year', 'date_upload_minute', 'date_upload_hour',
       'date_upload_day', 'date_upload_month', 'date_upload_year',
       'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18'])

print("Nunique\n", df.nunique)
# print("NaN\n", df.isna().sum())

# print(df.keys())

print(df.columns)
print(df[['date_taken_year', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18']].loc[df['Unnamed: 16'].isna() == False])

"""
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

for i in range(0,len(df)):
    folium.Marker(
      location=[df.iloc[i]['lat'], df.iloc[i]['long']],
      popup=df.iloc[i]['id'],
   ).add_to(m)
    
m
"""