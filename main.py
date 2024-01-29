
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
    print("-------------------------------------------------")
    print("-- Current Session ID: ", current_sessionid)

    
def display_login():
    global current_user, current_shoppingcart, current_sessionid

    while True:
        username = input("Please input your username : ")
        password = input("Please input your password : ")
        # Check credentials and display role
        user = lookup_user(username, password)
        if user:
            print("User Found " )
            current_user = user
            current_sessionid = create_login_sessionid()
            print("Generated session ID:", current_sessionid)
            if get_user_attribute("user_role") == "A":
                display_admin_menu()
            elif get_user_attribute("user_role") == "U":
                display_user_menu()
            break
        else:
            print("Invalid username or password")


def create_login_sessionid():
        print("Create Login Session")
        return str(uuid.uuid4())


def lookup_user(username, password):
    for user in users_db:
        if user['user_name'] == username and user['user_password'] == password:
            return user
    return None


def init_static_userdb():
    print("Initiaze Users Database")

def lookup_product_category():
        print("Initiaze Users Database")

### Part B Admin Functions
def display_admin_menu():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Welcome to the Admin Menu")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    print("-- Choose an option below: ")
    print("-- 1. Manage Product Catalogue ")
    print("-- 2. Manage Product Category ")
    print("-- 3. Logout ")
    print("-------------------------------------------------")

def display_admin_manage_product_menu():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Manage Product Catalogue")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    print("-- Choose an option below: ")
    print("-- 1. Display Current Products in Catalogue ")
    print("-- 2. Add New Product to Catalogue ")
    print("-- 3. Modify existing product from Catalogue ")
    print("-------------------------------------------------")

def admin_add_product():
    global current_sessionid
    print("-------------------------------------------------")
    print("-- Add New Product to Catalogue")
    print("-- Login Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    add_product_name = input("Please enter the new product name")
    add_product_price = input("Please enter the price for new product ", add_product_name)
    add_product_quantity = input("Please enter the the product available quantity")




### Part C User Functions
def display_user_menu():
    global current_sessionid

    print("-------------------------------------------------")
    print("-- Welcome to the User Menu")
    print("-- Session ID: ", current_sessionid)
    print("-------------------------------------------------")
    display_items_in_catalogue()
    print("-- Choose an option below: ")
    print("-- 1. Add Product To Cart ")
    print("-- 2. Remove Product From Cart ")
    print("-- 3. Display items in current cart ")
    print("-- 4. Logout ")
    print("-------------------------------------------------")


def user_add_product_to_cart():
    add_product = input("Input the product ID you want to add to cart")
    add_product_qty = input("Input the number product")
    print("Product added to cart")


def user_remove_product_from_cart():
    display_items_in_cart()
    add_product = input("Input the product ID you want to remove from cart")
    print("Product removed from cart")


def display_items_in_cart():
    print("-------------------------------------------------")
    print("-- You have current items in cart: ")
    print("-------------------------------------------------")


def display_items_in_catalogue():
    print("-------------------------------------------------")
    print("-- Current list of products in product catalogue ")
    print("-------------------------------------------------")
    header = "| {0:<10} | {1:<30} | {2:<15} | {3:<10} |".format("Product ID", "Product Name", "Category ID", "Price")
    print(header)
    print("-" * len(header))

    for product in product_catalogues:
        row = "| {product_id:<10} | {product_name:<30} | {category_id:<15} | {product_price:<10} |".format(**product)
        print(row)
    print("-------------------------------------------------")



### Part D Shopping Cart Arrays

#Initialize DB
# Default Product Catelogue
product_catalogues = [
    {"product_id": 1, "product_name": "Leather Boot", "category_id": 1, "product_price": 200},
    {"product_id": 2, "product_name": "Overhead Coat (Brown)", "category_id": 2, "product_price": 250},
    {"product_id": 3, "product_name": "Leather Jacket (Black)", "category_id": 3, "product_price": 350},
    {"product_id": 4, "product_name": "Baseball Cap (MLB)", "category_id": 4, "product_price": 50},
    {"product_id": 5, "product_name": "Google Chromecast", "category_id": 5, "product_price": 150}

]

# Default Product Categories
product_categories = [
    {"category_id": 1, "category_name": "Boots/Footwears"},
    {"category_id": 2, "category_name": "Coats"},
    {"category_id": 3, "category_name": "Jackets"},
    {"category_id": 4, "category_name": "Caps"},
    {"category_id": 5, "category_name": "General Electronics"},
]

users_db = [
     {"user_id": 1, "user_name": "user1", "user_password": "pass1", "user_role": "U", "email": "user1@demo-shoppingcart.com"},
     {"user_id": 2, "user_name": "user2", "user_password": "pass2", "user_role": "U", "email": "user2@demo-shoppingcart.com"},
     {"user_id": 3, "user_name": "admin", "user_password": "adminpass", "user_role": "A", "email": "admin@demo-shoppingcart.com"},     
]




#It is necessary to construct a sample product catalog with three to four product categories, such as Boots, Coats, Jackets, and Caps. 
#The product id, name, category id, and price should all be present for each item in the dummy database of the catalog. 
#Both users and administrators can view the catalog.














### Part E Program Execution
#   User login and admin login should be created once the code for the welcome message has been written. 
#   For the creation of demo login and admin login, demo databases for those should be created for the user and admin verification, and session id creation.
def main():
    display_welcome_msg()
    display_login()



#Execute Demo Marketplace Shopping Cart Program
main()