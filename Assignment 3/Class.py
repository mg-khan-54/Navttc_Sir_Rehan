"""Nested Fuction"""
# def parent():
#     print("this is nested function")
#     def child():
#         print("this is child function")
#     def child_2():
#         print("this is child_2 function")
#     child()
#     child_2()
# def main():
#    parent()
# main()

""" 2-Function return function."""
# def function_return_functuion(x,y):
#     add = x+y
#     return next_function(add)
#
# def next_function(add):
#     print(add)
#
# def main():
#     function_return_functuion(10,20)
# main()


""" 4-function take function as parameter."""
# def add(a,b):
#     return a+b
# def print_data(a):
#     print(a)
#
# def main():
#     print_data(add(10,30))
# main()



"""Make two functions :
1. convert Fahrenheit - It will take Celsius and will print it into
Fahrenheit.
2. convert Celsius - It will take Fahrenheit and will convert it
into Celsius."""

# def faren(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
#
# def celsius_fun(faren):
#     celsius = (faren - 32) * 5/9
#     return celsius
#
# def main():
#     print(faren(32))
#     print(celsius_fun(32))
#
# main()

"""Question 3:
Write a function in python to read the content from a text file
"poem.txt" line by line and display the same on screen."""
# with open("Poem.txt",'r',newline='' )as file:
#     for line in file:
#         print(line,end='')

"""Write a function in python to count the number of lines from a
text file "story.txt" which is not starting with an alphabet "T". """
COUNTER = 0
with open('Poem.txt') as file:
    for line in file:
        if line[0] != 'T' or line[0] != 't':
            COUNTER += 1
print("lines without T :",COUNTER)

"""You're going to write an interactive calculator!"""
# user_input = input("Enter a number: ")
#
# if len(user_input) >3:
#     print("You entered too many characters.")
# elif len(user_input)<1:
#     print("You entered too few characters.")
# else:
#     a = float(user_input[0])
#     operator = user_input[1]
#     c = float(user_input[2])
# print(a)
# print(operator)
# print(c)


