from datetime import datetime

"""Question 1:
Write a function in python to read the content
from a text file "poem.txt" line by line and
display the same on screen."""
# def read_file():
#     """This function opens a .txt file and print all lines one by one"""
#     with open("poem.txt", "r", newline='', encoding='utf-8') as file:
#         for line in file:
#             print(line, end="")
#
#
# read_file()

"""Question 2:
Write a function in python to count the number of lines from a text file "story.txt" which
is not starting with an alphabet "T"."""
# def count_alphabet():
#     """This function opens poem.txt and
# counts lines which starts with 'T'"""
#     alphabet_counter = 0
#     with open("poem.txt", "r" , encoding='utf-8') as story:
#         for line in story:
#             if line[0] == 'T' or line[0] == 't':
#                 alphabet_counter += 1
#     print(alphabet_counter)
#
# count_alphabet()

"""Question 3:
Write a function in Python to read lines from a text
file "notes.txt". Your function should
find and display the occurrence of the word "the"."""

# def count_the_occurrence():
#     """This function opens poem.txt and counts the word 'the'
# and prints total number of occurrence."""
#     count_the = 0
#     with open("poem.txt", "r") as file:
#         for line in file:
#             length_line = len(line)
#             for index in range(0, length_line):
#                 if length_line < index + 3:
#                     continue
#                 alphabet_1 = line[index].capitalize()
#                 alphabet_2 = line[index + 1].capitalize()
#                 alphabet_3 = line[index + 2].capitalize()
#                 if alphabet_1 == "T" and alphabet_2 == "H" and alphabet_3 == "E":
#                     count_the = count_the + 1
#     print(count_the)
#
#
# count_the_occurrence()

"""Question 4:
Write a Python program to create a person class. Include attributes like name, country
and date of birth. Implement a method to determine the person’s age."""
# class Person:
#     """This is a Person class"""
#
#     name = 'Ghani'
#     age = 0
#     country = 'Pakistan'
#     def get_data(self):
#         """This function takes value from user"""
#         self.name = input('Name: ')
#         self.age = input('Age: 2000-06-26 ')
#     def calculate_age(self):
#         """This function calculates the age and prints the data on console"""
#         today = datetime.today()
#         current_year = self.age[0:4]
#         current_age = today.year - int(current_year)
#         print(f"""Name: {self.name}
# Age: {current_age}
# Country: {self.country}""")
# def main():
#     """This is main function"""
#     person_obj = Person()
#     person_obj.get_data()
#     person_obj.calculate_age()
#
# main()

"""Question 5:
Write a Python program to create a class representing a bank. Include methods for
managing customer accounts and transactions.
Hint:
Create a class bank with create account.
A class bank with make deposit.
A class bank with make withdrawal.
A class bank with check balance.
Create an object of the class and execute all functions"""

# class Bank():
#     account_title = ''
#     account_number = ''
#     account_balance = 0
#
#     def __init__(self, account_title, account_number, account_balance):
#         self.account_title = account_title
#         self.account_number = account_number
#         self.account_balance = account_balance
#
#     def menu_account(self):
#         print(self.account_title)
#         print(self.account_number)
#         print(f"Your Account balance is: {self.account_balance}")
#         option = input("""Enter your choice:
# 1 for deposit
# 2 for withdrawal \n""")
#         ammount = int(input('Enter your amount: '))
#         if option == '1':
#             return self.cash_deposit(ammount)
#         elif option == '2':
#             if self.account_balance < ammount:
#                 print("insufficient balance")
#             else:
#                 return self.cash_withdrawal(ammount)
#
#     def cash_deposit(self, amount):
#         self.account_balance = self.account_balance + amount
#         print(f"Your new Account balance is:{self.account_balance}")
#
#     def cash_withdrawal(self, amount):
#         self.account_balance = self.account_balance - amount
#         print(f"Your new Account balance is:{self.account_balance}")
#
#
# def main():
#     account = Bank('Muhammad Ghani', '03236220946', 1500)
#     account.menu_account()
#
#
# main()

"""Question 5:
Write a Python program to create a class representing a shopping cart. Include methods
for adding and removing items, and calculating the total price.
Hint:
Create a class with functions add_item, remove_item, and calculate_total.
Create an object of a class and called functions of class."""


# class ShoppingCart():
#     """This is a class that stores information about a shopping cart."""
#     item_list = {'apple': 30, 'banana': 10, 'cherry': 10, 'orange': 25}
#     cart = {}
#
#     def cart_menu(self):
#         """This is a method that displays the cart menu."""
#         item_code = 1
#         print("Sr.\tItems\tPrice")
#         for item, price in self.item_list.items():
#             print(f"{item_code}\t{item}\t\t{price}")
#             item_code += 1
#         self.add_cart()
#
#     def add_cart(self):
#         """This is a method that adds items to the cart."""
#         item = ""
#         check = True
#         while check:
#             available = True
#             while available:
#                 item = input("Select item: ")
#                 if item not in self.item_list:
#                     print("Item is not available")
#                 else:
#                     available = False
#             quantity = int(input("Quantity: "))
#             if item in self.cart:
#                 qty = self.cart[item]+ quantity
#                 self.cart[item] = qty
#             else:
#                 self.cart[item] = quantity
#             option = input("Would you like to add another item? (y/n): ")
#             if option == 'y':
#                 check = True
#             elif option == 'n':
#                 # print(self.cart)
#                 print("Thank you!\n")
#                 check = False
#             else:
#                 print("Thank you!\n")
#                 check = False
#         self.show_cart()
#
#     def remove_cart(self):
#         """This is a method that removes items from the cart."""
#         # self.show_cart()
#         checkout = True
#         while checkout:
#             available = True
#             while available:
#                 item = input("Select item: ")
#                 if item not in self.cart:
#                     print("Item is not available")
#                 else:
#                     available = False
#             del self.cart[item]
#
#             option = input("Would you like to remove another item? (y): ")
#             if option == 'y':
#                 checkout = True
#             elif option == 'n':
#                 print("Thank you!\n")
#                 checkout = False
#             else:
#                 print("Thank you!\n")
#                 checkout = False
#         self.show_cart()
#
#     def show_cart(self):
#         """This is a method that displays the cart."""
#         print("Your cart items are:")
#         print("Item\tQuantity\tPrice")
#         print()
#         for item, quantity in self.cart.items():
#             price_item = self.item_list[item]
#             print(f"{item}\t\t{quantity}\t\t{price_item * quantity}")
#         print()
#         self.edit_cart()
#
#     def edit_cart(self):
#         """This is a method that displays menu of cart operations."""
#         print("Would you like to edit your cart?: ")
#         print("Enter 1 for add item")
#         choice = input("Enter 2 for remove item")
#         print("Press any key to exit the cart:")
#         if choice == '1':
#             self.cart_menu()
#         elif choice == '2':
#             self.remove_cart()
#         else:
#             exit()
#
# cart = ShoppingCart()
# cart.cart_menu()
