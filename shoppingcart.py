print("Welcome to the Demo Marketplace")
# Create demo database with user and admin credentials
user_db = {"user1": "pass1", "user2": "pass2"}
admin_db = {"admin1": "pass1", "admin2": "pass2"}
# Function to handle user login
def user_login():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user in user_db and user_db[user] == password:
        print("Login successful as user.")
        # Generate session id for user
        session_id = generate_session_id()
        print("Your session id is: ", session_id)
    else:
        print("Login failed. Please try again.")

# Function to handle admin login
def admin_login():
    admin = input("Enter your username: ")
    password = input("Enter your password: ")
    if admin in admin_db and admin_db[admin] == password:
        print("Login successful as admin.")
        # Generate session id for admin
        session_id = generate_session_id()
        print("Your session id is: ", session_id)
    else:
        print("Login failed. Please try again.")
# Function to generate a unique session id (dummy implementation)
def generate_session_id():
    return "12345"
# User or admin can call the login functions as per their choice
login_as = input("Enter 'u' for user login or 'a' for admin login: ")
if login_as == 'u':
    user_login()
elif login_as == 'a':
    admin_login()
else:
    print("Invalid option.")
# Create a demo catalogue of products
catalogue = [
    {"id": 1, "name": "Boots", "category": 1, "price": 2000},
    {"id": 2, "name": "Coats", "category": 2, "price": 2500},
    {"id": 3, "name": "Jackets", "category": 3, "price": 1500},
    {"id": 4, "name": "Caps", "category": 4, "price": 500}
]

# Function to display the catalogue
def display_catalogue():
    print("Product Id\tName\t\tCategory\tPrice")
    for product in catalogue:
        print(f"{product['id']}\t\t{product['name']}\t\t{product['category']}\t\t{product['price']}")

# Call the display_catalogue function to show the catalogue
display_catalogue()
# Create a demo cart
cart = []
# Function to display the cart
def display_cart():
    print("Session Id\tProduct Id\tName\t\tQuantity")
    for item in cart:
        print(f"{item['session_id']}\t\t{item['product_id']}\t\t{item['name']}\t\t{item['quantity']}")

# Function to add an item to the cart
def add_to_cart(session_id, product_id, quantity):
    product = [p for p in catalogue if p['id'] == product_id][0]
    cart.append({"session_id": session_id, "product_id": product_id, "name": product['name'], "quantity": quantity})
    print(f"{quantity} pieces of {product['name']} added to the cart.")
# Function to delete an item from the cart
def delete_from_cart(session_id, product_id):
    for i, item in enumerate(cart):
        if item['session_id'] == session_id and item['product_id'] == product_id:
            del cart[i]
            print(f"{item['name']} removed from the cart.")
            break
    else:
        print("Item not found in the cart.")

# User login
session_id = input("Enter your session id: ")
while True:
    print("\n1. View Cart")
    print("2. Add to Cart")
    print("3. Delete from Cart")
    print("4. Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_cart()
    elif choice == 2:
        product_id = int(input("Enter the product id: "))
        quantity = int(input("Enter the quantity: "))
        add_to_cart(session_id, product_id, quantity)
    elif choice == 3:
        product_id = int(input("Enter the product id: "))
        delete_from_cart(session_id, product_id)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
def checkout():
  payment_method = input("Please select the payment method (net_banking/PayPal/UPI): ")
  if payment_method == "net_banking":
    print("Your order is successfully placed, and the payment has been made using Net Banking.")
    print("Thank you for shopping with us! Have a great day :)")
  elif payment_method == "PayPal":
    print("Your order is successfully placed, and the payment has been made using PayPal.")
    print("Thank you for shopping with us! Have a great day :)")
  elif payment_method == "UPI":
    print("You will be shortly redirected to the portal for Unified Payment Interface to make a payment.")
    print("Thank you for shopping with us! Have a great day :)")
  else:
    print("Invalid payment method selected. Please choose a valid payment option.")
# Example usage
checkout()
# Output: 
# Please select the payment method (net_banking/PayPal/UPI): UPI
# You will be shortly redirected to the portal for Unified Payment Interface to make a payment.
# Thank you for shopping with us! Have a great day :)
#Admin Login Verification
def admin_login(username, password):
    admin_db = {"admin1": "pass1", "admin2": "pass2"}
    if username in admin_db and admin_db[username] == password:
        return True
    else:
        return False
    
#Admin Functionality
def admin_func(username, password):
    if admin_login(username, password):
        print("Admin Login Successful.")
        while True:
            print("Enter 1 to add product to the catalog")
            print("Enter 2 to update product in the catalog")
            print("Enter 3 to delete product from the catalog")
            print("Enter 4 to add category in the catalog")
            print("Enter 5 to delete category from the catalog")
            print("Enter 6 to Logout")
            admin_choice = int(input("Enter your choice: "))
            
            #Add product to the catalog
            if admin_choice == 1:
                product_id = int(input("Enter Product ID: "))
                product_name = input("Enter Product Name: ")
                category_id = int(input("Enter Category ID: "))
                price = float(input("Enter Price: "))
                add_product(product_id, product_name, category_id, price)
                print("Product Added Successfully.")
                
            #Update product in the catalog
            elif admin_choice == 2:
                product_id = int(input("Enter Product ID: "))
                product_name = input("Enter New Product Name: ")
                category_id = int(input("Enter New Category ID: "))
                price = float(input("Enter New Price: "))
                update_product(product_id, product_name, category_id, price)
                print("Product Updated Successfully.")
                
            #Delete product from the catalog
            elif admin_choice == 3:
                product_id = int(input("Enter Product ID: "))
                delete_product(product_id)
                print("Product Deleted Successfully.")
                
            #Add category in the catalog
            elif admin_choice == 4:
                category_name = input("Enter Category Name: ")
                add_category(category_name)
                print("Category Added Successfully.")
                
            #Delete category from the catalog
            elif admin_choice == 5:
                category_name = input("Enter Category Name: ")
                delete_category(category_name)
                print("Category Deleted Successfully.")
                
            #Logout
            elif admin_choice == 6:
                print("Admin Logout Successful.")
                break
            else:
                print("Invalid Input. Try Again.")
    else:
        print("Invalid Admin Login. Try Again.")


def add_to_cart(session_id, product_id, quantity, user_type):
    if user_type == "admin":
        print("Error: Admins cannot modify the cart.")
        return
    # Add the item to the cart using the session id, product id, and quantity
    # ...

def delete_from_cart(session_id, product_id, quantity, user_type):
    if user_type == "admin":
        print("Error: Admins cannot modify the cart.")
        return
    # Delete the item from the cart using the session id, product id, and quantity
    # ...

def view_cart(session_id, user_type):
    if user_type == "admin":
        print("Error: Admins cannot view the cart.")
        return
    # View the items in the cart for the user with the given session id
    # ...

def add_product(product_id, name, category_id, price, user_type):
    if user_type != "admin":
        print("Error: Only admin can add products.")
        return
    # Add the product to the catalog using the product id, name, category id, and price
    # ...

def update_product(product_id, name, category_id, price, user_type):
    if user_type != "admin":
        print("Error: Only admin can update products.")
        return
    # Update the product in the catalog using the product id, name, category id, and price
    # ...

def delete_product(product_id, user_type):
    if user_type != "admin":
        print("Error: Only admin can delete products.")
        return
    # Delete the product from the catalog using the product id
    # ...

def add_category(category_name, user_type):
    if user_type != "admin":
        print("Error: Only admin can add categories.")
        return
    # Add the category to the catalog using the category name
    # ...

def delete_category(category_id, user_type):
    if user_type != "admin":
        print("Error: Only admin can delete categories.")
        return
    # Delete the category from the catalog using the category id
    # ...

