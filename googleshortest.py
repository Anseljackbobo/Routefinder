from re import S
import pandas as pd
import numpy as np
from queue import PriorityQueue
import csv
def find_shortest_path():
    # read data from csv file
    df = pd.read_csv('googledistance.csv')

    data = []
    for i, row in df.iterrows():
        distance = df.at[i,'Distance']
        data.append(distance)

    array = np.array(data)
    reshaped1 = array.reshape((55,55))

    from ortools.constraint_solver import routing_enums_pb2
    from ortools.constraint_solver import pywrapcp


    def create_data_model():
        """Stores the data for the problem."""
        data = {}
        data['distance_matrix'] = reshaped1
        data['num_vehicles'] = 1
        data['depot'] = 54
        return data


    def print_solution(manager, routing, solution):
        """Prints solution on console."""
        # print('Objective: {} ms'.format(solution.ObjectiveValue()))
        distance = solution.ObjectiveValue()
        index = routing.Start(0)
        plan_output = ''
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += '{},'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += '{}'.format(manager.IndexToNode(index))
        route = plan_output
        # plan_output += 'Route distance: {}m\n'.format(route_distance)
        return distance, route


    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                            data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        result = print_solution(manager, routing, solution)

    # generate the final route seuqence csv
    outputstring = 'The total distance of the Route is ' + str(result[0]/1000) + ' km'
    print(outputstring)
    df2 = pd.read_csv('Routeplus.csv')
    pathsequence  = result[1].split(',')
    print(type(pathsequence))

    id_list = []
    for i in pathsequence:
        id_list.append(int(i))
        

    with open('finalroute.csv', 'w', newline='') as csvfile:
        fieldnames = ['order','Customer_ID', 'lat', 'lng']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        cunt = -1
        for i in id_list:
            lat = df2.at[i,'lat']
            lng = df2.at[i,'lng']
            ID = df2.at[i,'Customer ID']
            cunt += 1
            writer.writerow({'order' : cunt, 'Customer_ID': ID ,'lat': lat, 'lng': lng})

    with open('finalrouteforjson.csv', 'w', newline='') as csvfile:
        fieldnames = ['location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        cunt = -1
        for i in id_list:
            lat = df2.at[i,'lat']
            lng = df2.at[i,'lng']
            lat_lng = str(lat) + ',' + str(lng)
            cunt += 1
            # stopover = bool(True)
            writer.writerow({'location' : lat_lng})
        
        print("Shortest Path Found")
    
    print("--------find_shortest_path finished--------")

            
        
