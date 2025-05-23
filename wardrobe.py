import os

wardrobe = []

def load_wardrobe():
    """Load wardrobe items from the text file."""
    global wardrobe
    wardrobe = []
    if os.path.exists("wardrobe.txt"):
        with open("wardrobe.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    item = {
                        "name": parts[0],
                        "type": parts[1],
                        "color": parts[2],
                        "occasion": parts[3].split(";"),
                        "weather": parts[4].split(";")
                    }
                    wardrobe.append(item)

def save_wardrobe():
    """Save wardrobe items to the text file."""
    with open("wardrobe.txt", "w") as f:
        for item in wardrobe:
            occasions = ";".join(item["occasion"])
            weathers = ";".join(item["weather"])
            f.write(f"{item['name']},{item['type']},{item['color']},{occasions},{weathers}\n")

# Load wardrobe on module import
load_wardrobe()

def manage_wardrobe():
    """Main menu for wardrobe management."""
    print("\n===== Wardrobe Management (Style Companion) =====")
    print("1. Add Item")
    print("2. View Wardrobe")
    print("3. Delete Item")
    print("4. Return to Main Menu")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        add_clothing()
    elif choice == "2":
        view_wardrobe()
    elif choice == "3":
        delete_clothing()
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

    # Save wardrobe after any change
    save_wardrobe()

def add_clothing():
    """Add a new clothing item to the wardrobe."""
    item = {}
    item["name"] = input("Item name: ")
    item["type"] = input("Type (Top/Bottom/Shoes/Accessory): ")
    item["color"] = input("Color: ")
    item["occasion"] = input("Suitable occasions (separated by semicolon): ").split(";")
    item["weather"] = input("Suitable weather (separated by semicolon): ").split(";")

    wardrobe.append(item)
    print(f"{item['name']} has been added to your wardrobe.")

def view_wardrobe():
    """Display all items in the wardrobe."""
    if not wardrobe:
        print("Your wardrobe is empty.")
        return

    print("\nYour Wardrobe:")
    for i, item in enumerate(wardrobe):
        print(f"{i+1}. {item['color']} {item['name']} ({item['type']})")

def delete_clothing():
    """Delete a clothing item from the wardrobe."""
    view_wardrobe()
    if not wardrobe:
        return

    try:
        index = int(input("Enter the number of the item to delete: ")) - 1
        if 0 <= index < len(wardrobe):
            removed = wardrobe.pop(index)
            print(f"{removed['name']} has been deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def get_wardrobe():
    """Return the current wardrobe list."""
    return wardrobe