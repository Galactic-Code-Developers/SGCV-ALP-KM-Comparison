# sgcv_simulation.py

import numpy as np
import matplotlib.pyplot as plt

def generate_sgcv_events(n_events=10000, mass_dp=0.1, epsilon=1e-4, velocity_superluminal=1.0001):
    """
    Simulates SGCV-induced dark photon emissions.
    
    Parameters:
    - n_events: Number of events to simulate.
    - mass_dp: Dark photon mass in GeV.
    - epsilon: Kinetic mixing parameter.
    - velocity_superluminal: Superluminal speed ratio (v/c).
    
    Returns:
    - delta_x: Array of spatial displacement values (in meters).
    - delta_t: Array of temporal displacement values (in picoseconds).
    """
    c = 3e8  # Speed of light in m/s

    # Random event generation
    energies = np.random.exponential(scale=10, size=n_events)  # GeV
    angles = np.random.uniform(0, np.pi, size=n_events)

    # Superluminal velocity contribution
    velocities = velocity_superluminal * c * np.ones(n_events)

    # Time delay: t = d / v for each particle (in seconds)
    delta_t = np.random.normal(loc=1e-10, scale=5e-12, size=n_events)  # seconds
    delta_t_ps = delta_t * 1e12  # convert to picoseconds

    # Distance traveled: x = vt (in meters)
    delta_x = velocities * delta_t  # in meters

    return delta_x, delta_t_ps

def plot_sgcv_distribution(delta_x, delta_t_ps):
    """
    Plots Δx vs Δt distribution and histogram.
    """
    plt.figure(figsize=(12, 5))

    # Scatter plot
    plt.subplot(1, 2, 1)
    plt.scatter(delta_t_ps, delta_x, alpha=0.4, s=2)
    plt.title("SGCV Δx vs Δt")
    plt.xlabel("Δt (ps)")
    plt.ylabel("Δx (m)")

    # Histograms
    plt.subplot(1, 2, 2)
    plt.hist(delta_t_ps, bins=50, alpha=0.7, label="Δt (ps)")
    plt.hist(delta_x, bins=50, alpha=0.7, label="Δx (m)")
    plt.legend()
    plt.title("SGCV Δx and Δt Distributions")

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    x_vals, t_vals = generate_sgcv_events()
    plot_sgcv_distribution(x_vals, t_vals)
