import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive display
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_flowchart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Define the components of the flowchart with their summaries
    components = [
        ("Access Parking System", 3, 10, 10, 1, "User logs into the parking system via the web application."),
        ("Locate Available Parking Slot", 3, 8.5, 10, 1, "System provides available parking slots based on user's location."),
        ("Reserve Parking Slot", 3, 7, 10, 1, "User reserves a selected parking slot temporarily."),
        ("Record Parking Slot Information", 3, 5.5, 10, 1, "System records details of the reserved parking slot."),
        ("Monitor Parking Slot Usage", 3, 4, 10, 1, "System monitors the usage status of the reserved parking slot."),
        ("Exit Parking Area", 3, 2.5, 10, 1, "User exits the parking area after using the slot."),
        ("Process Payment", 3, 1, 10, 1, "System processes the payment for the reserved parking slot.")
    ]

    # Add the components to the plot
    for component, x, y, width, height, summary in components:
        ax.add_patch(patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))
        ax.text(x + width / 2, y + height / 2, component, ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(x + width + 1, y + height / 2, summary, ha='left', va='center', fontsize=10, fontstyle='italic')

    # Add arrows
    arrow_properties = dict(facecolor='black', edgecolor='black', width=0.5, headwidth=5, shrink=0.1)
    for i in range(len(components) - 1):
        ax.annotate('', xy=(8, components[i+1][2] + 1), xytext=(8, components[i][2] + 1), arrowprops=arrow_properties)

    plt.title("Temporary Parking Slot Management System Flowchart", fontsize=16)
    plt.show()


# Create the flowchart
create_flowchart()
