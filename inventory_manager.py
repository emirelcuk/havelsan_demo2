# inventory_manager.py
import json

DATA_FILE = 'inventory_data.json'


def load_inventory():
    """Loads inventory data from a JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_inventory(data):
    """Saves inventory data to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def add_product():
    """Adds a new product to the inventory."""
    name = input("Enter product name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input for quantity or price.")
        return

    inventory = load_inventory()
    if name in inventory:
        print(f"Product {name} already exists. Use update option.")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        save_inventory(inventory)
        print(f"Product {name} added successfully.")


def update_product():
    """Updates the details of an existing product."""
    name = input("Enter the product name to update: ")
    inventory = load_inventory()

    if name in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
        except ValueError:
            print("Invalid input for quantity or price.")
            return

        inventory[name] = {'quantity': quantity, 'price': price}
        save_inventory(inventory)
        print(f"Product {name} updated successfully.")
    else:
        print(f"Product {name} not found in the inventory.")








if __name__ == "__main__":
    main()
