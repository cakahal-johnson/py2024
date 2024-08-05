import matplotlib

matplotlib.use('TkAgg')  # Use TkAgg backend for interactive display
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_flowchart_with_summaries():
    fig, ax = plt.subplots(figsize=(20, 15))

    # Set limits and remove axes
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 18)
    ax.axis('off')

    # Define updated positions and summaries for each component
    updated_positions_with_summaries = {
        "Access Parking System": (1, 14),
        "Reserve Temporary Parking Slot": (1, 11),
        "Record Parking Slot Information": (4, 10),
        "Monitor Parking Slot Usage": (7, 10),
        "Exit Parking Area": (10, 14),
        "Process Payment for Reserved Slot": (10, 11),
        "Confirm Payment and Reservation": (13, 14),
        "Handle External Payment Processing": (13, 11),
        "Store Auditing Information": (10, 8),
        "Reviews": (7, 6),
        "Customer Services": (4, 14),
    }

    summaries = {
        "Access Parking System": "Users (students, staff, and visitors) access the parking system to locate available temporary parking slots.",
        "Reserve Temporary Parking Slot": "Users can reserve a parking slot through the web application.",
        "Record Parking Slot Information": "The system records details of the reserved parking slot, including the user's information and reservation time.",
        "Monitor Parking Slot Usage": "The system monitors the usage of the parking slots to ensure compliance with the reservation and to gather data for auditing purposes.",
        "Exit Parking Area": "Users exit the parking area after using the reserved slot.",
        "Process Payment for Reserved Slot": "The system processes payments for the reserved parking slots, either at the time of reservation or upon exit.",
        "Confirm Payment and Reservation": "The system sends confirmation details for both payment and reservation to the user.",
        "Handle External Payment Processing": "The system manages payments through third-party payment services.",
        "Store Auditing Information": "The system stores auditing information, including reservation and payment details, for future reference and compliance.",
        "Reviews": "Users can leave reviews and feedback about their parking experience.",
        "Customer Services": "Users can contact customer services for assistance with reservations, payments, or any other issues.",
    }

    # Add rectangles and text for each component
    for label, (x, y) in updated_positions_with_summaries.items():
        width = 2.5 if "Service" in label else 3
        height = 1
        ax.add_patch(patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.3", edgecolor='black',
                                            facecolor='lightgrey'))
        ax.text(x + width / 2, y + height / 2, label, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(x + width / 2, y - 0.7, summaries[label], ha='center', va='center', fontsize=8, wrap=True,
                bbox=dict(facecolor='white', edgecolor='none'))

    # Define the connections between updated components
    updated_connections_with_summaries = [
        ("Access Parking System", "Reserve Temporary Parking Slot"),
        ("Reserve Temporary Parking Slot", "Record Parking Slot Information"),
        ("Record Parking Slot Information", "Monitor Parking Slot Usage"),
        ("Exit Parking Area", "Process Payment for Reserved Slot"),
        ("Process Payment for Reserved Slot", "Confirm Payment and Reservation"),
        ("Confirm Payment and Reservation", "Handle External Payment Processing"),
        ("Process Payment for Reserved Slot", "Store Auditing Information"),
        ("Monitor Parking Slot Usage", "Store Auditing Information"),
        ("Exit Parking Area", "Reviews"),
        ("Access Parking System", "Customer Services"),
        ("Reserve Temporary Parking Slot", "Customer Services"),
        ("Process Payment for Reserved Slot", "Customer Services"),
        ("Reviews", "Customer Services"),
    ]

    # Add arrows for each connection
    for start, end in updated_connections_with_summaries:
        start_x, start_y = updated_positions_with_summaries[start]
        end_x, end_y = updated_positions_with_summaries[end]
        ax.annotate('', xy=(end_x + 1.5, end_y + 0.5), xytext=(start_x + 1.25, start_y + 0.5),
                    arrowprops=dict(arrowstyle="->", color='black'))

    # Display the updated diagram with summaries
    plt.title("Temporary Parking Slot Management System Flowchart", fontsize=16)
    plt.show()


# Create the flowchart with summaries
create_flowchart_with_summaries()
