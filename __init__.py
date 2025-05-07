# __init__.py

"""
SGCV_ALP_KM_Comparison Package

Includes simulation models for:
- SGCV: Superluminal Graviton Condensate Vacuum
- ALP: Axion-Like Particle
- KM: Kaluza–Klein photon excitations

Modules:
- sgcv_simulation: SGCV model simulation
- alp_simulation: ALP model simulation
- km_simulation: Kaluza–Klein model simulation
- event_generator: Higgs → γγ + γ′ MC generation
- plot_utils: Visualization helpers
- visualize_geometry: Detector geometry renderer
"""

from . import sgcv_simulation
from . import alp_simulation
from . import km_simulation
from . import event_generator
from . import plot_utils
from . import visualize_geometry
