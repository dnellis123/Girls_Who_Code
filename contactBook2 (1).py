myContacts = {"Emergency":["Phone Number","911"]}

#FUNCTIONS
def addToContacts():
    addContact = True

    while addContact == True:

        print("Would you like to add a contact to your Contacts? (y/n)")
        answer = input().lower()

        if (answer == 'y'):
            print("What is the name of the contact?")
            name = input()
            contact = []

            print("Would you like to add a phone number? (y/n)")
            answer2 = input()

            if (answer2 == 'y'):
                print("Enter the phone number")
                contact.append("Phone Number")
                number = input()
                contact.append(number)

            print("Would you like to add an email address?")
            answer3 = input()

            if (answer3 == 'y'):
                print("Enter the email address")
                contact.append("Email")
                email = input()
                contact.append(email)

            if (len(contact) == 0):
                contact.append("Empty")

            myContacts[name] = contact

            print("Contact Saved!")
            print()

        elif (answer == 'n'):
            addContact = False
            print()
            print("All your Contacts have been saved!")
            print()

        else:
            print("Please enter 'y' or 'n'")


def printContacts():
    print("________________________")
    print()
    print("MY CONTACTS:")
    print()

    for contact in myContacts:
        print("Name: " + contact)

        info = myContacts[contact]
        if (len(info) == 1):
            print(info[0])
        else:
            location = 0

            while(location < len(info)):
                print(info[location] + ": " + info[location + 1])
                location += 2

        print()


            
#RUNNING CODE
addToContacts()
printContacts()











