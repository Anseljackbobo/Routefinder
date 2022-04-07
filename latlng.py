import pandas as pd
import requests
import json

def find_lat_lng():
    df = pd.read_csv("Route.csv")
    pd.set_option('display.max_rows', None)

    for i, row in df.iterrows():
        apiAddress = str(df.at[i,'Address'])+','+str(df.at[i,'City'])+','+str(df.at[i,'State'])+','+str(df.at[i,'Zip'])
        
        parameters = {
            "key": "wBNilxOAgvC15cuUpeFA2MhDJ2JxKtYM",
            "location": apiAddress
        }

        response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
        data = response.text
        dataJ = json.loads(data)['results']
        lat = (dataJ[0]['locations'][0]['latLng']['lat'])
        lng = (dataJ[0]['locations'][0]['latLng']['lng'])
        
        df.at[i,'lat'] = lat
        df.at[i,'lng'] = lng
        
    df.to_csv('Routeplus.csv')
    print("--------find_lat_lng is succesful--------")