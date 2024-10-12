import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs_visual(graph, start_node, goal_node):
    visited = set()
    queue = deque([start_node])
    level = 0
    parent = {start_node: None}
    found = False
    
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    
    while queue:
        level_size = len(queue)        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node not in visited:
                visited.add(node)                
                draw_graph(graph, visited, pos, level, node)
                if node == goal_node:
                    found = True
                    print(f"Goal node {goal_node} found at level {level}")
                    return
                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        parent[neighbor] = node
        level += 1

    if not found:
        print("Goal node not found!")

def draw_graph(graph, visited, pos, level, current_node):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, font_weight = 'bold', edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_nodes(graph, pos, nodelist = [current_node], node_color = 'orange', node_size = 700)    
    plt.title(f"BFS - Level {level}")
    plt.pause(1)

graph = nx.Graph()
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K')])

start_node = 'A'
goal_node = 'J'
bfs_visual(graph, start_node, goal_node)

plt.show()