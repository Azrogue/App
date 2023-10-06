import networkx as nx
import matplotlib.pyplot as plt
import random

class DisjointSet:
    def __init__(self, elements):
        self.parent = {element: element for element in elements}

    def union(self, element1, element2):
        parent1 = self.find(element1)
        parent2 = self.find(element2)
        if parent1 != parent2:
            self.parent[parent1] = parent2

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

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

def kruskal(G):
    # Créez une copie du graphe pour travailler dessus
    G_copy = G.copy()
    # Triez les arêtes par poids (dans ce cas, nous supposons que le poids est 1 pour toutes les arêtes)
    edges = list(G_copy.edges(data=True))
    edges.sort(key=lambda x: x[2].get('weight', 1))
    # Créez un nouveau graphe pour stocker l'arbre couvrant minimal
    MST = nx.Graph()
    # Ajoutez les nœuds au MST
    MST.add_nodes_from(G_copy.nodes(data=True))
    # Utilisez un ensemble disjoint pour suivre les composantes connectées
    ds = DisjointSet(G_copy.nodes())
    for u, v, data in edges:
        # Si l'ajout de cette arête ne crée pas de cycle
        if ds.find(u) != ds.find(v):
            # Ajoutez l'arête au MST
            MST.add_edge(u, v, attr_dict=data)
            # Fusionnez les ensembles contenant u et v
            ds.union(u, v)
    return MST


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
        G = kruskal(G)
        draw_network(G)

if __name__ == "__main__":
    main()
