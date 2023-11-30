#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

def destCity(paths): #This function creates sets for outgoing and incoming cities and then finds the city without an outgoing path by taking the set difference (incoming_cities - outgoing_cities)
    outgoing_cities = set()
    incoming_cities = set()

    # Create sets of outgoing and incoming cities
    for path in paths: #Starts a 'for' loop that iterates through each path in the list of paths 
        outgoing_cities.add(path[0]) #In each iterates, the first city is added to the outgoing cities and the second city is added to the incoming cities
        incoming_cities.add(path[1])

    # Find the city without outgoing path
    destination_city = incoming_cities - outgoing_cities #This line calculates the set difference between 'incoming cities' and 'outgoing cities' and gives a set containing cites with incoming paths without outgoing paths 

    return destination_city.pop() #Retreives and recovers inconsistent elements from the set 

# Example usage:
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
result = destCity(paths)
print(result)
