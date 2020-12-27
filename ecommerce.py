class Customer:
    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("Out of stock!")

        else:
            print("We don't have that product!")

    def print_purchases(self):
        print("Customer has purchased!")
        for item in self.purchases :
            print(item.name)



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory .items():
            print(key.name + ':'+ str(value))
        print()

customer = Customer('Hitesh', 'hiteshk@gmail.com')
#print(customer.name)
#print(customer.email)

smart_watch = Product('noise colorfit', 2000)
#print(smart_watch.name)
#print(smart_watch.price)

mac_book = Product('MacBook pro', 120000)

inventory = Inventory()
inventory.add_product(smart_watch,100)
#inventory.print_inventory()
inventory.add_product(mac_book,350)

inventory.print_inventory()
customer.purchase(inventory, smart_watch)
customer.purchase(inventory, mac_book)
inventory.print_inventory()
customer.print_purchases()
