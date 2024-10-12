import matplotlib.pyplot as plt
import networkx as nx
from heapq import heappop, heappush

def a_star_search(graph, start_node, goal_node, heuristic):
    extended_list = set()
    priority_queue = []

    heappush(priority_queue, (heuristic[start_node], 0, [start_node]))

    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))

    while priority_queue:
        f_value, g_value, path = heappop(priority_queue)
        current_node = path[-1]

        draw_graph(graph, path, extended_list, pos, f_value)

        if current_node == goal_node:
            print(f"Goal node {goal_node} reached with total cost {g_value}")
            break

        extended_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in extended_list:
                edge_cost = graph[current_node][neighbor]['weight']
                new_g_value = g_value + edge_cost
                f_value = new_g_value + heuristic[neighbor]
                new_path = path + [neighbor]
                heappush(priority_queue, (f_value, new_g_value, new_path))

    if goal_node not in path:
        print("Goal node not found!")

    plt.show()

def draw_graph(graph, path, extended_list, pos, f_value):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(extended_list), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_edges(graph, pos, edgelist = [(path[i], path[i + 1]) for i in range(len(path) - 1)], width = 2, edge_color = 'orange')
    nx.draw_networkx_nodes(graph, pos, nodelist = path, node_color = 'orange', node_size = 700)
    plt.title(f"A* Search - : {f_value}")
    plt.pause(1)

graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 2), ('A', 'C', 4), ('B', 'D', 3), ('B', 'E', 6), ('C', 'F', 5), ('C', 'G', 2), ('D', 'H', 4), ('E', 'I', 3), ('F', 'J', 2), ('G', 'K', 7)])

heuristic = {'A': 10, 'B': 8, 'C': 6, 'D': 7, 'E': 4, 'F': 3, 'G': 5, 'H': 9, 'I': 2, 'J': 0, 'K': 1}

start_node = 'A'
goal_node = 'J'
a_star_search(graph, start_node, goal_node, heuristic)

plt.show()
