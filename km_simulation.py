# km_simulation.py

import numpy as np
import matplotlib.pyplot as plt

def generate_km_events(n_events=10000, radius=1e-18, max_mode=10):
    """
    Simulates events for Kaluza–Klein photon excitations in Higgs → γ + γ*_n decays.

    Parameters:
    - n_events: Number of events to simulate.
    - radius: Compactification radius R (in meters).
    - max_mode: Highest KK mode n to include.

    Returns:
    - delta_x: Array of spatial displacements (in meters).
    - delta_t: Array of temporal displacements (in picoseconds).
    """
    c = 3e8  # m/s
    hbar = 6.582e-25  # GeV·s
    n_vals = np.random.randint(1, max_mode + 1, n_events)

    # KK mass: m_n = n / R
    masses_kk = n_vals / (radius * 5.068e15)  # convert meters to GeV⁻¹

    # Sample energy spectrum from truncated normal above threshold
    energies = np.random.uniform(low=masses_kk + 1, high=150, size=n_events)  # GeV

    # Boost γ
    gamma = energies / masses_kk
    lifetimes = hbar / masses_kk  # τ ~ ħ / m

    decay_times = np.random.exponential(scale=lifetimes, size=n_events)
    decay_lengths = gamma * c * decay_times  # meters
    delta_t = decay_lengths / (gamma * c)  # seconds
    delta_t_ps = delta_t * 1e12  # ps

    return decay_lengths, delta_t_ps

def plot_km_distribution(delta_x, delta_t_ps):
    """
    Plots Δx vs Δt distribution and histograms for KK model.
    """
    plt.figure(figsize=(12, 5))

    # Scatter plot
    plt.subplot(1, 2, 1)
    plt.scatter(delta_t_ps, delta_x, alpha=0.4, s=2, c="green")
    plt.title("KM Δx vs Δt")
    plt.xlabel("Δt (ps)")
    plt.ylabel("Δx (m)")

    # Histograms
    plt.subplot(1, 2, 2)
    plt.hist(delta_t_ps, bins=50, alpha=0.7, label="Δt (ps)", color="green")
    plt.hist(delta_x, bins=50, alpha=0.7, label="Δx (m)", color="navy")
    plt.legend()
    plt.title("KM Δx and Δt Distributions")

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    x_vals, t_vals = generate_km_events()
    plot_km_distribution(x_vals, t_vals)
