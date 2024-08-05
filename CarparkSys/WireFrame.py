# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to create wireframe for mobile view
def create_mobile_wireframe():
    fig, ax = plt.subplots(figsize=(5, 10))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 20)
    ax.axis('off')

    components = [
        ("Header", 0, 19, 5, 1),
        ("Access Parking System", 0, 17, 5, 2),
        ("Reserve Temporary Parking Slot", 0, 15, 5, 2),
        ("Record Parking Slot Information", 0, 13, 5, 2),
        ("Monitor Parking Slot Usage", 0, 11, 5, 2),
        ("Exit Parking Area", 0, 9, 5, 2),
        ("Process Payment for Reserved Slot", 0, 7, 5, 2),
        ("Confirm Payment and Reservation", 0, 5, 5, 2),
        ("Handle External Payment Processing", 0, 3, 5, 2),
        ("Store Auditing Information", 0, 1, 5, 2)
    ]

    for component, x, y, width, height in components:
        ax.add_patch(patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))
        ax.text(x + width / 2, y + height / 2, component, ha='center', va='center', fontsize=10, fontweight='bold')

    plt.title("Mobile View Wireframe", fontsize=14)
    plt.show()

# Function to create wireframe for desktop view
def create_desktop_wireframe():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 16)
    ax.axis('off')

    # Header
    ax.add_patch(patches.FancyBboxPatch((0, 15), 20, 1, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))
    ax.text(10, 15.5, "Header", ha='center', va='center', fontsize=10, fontweight='bold')

    # Left Sidebar
    ax.add_patch(patches.FancyBboxPatch((0, 0), 4, 15, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))
    ax.text(2, 7.5, "Sidebar", ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)

    # Main Content Area
    components = [
        ("Access Parking System", 5, 12, 10, 3),
        ("Reserve Temporary Parking Slot", 5, 9, 10, 3),
        ("Record Parking Slot Information", 5, 6, 10, 3),
        ("Monitor Parking Slot Usage", 5, 3, 10, 3),
        ("Exit Parking Area", 5, 0, 10, 3)
    ]

    for component, x, y, width, height in components:
        ax.add_patch(patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))
        ax.text(x + width / 2, y + height / 2, component, ha='center', va='center', fontsize=10, fontweight='bold')

    plt.title("Desktop View Wireframe", fontsize=14)
    plt.show()

# Create wireframes for mobile and desktop views
create_mobile_wireframe()
create_desktop_wireframe()
