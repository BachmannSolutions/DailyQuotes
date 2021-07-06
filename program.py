import re
import sys


#quotes_file = open("quotes_file.txt", encoding="utf-8")
#data = quotes_file.read()

#quote = re.compile(r"""
#    ^(?P<quote>([-\w ]*)\t # Quote
#    (?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))$ # First Last Name
#""", re.X|re.MULTILINE)

#quotes_file.close()


#def quote(thing):
    # open file
#    with open("database.txt", "r") as file:
        # read thing to file
#        file.read(thing+"\n")

#def show():
    # open file
#    with open("database.txt") as file:
#        for line in file:
#            print(line)

        
print("Welcome to your Daily Quote Generator!")
print("\tEnter YES to view your daily quote")
print("\tEnter QUIT to quit\n")


while True:
    user_response = input("Would you like to see your quote of the day?:  ")
    user_response = user_response.upper()

    if user_response == "QUIT":
        print("\nThanks for visiting! Be sure to come back tomorrow for your new quote!\n")
        sys.exit()
    elif user_response == "YES":
        print("Your quote of the day is:  ")
        print("")
        #TODO: if user already got a response, and says 'yes' again, can I say "sorry. have to wait til tomorrow"
