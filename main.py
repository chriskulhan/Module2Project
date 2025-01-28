# Chris Kulhanek
# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    """Display a welcome message for the donut shop."""
    print("🍩 Welcome to North Loop Provisions!🍩")
    print("Crafting artisanal donuts in Minneapolis's North Loop")
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

    #Our complete menu organized by category
    donut_menu = { #dictionary list
        #list is the value for the key of Small Batch
        'Small Batch': [
            'Wild Rice & Honey',
            'Maple Bacon',
            'Swedish Cardomom'
        ],
        'Seasonal': [
            'Apple Cider',
            'Juicy Lucy',
            'Lake of the Woods'
        ], 
        'Local Collabs': [
            'Spyhouse Coffee Cake',
            'Fulton Beer and Pretzel',
            'Sweet Science Ice Cream'
        ]
    } #closing brace for the dictionary

        #Locally-sourced toppings
    toppings = [
        'House-Made Sprinkles',
        'Candied Hazelnuts',
        'Bee Pollen',
        'Cookie Butter Drizzle'
    ]
    
    # Track our morning sales with a dictionary (because there will be key-value pairs)
    morning_sales = []

    #record our first sale
    #Add a new item to a list by using .append to append a transaction to the sales dictionary
    morning_sales.append ({
        'item': 'Wild Rice & Honey',
        'quantity': 2,
        'toppings': ['Bee Pollen'],
        'time': '7:30 AM'
    })

    #Display our current menu using a for loop
    print("Today's Morning Menu:")
    for category, items in donut_menu.items():
        print(category + ":")
        for item in items:
            #this is a concatenation operator (using +) works 
            print(" - " + item)

