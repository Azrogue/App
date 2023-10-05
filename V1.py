import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_network(topology_type, num_nodes):
    if topology_type == 1:  # Ring topology
        G = nx.cycle_graph(num_nodes)
    elif topology_type == 2:  # Hierarchical topology
        G = nx.balanced_tree(2, num_nodes-2)
    elif topology_type == 3:  # Bus topology
        G = nx.path_graph(num_nodes)
    elif topology_type == 4:  # Star topology
        G = nx.star_graph(num_nodes-1)
    elif topology_type == 5:  # Line topology
        G = nx.path_graph(num_nodes)
    elif topology_type == 6:  # Mesh topology
        G = nx.complete_graph(num_nodes)
    else:
        print("Invalid topology type")
        return None

    return G

def draw_network(G):
    nx.draw(G, with_labels=True)
    plt.show()

def main():
    print("Choose the network topology type:")
    print("1. Ring")
    print("2. Hierarchical")
    print("3. Bus")
    print("4. Star")
    print("5. Line")
    print("6. Mesh")
    
    topology_type = int(input())
    
    print("Enter the number of nodes (between 3 and 30):")
    num_nodes = int(input())
    
    if num_nodes < 3 or num_nodes > 30:
        print("Invalid number of nodes")
        return
    
    G = generate_network(topology_type, num_nodes)
    
    if G is not None:
        draw_network(G)

if __name__ == "__main__":
    main()
