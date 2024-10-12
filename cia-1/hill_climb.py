import matplotlib.pyplot as plt
import networkx as nx

def hill_climbing_dfs_visual(graph, start_node, goal_node, heuristic):
    visited = set()
    parent = {start_node: None}
    found = [False]
    
    pos = nx.spring_layout(graph)
    plt.figure(figsize = (8, 6))

    hill_climbing_dfs_recursive(graph, start_node, goal_node, heuristic, visited, parent, pos, 0, found)
    
    if not found[0]:
        print("Goal node not found!")
    
    plt.show()

def hill_climbing_dfs_recursive(graph, node, goal_node, heuristic, visited, parent, pos, level, found):
    if node not in visited:
        visited.add(node)
        
        draw_graph(graph, visited, pos, level, node)
        
        if node == goal_node:
            found[0] = True
            print(f"Goal node {goal_node} found at level {level}")
            return
        
        neighbors = sorted(graph[node], key = lambda neighbor: heuristic[neighbor])

        for neighbor in neighbors:
            if neighbor not in visited:
                parent[neighbor] = node
                hill_climbing_dfs_recursive(graph, neighbor, goal_node, heuristic, visited, parent, pos, level + 1, found)
                
                if found[0]:
                    return

def draw_graph(graph, visited, pos, level, current_node):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, font_weight = 'bold', edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_nodes(graph, pos, nodelist = [current_node], node_color = 'orange', node_size = 700)
    plt.title(f"Hill Climb Search - Level {level}")
    plt.pause(1)

graph = nx.Graph()
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K')])

heuristic = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 6, 'F': 3, 'G': 2, 'H': 9, 'I': 4, 'J': 1, 'K': 0}

start_node = 'A'
goal_node = 'J'
hill_climbing_dfs_visual(graph, start_node, goal_node, heuristic)

plt.show()
