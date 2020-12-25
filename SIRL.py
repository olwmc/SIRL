from typing import List

def make_relation(string):
    # Split string into bytes
    string = list(string)
    
    # Key, info, and children strings
    key = ""
    info = ""
    children = []

    # Get rid of leading (
    string.pop(0)

    # While not separator, add to key
    while(string[0] != "|"):
        key += string[0]
        string.pop(0)

    # Strip l/r whitespace from key
    key = key.strip()

    # Drop |
    string.pop(0)

    # While not ), add to info
    while(string[0] != ")"):
        info += string[0]
        string.pop(0)

    # Strip whitespace
    info = info.strip()
    
    # Buffer for arrow and lead
    buf = ""

    # Get past arrow
    while buf[-2:] != "=>":
        buf += string[0]
        string.pop(0)

    while string[0].isspace():
        string.pop(0)

    children = "".join(string).split(",")
    
    for i in range(len(children)):
        children[i] = children[i].strip()

    return key, info, children


def make_flow(statements):
    """Makes the individual realtions between parent and children nodes"""
    # Temporary "chart"
    chart = {}
    current_statement: list

    """
    For each statement, get its individual parts and decide
    appropriately how to add it to the dictionary
    """
    for statement in statements:
        # Split the statement into individual parts 
        current_statement = make_relation(statement)
        
        # If the statement has 1 child and it's "END", then it's a terminal
        if len(current_statement[2]) == 1 and current_statement[2][0] == "END":
            # Set the terminal key
            chart[current_statement[0]] = current_statement[1]

        # Otherwhise, it's a relation
        else:
            # For each child, replace it with the corresponding chart value
            for i in range(len(current_statement[2])):
                current_statement[2][i] = chart[current_statement[2][i]]

            # Set the new chart as name : info, [children]
            if current_statement[0] not in chart.keys():
                chart[current_statement[0]] = {current_statement[1] : current_statement[2]}
            else :
                chart[current_statement[0]].update({current_statement[1]: current_statement[2]})

    # Return the root chart
    return chart["ROOT"]

def read_chart(file_name):
    """Read file and load in lines ignoring comments and newlines"""
    flow = []
    for line in reversed(open(file_name).readlines()):
        if line[0] != "#" and line.isspace() == False:
            flow.append(line)

    return flow