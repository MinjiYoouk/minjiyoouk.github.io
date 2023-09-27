# Purr Purr Cat Adventure
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
# 
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random

# an object describing our cat player
player = { 
    "name": "Whiskers", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "a wood cottage",
    "room2" : "a forest path",
    "room3" : "an alternate path"
}


def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result


def printGraphic(name):
    if (name == "cat"):
        print ('            /\_/\           ')
        print ('           ( o.- )          ')
        print ('            > ^ <           ')
        print ('            /   \           ')
        print ('        Purr..Purr..        ')
        print ('   Nice to see you friend!  ')

    if (name == "fish"):
        print ('         ><(((º>            ')
        print ('        Purr..Purr..        ')
        print ('         Yum! Yum!          ')

    if (name == "box"):
        print ('          ________          ')
        print ('         /       /|         ')
        print ('        /_______/ |         ')
        print ('        |       | |         ')
        print ('        |       | /         ')
        print ('        |_______|/          ')
        print ('        Purr..Purr..        ')
        print ('        I love Box!         ')

    if (name == "dog"):
        print ('           / \__            ')
        print ('          (    @\___        ')
        print ('         /         O        ')
        print ('        /   (_____/         ')
        print ('       /_____/   U          ')
        print ('        Purr..Purr..        ')
        print ('   Nice to see you friend!  ')


    if (name == "title"):
        print (' __________                   __________                      ')
        print (' \______   \__ _______________\______   \__ ________________  ')
        print ('  |     ___/  |  \_  __ \_  __ \     ___/  |  \_  __ \_  __ \ ')
        print ('  |    |   |  |  /|  | \/|  | \/    |   |  |  /|  | \/|  | \/ ')
        print ('  |____|   |____/ |__|   |__|  |____|   |____/ |__|   |__|    ')
                                                            

                                              
                                              


def gameOver():

    printGraphic("cat")

    print("-------------------------------")
    print("to be continued!")
    print("name: " + player["name"] ) # customized with a name
    print( "score: " + str(player["score"]) ) # customized with a score
    return

def strangePath():
    print("You're in luck, someone knows your birthday and has your favorite treat ready for you.")
    printGraphic("fish")
    input("press enter >")

    print("You consider your options.")
    print("options: [move around , keep going , back to cottage]")

    pcmd = input(">")

    if (pcmd == "search treat"): 
        print ("You search the treat...")
        print ("Let's roll a dice to see what happens next!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 10
        roll = rollDice(0, 20, difficulty)
        
        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print ("It look so delicious!")
            print ("Do you take the fish?")
            
            printGraphic("fish")

            # we dive further into the logic
            pcmd = input("yes or no >")

            if (pcmd == "no"):
                print ("You leave it there.")
                strangePath()

            elif (pcmd == "yes"):
                print ("You take the box and return to the cottage.")
                player["items"].append("box") # add an item to the array with append
                player["score"] += 100 # add to the score
                woodCottage()

            else:
                print ("You leave it there.")
                woodCottage()

        else:
            print ("Turns out it's nothing... oh well.")
            strangePath()

    elif (pcmd == "keep going"):
        print ("You keep going forward... you have a strange feeling")
        print ("that you keep seeing the same trees over and over...") # the lost woods reference
        woodCottage()

    elif (pcmd == "back to cottage"):
        print ("You decide to go back.")
        pcmd = input(">")
        woodCottage()

    else:
        print ("Oh!")
        strangePath()


def forestPath():
    print ("The forest path leads you down a narrow path of small town.")
    print ("I have a good feeling!")
    input("press enter >")

    printGraphic("cat")
    print ("You walk for a while and see a small cat jump onto the path")
    print ("Hi! Nice to meet you.")
    print ("...She can talk!")
    input("press enter >")
    
    print ("You consider your options.")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("box" in player["items"]):
        print ("options: [ look around , talk to cat , give box, run ]")
    else:
        print ("options: [ go back, talk to cat, run ]")

    pcmd = input(">")

    # option 1: look at the cat
    if (pcmd == "go back"):
        print ("You go back...")
        woodCottage() # try again
    
    # option 2: talk to the cat
    elif (pcmd == "talk to cat"):
        print ("You try and talk to the furry cat!")
        print ("Hey! Nice to meet you. Let's roll a dice to see what happens next!")
        input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("It's you're lucky day! He want's to be your friend.")
            player["score"] += 50
        else:
            print ("You try to talk to the cat, but... it looks at you confused.")
            forestPath() # try again
        
        # nested actions and ifs
        pcmd = input("be friends with the white cat? yes or no >")

        # yes
        if (pcmd == "yes"):

            print ("The cat becomes your friend!")
            printGraphic("cat")

            player["friends"].append("cat")

            # string and int converstion!
            # we need to convert the score to a number to add to it
            # then convert it back to a string to display it to the player
            player["score"] = int(player["score"]) + 100 # conversion

            # we generate a custom string and add the score
            print ( "Your score increased to: " + str(player["score"]) ) 
            
            gameOver()

        # no
        elif (pcmd == "no"):
            print ("The cat runs away!")
            forestPath()
        
        # try again
        else:
            forestPath()

    elif (pcmd == "give fish to dog"):
        print ("You give the treat to the dog!")
        input("press enter>")
        printGraphic("dog")
        gameOver()


    # option 3: run
    elif (pcmd == "run"):
        print ("You run!")
        woodCottage() # back to start

    # try again
    else:
        print ("I don't understand.")
        forestPath() # forest path

def woodCottage():
    print ("You stand in a cottage.")
    print ("There is a path ahead of you and another path to the right.")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

    if (("box" in player["items"]) and not ("cat" in player["friends"])):
        print ("Your options: [ look around, path, give the box to your friend]")

    elif ("box" in player["items"]):
        print ("Your options: [ look around, path, exit ]")

    else:
        print ("Your options: [ look around, path , other path , exit ]")

    pcmd = input(">") # user input

    # player options
    if (pcmd == "look around"):
        # its a trick!
        print ("You look around... the path behind you is .... gone?")

        input("press enter >")
        woodCottage()

    # path option
    elif (pcmd == "path"):
        print ("You take the path.")
        input("press enter >")
        forestPath() # path 1

    # path2 option
    elif (pcmd == "other path"):
        print ("You take the other path.")
        input("press enter >")
        strangePath() # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "exit"):
        print ("you exit.")
        return # exit the application
        
    elif (pcmd == "give the box to your friend"):
        print ("you give the box to your friend... hugh?")
        printGraphic("dog")

        print ("'tooooodaaloooooo'\", he says.") # escaped
        return # exit the application, secret ending

    else:
        print ("I don't understand that")
        woodCottage() # the beginning

def introStory():
    # let's introduce them to our world
    print ("Hello! What should I call your cat?")
    player["name"] = input("Please enter your cat name >")

    # intro story, quick and dirty (think star wars style)
    print ("Welcome to the purr purr " + player["name"] + "'s adventure!")
    print ("One day you went for a walk.")
    print ("As you wandered around your neighborhood, you came across a dark and mysterious forest.")
    print ("A mysterious story awaits you.")
    print ("Do you decide to go for it?")

    pcmd = input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You go deeper into the forest, you find a small cottage...")
        input("press enter >")
        woodCottage()
    else:
        print ("No? ... That doesn't work here.")
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens
