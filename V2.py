import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_mesh_network(num_nodes):
    # Vérifiez que le nombre de nœuds est dans la plage spécifiée
    if num_nodes < 3 or num_nodes > 30:
        raise ValueError("Le nombre de nœuds doit être entre 3 et 30.")
    
    G = nx.Graph()
    
    # Ajoutez les nœuds au graphe
    G.add_nodes_from(range(1, num_nodes + 1))
    
    # Créez une liste de nœuds terminaux pour l'Arbre de Steiner
    terminal_nodes = list(G.nodes())
    
    # Générez l'arbre de Steiner minimal pour les nœuds terminaux
    steiner_tree = generate_steiner_tree(G, terminal_nodes)
    
    # Ajoutez les liens de l'arbre de Steiner au graphe
    G.add_edges_from(steiner_tree.edges())
    
    # Ajoutez des liaisons supplémentaires pour chaque nœud
    for node in G.nodes():
        num_links = random.randint(1, 4)
        neighbors = list(G.neighbors(node))
        
        while len(neighbors) < num_links:
            possible_neighbors = [n for n in G.nodes() if n != node and n not in neighbors]
            if possible_neighbors:
                neighbor = random.choice(possible_neighbors)
                G.add_edge(node, neighbor)
                neighbors.append(neighbor)
    
    return G

def generate_steiner_tree(graph, terminal_nodes):
    steiner_tree = nx.algorithms.approximation.steiner_tree(graph, terminal_nodes)
    return steiner_tree

if __name__ == "__main__":
    num_nodes = int(input("Entrez le nombre de nœuds (entre 3 et 30) : "))
    
    if num_nodes < 3 or num_nodes > 30:
        print("Le nombre de nœuds doit être entre 3 et 30.")
    else:
        mesh_network = generate_mesh_network(num_nodes)
        nx.draw(mesh_network, with_labels=True, node_color='lightblue', font_weight='bold')
        plt.show()