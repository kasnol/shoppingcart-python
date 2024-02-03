import uuid


# Global Variables
current_shoppingcart = []
current_user = None
current_sessionid = None

# ANSI escape codes for some color output
COLOR_ATTENTION = '\033[91m' # Color for Errors / Issues
COLOR_HIGHLIGHT = '\033[92m' # Color for highlight certain wordings
COLOR_ACTION = '\033[33m' # Color for for actions done
COLOR_NORMAL = '\033[0m'  # Normal Color 
COLOR_ADMIN_MENU = '\033[96m' # Admin Menu Colors
COLOR_USER_MENU = '\033[36m' # User Menu Colors


### Part A Shopping Cart Login Functions

#   A welcome message should initially be displayed in the e-commerce application, such as "Welcome to the Demo Marketplace".
def display_welcome_msg():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL
    print(COLOR_HIGHLIGHT + "-------------------------------------------------")
    print("-- Welcome to the Demo Marketplace             --")
    print("------------------------------------------------- \n"  + COLOR_NORMAL)

#   User Login Prompts  
def display_login():
    global current_user, current_shoppingcart, current_sessionid

    while True:
        username = input("Please input your username : ")
        password = input("Please input your password : ")
        # Check credentials and display role
        user = lookup_user(username, password)
        if user:
            current_user = user
            current_sessionid = create_login_sessionid()
            if get_user_attribute("user_role") == "A":
                display_admin_menu()
            elif get_user_attribute("user_role") == "U":
                display_user_menu()
            break
        else:
            print(COLOR_ATTENTION + "Wrong username or password combination" + COLOR_NORMAL)
            print("------------------------------------------------- \n")

#   A common function to get user details after login
def get_user_attribute(attribute):
    global current_user
    return current_user[attribute]


#   A common function for Session ID generation, for simplicity, use system generated UUID as session ID
def create_login_sessionid():
        return str(uuid.uuid4())

#   A common function to authen users for login
def lookup_user(username, password):
    for user in user_database.users:  
        if user['user_name'] == username and user['user_password'] == password:
            return user
    return None



### Part B Admin Functions

#   Admin User Main Menu
def display_admin_menu():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL, current_user

# make sure the user is a valid user, and role is admin
    if not current_user or current_user['user_role'] != 'A':
        print(COLOR_ATTENTION + "Your Access is denied. You must be an admin to access this menu." + COLOR_NORMAL)
        return  # Exit the function if the user is not an admin

    while current_user:
        print(COLOR_ADMIN_MENU + "-------------------------------------------------")
        print("-- Admin Menu")
        print("-- Login Session ID: ", current_sessionid)
        print("-------------------------------------------------"+COLOR_NORMAL)
        print("-- Choose an option below: \n")
        print("-- 1. Manage Product Catalogue ")
        print("-- 2. Manage Product Category ")
        print("-- Q. Logout ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-2, or 'Q' ): ")
            
        if option == '1':
            display_admin_manage_product_menu()
        elif option == '2':
            display_admin_manage_product_category()
        elif option.upper() == 'Q':
            print(COLOR_ACTION + "Logging out now, see you next time !" + COLOR_NORMAL)
            current_sessionid = None
            current_user = None  
            break
        else:
            print(COLOR_ATTENTION + "Invalid option. Please enter a valid option (1-2, or 'Q')" + COLOR_NORMAL)

# Admin Manage Product & Menu
def display_admin_manage_product_menu():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL
    while True:
        print(COLOR_ADMIN_MENU + "-------------------------------------------------")
        print("-- Admin: Manage Product Catalogue")
        print("-- Login Session ID: ", current_sessionid)
        print("-------------------------------------------------"+COLOR_NORMAL)
        print("-- Choose an option below: \n")
        print("-- 1. Display Current Products in Catalogue ")
        print("-- 2. Add New Product to Catalogue ")
        print("-- 3. Modify existing product in Catalogue ")
        print("-- 4. Remove existing Product from Catalogue ")
        print("-- B. Back to Admin Main Menu ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-4, or B): ")

        if option == '1':
            product_catalogue.display_product_catalogue()
        elif option == '2':
            admin_add_product()
        elif option == '3':
            # Implement modify product functionality (not provided in script)
            admin_modify_product()
        elif option == '4':
            admin_remove_product()
        elif option.upper() == 'B':
            break
        else:
            print(COLOR_ATTENTION + "Invalid option. Please enter a valid option (1-4, or 'B')" + COLOR_NORMAL)

#   Admin Manage Product Category & Menu
def display_admin_manage_product_category():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL
    while True:
        print(COLOR_ADMIN_MENU + "-------------------------------------------------")
        print("-- Admin: Manage Product Category")
        print("-- Login Session ID: ", current_sessionid)
        print("-------------------------------------------------"+COLOR_NORMAL)
        print("-- Choose an option below: \n")
        print("-- 1. Display Current Product Categories ")
        print("-- 2. Add a New Category ")
        print("-- 3. Modify an existing Category ")
        print("-- 4. Remove an existing Category ")
        print("-- B. Back to Admin Menu ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-4, or B): ")
        if option == '1':
            product_category.display_existing_category()
        elif option == '2':
            admin_add_category()
        elif option == '3':
            admin_modify_category()
        elif option == '4':
            admin_remove_category()
        elif option.upper() == 'B':
            break
        else:
            print(COLOR_ATTENTION + "Invalid option. Please enter a valid option (1-4, or 'B')" + COLOR_NORMAL)

#   Admin: Common function to display current list of category
def admin_display_existing_category():
    global product_category, COLOR_HIGHLIGHT, COLOR_NORMAL

    print(COLOR_HIGHLIGHT + "-------------------------------------------------")
    print("-- Current Product Categories")
    print("-------------------------------------------------" + COLOR_NORMAL)

    # Check if there are any categories
    if not product_category.categories:
        print(COLOR_ATTENTION + "No categories available." + COLOR_NORMAL)
        return

    # Table headers
    header = "| {0:<15} | {1:<30} |".format("Category ID", "Category Name")
    print(header)
    print("-" * len(header))

    # Table rows
    for category in product_category.categories:
        row = "| {category_id:<15} | {category_name:<30} |".format(**category)
        print(row)
    print("-------------------------------------------------")
    
#   Admin: function to add a new category
def admin_add_category():
    global product_category, COLOR_ATTENTION, COLOR_ACTION, COLOR_NORMAL
    print(COLOR_ADMIN_MENU + "-------------------------------------------------")
    print("-- Admin Menu: Add a New Category")
    print("-------------------------------------------------" + COLOR_NORMAL)

    while True:
        category_name = input("Enter new category name: ").strip()
        if category_name:
            # Automatically assign the next available ID, similar to SQL autoincrement 
            new_category_id = max(category['category_id'] for category in product_category.categories) + 1 if product_category.categories else 1
            product_category.add_category(new_category_id, category_name)
            print(COLOR_ACTION + f"New category '{category_name}' created with ID {new_category_id}." + COLOR_NORMAL)
            break
        else:
            print(COLOR_ATTENTION + "Category name cannot be empty. Please enter a valid name." + COLOR_NORMAL)

#   Admin: function to modify existing category
def admin_modify_category():
    global product_category, COLOR_ATTENTION, COLOR_ACTION, COLOR_NORMAL

    print(COLOR_ADMIN_MENU + "-------------------------------------------------")
    print("-- Admin Menu: Modify an existing Category")
    print("-------------------------------------------------" + COLOR_NORMAL)
    product_category.display_existing_category()

    while True:
        try:
            category_id_input = input("Enter the category ID you want to modify: ")
            category_id = int(category_id_input)
            break
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric category ID." + COLOR_NORMAL)

    old_category_name = product_category.lookup_category_name(category_id)
    if old_category_name == "Uncategorized":
        print(COLOR_ATTENTION + f"Category ID {category_id} not found." + COLOR_NORMAL)
        return

    while True:
        new_category_name = input(f"Enter new category name for existing '{old_category_name}': ").strip()
        if new_category_name:
            product_category.remove_category(category_id)
            product_category.add_category(category_id, new_category_name)
            print(COLOR_ACTION + f"Category ID '{category_id}' name is changed to '{new_category_name}'" + COLOR_NORMAL)
            break
        else:
            print(COLOR_ATTENTION + "Category name cannot be empty. Please enter a valid name." + COLOR_NORMAL)

#   Admin: function to remove existing category
def admin_remove_category():
    global product_category, COLOR_ATTENTION, COLOR_ACTION, COLOR_NORMAL
    print(COLOR_ADMIN_MENU + "-------------------------------------------------")
    print("-- Admin Menu: Remove an existing Category")
    print("-------------------------------------------------" + COLOR_NORMAL)
    while True:

        product_category.display_existing_category()

        category_id_input = input("Enter category ID to remove (or 'B' to go back to previous menu): ")

        if category_id_input.upper() == 'B':
            print(COLOR_ACTION + "Go back to previous menu." + COLOR_NORMAL)
            break

        try:
            category_id = int(category_id_input)
            if any(category['category_id'] == category_id for category in product_category.categories):
                product_category.remove_category(category_id)
                print(COLOR_HIGHLIGHT + f"Category ID {category_id} has been removed." + COLOR_NORMAL)
                break
            else:
                print(COLOR_ATTENTION + f"Category ID {category_id} not found." + COLOR_NORMAL)
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric category ID." + COLOR_NORMAL)

#   Admin: function to add a new product
def admin_add_product():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL, product_catalogue, product_category

    print(COLOR_ADMIN_MENU + "-------------------------------------------------")
    print("-- Admin Menu: Add New Product to Catalogue")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------" + COLOR_NORMAL)

    # Prompt for product name with validation for non-empty input
    add_product_name = input("Please enter the new product name: ").strip()
    while not add_product_name:  # Ensure the product name is not empty
        print(COLOR_ATTENTION + "Product name cannot be empty." + COLOR_NORMAL)
        add_product_name = input("Please enter the new product name: ").strip()

    # Continue with product price input
    while True:
        try:
            add_product_price = float(input(f"Please enter the price for the new product '{add_product_name}': "))
            break
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric value for the price." + COLOR_NORMAL)

    # Category ID input with validation
    while True:
        product_category.display_existing_category()
        add_product_category = input(f"Please enter the category ID in which '{add_product_name}' belongs to: ")
        try:
            add_product_category = int(add_product_category)
            if not any(category['category_id'] == add_product_category for category in product_category.categories):
                print(COLOR_ATTENTION + f"Category ID {add_product_category} not found." + COLOR_NORMAL)
                continue  # Prompt again for a valid category ID
            break
        except ValueError:
            print(COLOR_ATTENTION+"Invalid input. Please enter a numeric category ID."+COLOR_NORMAL)
    
    # Generating new product ID, using maximum product id of current product id + 1, simulate SQL DB AUTO_INCREMENT logic
    new_product_id = max([product['product_id'] for product in product_catalogue.products], default=0) + 1

    product_catalogue.add_product(new_product_id, add_product_name, add_product_category, add_product_price)

    print(COLOR_ACTION + f"The product ID {new_product_id} is added to the following: " + COLOR_NORMAL)
    print(COLOR_ACTION + f"Product Name : {add_product_name}, Product Price: ${add_product_price}, Product Category ID: {add_product_category}, Category Name: {product_category.lookup_category_name(add_product_category)} " + COLOR_NORMAL)


#   Admin: function to remove existing product
def admin_remove_product():
    global product_catalogue, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL

    while True:
        print(COLOR_ADMIN_MENU + "-------------------------------------------------")
        print("-- Admin: Remove Existing Product from Catalogue")
        print("-------------------------------------------------" + COLOR_NORMAL)

        product_catalogue.display_product_catalogue()

        product_id_input = input("Enter product ID to remove from catalogue (or 'B' to go back to previous menu): ")

        if product_id_input.upper() == 'B':
            print(COLOR_ACTION + "Go back to previous menu." + COLOR_NORMAL)
            break

        try:
            product_id = int(product_id_input)
            product = product_catalogue.lookup_product(product_id)
            if product != "Unknown Product":
                product_catalogue.remove_product(product_id)
                print(COLOR_ACTION + f"Product ID {product_id} has been removed from catalogue." + COLOR_NORMAL)
                break
            else:
                print(COLOR_ATTENTION + f"Product ID {product_id} not found in catalogue." + COLOR_NORMAL)
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric product ID." + COLOR_NORMAL)

#   Admin: function to modify existing product
def admin_modify_product():
    global product_catalogue, product_category, COLOR_ATTENTION, COLOR_ACTION, COLOR_NORMAL

    while True:
        print(COLOR_ADMIN_MENU + "-------------------------------------------------")
        print("-- Admin: Modify Existing Product in Catalogue")
        print("-------------------------------------------------" + COLOR_NORMAL)

        product_catalogue.display_product_catalogue()

        product_id_input = input("Enter product ID to modify (or 'B' to go back to previous menu): ")

        if product_id_input.upper() == 'B':
            print(COLOR_ACTION + "Go back to previous menu." + COLOR_NORMAL)
            break  # Exit the function to return to the previous menu

        try:
            product_id = int(product_id_input)
            product = product_catalogue.lookup_product(product_id)
            if product == "Unknown Product":
                print(COLOR_ATTENTION + f"Product ID {product_id} not found in catalogue." + COLOR_NORMAL)
                continue  # Prompt again for a valid product ID

            # Prompt for new product name with validation for non-empty input
            new_product_name = input(f"Enter the new name for the product '{product['product_name']}': ").strip()
            while not new_product_name:  # Ensure the new name is not empty
                print(COLOR_ATTENTION + "Product name cannot be empty." + COLOR_NORMAL)
                new_product_name = input(f"Enter the new name for the product '{product['product_name']}': ").strip()

            # Continue with price input
            while True:
                try:
                    new_product_price = float(input(f"Enter the new price for the product '{new_product_name}': "))
                    break
                except ValueError:
                    print(COLOR_ATTENTION + "Invalid input. Please enter a numeric value for the price." + COLOR_NORMAL)

            # Category ID input with validation
            while True:
                product_category.display_existing_category()
                new_category_id_input = input(f"Enter the category ID for this Product '{new_product_name}': ")
                try:
                    new_category_id = int(new_category_id_input)
                    if not any(category['category_id'] == new_category_id for category in product_category.categories):
                        print(COLOR_ATTENTION + f"Category ID {new_category_id} not found." + COLOR_NORMAL)
                        continue  # Prompt again for a valid category ID
                    break
                except ValueError:
                    print(COLOR_ATTENTION + "Invalid input. Please enter a numeric category ID." + COLOR_NORMAL)

            # Proceed with product update
            product_catalogue.remove_product(product_id)
            product_catalogue.add_product(product_id, new_product_name, new_category_id, new_product_price)
            print(COLOR_ACTION + f"The product ID {product_id} is updated to the following: " + COLOR_NORMAL)
            print(COLOR_ACTION + f"Name: {new_product_name}, Price: {new_product_price}, Category ID: {new_category_id}, Category Name: {product_category.lookup_category_name(new_category_id)} " + COLOR_NORMAL)
            break  # Successfully updated and exit the loop
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric product ID." + COLOR_NORMAL)


### Part C User Shoppping Cart Functions
            
#   User: Shopping Cart User Main Menu & Functions

def display_user_menu():
    global current_sessionid, COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL, current_user
    # Check if user is login
    if not current_user:  
        return
    while current_user:
        print(COLOR_USER_MENU + "-------------------------------------------------")
        print("-- User Menu ")
        print(f"-- Welcome " + COLOR_ATTENTION + f"{current_user['user_name']} " + COLOR_USER_MENU + "!")
        print("-- Session ID: ", current_sessionid)
        print("-------------------------------------------------" + COLOR_NORMAL)
        print("Choose an option below: \n")
        print("   1. Display Current Products in Catalogue ")              
        print("   2. Add a Product To Cart from Catalogue ")
        print("   3. Remove Product From Cart ")
        print("   4. Display items in your shopping cart ")
        print("   5. Checkout ")
        print("   Q. Logout and quit")
        print("\n")
        option = input("Enter your option (1-5, or 'Q'): ")

        if option == '1':
            product_catalogue.display_product_catalogue()
        elif option == '2':
            user_add_product_to_cart(current_sessionid)
        elif option == '3':
            user_remove_product_from_cart(current_sessionid)
        elif option == '4':
            shopping_cart.display_items_in_cart(current_sessionid)
        elif option == '5':
            initiate_checkout(current_sessionid)
        elif option.upper() == 'Q':
            current_sessionid = None
            current_user = None
            print(COLOR_ACTION + "Logging out now, see you next time !" + COLOR_NORMAL)
            break
        else:
            print(COLOR_ATTENTION + "Invalid option. Please enter a valid option (1-5, or 'Q')" + COLOR_NORMAL)


#   User: Add a Product to Cart from Catalogue function
def user_add_product_to_cart(current_sessionid):
    print(COLOR_USER_MENU + "-------------------------------------------------")
    print("-- User: Add a Product to Cart from Catalogue ")
    print("-------------------------------------------------" + COLOR_NORMAL)
    product_catalogue.display_product_catalogue()
    while True:  # Validation logic to force input is numeric & valid 
        try:
            product_id_input = input("Input the product ID you want to add to cart: ")
            product_id = int(product_id_input)
            break 
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric product id." + COLOR_NORMAL)

    while True: # Validation logic to force input is numeric & valid 
        try:
            product_qty_input = input("Input the quantity you want to add to cart: ")
            product_qty = int(product_qty_input)
            break  # Exit loop if input is valid (numeric)
        except ValueError:
            print(COLOR_ATTENTION + "Invalid input. Please enter a numeric quantity to add to cart." + COLOR_NORMAL)

    shopping_cart.add_product_to_cart(current_sessionid, product_id, product_qty)

#   User:  Remove a Product from Cart function
def user_remove_product_from_cart(current_sessionid):
    print(COLOR_USER_MENU + "-------------------------------------------------")
    print("-- User: Remove a Product from Cart  ")
    print("-------------------------------------------------" + COLOR_NORMAL)
    # Check if the cart is empty
    if not any(item['session_id'] == current_sessionid for item in shopping_cart.cart):
        print(COLOR_ATTENTION + "-------------------------------------------------")
        print("-- Your cart is currently empty." )
        print("-------------------------------------------------"+ COLOR_NORMAL)
        display_user_menu()  # Call the display_user_menu to return to user menu
        return
    shopping_cart.display_items_in_cart(current_sessionid)
    while True:
        try:
            product_id = int(input("Input the product ID you want to remove from cart: "))
            # Check if the product exists in the cart
            if any(item['session_id'] == current_sessionid and item['product_id'] == product_id for item in shopping_cart.cart):
                shopping_cart.remove_product_from_cart(current_sessionid, product_id)
                print(COLOR_ATTENTION + "-------------------------------------------------")
                print(f"-- Product {product_catalogue.lookup_product_name(product_id)} is removed from cart ")
                print("-------------------------------------------------"+COLOR_NORMAL)
                break
            else:
                print(COLOR_ATTENTION + "-------------------------------------------------")
                print(f"-- Your inputted product id is not found in your shopping cart.")
                print("-------------------------------------------------"+COLOR_NORMAL)
        except ValueError:
            print(COLOR_ATTENTION + "-- Invalid input. Please enter a numeric product id." + COLOR_NORMAL)


#   User: Checkout the items from shopping cart function
def initiate_checkout(session_id):
    global COLOR_ATTENTION, COLOR_HIGHLIGHT, COLOR_NORMAL, current_sessionid, current_user

    # Check if the cart is empty
    if not any(item['session_id'] == session_id for item in shopping_cart.cart):
        print(COLOR_ATTENTION + "-------------------------------------------------")
        print("-- Currently, there are no items in your cart.")
        print("-- Please add products to your cart to perform checkout.")
        print("-------------------------------------------------" + COLOR_NORMAL)
        return

    while True:
        print(COLOR_USER_MENU + "-------------------------------------------------")
        print("-- User: Checkout Shopping Cart " + COLOR_NORMAL)
        print("-------------------------------------------------"+COLOR_NORMAL)
        shopping_cart.display_items_in_cart(session_id)
        invoice_total = shopping_cart.calculate_invoice(session_id)
        print(COLOR_ACTION + f"Total Amount in cart: ${invoice_total}" + COLOR_NORMAL)

        # Display available payment gateways
        pgw.display_available_pgw()
        checkout_pgw = input(f"Please select your preferred payment method: (1 for VISA/MASTER, 2 for PAYPAL, 3 for UPI, 4 for BITCOIN PAYMENT) or 'B' to go back to previous menu: ")
        if checkout_pgw.upper() == 'B':
            break  # Go back to the previous menu
        elif checkout_pgw == '1':
            PaymentGateway.checkout_by_visa_master(session_id, invoice_total)
        elif checkout_pgw == '2':
            PaymentGateway.checkout_by_paypal(session_id, invoice_total)
        elif checkout_pgw == '3':
            PaymentGateway.checkout_by_upi(session_id, invoice_total)
        elif checkout_pgw == '4':
            PaymentGateway.checkout_by_bitcoin(session_id, invoice_total)
        else:
            print(COLOR_ATTENTION + "Invalid input. Please select a valid payment method or press 'B' to go back." + COLOR_NORMAL)
            
        print(COLOR_ACTION + "-------------------------------------------------")
        print("-- Checkout complete ! ")
        print("-- You will now be logout; Thank you for placing the order !")
        print("-------------------------------------------------"+COLOR_NORMAL)
        # Reset session state for safety before returning to login
        current_sessionid = None
        current_user = None
        return

### Part D Shopping Cart Application classes

#   Class: Product Catalogue

class ProductCatalogue:
    # Initialize Default Product Catalogue
    def __init__(self):
        self.products = [
        {"product_id": 1, "product_name": "Leather Boots", "category_id": 1, "product_price": 200.0},
        {"product_id": 2, "product_name": "Overhead Coat (Brown)", "category_id": 2, "product_price": 250.0},
        {"product_id": 3, "product_name": "Leather Jacket (Black)", "category_id": 3, "product_price": 350.0},
        {"product_id": 4, "product_name": "Baseball Cap (MLB)", "category_id": 4, "product_price": 50.0},
        {"product_id": 5, "product_name": "Google Chromecast", "category_id": 5, "product_price": 150.0}
    ]

#   add product to catalogue
    def add_product(self, product_id, product_name, category_id, product_price):
        self.products.append({
            "product_id": int(product_id),
            "product_name": product_name,
            "category_id": int(category_id),
            "product_price": product_price
        })

#   remove product from catalogue
    def remove_product(self, product_id):
        self.products = [product for product in self.products if product["product_id"] != product_id]

#   display products in current catalogue
    def display_product_catalogue(self):
        global COLOR_NORMAL, COLOR_ACTION, COLOR_HIGHLIGHT

        #check if products exist in list first
        if not self.products:
            print(COLOR_ATTENTION + "No products available." + COLOR_NORMAL)
            return

        header = "| {0:<10} | {1:<30} | {2:<20} | {3:<10} |".format("Product ID", "Product Name", "Category", "Price")
        print("-" * len(header))
        print(COLOR_HIGHLIGHT + "-- Current list of products in current product catalogue " + COLOR_NORMAL)
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # Sort the products by product_id in ascending order first
        sorted_products = sorted(self.products, key=lambda x: x['product_id'])


        for product in sorted_products:
            category_name = product_category.lookup_category_name(product['category_id'])  # Lookup category name
            row = "| {product_id:<10} | {product_name:<30} | {category:<20} | {product_price:<10} |".format(
                product_id=product['product_id'],
                product_name=product['product_name'],
                category=category_name,
                product_price=product['product_price'])
            print(row)
        print("-" * len(header))

#   common function to display product name using product id
    def lookup_product_name(self, product_id):
            for product in self.products:
                if product['product_id'] == product_id:
                    return product['product_name']
            return "Unknown Product"

#   common function to return the entire product attributes using product id
    def lookup_product(self, product_id):
            for product in self.products:
                if product['product_id'] == product_id:
                    return product
            return "Unknown Product"

#   Class: Product Category

class ProductCategory:
    # Initialize Default Product Categories
    def __init__(self):
        self.categories = [
            {"category_id": 1, "category_name": "Boots/Footwears"},
            {"category_id": 2, "category_name": "Coats"},
            {"category_id": 3, "category_name": "Jackets"},
            {"category_id": 4, "category_name": "Caps"},
            {"category_id": 5, "category_name": "General Electronics"},
    ]
        
#   add a new category
    def add_category(self, category_id, category_name):
        self.categories.append({"category_id": category_id, "category_name": category_name})

#   remove a category
    def remove_category(self, category_id):
        self.categories = [category for category in self.categories if category["category_id"] != category_id]

#   modify a category
    def modify_category(self, category_id):
        global product_category  
        product_category.display_existing_category()
        category_id = input("Enter the category ID you want to modify: ")
        # Check if category exists
        old_category_name = product_category.lookup_category_name(category_id)
        if old_category_name == "Uncategorized":
            print(COLOR_ATTENTION + f"Category ID {category_id} not found." + COLOR_NORMAL)
            return
        new_category_name = input(f"Enter new category name for existing '{old_category_name}': ")
        product_category.remove_category(category_id)
        product_category.add_category(category_id, new_category_name)
        print(COLOR_ACTION + f"Category ID '{category_id}' name is changed to '{new_category_name}'"+COLOR_NORMAL)

#   display current category as a list
    def display_existing_category(self):
        global product_category, COLOR_HIGHLIGHT, COLOR_NORMAL
        print(COLOR_HIGHLIGHT + "-------------------------------------------------")
        print("-- Current Product Categories" )
        print("-------------------------------------------------"+ COLOR_NORMAL)

        # Check if there are any categories
        if not product_category.categories:
            print(COLOR_ATTENTION + "No categories available." + COLOR_NORMAL)
            return

        # Table headers
        header = "| {0:<15} | {1:<30} |".format("Category ID", "Category Name")
        print(header)
        print("-" * len(header))


        # Sort the categories by category_id in ascending order
        sorted_categories = sorted(self.categories, key=lambda x: x['category_id'])
        for category in sorted_categories:
            row = "| {category_id:<15} | {category_name:<30} |".format(**category)
            print(row)
        print("-------------------------------------------------")


#   lookup a category name using category id, return "Uncategorized" if the category id no longer exist (or cannot be found)

    def lookup_category_name(self, category_id):
            for category in self.categories:
                if category['category_id'] == category_id:
                    return category['category_name']
            return "Uncategorized" 


# User Class: Login DB and general functions
class UserDatabase:
    # Initialize Default User DB
    def __init__(self):
        self.users = [
            {"user_id": 1, "user_name": "user1", "user_password": "pass1", "user_role": "U", "email": "user1@demo-shoppingcart.com"},
            {"user_id": 2, "user_name": "user2", "user_password": "pass2", "user_role": "U", "email": "user2@demo-shoppingcart.com"},
            {"user_id": 3, "user_name": "admin", "user_password": "adminpass", "user_role": "A", "email": "admin@demo-shoppingcart.com"},     
        ]

#   Add a new user to  current users 
    def add_user(self, user_id, user_name, user_password, user_role, email):
        self.users.append({
            "user_id": user_id,
            "user_name": user_name,
            "user_password": user_password,
            "user_role": user_role,
            "email": email
        })

#   Remove a user 
    def remove_user(self, user_id):
        self.users = [user for user in self.users if user["user_id"] != user_id]

# Lookup user with username and password, if match return the user 
    def lookup_user(self, username, password):
        for user in self.users:
            if user['user_name'] == username and user['user_password'] == password:
                return user
        return None

# ShoppingCart Class: for user shopping experience

class ShoppingCart:
    def __init__(self):
        self.cart = []

#   add a product to ShoppingCart
    def add_product_to_cart(self, session_id, product_id, qty):
        product = next((item for item in product_catalogue.products if item["product_id"] == product_id), None)
        print("-------------------------------------------------")

        if product:

            # Check if there is a product already placed in cart
            for item in self.cart:
                if item["session_id"] == session_id and item["product_id"] == product_id:
                    item["quantity"] += qty
                    print(COLOR_ACTION + f"Added {qty} unit(s) more of {product['product_name']} to cart." + COLOR_NORMAL)
                    return
                
            #  If this is a new item added to cart    
            cart_item = {
                "session_id": session_id,
                "product_id": product_id,
                "product_name": product["product_name"],
                "quantity": qty,
                "product_price": product["product_price"]
            }
            self.cart.append(cart_item)
            print(COLOR_ACTION + f"Added {qty} unit(s) of {product['product_name']} to cart." + COLOR_NORMAL)
        else:
            print(COLOR_ATTENTION + "Product not found in catalogue."+ COLOR_NORMAL)
        print("-------------------------------------------------")

        
#   Function to remove a product from ShoppingCart
    def remove_product_from_cart(self, session_id, product_id):
        self.cart = [item for item in self.cart if not (item["session_id"] == session_id and item["product_id"] == product_id)]

#   Function to display current items in ShoppingCart
    def display_items_in_cart(self, session_id):
        global COLOR_NORMAL, COLOR_ACTION, COLOR_HIGHLIGHT

        # Check if the cart is empty
        if not any(item['session_id'] == session_id for item in self.cart):
            print(COLOR_ATTENTION + "-------------------------------------------------")
            print("-- Your cart is empty.")
            print("-------------------------------------------------" + COLOR_NORMAL)
            return

        # Table headers
        header = "| {0:<36} | {1:<10} | {2:<30} | {3:<15} | {4:<10} |".format("Session ID", "Product ID", "Name", "Quantity", "Price $")
        print(COLOR_HIGHLIGHT)
        print("-" * len(header))       
        print("-- You have the following products added in your cart: " + COLOR_NORMAL)
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        
        #calculate subtotal of the shopping cart
        subtotal = 0
        # Updated table rows to include Session ID
        for item in self.cart:
            if item['session_id'] == session_id:
                row = "| {session_id:<36} | {product_id:<10} | {product_name:<30} | {quantity:<15} | {product_price:<10} |".format(**item)
                print(row)
                subtotal += item['quantity'] * item['product_price']

        print("-" * len(header))
        print(COLOR_ACTION + f"Subtotal: ${subtotal}" + COLOR_NORMAL)

#   Function to calculate total amount $ of items in ShoppingCart
    def calculate_invoice(self, session_id):
        total_cost = 0
        for item in self.cart:
            if item['session_id'] == session_id:
                total_cost += item['product_price'] * item['quantity']
        return total_cost

# PaymentGateway Class for Checkout, link to external payment gateways or further payment flows
class PaymentGateway:
 # Initialize Default Options for payment Gateway
    def __init__(self):
        self.pgw = [
            {"pgw_id": 1, "pgw_name": "NET BANKING VISA/MASTER"},
            {"pgw_id": 2, "pgw_name": "PAYPAL"},
            {"pgw_id": 3, "pgw_name": "UPI"},     
            {"pgw_id": 4, "pgw_name": "BITCOIN PAYMENT"},     
        ]

#   Display current list of available payment gateways
    def display_available_pgw(self):
        print(COLOR_HIGHLIGHT + "-------------------------------------------------")
        print("-- Available Payment Gateways")
        print("-------------------------------------------------" + COLOR_NORMAL)

        # Check if there are any payment gateways available
        if not self.pgw:
            print(COLOR_ATTENTION + "No payment gateways available.")
            return

        # Table headers
        header = "| {0:<10} | {1:<30} |".format("Gateway ID", "Gateway Name")
        print(header)
        print("-" * len(header))

        # Table rows
        for gateway in self.pgw:
            row = "| {pgw_id:<10} | {pgw_name:<30} |".format(**gateway)
            print(row)
        print("-------------------------------------------------")

#   Checkout by Visa / Master via Net Banking
    def checkout_by_visa_master(session_id, payment_amount):
        print(COLOR_ATTENTION + f"Your payment link is generated. please open this link in browser to continue the payment")
        print(COLOR_ACTION + f"https://www.net-banking.com/pay.php?order={session_id}&amount={payment_amount}")    

#   Checkout by Paypal
    def checkout_by_paypal(session_id, payment_amount):
        print(COLOR_ATTENTION +f"Your  link is generated. Please continue to paypal.com to proceed payment")
        print(COLOR_ACTION + f"https://www.paypal.com/pay.php?order={session_id}&amount={payment_amount}")    

#   Checkout by UPI
    def checkout_by_upi(session_id, payment_amount):
        print(COLOR_ATTENTION + f"You will soon receive an email at your registered email address. Please continue the payment amount of ${payment_amount} detailed in the email.")


#   Checkout by crytocurrency
    def checkout_by_bitcoin(session_id, payment_amount):
        print(COLOR_ATTENTION + f"You will soon receive an email at your registered email address. Please continue the payment amount of ${payment_amount} from your cryptocurrency wallet with instructions in the email.")
   

## Part E Program Execution
    
# Instantiate Classes
product_catalogue = ProductCatalogue()
product_category = ProductCategory()
user_database = UserDatabase()
shopping_cart = ShoppingCart()
pgw = PaymentGateway()

##DEMO Shopping Cart Main Code
def main():
    while True:
        display_welcome_msg()
        display_login()


#Execute Demo Marketplace Shopping Cart Program via commandline python
#> python3 main.py
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShoppingCart Application quit by Ctrl-C / Keyboard Interrupt")