import re
import sys
# import random

quotes_file = open("quotes_file.txt", encoding="utf-8")
data = quotes_file.read()
quotes_file.close()


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
print("\tEnter YES to view your daily quote")
print("\tEnter NO to quit\n")


while True:
    user_response = input("Would you like to see your quote of the day?:  ")
    user_response = user_response.upper()
    user_response_yes_count = 1

    if user_response == "NO":
        print("\nThanks for visiting! Be sure to come back tomorrow for your new quote!\n")
        sys.exit()

#TODO: Where do I add this to direct user to QUIT or YES
#        raise ValueError("Be sure to enter QUIT to quit or YES to view quote of the day")
    
#    if user_response == "YES":
    if user_response_yes_count > 2:
        print("\nYour quote of the day is:  {}".format(data))
        print("")
        user_response_yes_count += 1

    #TODO: if user already got a response, and says 'yes' again, can I say "Sorry. You have to wait til tomorrow"
    if user_response == "YES":
        print("Sorry. You have to wait until tomorrow to recieve your next quote. \n")
        sys.exit()