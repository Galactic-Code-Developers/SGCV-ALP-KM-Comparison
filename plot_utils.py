# plot_utils.py

import matplotlib.pyplot as plt
import numpy as np

def plot_delta_x_vs_delta_t(delta_x, delta_t, model_name="Model", save_path=None):
    """
    Scatter plot of Δx vs Δt for a given model.

    Parameters:
    - delta_x: Array of spatial displacements [m]
    - delta_t: Array of time displacements [s]
    - model_name: String to label the model
    - save_path: If provided, saves the plot to this path
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(delta_t, delta_x, alpha=0.5, s=10, label=f'{model_name}')
    plt.xlabel("Δt [s]")
    plt.ylabel("Δx [m]")
    plt.title(f"Δx vs Δt - {model_name}")
    plt.grid(True)
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()


def plot_histogram_comparison(models_data, bins=50, observable="Δx", units="m", save_path=None):
    """
    Plot overlaid histograms of an observable (Δx or Δt) across models.

    Parameters:
    - models_data: List of tuples (data_array, model_name)
    - bins: Number of histogram bins
    - observable: 'Δx' or 'Δt'
    - units: Units for the axis label
    - save_path: Optional path to save the figure
    """
    plt.figure(figsize=(10, 6))
    for data, name in models_data:
        plt.hist(data, bins=bins, alpha=0.5, label=name, histtype='stepfilled')

    plt.xlabel(f"{observable} [{units}]")
    plt.ylabel("Counts")
    plt.title(f"{observable} Distribution Across Models")
    plt.legend()
    plt.grid(True)
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()


def compare_all_delta_x_and_t(delta_x_dict, delta_t_dict, bins=50):
    """
    Generate side-by-side histograms for Δx and Δt across all models.

    Parameters:
    - delta_x_dict: Dict with model names as keys and Δx arrays as values
    - delta_t_dict: Dict with model names as keys and Δt arrays as values
    """
    # Δx comparison
    models_x = [(delta_x_dict[key], key) for key in delta_x_dict]
    plot_histogram_comparison(models_x, bins=bins, observable="Δx", units="m")

    # Δt comparison
    models_t = [(delta_t_dict[key], key) for key in delta_t_dict]
    plot_histogram_comparison(models_t, bins=bins, observable="Δt", units="s")

