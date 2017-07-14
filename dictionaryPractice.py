#myDict = {}
contactBook = {}
add = True
add2 = True
add3 = True
lissy = []

while add == True:
    print("Would you like to add a contact to your contact book? (y/n)")
    answer = input().lower()
    
    if (answer == 'y'):
        print("What is the name of the contact?")
        name = input()
        number = ""
        address = ""
        add2 = True
        add3 = True

        while add2 == True:
            print("Do you want to add the phone number of %s? (y/n)" %name)
            numberAns = input()
            if (numberAns == 'y'):
                print("What is the phone number?")
                number = input()
                lissy.append(number)
                add2 = False
            elif (numberAns == 'n'):
                add2 = False
            elif (numberAns != 'n'):
                print("Please enter 'y' or 'n'")

        while add3 == True:            
            print("Do you want to add an address? (y/n)")
            addressAns = input()
            if (addressAns == 'y'):
                print("What is the address?")
                address = input()
                lissy.append(address)
                add3 = False
            elif (addressAns == 'n'):
                add3 = False
                add = False
            else:
                print("Please enter 'y' or 'n'")

        
        contactBook[name] = [lissy]
        
    elif (answer == 'n'):
        add = False
    else:
        print("Please enter 'y' or 'n'")


print("Your dictionary has been saved!")
print("_____________________________________________")
print()
print("Your contact book:")
print()

for key in contactBook:
    print("Name: " + key)
    #number = contactBook[key]
    if len(lissy) == 2:
        print("Number: " + lissy[0])
        print("Address: " + lissy[1])
    elif len(lissy) == 1:
        print(lissy[0])
    else:
        print()

#_______________________________________________________________________________
    
    #defineType = type(number)
    
    #if (defineType == str):
        #print("Phone number: " + number)
        
    #elif (defineType == list):
        
        #for x in number:
            #print("- " + x)
    #print()
