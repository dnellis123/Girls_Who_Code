print("Welcome to the Zoo! We have 3 exhibits for you to choose from.")
print("You have 12 hours from 9am to 9pm to do whatever the heck you want!")
print("You can visit the rainforest, desert, or aquatic exhibit. Which do you choose?")


choosingExhibit = True
exhibitChoice = ""
stealChoice = ""
time = 12

while choosingExhibit == True:
    exhibitChoice = input()

    if (exhibitChoice == "rainforest"):
        #choosingExhibit = False
        print("Welcome to the Rainforest!")
        print("You can visit the frogs (1 hr) or the sloths (2 hr)")
        print("Which do you choose?")

        rainforestChoice = input()
        if (rainforestChoice == "leave"):
            exit()
            print("Have a nice day! BYYYYYYEEEE!")
        elif(rainforestChoice == "frogs"):
            print("Great choice! Did you know that frogs don't drink water but absorb it through their skin?!")
            time -= 1
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")
        elif(rainforestChoice == "sloths"):
            print("Great choice! Did you know that sloths can take months to digest a meal?")
            time -= 2
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")

    elif(exhibitChoice == "desert"):
        #choosingExhibit = False
        print("Welcome to the Desert!")
        print("You can visit the snakes (1 hr) or the gazelles (2 hr)")
        print("Which do you choose?")

        desertChoice = input()
        if (desertChoice == "leave"):
            exit()
            print("Have a nice day! BYYYYYYEEEE!")
        elif(desertChoice == "snakes"):
            print("Great choice! Did you know that snakes smell with their tongues!")
            time -= 1
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")
        elif(desertChoice == "gazelles"):
            print("Great choice! Did you know that gazelles are orginally from India, not Africa?")
            time -= 2
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")

    elif(exhibitChoice == "aquatic"):
        #choosingExhibit = False
        print("Welcome to the Aquatic!")
        print("You can visit the dolphins (3 hrs) or the turtles (2 hrs)")
        print("Which do you choose?")

        aquaticChoice = input()
        if (aquaticChoice == "leave"):
            exit()
            print("Have a nice day! BYYYYYYEEEE!")
        elif(aquaticChoice == "dolphins"):
            print("Great choice! The killer whale is actually a type of dolphin! WHAAAAA?!")
            time -= 3
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")
        elif(aquaticChoice == "turtles"):
            print("Great choice! Turtles have existed around 215 million years!")
            time -= 2
            print("You have %d hours left" %(time))
            print("That was the end of this exhibit. Please choose another one: rainforest, desert, aquatic.")
    elif exhibitChoice == "leave":
        print("Have a nice day! BYYYYYYEEEE!")
        exit()

    if time < 6:
       
        print("hey....")
        print("Do want to do steal... an animal? :) (type in yes or no)")
        stealChoice = input()
        if stealChoice == "yes":
            print("Which animal: penguin(2 hr), pigeon(1 hr), or sea otter(3 hr)?")
            choiceAnimal = input()
            if (choiceAnimal == "penguin"):
                print("You broke into the Artic exhibit, disguised as a giant mother penguin.")
                print("The moment you walked in, all of the penguins flocked towards you, expecting to be fed.")
                print("After feeding them, you let go all but one, named HAPPY FEET.")
                print("You ran off happily with the love of your life and now you and Happy Feet live in a cute house in Japan.")
                exit()
            #elif 
                      
            
        elif stealChoice == "no":
            print("Fine then, goody-two-shoes.")
            print("Bye :( you didn't hear anything...")
            exit()
        
    else:
        print("Please choose one of the exhibits listed above or type leave to exit the zoo.")
      
    
        


        
