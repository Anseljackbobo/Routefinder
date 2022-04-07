import pandas as pd
import googlemaps
from itertools import tee

def find_distance_matrix():
    df = pd.read_csv('googleresults.csv')
    API_key = 'your_API_Key'   #enter the key you got from Google. I removed mine here

    gmaps = googlemaps.Client(key=API_key)

    list = []
    for i, row in df.iterrows():
        origins = eval(df.at[i,'origins'])
        destination = eval(df.at[i,'destinations'])

        #pass origin and destination variables to distance_matrix function# output in meters
        result = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]['status']
        if result == 'OK':
            distance  = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]['distance']['value']
        else:
            distance = 0
        print(distance)
        # append result to list
        list.append(distance)
        
    df['Distance'] = list
    df.to_csv('googledistance.csv')
    print("--------google distance matrix is ready--------")