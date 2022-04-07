import googlemaps
import pandas as pd
from PIL import Image

def visual_full_route():

    df = pd.read_csv('finalroute.csv')

    data = []
    for i, row in df.iterrows():
        lat = df.at[i,'lat']
        lng = df.at[i,'lng']
        lat_lng = str(lat) + ',' + str(lng)
        data.append(lat_lng)

    gmaps = googlemaps.Client(key='AIzaSyBc7_XJXo_asnlXkQhwuQGGnyC6rDXYZVQ')
    waypoints1 = []
    waypoints2 = []
    waypoints3 = []
    for i in range(len(data)):
        if i <= 23:
            waypoints1.append(data[i])
        elif i >= 23 and i <= 45:
            waypoints2.append(data[i])
        elif i >= 45:
            waypoints3.append(data[i])
            
    results1 = gmaps.directions(origin = waypoints1[0],
                                            destination = waypoints1[-1],                                     
                                            waypoints = waypoints1,
                                            optimize_waypoints = True,
    )
    results2 = gmaps.directions(origin = waypoints2[0],
                                            destination = waypoints2[-1],                                     
                                            waypoints = waypoints2,
                                            optimize_waypoints = True,
    )
    results3 = gmaps.directions(origin = waypoints3[0],
                                            destination = waypoints3[-1],                                     
                                            waypoints = waypoints3,
                                            optimize_waypoints = True,
    )
    # for i, leg in enumerate(results1[0]["legs"]):
    #     print("Stop:" + str(i),
    #         leg["start_address"], 
    #         "==> ",
    #         leg["end_address"], 
    #         "distance: ",  
    #         leg["distance"]["value"], 
    #         "traveling Time: ",
    #         leg["duration"]["value"]
    #     )

    markers = ["color:blue|size:mid|label:" + chr(65+i) + "|" 
                    + r for i, r in enumerate(data)]

    marker_points = []
    waypoints = []

    #extract the location points from the previous directions function

    for leg in results1[0]["legs"]:
        leg_start_loc = leg["start_location"]
        marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
        for step in leg["steps"]:
            end_loc = step["end_location"]
            waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
    last_stop = results1[0]["legs"][-1]["end_location"]
    marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')


    for leg in results2[0]["legs"]:
        leg_start_loc = leg["start_location"]
        marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
        for step in leg["steps"]:
            end_loc = step["end_location"]
            waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
    last_stop = results2[0]["legs"][-1]["end_location"]
    marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')

    for leg in results3[0]["legs"]:
        leg_start_loc = leg["start_location"]
        marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
        for step in leg["steps"]:
            end_loc = step["end_location"]
            waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
    last_stop = results3[0]["legs"][-1]["end_location"]
    marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')

    markers = [ "color:blue|size:mid|label:" + chr(65+i) + "|" 
            + r for i, r in enumerate(marker_points)]

    # print(results1)
    # print("--------------------")
    # print(results2)
    # print("--------------------")
    # print(results3)
    # print("--------------------")

    result_map = gmaps.static_map(
                    center = waypoints[0],
                    scale=2, 
                    zoom=10.5,
                    size=[640, 640], 
                    format="jpg", 
                    maptype="roadmap",
                    markers=markers,
                    path="color:0x0000ff|weight:2|" + "|".join(waypoints))

    with open("driving_route_map.jpg", "wb") as img:
        for chunk in result_map:
            img.write(chunk)


    # image = Image.open('driving_route_map.jpg')
    # image.show()
    print("--------visual_full_route finished--------")