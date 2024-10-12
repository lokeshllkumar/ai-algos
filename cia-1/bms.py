import matplotlib.pyplot as plt
import networkx as nx

def exhaustive_search(graph, start_node, goal_node):
    all_paths = []
    visited = set()
    pos = nx.spring_layout(graph)

    def explore_path(current_node, path):
        path.append(current_node)
        visited.add(current_node)

        visualize_graph(graph, path, visited, pos)

        if current_node == goal_node:
            all_paths.append(list(path))
        else:
            for neighbor in graph[current_node]:
                if neighbor not in path:
                    explore_path(neighbor, list(path))

    explore_path(start_node, [])

    print(f"All paths from {start_node} to {goal_node}:")
    for i, path in enumerate(all_paths):
        print(f"Path {i + 1}: {path}")

    plt.show()

def visualize_graph(graph, path, visited, pos):
    plt.clf()
    nx.draw(graph, pos, with_labels = True, node_color = 'lightgray', node_size = 500, font_size = 10, edge_color = 'gray')
    nx.draw_networkx_nodes(graph, pos, nodelist = list(visited), node_color = 'lightblue', node_size = 700)
    nx.draw_networkx_edges(graph, pos, edgelist = [(path[i], path[i + 1]) for i in range(len(path) - 1)], width = 2, edge_color = 'orange')
    nx.draw_networkx_nodes(graph, pos, nodelist = path, node_color = 'orange', node_size = 700)
    plt.pause(1)

graph = nx.Graph()
graph.add_edges_from([
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('D', 'H'), ('E', 'I'),
    ('F', 'J'), ('G', 'K')
])

start_node = 'A'
goal_node = 'J'
exhaustive_search(graph, start_node, goal_node)
