# event_generator.py

import numpy as np

def higgs_to_photons_and_darkphoton(n_events=10000, m_h=125.0, m_dp=1.0, eps=1e-3):
    """
    Simulates Higgs decays into two visible photons and one dark photon γ'.

    Parameters:
    - n_events: Number of events to generate.
    - m_h: Higgs boson mass (GeV).
    - m_dp: Dark photon mass (GeV).
    - eps: Kinetic mixing parameter (ε), dimensionless.

    Returns:
    - photons: 4-momenta of two visible photons [n_events x 2 x 4]
    - dark_photons: 4-momenta of dark photons [n_events x 4]
    - metadata: Dictionary of event parameters
    """
    c = 3e8  # speed of light in m/s
    photons = np.zeros((n_events, 2, 4))       # E, px, py, pz for each visible photon
    dark_photons = np.zeros((n_events, 4))     # E, px, py, pz for γ'

    for i in range(n_events):
        # Decay kinematics
        E_dp = np.random.uniform(low=m_dp + 0.1, high=m_h / 2.0)
        E_photon = (m_h - E_dp) / 2.0

        # Generate random angles
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2 * np.pi)

        # Photon 1 momentum
        px1 = E_photon * np.sin(theta) * np.cos(phi)
        py1 = E_photon * np.sin(theta) * np.sin(phi)
        pz1 = E_photon * np.cos(theta)
        photons[i, 0] = [E_photon, px1, py1, pz1]

        # Photon 2 momentum (back-to-back)
        photons[i, 1] = [E_photon, -px1, -py1, -pz1]

        # Dark photon momentum: isotropic
        theta_dp = np.random.uniform(0, np.pi)
        phi_dp = np.random.uniform(0, 2 * np.pi)
        p_dp = np.sqrt(E_dp**2 - m_dp**2)
        px_dp = p_dp * np.sin(theta_dp) * np.cos(phi_dp)
        py_dp = p_dp * np.sin(theta_dp) * np.sin(phi_dp)
        pz_dp = p_dp * np.cos(theta_dp)
        dark_photons[i] = [E_dp, px_dp, py_dp, pz_dp]

    metadata = {
        "n_events": n_events,
        "m_h": m_h,
        "m_dp": m_dp,
        "eps": eps,
        "description": "Higgs → γγ + γ′ event generator"
    }

    return photons, dark_photons, metadata

# Example usage
if __name__ == "__main__":
    photons, dark_photons, meta = higgs_to_photons_and_darkphoton()
    print(f"Generated {meta['n_events']} events.")
    print("Example photon 4-momentum:", photons[0])
    print("Example dark photon 4-momentum:", dark_photons[0])

