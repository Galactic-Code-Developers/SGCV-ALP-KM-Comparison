# SGCV/ALP/KM Comparison
## Project Codename "Condor"

A unified simulation and analysis framework comparing three dark photon production models:

- **SGCV**: Superluminal Graviton Condensate Vacuum  
- **ALP**: Axion-Like Particle scenario  
- **KM**: Kaluza–Klein photon excitations  

---

## 📁 Project Structure

```
SGCV_ALP_KM_Comparison/
│
├── SGCV_ALP_KM_Comparison_v_e31ca7f9.ipynb     # Colab notebook
├── main_simulation_runner.py                  # Main orchestrator
├── sgcv_simulation.py                         # SGCV model
├── alp_simulation.py                          # ALP model
├── km_simulation.py                           # Kaluza–Klein model
├── event_generator.py                         # Higgs → γγ + γ′ event generator
├── plot_utils.py                              # Plotting functions
├── detector_geometry.gdml                     # Detector geometry file
├── requirements.txt                           # Python dependencies
├── __init__.py                                # Package initializer
├── LICENSE                                    # (Optional: MIT / GPL)
└── README.md                                  # Project description
```

---

## 🔧 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Galactic-Code-Developers/SGCV_ALP_KM_Comparison.git
cd SGCV_ALP_KM_Comparison
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the simulation from the notebook or terminal:

```bash
python main_simulation_runner.py
```

---

## 📊 Output

- Δx vs Δt scatter plots  
- Overlaid histograms for SGCV, ALP, and KM  
- Model comparison visuals for publication and export

---

## 📄 License

MIT License

Copyright (c) 2025 [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
