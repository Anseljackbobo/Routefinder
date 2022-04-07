import pandas as pd
import csv

def create_date_for_google_map():
    df = pd.read_csv('Routeplus.csv')

    with open('googleresults.csv', 'w', newline='') as csvfile:
        fieldnames = ['Customer ID', 'origins', 'destinations']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        cunt = 0
        for i, row in df.iterrows():
            lat = df.at[i,'lat']
            lng = df.at[i,'lng']
            origins = str(lat) + ',' + str(lng)
            for j, row in df.iterrows():
                lat2 = df.at[j,'lat']
                lng2 = df.at[j,'lng']
                destination = str(lat2) + ',' +str(lng2)
                cunt += 1
                writer.writerow({'Customer ID': cunt ,'origins': origins, 'destinations': destination})
    print("--------google map data is ready--------")
    

