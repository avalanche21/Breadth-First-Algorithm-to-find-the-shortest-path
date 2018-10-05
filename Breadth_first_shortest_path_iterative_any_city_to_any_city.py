# libraries
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
########## Store the data in a dataframe
df = pd.DataFrame([['NY', 'Chicago', 1000],
                    ['Chicago', 'Denver', 1000],
                    ['NY', 'Toronto', 800],
                    ['NY', 'Denver', 1900],
                    ['Toronto', 'Calgary', 1500],
                    ['Toronto', 'LA', 1800],
                    ['Toronto', 'Chicago', 500],
                    ['Denver', 'Urbana', 1000],
                    ['Denver', 'Houston', 1500],
                    ['Houston', 'LA', 1500],
                    ['Denver', 'LA', 1000],],
                    columns = ['city1','city2','distance'])
# Construct a graph using MultiDiGraph from NetworkX library
G= nx.from_pandas_edgelist(df, 'city1', 'city2', edge_attr=['distance'],
                                    create_using=nx.MultiDiGraph())
#print(len(G))
print(G.nodes())
print(G.edges(data=True))
# Draw the graph showing the City Names (Nodes) and Distances (Attributes)
edge_labels = nx.get_edge_attributes(G,'distance')
pos = nx.spring_layout(G)
nx.draw(G,pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos, labels = edge_labels)
#plt.show()
####################################################################################
# Start the algorithm by finding "NY" in the data frame (both city 1 and city2)
# Create the lists to store the information
# frontiers List is the list we are going to explore


# For this problem, we will set Origin = "NY", Destination = "LA"
Origin = 'Calgary'
Destination = 'Chicago'

frontiers = []
# explored List is the list we have already visited and will never visit again
explored = [Origin]
# path memory List is the history of each path we have visited from city to city
path_memory= [[Origin]]
# final_path List is the path we have reached the destination (from "NY" to "LA")
final_path=[]


print(df)

break_outer_loop = False
n = 1
while True:
    if len(path_memory)>0 and Destination in path_memory[-1]:
        break
    if break_outer_loop == True:
        break
    print("#######################iteration", n,"############################")
    #now the frontiers list from last iteration became the explored list for the new iterations
    explored = explored + frontiers
    # clear the frontier List for this new iteration
    frontiers = []

    print("explored list :",explored)
    print("path_memory list :",path_memory)

    # try tp explored every frontiers, starting from the left hand side
    # if we find the path to LA, we will break the loop
    #break_outer_loop = False
    for k in range(0,len(explored)):
        if break_outer_loop == True:
            break
        for i in range(0, df.shape[0]):
            print("check1")
            if df["city2"][i] not in explored:
                print("check2")
                # if we see "LA", it means we have reached our destination, so we can break the loop
                # when this condition happen, we will update the path and break both inner loop and outer loop
                if df["city1"][i] == explored[k] and df["city2"][i] == Destination:
                    print("check3")
                    frontiers.append(df["city2"][i])
                    for m in range(0,len(path_memory)):
                        if df['city1'][i] == path_memory[m][-1]:
                            xxx = path_memory[m].copy()
                            path_memory.append(xxx)
                            path_memory[m].append(df['city2'][i])
                            print("final path is...",path_memory[m])
                            final_path = path_memory[m]

                    break_outer_loop = True
                    print("break")
                    break
                elif df["city1"][i] == explored[k] and df["city2"][i] != Destination:
                    frontiers.append(df['city2'][i])
                    for m in range(0,len(path_memory)):
                        if df['city1'][i] == path_memory[m][-1]:
                            xxx = path_memory[m].copy()
                            path_memory.append(xxx)
                            path_memory[m].append(df['city2'][i])
            if df["city1"][i] not in explored:
                if df["city2"][i] == explored[k] and df["city1"][i] == Destination:
                    frontiers.append(df["city1"][i])
                    for m in range(0,len(path_memory)):
                        if df['city2'][i] == path_memory[m][-1]:
                            xxx = path_memory[m].copy()
                            path_memory.append(xxx)
                            path_memory[m].append(df['city1'][i])
                            print("final path is...",path_memory[m])
                            final_path = path_memory[m]

                    break_outer_loop = True
                    print("break")
                    break
                elif df["city2"][i] == explored[k] and df["city1"][i] != Destination:
                    frontiers.append(df['city1'][i])
                    for m in range(0,len(path_memory)):
                        if df['city2'][i] == path_memory[m][-1]:
                            xxx = path_memory[m].copy()
                            path_memory.append(xxx)
                            path_memory[m].append(df['city1'][i])


    n += 1
print("frontiers list :", frontiers)
print("path_memory list :",path_memory)


print("########################## RESULT ################################")
print("final path is...",final_path)

# calculate the total cost of the trip cost
total_cost = 0

for i in range (0,len(final_path)-1):
    for k in range (0,df.shape[0]):
        if df["city1"][k] == final_path[i] and df["city2"][k] == final_path[i+1]:
            total_cost = total_cost + df['distance'][k]
            print("cost:",df['distance'][k]," from ",final_path[i],"to",final_path[i+1])

        elif df["city2"][k] == final_path[i]and df["city1"][k] == final_path[i+1]:
            total_cost = total_cost + df['distance'][k]
            print("plus:", df['distance'][k])
print("total_cost = ",total_cost)


# show the network graph
plt.show()











