# SGCV ALP KM Comparison

## Overview

This repository provides a simulation framework for comparing three dark photon generation models within high-energy physics experiments:

- **SGCV**: Superluminal Graviton Condensate Vacuum — a novel framework with Lorentz-invariant superluminal segments.
- **ALP**: Axion-Like Particle models — representing pseudoscalar extensions that couple to photons.
- **KM**: Kaluza–Klein excitations of the photon in compactified extra dimensions.

Each model simulates the rare Higgs decay channel:  
**H → γγ′**, where γ′ is a dark photon or exotic vector particle.

## Features

- 🧮 **Monte Carlo generator** for Higgs decays: `event_generator.py`
- 📐 **Detector geometry** using a simplified GDML for ATLAS/SHiP: `detector_geometry.gdml`
- ⏱️ **Simulation modules** for:
  - SGCV (`sgcv_simulation.py`)
  - ALP (`alp_simulation.py`)
  - KM (`km_simulation.py`)
- 📊 **Visualization** of Δx vs Δt and histograms via `plot_utils.py`
- 🔀 **Integrated execution** in `main_simulation_runner.py`
- 📓 **Jupyter notebook** version for Colab: `SGCV_ALP_KM_Comparison_v_e31ca7f9.ipynb`

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/SGCV_ALP_KM_Comparison.git
cd SGCV_ALP_KM_Comparison
pip install -r requirements.txt
