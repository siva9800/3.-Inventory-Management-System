class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManagement:
    def __init__(self):
        self.inventory = []

    def add_product(self, name, price, quantity):
        self.inventory.append(Product(name, price, quantity))
        print(f"{name} added to inventory.")

    def process_sale(self, name, quantity_sold):
        product = self.find_product(name)
        if product and product.quantity >= quantity_sold:
            product.quantity -= quantity_sold
            print(f"{quantity_sold} units of {name} sold.")
        else:
            print("Product not found or insufficient quantity.")

    def generate_report(self):
        print("Inventory Report:")
        print("-----------------")
        for product in self.inventory:
            print(f"{product.name}: {product.quantity} units (Price: ${product.price:.2f} each)")

    def find_product(self, name):
        for product in self.inventory:
            if product.name == name:
                return product
        return None

    def save_inventory_to_file(self, inventory_data.txt):
        with open('inventory_data.txt', 'w') as file:
            for product in self.inventory:
                file.write(f"{product.name},{product.price},{product.quantity}\n")

    def load_inventory_from_file(self, inventory_data.txt):
        self.inventory = []
        try:
            with open('inventory_data.txt', 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.add_product(name, float(price), int(quantity))
        except FileNotFoundError:
            pass

def main():
    inventory_system = InventoryManagement()

    # Load existing inventory from file (if any)
    inventory_system.load_inventory_from_file("inventory_data.txt")

    while True:
        print("1. Add Product")
        print("2. Process Sale")
        print("3. Generate Report")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            inventory_system.add_product(name, price, quantity)
        elif choice == '2':
            name = input("Enter product name: ")
            quantity_sold = int(input("Enter quantity sold: "))
            inventory_system.process_sale(name, quantity_sold)
        elif choice == '3':
            inventory_system.generate_report()
        elif choice == '4':
            inventory_system.save_inventory_to_file("inventory_data.txt")
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
