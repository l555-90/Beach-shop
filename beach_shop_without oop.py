# Welcome message
print("Hello sunshine! Welcome to the Beach Shop! We've got all the seaside essentials waiting for you.")

# Get user name
name = input("Can I have your name: ").strip()
print(f"Thank you, {name.title()}!")

# Get age safely
try:
    age = int(input("How old are you?: "))
    if age <= 0:
        print("Invalid age. Please enter a valid age.")
    elif age >= 18:
        print("You are an adult. Feel free to explore all our products!")
    else:
        print("You are a minor. You might need parental guidance for some products.")
except ValueError:
    print("Invalid input for age. Please enter a number.")

shop_now = input("Would you like to look around and shop (yes/no): ").strip().lower()
if shop_now != "yes":
    print("No worries! Thanks for visiting. Enjoy your day at the beach.")
else:
    # Product sections
    beach_products = {
        "mat": 10,
        "beach tube": 15,
        "floaty": 20,
        "umbrella": 25,
        "life guard": 50
    }

    skin_products = {
        "sunscreen": 12,
        "aloe vera gel": 8,
        "lip balm": 5,
        "face wash": 15,
        "body lotion": 20
    }

    overall_grand_total = 0
    main_shopping = "yes"

    while main_shopping == "yes":
        print("\nWhat can we help you find today?")
        print("1. Beach Products")
        print("2. Skin Products")
        print("3. Dress")

        section_choice = input("Choose 1, 2 or 3: ").strip().lower()

        if section_choice in ["1", "beach products"]:
            products = beach_products
            section_name = "Beach Products"
        elif section_choice in ["2", "skin products"]:
            products = skin_products
            section_name = "Skin Products"
        elif section_choice == "3":
            print("Dress section coming soon!")
            continue
        else:
            print("Invalid section. Try again.")
            continue

        cart = {}
        section_total = 0
        shopping = "yes"

        while shopping == "yes":
            print(f"\nAvailable {section_name}:")
            for item, price in products.items():
                print(f"{item} : ${price}")

            choice = input(f"\nEnter product name: ").strip().lower()

            if choice in products:
                try:
                    qty = int(input(f"Enter quantity of {choice}: "))
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue
                except ValueError:
                    print("Invalid quantity. Enter a number.")
                    continue

                price = products[choice] * qty
                section_total += price

                cart[choice] = cart.get(choice, 0) + qty

                print(f"Price of {qty} {choice} → ${price}")
            else:
                print("Invalid choice! Please select again.")

            shopping = input(f"Buy more from {section_name}? (yes/no): ").strip().lower()

        print(f"\n--- {section_name} Receipt ---")
        for item, qty in cart.items():
            total_item_price = qty * products[item]
            print(f"{item} | Quantity: {qty} | Total: ${total_item_price}")

        print(f"Total for {section_name}: ${section_total}")
        overall_grand_total += section_total

        main_shopping = input("Shop another section? (yes/no): ").strip().lower()

    print(f"\n--- Grand Total: ${overall_grand_total} ---")
    print("Goodbye! Have a nice day!")