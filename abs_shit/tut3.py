def contacts():
    print("Welcome to contacts\n\n")

def settings():
    print("Welcome to settings")

def Apps():
    print("Welcome to Apps")

def Calculator():
    print("Maths baby")

def display_menu(op):
    if op==1:
        contacts()

    if op==2:
        settings()

    if op==3:
        Apps()

    if op==4:
        Calculator()


op=0

print("Please choose an application:\n"
      "1. Contacts\n"
      "2. Settings\n"
      "3. Apps\n"
      "4. Calculator\n\n")

op=input("\n\nPlease enter an option: ")

display_menu(op)