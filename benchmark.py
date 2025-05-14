import time
from graph_generator import generate_graph
from euler import find_euler_cycle
from hamilton import find_hamilton_cycle

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    result = end - start
    return result

def run_experiments(density: float):
    ns = list(range(100, 1500, 100))
    times_euler = []
    times_hamilton = []

    for n in ns:
         print(f"n = {n}, density = {density}")
         graph = generate_graph(n , density, seed=42 + n)

         t1 = measure_time(find_euler_cycle, graph)
         t2 = measure_time(find_hamilton_cycle, graph)

         times_euler.append(t1)
         times_hamilton.append(t2)

    return ns, times_euler, times_hamilton
