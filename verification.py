def read_adjacency_matrix(filename: str) -> dict[int, list[int]]:
    graph = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        row = list(map(int, line.strip().split()))
        graph[i + 1] = [j + 1 for j, val in enumerate(row) if val == 1]  

    return graph

