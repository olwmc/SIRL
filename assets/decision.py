from SIRL import *

chart = make_flow(read_chart("donut.txt"))

def do_paths(chart):
    # Keys of the chart
    keys = chart.keys()
    
    # List of keys
    key_list = list(keys)
    
    # Current dict entry
    current = chart[key_list[0]] 

    # Print off root node
    print(key_list[0])

    # While there's still more dict to traverse
    while(type(current[0]) == dict):

        # First traverse through all single nodes and
        # display their contents
        while len(current) < 2:
        
            keys = current[0].keys()
            key_list = list(keys)
            current = current[0][key_list[0]]
        
            print(key_list[0])
        
        # Once we've gone through all the single
        # nodes, make a temp dict for the first
        # branching one
        temp = {}
        for d in current:
            temp.update(d)
        
        # Print out the keys
        for key in temp.keys():
            print("\t" + key)
       
        # Get user input on keys
        path = input("> ")

        # Set new current
        current = temp[path]

    # Print out final node
    print(current[0])
do_paths(chart)
