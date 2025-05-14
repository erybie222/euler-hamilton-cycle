import random
from collections import defaultdict
from typing import Dict, Set
def generate_graph(n: int , density:float , seed=None)-> dict[int, Set[int]]:
    if seed is not None:
        random.seed(seed)
    
    graph = defaultdict(set)
    edges = set()

    nodes = list(range(n))
    random.shuffle(nodes)

    for i in range(n):
        u = nodes[i]
        v = nodes[(i+1) % n]
        graph[u].add(v)
        graph[v].add(u)
        edges.add(tuple(sorted((u,v))))

    e_max = n * (n-1) // 2
    e_target = int(density * e_max)

    while len(edges) < e_target:
        u, v = random.sample(range(n), 2)
        a , b = min(u,v), max(u, v)
        if b not in graph[a]:
            graph[a].add(b)
            graph[b].add(a)
            edges.add((a,b))

    odd_degree_nodes = [v for v in range(n) if len(graph[v]) % 2 == 1]

    while len(odd_degree_nodes) >= 2:
        u = odd_degree_nodes.pop()
        for v in odd_degree_nodes:
            if v!=u and v not in graph[u]:
                graph[u].add(v)
                graph[v].add(u)
                edges.add(tuple(sorted((u, v))))
                odd_degree_nodes.remove(v)
                break
    return graph