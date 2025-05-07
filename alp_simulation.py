# alp_simulation.py

import numpy as np
import matplotlib.pyplot as plt

def generate_alp_events(n_events=10000, mass_alp=0.05, coupling=1e-3, decay_constant=1e4):
    """
    Simulates events for Axion-Like Particles (ALPs) in Higgs → γ + a.

    Parameters:
    - n_events: Number of events to simulate.
    - mass_alp: ALP mass in GeV.
    - coupling: Effective photon–ALP coupling strength.
    - decay_constant: Decay constant scale (in GeV).

    Returns:
    - delta_x: Array of spatial displacement values (in meters).
    - delta_t: Array of temporal displacement values (in picoseconds).
    """
    c = 3e8  # m/s

    # Energy spectrum: exponential falloff in ALP energy
    energies = np.random.exponential(scale=20, size=n_events)  # in GeV

    # ALP lifetime (in seconds), assuming boosted decay: τ = f² / (m³ × g²)
    lifetimes = decay_constant**2 / (mass_alp**3 * coupling**2)
    decay_times = np.random.exponential(scale=lifetimes, size=n_events)

    # Boost factor γ ~ E/m
    gamma = energies / mass_alp
    decay_lengths = c * decay_times * gamma  # meters

    # Time in lab frame
    delta_t = decay_lengths / (c * gamma)  # seconds
    delta_t_ps = delta_t * 1e12  # convert to picoseconds

    return decay_lengths, delta_t_ps

def plot_alp_distribution(delta_x, delta_t_ps):
    """
    Plots Δx vs Δt distribution and histograms for ALP model.
    """
    plt.figure(figsize=(12, 5))

    # Scatter plot
    plt.subplot(1, 2, 1)
    plt.scatter(delta_t_ps, delta_x, alpha=0.4, s=2, c="darkorange")
    plt.title("ALP Δx vs Δt")
    plt.xlabel("Δt (ps)")
    plt.ylabel("Δx (m)")

    # Histograms
    plt.subplot(1, 2, 2)
    plt.hist(delta_t_ps, bins=50, alpha=0.7, label="Δt (ps)", color="darkorange")
    plt.hist(delta_x, bins=50, alpha=0.7, label="Δx (m)", color="royalblue")
    plt.legend()
    plt.title("ALP Δx and Δt Distributions")

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    x_vals, t_vals = generate_alp_events()
    plot_alp_distribution(x_vals, t_vals)
