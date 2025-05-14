from typing import Dict , Set, List, Optional

def find_hamilton_cycle(graph: Dict[int, Set[int]]) -> Optional[List[int]]:
    n = len(graph)
    path = []

    def dfs(v, visited):
        path.append(v)
        if len(path) == n:
            if path[0] in graph[v]:
                path.append(path[0])
                return True
            else:
                path.pop()
                return False
            
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                if dfs(u, visited):
                    return True
                visited.remove(u)

        path.pop()
        return False
    
    for start in graph:
        path.clear()
        if dfs(start, {start}):
            return path
    
    return None