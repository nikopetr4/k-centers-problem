import networkx as nx
import itertools
from timeit import default_timer


def k_centers_objective_value(G, centers):
    d = nx.multi_source_dijkstra_path_length(G, centers, weight='weight')
    value = max(d.values())
    return value


def k_centers_brute_force(G, k, time_limit):
    start = default_timer()
    optimal_solution_found = True
    setofcenters = set(G.nodes()) #set of centers
    best_centers = tuple()       #optimal centers
    best_value = float('inf')     #optimal value
    comb = itertools.combinations(setofcenters, k)
    for subset in comb:
        dist = k_centers_objective_value(G, subset)
        if dist < best_value:
            best_value = dist
            best_centers = subset
        duration = default_timer() - start
        # print(f'{duration=}')
        if duration > time_limit:
            # print(f'Time limit exceeded: {time_limit} sec. Exiting ...')
            optimal_solution_found = False
            break

    return best_value, best_centers, optimal_solution_found

k = 3
timelimit = 100
G = nx.read_gexf('graph_0020_07481.gexf', node_type=int)
optVal, optCenters, found = k_centers_brute_force(G, k=k, time_limit = timelimit)
print(optVal, optCenters, found)
#cost, centers = k_centers_brute_force(G, k=k)
#print(cost, centers)