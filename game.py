"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Text-based adventure game, the user is presented a scenario with different options.

"""
print()
print("******SURVIVING GAME*****LIVE OR DEATH******")
option=str(input("Your plane is crashed, you survived, there are people death in the floor, in the middle of an Amazonas, suddenly you see a tiger, but he doesn't see you yeat, you RUN or you play DEATH? "))
if option.upper()=="RUN":
    option1=str(input("You starting to RUN, the tiger see you like a prey! you see a cave in a few metters, you are so tired, and don't want to turn your head around, before the cave there is a tree, but you are not sure if you can climb it, what do you do? TREE or CAVE? "))

    if option1.upper()=="CAVE":
        option2=input("You are now in the cave, you cannot see anything, you starting to have an hiperventilation, you feel the mud in your shoes, you try to control your respiration, you hear the tiger, what do you do? PRAY or CRY? ")
        if option2.upper()=="PRAY":
            print("Suddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!! YOUR WIN!! ")
        else:
            option2.upper()=="CRY"
            option3=str(input("Your tears help you to feel better, you starting to feel bites, you cannot smell or hear the tiger, but the bites make you crazy, what do you do? GO out of the the cave or STAY because of the tiger "))
            if option3.upper()=="GO":
                option4=str(input("You are now out, the bites came of the spiders, you starting to regreat of all your sins and Pray for help, YES or NOT? "))
                if option4.upper()=="YES":
                   print("Suddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!! ")
                else:
                    option4=="NOT"
                    print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...**GAME OVER**")

            else:
                option3.upper()=="STAY"
                print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...you lose **GAME OVER**")
    else:
        option1.upper=="TREE"   
        option=str(input("You are in the tree, the tiger starting to eat someone else, you cut your self with a branch, you are safe but you are bleeding, what do you do? PRAY or WAIT you death "))
        if option.upper()=="PRAY":
          print("Suddenly you see an helicopter searching living people, they see you!! you are safe now!! Pray always is the answer!! YOUR WIN!!")
        else:
            print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...**GAME OVER**")
else:
    option.upper()=="DEATH"
    option1=str(input("the tiger is close to you but he starting to eat someone else, you see a CAVE not soo far away, but you are so afraid to run, there is a TREE and you thing you probably can climb it, what do you do? CAVE or TREE "))
    if option1.upper()=="CAVE":
        option2=str(input("You are now in the cave, you cannot see anything, you starting to have an hiperventilation, you feel the mud in your shoes, you try to control your respiration, you hear the tiger, what do you do? PRAY or CRY? "))
        if option2.upper()=="PRAY":
            print("Suddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!! YOUR WIN!! ")
        else:
            option2.upper()=="CRY"
            option3=str(input("Your tears help you to feel better, you starting to feel bites, you cannot smell or hear the tiger, but the bites make you crazy, what do you do? GO out of the the cave or STAY because of the tiger "))
            if option3.upper()=="GO":
                option4=str(input("You are now out, the bites came of the spiders, you starting to regreat of all your sins and Pray for help, YES or NOT? "))
                if option4.upper()=="YES":
                   print("Suddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!!")
                else:
                    option4=="NOT"
                    print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...**GAME OVER**")

            else:
                option3.upper()=="STAY"
                print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...you lose **GAME OVER**")
    else:
        option1.upper=="TREE"   
        option=str(input("You are in the tree, the tiger starting to eat someone else, you cut your self with a branch, you are safe but you are bleeding, what do you do? PRAY or WAIT you death "))
        if option.upper()=="PRAY":
          print("Suddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!! YOUR WIN!!")
        else:
            print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...**GAME OVER**")
