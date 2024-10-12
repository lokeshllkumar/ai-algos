import matplotlib.pyplot as plt
import networkx as nx
from heapq import heappop, heappush

def branch_and_bound_visual(graph, start_node, goal_node):
    visited = set()
    priority_queue = []
    heappush(priority_queue, (0, [start_node]))
    pos = nx.spring_layout(graph)
    plt.figure(figsize = (8, 6))
    
    while priority_queue:
        cumulative_cost, path = heappop(priority_queue)
        current_node = path[-1]
        
        draw_graph(graph, path, visited, pos, cumulative_cost)
        
        if current_node == goal_node:
            print(f"Goal node {goal_node} reached with cost {cumulative_cost}")
            break

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                edge_cost = graph[current_node][neighbor]['weight']
                new_path = path + [neighbor]
                new_cost = cumulative_cost + edge_cost
                heappush(priority_queue, (new_cost, new_path))
    
    if goal_node not in path:
        print("Goal node not found!")

    plt.show()

def draw_graph(graph, path, visited, pos, cost):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color  ='lightblue', node_size = 700)
    nx.draw_networkx_edges(graph, pos, edgelist = [(path[i], path[i + 1]) for i in range(len(path) - 1)], width = 2, edge_color = 'orange')
    nx.draw_networkx_nodes(graph, pos, nodelist = path, node_color = 'orange', node_size = 700)
    plt.title(f"Branch and Bound - Cumulative Cost: {cost}")
    plt.pause(1)

graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 2), ('A', 'C', 4), ('B', 'D', 7), ('B', 'E', 1), ('C', 'F', 3), ('C', 'G', 5), ('D', 'H', 2), ('E', 'I', 6), ('F', 'J', 4), ('G', 'K', 8)])

start_node = 'A'
goal_node = 'J'
branch_and_bound_visual(graph, start_node, goal_node)

plt.show()
