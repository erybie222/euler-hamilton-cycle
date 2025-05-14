import matplotlib.pyplot as plt
import os

def plot_results(ns, times_euler, times_hamilton, density):
    os.makedirs("plots", exist_ok=True)

    plt.figure()
    plt.plot(ns, times_euler, label= "Euler")
    plt.plot(ns, times_hamilton, label= "Hamilton")
    plt.title(f"Czas działania algorytmów (nasycenie {int(density * 100)}%)")
    plt.xlabel("Liczba wierzchołków (n)")
    plt.ylabel("Czas [s]")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/wykres_{int(density * 100)}.png")
    plt.show()