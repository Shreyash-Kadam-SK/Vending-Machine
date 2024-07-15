item_dict = {'cadbury': 5.0, 'chips': 20.0, 'bar': 15.0}

selected_items = {}

def add_to_cart(item, quantity):
    if item in selected_items:
        selected_items[item] += quantity
    else:
        selected_items[item] = quantity

    print(f"\nSelected items: {selected_items}\n")


def remove_from_cart(item, quantity):
    if item in selected_items:
        existing_quantity = selected_items[item]
        if quantity >= existing_quantity:
            del selected_items[item]
            print(f"Removed {existing_quantity} {item} from the list.")
        else:
            selected_items[item] -= quantity
            print(f"Removed {quantity} {item} from the list. {selected_items[item]} {item} remaining.")
    else:
        print(f"{item} is not in the cart.")
    print(f"\nSelected items: {selected_items}\n")

def calculate_total_price(item_dict, selected_items):
    total_price = 0.0
    print(f"\nSelected items: {selected_items}\n")
    for item, quantity in selected_items.items():
        if item in item_dict:
            total_price += item_dict[item] * quantity
    return total_price


# Main Function
while True:
    user_choice = input(f"Choose an item {item_dict} or type 'done' to pay for the chosen items: ")

    if user_choice in item_dict:
        while True:
            user_amount = input(f"Input how many {user_choice} you want in your list: ")
            if user_amount.isdigit():
                user_amount = int(user_amount)
                print(f"Added {user_amount} {user_choice} to the list. If you want to remove any items from your list, type 'remove'.")
                add_to_cart(user_choice,user_amount)
                break
            else:
                print("Please enter a valid amount (a positive integer).")
    elif user_choice == 'remove':
        # Ask for the item and quantity to remove
        item_to_remove = input("Enter the item you want to remove: ")
        quantity_to_remove = int(input("Enter the quantity to remove: "))
        remove_from_cart(item_to_remove, quantity_to_remove)
    elif user_choice == 'done':
        break
    else:
        print("Invalid choice. Please select a valid item or type 'done' to finish.")

total_price_payable = calculate_total_price(item_dict, selected_items)
print(f"Total price payable: ${total_price_payable:}")
