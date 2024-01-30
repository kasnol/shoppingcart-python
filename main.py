
import uuid

# Global Variables
current_shoppingcart = []
current_user = None
current_sessionid = None



### Part A Shopping Cart General Functions
#   A welcome message should initially be displayed in the e-commerce application, such as "Welcome to the Demo Marketplace".




def get_user_attribute(attribute):
    global current_user
    return current_user[attribute]



def display_welcome_msg():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Welcome to the Demo Marketplace             --")
    print("------------------------------------------------- \n")

    
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
            print("Invalid username or password")

# For simplicity, use system generated UUID as session ID
def create_login_sessionid():
        return str(uuid.uuid4())


def lookup_user(username, password):
    for user in user_database.users:  
        if user['user_name'] == username and user['user_password'] == password:
            return user
    return None




### Part B Admin Functions
def display_admin_menu():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Admin Menu")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    
    while True:
        print("-- Choose an option below: ")
        print("-- 1. Manage Product Catalogue ")
        print("-- 2. Manage Product Category ")
        print("-- Q. Logout ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-3): ")
            
        if option == '1':
            display_admin_manage_product_menu()
        elif option == '2':
            display_admin_manage_product_category()
        elif option == 'Q':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please enter a valid option (1-3):")

def display_admin_manage_product_menu():
    global current_sessionid
    while True:
        print("-------------------------------------------------")
        print("-- Admin: Manage Product Catalogue")
        print("-- Login Session ID: ", current_sessionid)
        print("-------------------------------------------------")
        print("-- Choose an option below: ")
        print("-- 1. Display Current Products in Catalogue ")
        print("-- 2. Add New Product to Catalogue ")
        print("-- 3. Modify existing product in Catalogue ")
        print("-- 4. Remove existing Product from Catalogue ")
        print("-- B. Back to Admin Main Menu ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-4 or B): ")

        if option == '1':
            product_catalogue.display_product_catalogue()
        elif option == '2':
            admin_add_product()
        elif option == '3':
            # Implement modify product functionality (not provided in script)
            pass
        elif option == '4':
            admin_remove_product()
        elif option.upper() == 'B':
            break
        else:
            print("Invalid option. Please enter a valid option (1-4 or B)")

def display_admin_manage_product_category():
    global current_sessionid
    while True:
        print("-------------------------------------------------")
        print("-- Admin: Manage Product Category")
        print("-- Login Session ID: ", current_sessionid)
        print("-------------------------------------------------")
        print("-- Choose an option below: ")
        print("-- 1. Display Current Product Categories ")
        print("-- 2. Add a New Category ")
        print("-- 3. Modify an existing Category ")
        print("-- 4. Remove an existing Category ")
        print("-- B. Back to Admin Menu ")
        print("-------------------------------------------------")
        option = input("Enter your option (1-4 or B): ")
        if option == '1':
            product_category.display_existing_category()
            pass
        elif option == '2':
            admin_add_category()
        elif option == '3':
            # Implement modify category functionality (not provided in script)
            pass
        elif option == '4':
            admin_remove_category()
        elif option.upper() == 'B':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def admin_display_existing_category():
    pass            

def admin_add_category():
    category_id = input("Enter new category ID: ")
    category_name = input("Enter new category name: ")
    product_category.add_category(category_id, category_name)
    print(f"Category '{category_name}' added.")

def admin_remove_category():
    category_id = input("Enter category ID to remove: ")
    product_category.remove_category(category_id)
    print(f"Category with ID {category_id} removed.")

def admin_add_product():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Admin Menu: Add New Product to Catalogue")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    add_product_name = input("Please enter the new product name")
    add_product_price = input("Please enter the price for new product ", add_product_name)
    add_product_quantity = input("Please enter the the product available quantity")

def admin_remove_product():
    product_id = int(input("Enter product ID to remove: "))
    product_catalogue.remove_product(product_id)
    print(f"Product with ID {product_id} removed.")


### Part C User Functions
def display_user_menu():
    global current_sessionid
    while True:
        print("-------------------------------------------------")
        print("-- User Menu ")
        print(f"-- Welcome User {current_user['user_name']} !")
        print("-- Session ID: ", current_sessionid)
        print("-------------------------------------------------")
        print("Choose an option below: ")
        print("   1. Add Product To Cart ")
        print("   2. Remove Product From Cart ")
        print("   3. Display items in current cart ")
        print("   4. Checkout ")
        print("   Q. Logout and quit")
        print("-------------------------------------------------")
        option = input("Enter your option (1-4 or Q): ")

        if option == '1':
            user_add_product_to_cart(current_sessionid)
        elif option == '2':
            user_remove_product_from_cart(current_sessionid)
        elif option == '3':
            shopping_cart.display_items_in_cart(current_sessionid)
        elif option == '4':
            pgw.initiate_checkout(current_sessionid)
        elif option == 'Q':
            print("Logging out now, see you next time !")
            break
        else:
            print("Invalid option, please choose a number between 1 and 4.")

def user_add_product_to_cart(current_sessionid):
    shopping_cart.display_items_in_cart(current_sessionid)
    while True:  # Validation logic to force input is numeric & valid 
        try:
            product_id_input = input("Input the product ID you want to add to cart: ")
            product_id = int(product_id_input)
            break 
        except ValueError:
            print("Invalid input. Please enter a numeric product id.")

    while True: # Validation logic to force input is numeric & valid 
        try:
            product_qty_input = input("Input the quantity you want to add to cart: ")
            product_qty = int(product_qty_input)
            break  # Exit loop if input is valid (numeric)
        except ValueError:
            print("Invalid input. Please enter a numeric quantity to add to cart.")

    shopping_cart.add_product_to_cart(current_sessionid, product_id, product_qty)
    print(f"-- Product {product_id} with qty {product_qty} added to cart")


def user_remove_product_from_cart(current_sessionid):
    while True:  # Validation logic to force input is numeric & valid 
        try:
            product_id = int(input("Input the product ID you want to remove from cart"))
            break 
        except ValueError:
            print("Invalid input. Please enter a numeric product id.")
        shopping_cart.remove_product(current_sessionid, product_id)
        print(f"-- Product {product_id} removed from cart")


def display_items_in_cart(self, session_id):   
    # Check if the cart is empty
    if not any(item['session_id'] == session_id for item in self.cart):
        print("-------------------------------------------------")
        print("-- Your cart is empty.")
        print("-------------------------------------------------")
        return

    # Table headers
    print("-- You have current items in cart: ")
    header = "| {0:<10} | {1:<30} | {2:<10} | {3:<10} |".format("Product ID", "Name", "Quantity", "Price")
    print(header)
    print("-" * len(header))

    # Table rows
    for item in self.cart:
        if item['session_id'] == session_id:
            row = "| {product_id:<10} | {product_name:<30} | {quantity:<10} | {product_price:<10} |".format(**item)
            print(row)
    print("-" * len(header))

def initiate_checkout(session_id):
    while True:
        print("-------------------------------------------------")
        print("-- User: Checkout ")
        print("-------------------------------------------------")
        shopping_cart.display_items_in_cart(session_id)
        invoice_total = shopping_cart.calculate_invoice(session_id)
        print(f"Total Amount in cart: {invoice_total}")

        # Display available payment gateways
        pgw.display_available_pgw()
        checkout_pgw = input(f"Please select your preferred payment method: (1 for VISA/MASTER, 2 for PAYPAL, 3 for BITCOIN PAYMENT) or 'B' to go back: ")

        if checkout_pgw.upper() == 'B':
            break  # Go back to the previous menu
        elif checkout_pgw == '1':
            pgw.checkout_by_visa_master(session_id, invoice_total)
            break
        elif checkout_pgw == '2':
            pgw.checkout_by_paypal(session_id, invoice_total)
            break
        elif checkout_pgw == '3':
            pgw.checkout_by_bitcoin(session_id, invoice_total)
            break
        else:
            print("Invalid payment method selected. Please try again.")


### Part D Shopping Cart Application classes





class ProductCatalogue:
    # Initialize Default Product Catalogue
    def __init__(self):
        self.products = [
        {"product_id": 1, "product_name": "Leather Boot", "category_id": 1, "product_price": 200},
        {"product_id": 2, "product_name": "Overhead Coat (Brown)", "category_id": 2, "product_price": 250},
        {"product_id": 3, "product_name": "Leather Jacket (Black)", "category_id": 3, "product_price": 350},
        {"product_id": 4, "product_name": "Baseball Cap (MLB)", "category_id": 4, "product_price": 50},
        {"product_id": 5, "product_name": "Google Chromecast", "category_id": 5, "product_price": 150}
    ]

    def add_product(self, product_id, product_name, category_id, product_price):
        self.products.append({
            "product_id": product_id,
            "product_name": product_name,
            "category_id": category_id,
            "product_price": product_price
        })

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product["product_id"] != product_id]

    def display_product_catalogue(self):
        header = "| {0:<10} | {1:<30} | {2:<15} | {3:<10} |".format("Product ID", "Product Name", "Category ID", "Price")

        print("-" * len(header))
        print("-- Current list of products in current product catalogue ")
        print("-" * len(header))
        header = "| {0:<10} | {1:<30} | {2:<15} | {3:<10} |".format("Product ID", "Product Name", "Category ID", "Price")
        print(header)
        print("-" * len(header))
        for product in self.products:
            row = "| {product_id:<10} | {product_name:<30} | {category_id:<15} | {product_price:<10} |".format(**product)
            print(row)
        print("-" * len(header))



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

    def add_category(self, category_id, category_name):
        self.categories.append({"category_id": category_id, "category_name": category_name})

    def remove_category(self, category_id):
        self.categories = [category for category in self.categories if category["category_id"] != category_id]

    def display_existing_category():
        global product_category
        print("-------------------------------------------------")
        print("-- Current Product Categories")
        print("-------------------------------------------------")

        # Check if there are any categories
        if not product_category.categories:
            print("No categories available.")
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


class UserDatabase:
    # Initialize Default User DB
    def __init__(self):
        self.users = [
            {"user_id": 1, "user_name": "user1", "user_password": "pass1", "user_role": "U", "email": "user1@demo-shoppingcart.com"},
            {"user_id": 2, "user_name": "user2", "user_password": "pass2", "user_role": "U", "email": "user2@demo-shoppingcart.com"},
            {"user_id": 3, "user_name": "admin", "user_password": "adminpass", "user_role": "A", "email": "admin@demo-shoppingcart.com"},     
        ]

    def add_user(self, user_id, user_name, user_password, user_role, email):
        self.users.append({
            "user_id": user_id,
            "user_name": user_name,
            "user_password": user_password,
            "user_role": user_role,
            "email": email
        })

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user["user_id"] != user_id]

    def lookup_user(self, username, password):
        for user in self.users:
            if user['user_name'] == username and user['user_password'] == password:
                return user
        return None


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product_to_cart(self, session_id, product_id, qty):
        product = next((item for item in product_catalogue.products if item["product_id"] == product_id), None)
        if product:
            # Check if there is a product already placed in cart
            for item in self.cart:
                if item["session_id"] == session_id and item["product_id"] == product_id:
                    item["quantity"] += qty
                    print(f"Added {qty} more of {product['product_name']} to cart.")
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
            print(f"Added {qty} of {product['product_name']} to cart.")
        else:
            print("Product not found in catalogue.")

    def remove_product_from_cart(self, session_id, product_id):
        self.cart = [item for item in self.cart if not (item["session_id"] == session_id and item["product_id"] == product_id)]
        print("Product with ID {product_id} removed from cart.")

        
    def display_items_in_cart(self, session_id):


        # Check if the cart is empty
        if not any(item['session_id'] == session_id for item in self.cart):
            print("-- Your cart is empty.")
            return

        # Table headers
        print("-- You have the following products added in your cart: ")
        header = "| {0:<36} | {1:<10} | {2:<30} | {3:<15} | {4:<10} |".format("Session ID", "Product ID", "Name", "Quantity", "Price")
        print(header)
        print("-" * len(header))

        # Updated table rows to include Session ID
        for item in self.cart:
            if item['session_id'] == session_id:
                row = "| {session_id:<36} | {product_id:<10} | {product_name:<30} | {quantity:<15} | {product_price:<10} |".format(**item)
                print(row)
        print("-" * len(header))

    def calculate_invoice(self, session_id):
        total_cost = 0
        for item in self.cart:
            if item['session_id'] == session_id:
                total_cost += item['product_price'] * item['quantity']
        return total_cost

class PaymentGateway:
 # Initialize Default Options for payment Gateway
    def __init__(self):
        self.pgw = [
            {"pgw_id": 1, "pgw_name": "VISA/MASTER"},
            {"pgw_id": 2, "pgw_name": "PAYPAL"},
            {"pgw_id": 3, "pgw_name": "BITCOIN PAYMENT"},     
        ]
    def display_available_pgw(self):
        def display_available_pgw(self):
            print("-------------------------------------------------")
            print("-- Available Payment Gateways")
            print("-------------------------------------------------")

            # Check if there are any payment gateways available
            if not self.pgw:
                print("No payment gateways available.")
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

    def checkout_by_visa_master(session_id, payment_amount):
        print(f"Your payment link is generated. please open this link in browser to continue the payment")
        print(f"https://www.visa-payment.com/pay.php?order={session_id}&amount={payment_amount}")    

    def checkout_by_paypal(session_id, payment_amount):
        print(f"Your  link is generated. Please continue to paypal.com to proceed payment")
        print(f"https://www.paypal.com/pay.php?order={session_id}&amount={payment_amount}")    
   

    def checkout_by_bitcoin(session_id, payment_amount):
        print(f"You will soon receive an email at your registered email address. Please continue the payment from your cryptocurrency wallet")
   


#It is necessary to construct a sample product catalog with three to four product categories, such as Boots, Coats, Jackets, and Caps. 
#The product id, name, category id, and price should all be present for each item in the dummy database of the catalog. 
#Both users and administrators can view the catalog.














## Part E Program Execution
#   User login and admin login should be created once the code for the welcome message has been written. 
#   For the creation of demo login and admin login, demo databases for those should be created for the user and admin verification, and session id creation.
    
# Instantiate Classes
product_catalogue = ProductCatalogue()
product_category = ProductCategory()
user_database = UserDatabase()
shopping_cart = ShoppingCart()
pgw = PaymentGateway()
def main():
    display_welcome_msg()
    display_login()



#Execute Demo Marketplace Shopping Cart Program
main()