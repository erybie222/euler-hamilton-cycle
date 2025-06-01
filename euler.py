from typing import Set

def find_euler_cycle(graph: dict[int , list[int]]) -> list[int]:
    g = {u: list(neigh) for u, neigh in graph.items()}

    stack = []
    cycle = []

    start = 1
    stack.append(start)

    while stack:
        v = stack[-1]
        if g[v]:
            u = g[v].pop(0)  
            g[u].remove(v)
            stack.append(u)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]
