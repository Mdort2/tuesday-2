# Function to print the Taco Palace Menu
def display_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


# Function to retrieve the price of a given food item
def get_price(item_name):
    prices = {
        "Taco": 4.95,
        "Burrito": 6.50,
        "Nachos": 5.50,
        "Soft Drink": 2.50
    }
    return prices.get(item_name, 0.0)


def main():
    # Welcome message
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    # Lists and variables to track the order
    ordered_items = []
    total_price = 0.0

    # Mapping selection numbers to clean display names for user confirmation
    menu_mapping = {
        1: "Taco",
        2: "Burrito",
        3: "Nachos",
        4: "Drink"  # Matches the example output format ("You selected a Drink")
    }

    # Mapping selection numbers to internal names for price retrieval
    price_mapping = {
        1: "Taco",
        2: "Burrito",
        3: "Nachos",
        4: "Soft Drink"
    }

    # Main application loop
    while True:
        display_menu()

        try:
            choice = int(input("\nUser entered: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            break
        elif choice in menu_mapping:
            item_display = menu_mapping[choice]
            item_real_name = price_mapping[choice]

            # Print selection confirmation
            print(f"You selected a {item_display}")

            # Save ordered item and update total price using the function
            ordered_items.append(item_display)
            total_price += get_price(item_real_name)
        else:
            print("Invalid selection. Please choose an option from 1 to 5.")

    # Format and print the final order summary when quitting
    if ordered_items:
        if len(ordered_items) == 1:
            items_str = ordered_items[0]
        elif len(ordered_items) == 2:
            items_str = f"{ordered_items[0]} and a {ordered_items[1]}"
        else:
            # Commas for 3 or more items
            items_str = ", ".join(ordered_items[:-1]) + f", and a {ordered_items[-1]}"

        print(f"\nYou ordered a {items_str}. Your total is ${total_price:.2f}")
    else:
        print(f"\nYou did not order anything. Your total is ${total_price:.2f}")


if __name__ == "__main__":
    main()
