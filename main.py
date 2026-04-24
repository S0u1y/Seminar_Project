import networkx as nx
import networkx.algorithms.community as nx_comm
import csv
import numpy as np

import matplotlib.pyplot as plt

import timeit


base_network_path = "..\\Base.gexf"

def get_naive_communities():
    G = nx.read_gexf(base_network_path)
    communities = nx_comm.louvain_communities(G, seed=42)
    return communities

def show_plot(callback):
    callback()
    plt.show()
    plt.close()

if __name__ == '__main__':
    # Numerical labels. Actual label names are in labelidx2arxivcategory
    labels_file = "..\\ogbn-arxiv\\raw\\node-label.csv"

    with open(labels_file, "r") as file:
        content = np.array(list(csv.reader(file)), dtype=np.int8)

    unique_counts = np.unique_counts(content).counts

#   Let's use the labels as "ground truth" for checking topological community's accuracy.

    # plt.bar(x=np.unique(content), height=unique_counts)
    # print(timeit.timeit(lambda: max(unique_counts)))
    # print(timeit.timeit(lambda: unique_counts.max())) # Is faster
    plt.hist(content, bins=40)
    plt.show()
    plt.close()

    print(unique_counts.argmax()) # Computer Vision has the most entries.

    plt.title("test")
    plt.boxplot(unique_counts, tick_labels="n")
    plt.show()
    plt.close()

