import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_detector_layers():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Define layers with radii and colors
    layers = [
        {"radius": 2.0, "color": "cyan", "label": "Tracker"},
        {"radius": 4.0, "color": "orange", "label": "ECAL"},
        {"radius": 6.0, "color": "red", "label": "HCAL"}
    ]

    for layer in layers:
        circle = patches.Circle((0, 0), layer["radius"], edgecolor='black',
                                facecolor=layer["color"], alpha=0.5, label=layer["label"])
        ax.add_patch(circle)

    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    ax.set_aspect('equal')
    ax.set_title("Simplified Layered Detector Geometry")
    ax.legend(loc="upper right")
    plt.grid(True)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()

if __name__ == "__main__":
    visualize_detector_layers()
