import sys
import random

quotes = []

with open("quotes_file.txt", 'r') as text_file:
    for line in text_file:
        items = line.split('"')
        quote = items[1]
        quotes.append(quote)


menu = "MENU:\tEnter YES to view your daily quote\n\tEnter NO to quit\n"


print("\n","*"*41,"\n * Welcome to your Daily Quote Generator *\n","*"*41)
print(menu)

user_response_yes_count = 0

while True:
    user_response = input("Would you like to see your quote of the day?:  ")
    user_response = user_response.upper()

    if user_response == "NO":
        print("\n\tThanks for visiting! Be sure to come back tomorrow for more quotes!\n")
        sys.exit()

    elif user_response == "MENU":
        print("\n",menu)

    elif user_response == "YES":
        user_response_yes_count += 1
        # If has not recieved quote for the day, quote becomes available
        if user_response_yes_count <= 2:
            quote_idx = random.randint(0,len(quotes)-1)
            print("\n\tYour quote of the day is: {}".format(quotes[quote_idx]))
            print("")
            user_response_yes_count += 1
        # If user already got a quote for the day, ask to come back again tomorrow
        else:
            print("\n\tSorry. You have to wait until tomorrow to recieve your next quote. \n")
            sys.exit()
    else:
        print("\n\tBe sure to enter: YES to view quote of the day; NO to quit; or MENU for menu \n")