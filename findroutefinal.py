from latlng import find_lat_lng
from googlecsv import create_date_for_google_map
from googleway import find_distance_matrix
from googleshortest import find_shortest_path
from finalroutevisual import visual_full_route
from getfinalroutewaypoints import print_out_waypoints

find_lat_lng()
print("--------find_lat_lng success")
create_date_for_google_map()
print("--------create_date_for_google_map success")
find_distance_matrix()
print("--------find_distance_matrix success")
find_shortest_path()
print("--------find_shortest_path success")
visual_full_route()
print("--------visual_full_route success")
print_out_waypoints()
print("--------visual_full_route success")






