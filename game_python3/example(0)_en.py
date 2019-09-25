def bacon():
    spam = 99  # Creating a local variable named spam
    print(spam)  # Displays 99


spam = 42  # Create a global variable named spam
print(spam)  # Displays 42
bacon()  # Calls the bacon () function and outputs 99
print(spam)  # Displays 42
