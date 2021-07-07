import re
import sys
# import random

quotes_file = open("quotes_file.txt", encoding="utf-8")
data = quotes_file.read()
quotes_file.close()

menu = "\t**Enter YES to view your daily quote**\n\t**Enter NO to quit**\n"

#quote = re.compile(r"""
#    ^(?P<quote>([-\w ]*)\t # Quote
#    (?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))$ # First Last Name
#""", re.X|re.MULTILINE)


#def quote(quote):
#    # open file
#    with open("quotes_file.txt", "r") as file:
#        # read thing to file
#        file.read(thing+"\n")

#def show():
    # open file
#    with open("quotes_file.txt") as file:
#        for line in file:
#            print(line)


print("Welcome to your Daily Quote Generator!")
print(menu)

user_response_yes_count = 0

while True:
    user_response = input("Would you like to see your quote of the day?:  ")
    user_response = user_response.upper()

    if user_response == "NO":
        print("\nThanks for visiting! Be sure to come back tomorrow for your new quote!\n")
        sys.exit()

    elif user_response == "MENU":
        print("\n",menu)

#TODO: Where do I add this to direct user to MENU or QUIT or YES
#        raise ValueError("Be sure to enter: YES to view quote of the day; NO to quit; or MENU for menu ")

    elif user_response == "YES":
        user_response_yes_count += 1
        if user_response_yes_count <= 2:
            print("\n\tYour quote of the day is:  {}".format(data))
            print("")
            user_response_yes_count += 1
        # If user already got a quote for the day, ask to come back again tomorrow
        else:
            print("\n\tSorry. You have to wait until tomorrow to recieve your next quote. \n")
            sys.exit()
