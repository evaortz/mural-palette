from mural_analyzer.core.pipeline import analyze_image
from mural_analyzer.core.circle_packing import pack_circles
import matplotlib.pyplot as plt
import matplotlib.patches as patches


palette_info = analyze_image("assets/samples/sketch1.jpeg")
palette_circles_info = pack_circles(palette_info)
fig, ax = plt.subplots()

for circle_item in palette_circles_info:
    circle = circle_item["circle"]
    r, g, b = circle_item["rgb"]
    color = (r/255, g/255, b/255)
    circle_patch = patches.Circle((circle["x"], circle["y"]), radius=circle["r"], color=color)
    ax.add_patch(circle_patch)



ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")
ax.axis('off')
plt.savefig("assets/samples/test_circle.png")