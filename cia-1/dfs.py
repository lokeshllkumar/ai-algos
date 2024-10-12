import matplotlib.pyplot as plt
import networkx as nx

def dfs_visual(graph, start_node, goal_node):
    visited = set()
    parent = {start_node: None}
    found = [False]
    
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))

    dfs_recursive(graph, start_node, goal_node, visited, parent, pos, 0, found)
    
    if not found[0]:
        print("Goal node not found!")
    
    plt.show()

def dfs_recursive(graph, node, goal_node, visited, parent, pos, level, found):
    if node not in visited:
        visited.add(node)
        
        draw_graph(graph, visited, pos, level, node)
        
        if node == goal_node:
            found[0] = True
            print(f"Goal node {goal_node} found at level {level}")
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                dfs_recursive(graph, neighbor, goal_node, visited, parent, pos, level + 1, found)
                
                if found[0]:
                    return

def draw_graph(graph, visited, pos, level, current_node):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, font_weight = 'bold', edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_nodes(graph, pos, nodelist = [current_node], node_color = 'orange', node_size = 700)
    plt.title(f"DFS Traversal - Level {level}")
    plt.pause(1)

graph = nx.Graph()
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'),('D', 'H'), ('E', 'I'),('F', 'J'), ('G', 'K')])

start_node = 'A'
goal_node = 'J'
dfs_visual(graph, start_node, goal_node)

plt.show()
