import matplotlib.pyplot as plt
import networkx as nx
from heapq import heappop, heappush

def best_first_search(graph, start_node, goal_node, heuristic):
    visited = set()
    priority_queue = []

    heappush(priority_queue, (heuristic[start_node], [start_node]))

    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))

    while priority_queue:
        h_value, path = heappop(priority_queue)
        current_node = path[-1]

        draw_graph(graph, path, visited, pos, h_value)

        if current_node == goal_node:
            print(f"Goal node {goal_node} reached with path: {path}")
            break

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                heappush(priority_queue, (heuristic[neighbor], new_path))

    if goal_node not in path:
        print("Goal node not found!")

    plt.show()

def draw_graph(graph, path, visited, pos, h_value):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_edges(graph, pos, edgelist = [(path[i], path[i + 1]) for i in range(len(path) - 1)], width = 2, edge_color = 'orange')
    nx.draw_networkx_nodes(graph, pos, nodelist = path, node_color = 'orange', node_size = 700)
    plt.title(f"Best-First Search -  {h_value}:")
    plt.pause(1)

graph = nx.Graph()
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K')])

heuristic = {'A': 10, 'B': 8, 'C': 6, 'D': 7, 'E': 4, 'F': 3, 'G': 5, 'H': 9, 'I': 2, 'J': 0, 'K': 1}

start_node = 'A'
goal_node = 'J'
best_first_search(graph, start_node, goal_node, heuristic)

plt.show()
