"""
main_simulation_runner.py
-------------------------
Master runner script to execute SGCV, ALP, and KM simulations,
visualize Δx vs Δt, and compare model histograms.
"""

from sgcv_simulation import run_sgcv_simulation
from alp_simulation import run_alp_simulation
from km_simulation import run_km_simulation
from plot_utils import plot_comparative_histograms, plot_scatter

def main():
    print("Running SGCV simulation...")
    sgcv_data = run_sgcv_simulation()

    print("Running ALP simulation...")
    alp_data = run_alp_simulation()

    print("Running KM simulation...")
    km_data = run_km_simulation()

    print("Generating scatter plots for each model...")
    plot_scatter(sgcv_data, label="SGCV")
    plot_scatter(alp_data, label="ALP")
    plot_scatter(km_data, label="KM")

    print("Generating comparative histograms...")
    plot_comparative_histograms({
        "SGCV": sgcv_data,
        "ALP": alp_data,
        "KM": km_data
    })

if __name__ == "__main__":
    main()
