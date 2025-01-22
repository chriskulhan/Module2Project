# Chris Kulhanek
# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    """Display a welcome message for the donut shop."""
    print("🍩 Welcome to North Loop Provisions!🍩")
    print("Crafting artisinal donuts in Minneapolis's North Loop")
    print("---------------------------------------")

def show_menu():
    #Display current donut menu
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "Lingenberry": 4.25,
        "Local Honey": 4.00
    }

    print("\nToday's Donut Menu:")
    print("----------------")

    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")

#Main program
#this main function is the director of the show
#this will be first (not required but good practice)
if __name__ == "__main__" :
    #call the welcome message
    welcome_message()
    #call the show menu message
    show_menu()
    print("\nReady to serve our community with the finest donuts!")
