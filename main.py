import networkx as nx
import networkx.algorithms.community as nx_comm

base_network_path = "D:\prace\Vysoka\Semestralka\Base.gexf"

if __name__ == '__main__':
    G = nx.read_gexf(base_network_path)
    communities = nx_comm.louvain_communities(G, seed=42)
