import sys

def get_items():
    items = {}
    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        if not item.strip():
            print("Item cannot be blank. Please enter a non-empty item.")
            continue
        quantity = input(f"Enter the quantity of {item}: ")
        items[item] = int(quantity)
    return items

def display_items(items):
    print("Items and their quantities:")
    for item, quantity in items.items():
        print(f"{item}: {quantity}")

items = get_items()
display_items(items)
sys.exit(0)
