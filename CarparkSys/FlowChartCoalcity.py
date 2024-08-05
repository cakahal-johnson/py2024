# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
#
#
# def add_box(ax, text, position):
#     box = patches.FancyBboxPatch(position, width=30, height=10,
#                                  boxstyle="round,pad=0.3",
#                                  ec="black", fc="lightgrey", alpha=0.5)
#     ax.add_patch(box)
#     ax.text(position[0] + 15, position[1] + 5, text,
#             horizontalalignment='center', verticalalignment='center', fontsize=10, color='black')
#     return box
#
#
# fig, ax = plt.subplots(figsize=(10, 8))
#
# # Set limits and hide axes
# ax.set_xlim(0, 100)
# ax.set_ylim(0, 100)
# ax.axis('off')
#
# # Add boxes
# start_box = add_box(ax, "Start", (30, 90))
# input_box = add_box(ax, "Input Certificate", (30, 70))
# verify_box = add_box(ax, "Verify Certificate", (30, 50))
# result_box = add_box(ax, "Show Result", (30, 30))
# end_box = add_box(ax, "End", (30, 10))
#
#
# # Add arrows
# def add_arrow(ax, start, end):
#     ax.annotate('', xy=end, xytext=start,
#                 arrowprops=dict(facecolor='black', shrink=0.05))
#
#
# add_arrow(ax, (45, 90), (45, 80))
# add_arrow(ax, (45, 70), (45, 60))
# add_arrow(ax, (45, 50), (45, 40))
# add_arrow(ax, (45, 30), (45, 20))
#
# # Save the flowchart as a PNG file
# plt.savefig('/mnt/data/FlowChartCoalcity.png')
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def add_box(ax, text, position):
    box = patches.FancyBboxPatch(position, width=30, height=10,
                                 boxstyle="round,pad=0.3",
                                 ec="black", fc="lightgrey", alpha=0.5)
    ax.add_patch(box)
    ax.text(position[0] + 15, position[1] + 5, text,
            horizontalalignment='center', verticalalignment='center', fontsize=10, color='black')
    return box


fig, ax = plt.subplots(figsize=(10, 8))

# Set limits and hide axes
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Add boxes (you can customize the positions and labels)
start_box = add_box(ax, "Start", (30, 90))
input_box = add_box(ax, "Input Certificate", (30, 70))
verify_box = add_box(ax, "Verify Certificate", (30, 50))
result_box = add_box(ax, "Show Result", (30, 30))
end_box = add_box(ax, "End", (30, 10))

# Save the flowchart as a PNG file
plt.savefig('FlowChartCoalcity.png')
plt.show()
