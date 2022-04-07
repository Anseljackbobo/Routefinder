import pandas as pd

def print_out_waypoints():
    df = pd.read_csv('finalrouteforjson.csv')

    data = []
    for i, row in df.iterrows():
        location = df.at[i,'location']
        data.append(location)
    # print(data)
    # output = ''
    # for i in data:
    #     output += '{location:"'+ str(i) + '", stopover: true},'
    # print(output)
    waypoints1 = ''
    waypoints2 = ''
    waypoints3 = ''
    for i in range(len(data)):
        if i <= 23:
            waypoints1 += '{location:"'+ str(data[i]) + '", stopover: true},'
        elif i >= 23 and i <= 45:
            waypoints2 += '{location:"'+ str(data[i]) + '", stopover: true},'
        elif i >= 45:
            waypoints3 += '{location:"'+ str(data[i]) + '", stopover: true},'

    print(waypoints1)
    print('-----------------------------------------')
    print(waypoints2)
    print('-----------------------------------------')
    print(waypoints3) 
    print('-----------------------------------------')
    
    output_file = open('waypoints1.txt', 'w')
    for i in waypoints1:
        output_file.write(i)

    output_file.close()
    
    output_file = open('waypoints2.txt', 'w')
    for i in waypoints2:
        output_file.write(i)

    output_file.close()
    
    output_file = open('waypoints3.txt', 'w')
    for i in waypoints3:
        output_file.write(i)

    output_file.close()
    
    print("--------print_out_waypoints finished--------")