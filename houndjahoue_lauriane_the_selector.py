"""
Description: This Python program facilitates user-driven 
decision-making by providing recommendations
in various categories such as movies, snacks, and hobbies. 
Users can add, modify, and randomly select options within
a chosen category, with the flexibility to either explore
additional categories or exit the program.

Author: Lauriane Houndjahoue
"""
from random import choice

categories = {"movies": ["Girl from Nowhere", "Sweet Home", "The Glory"],
              "snacks": ["Potato Chips", "Ritz", "Twix"],
              "hobbies": ["Reading", "Cooking", "Painting"]}
#welcome message
print("\nWelcome to the 'Selector'!")
print("=======================================================================================\n")

while True:
    #allow user to pick a category
    user_choice = input("What category would you like to select from? (Movies, Snacks, Hobbies, or 'exit' to end): ").lower()
    #allowing user to exit the program
    if user_choice == "exit":
        print("Exiting the program. Goodbye!")
        break
    #checking user's input is valid
    if user_choice in categories:
        print(f"You chose {user_choice}! Here are some recommendations:")
        print(categories[user_choice])

        #allwing user to add more options
        add_more_options = input("\nWould you like to add some more options? (y or n): ").lower()
        while add_more_options == "y":
            new_option = input("Enter a new option: ")
            categories[user_choice].append(new_option)
            add_more_options = input("Would you like to keep going? (y or n): ").lower()
        print("")
        print(categories[user_choice])
        print("")

        #picking a random choice for user
        random_choice = input("Would you like the program to pick a random choice from the options? (y or n): ").lower()
        if random_choice == "y":
            selected_option = choice(categories[user_choice])
            print("Randomly selected option:", selected_option)

    else:
        print("Invalid selection. Try again!")
    print("")
    change_category = input("Would you like to select a different category? (y or n): ").lower()
    if change_category != "y":
        print("Exiting the program. Goodbye!")
        break
