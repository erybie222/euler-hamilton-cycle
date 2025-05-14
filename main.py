from benchmark import run_experiments
from plot import plot_results

def main():
    for density in [0.3 , 0.7]:
        ns, times_euler, times_hamilton = run_experiments(density)
        plot_results(ns, times_euler, times_hamilton, density)

if __name__ == "__main__":
    main()