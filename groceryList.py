
groceryList = []
a = True

print ("Hi!") 

while (a == True):
    print ("Do you want to add something to your grocery list?")
    answer = input()
    answer = answer.lower()

    if (answer == "yes"):
        print ("What would you like to add to your list?")
        groceries = input()
        groceryList.append(groceries)
        print ("Your grocery list currently contians:")
        for x in groceryList:
            print(x)
        
    elif (answer == "no"):
        print ("Ok. Your final grocery list contains:")
        for x in groceryList:
            print(x)
        a = False
        exit()

    else:
        print ("Please answer yes or no.")

