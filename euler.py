def find_euler_cycle(graph: dict[int , Set[int]]) -> list[int]:
    g = {u: set(neigh) for u, neigh in graph.items()}

    stack = []
    cycle = []

    start = next(iter(g))
    stack.append(start)

    while stack:
        v= stack[-1]
        if g[v]:
            u = g[v].pop()
            g[u].remove(v)
            stack.append(u)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]