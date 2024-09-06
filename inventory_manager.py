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


def delete_product():
    """Deletes a product from the inventory."""
    name = input("Enter the product name to delete: ")
    inventory = load_inventory()

    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        print(f"Product {name} deleted successfully.")
    else:
        print(f"Product {name} not found in the inventory.")


def list_inventory():
    """Lists all products in the inventory."""
    inventory = load_inventory()
    if not inventory:
        print("No products in the inventory.")
        return
    print("\nCurrent Inventory:")
    for name, details in inventory.items():
        print(f"Product: {name}, Quantity: {details['quantity']}, Price: ${details['price']}")


def main():
    while True:
        print("\nInventory Manager")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. List Inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            list_inventory()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
