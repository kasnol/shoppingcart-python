
import uuid


### Part A Shopping Cart General Functions
#   A welcome message should initially be displayed in the e-commerce application, such as "Welcome to the Demo Marketplace".
def display_welcome_msg():
    print("-------------------------------------------------")
    print("-- Welcome to the Demo Marketplace             --")
    print("-------------------------------------------------")
    print("-- Current Session ID: ", current_sessionid)

    
def display_login():
    while True:
        username = input("Please input your username : ")
        password = input("Please input your password : ")
        # Check credentials and display role
        user = lookup_user(username, password)
        if user:
            print("User Found " )
            print(user)
            global current_shoppingcart, current_user, current_role, current_sessionid
            current_shoppingcart =[]
            current_user = user["user_name"]
            current_role = user["user_role"]
            current_sessionid = generate_sessionid()
            print("Generated session ID:", current_sessionid)
            if current_role == "A":
                display_admin_menu()
            elif current_role == "U":
                display_user_menu()
            break
        else:
            print("Invalid username or password")


def generate_sessionid():
        return str(uuid.uuid4())


def lookup_user(username, password):
    for user in users_db:
        if user['user_name'] == username and user['user_password'] == password:
            return user
    return None


def create_login_session():
    print("Create Login Session")

def init_static_userdb():
    print("Initiaze Users Database")

def lookup_product_category():
        print("Initiaze Users Database")

### Part B User Functions
def display_user_menu():
    print("-------------------------------------------------")
    print("-- Welcome to the User Menu             --")
    print("-------------------------------------------------")
    print("-- Choose an option below: ")
    print("-- 1. Manage Product Catalogue ")
    print("-- 2. Manage Product Category ")
    print("-- 3. Logout ")
    print("-------------------------------------------------")

### Part C Admin Functions
def display_admin_menu():
    print("-------------------------------------------------")
    print("-- Welcome to the Admin Menu             --")
    print("-------------------------------------------------")
    print("-- Choose an option below: ")
    print("-- 1. Add Product To Cart ")
    print("-- 2. Remove Product From Cart ")
    print("-- 3. Display Current Cart ")
    print("-- 4. Logout ")
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
     {"user_id": 1, "user_name": "user1", "user_password": "pass1", "user_role": "U"},
     {"user_id": 2, "user_name": "user2", "user_password": "pass2", "user_role": "U"},
     {"user_id": 3, "user_name": "admin", "user_password": "adminpass", "user_role": "A"},     
]


# Global Variables
current_shoppingcart = []
current_user = None
current_role = None
current_sessionid = None


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