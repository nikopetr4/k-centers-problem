import networkx as nx
import random


def k_centers_objective_value(G, centers):
    d = nx.multi_source_dijkstra_path_length(G, centers, weight='weight')
    value = max(d.values())
    return value


def k_centers_greedy(G, k, first_center=None):
    centers = []
    if first_center is None:
        length_center = len(G) - 1
        first_center = random.randint(0, length_center)
    centers.append(first_center)
    index = None
    while len(centers) < k:
        max_distance_from_center = float('-inf')
        if len(centers) > 1:
            for node in G.nodes():
                distance_from_center = list()
                for center in centers:
                    if node == center:
                        distance_from_center.append(0)
                    else:
                        distance_from_center.append(int(G[node][center]['weight']))
                min_dist = min(distance_from_center)
                if min_dist > max_distance_from_center:
                    max_distance_from_center = min_dist
                    index = node
        else:
            max_weight = float('-inf')
            for node in G.nodes():
                if node not in centers:
                    if G[node][centers[0]]['weight'] > max_weight:
                        max_weight = G[node][first_center]['weight']
                        index = node
        centers.append(index)
    cost = k_centers_objective_value(G, centers)
    return cost, centers

k = 3
G020 = nx.read_gexf('graph_0020_07481.gexf', node_type=int)
cost, centers = k_centers_greedy(G020, k = k)
print(cost)
print(centers)