from verification import read_adjacency_matrix
from euler import find_euler_cycle
from hamilton import find_hamilton_cycle

graph = read_adjacency_matrix('euler.txt')

euler_cycle = find_euler_cycle(graph)

hamilton_cycle = find_hamilton_cycle(graph)

# Wypisujemy
print("Euler : ")
print(" ".join(map(str, euler_cycle)))
print("\nHamilton:")
print(" ".join(map(str, hamilton_cycle)))
