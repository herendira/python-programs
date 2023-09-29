"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Text-based adventure game, the user is presented a scenario with different options.

"""
print("******SURVIVING GAME*****LIVE OR DEATH******")
def scene1():
    import time
    print("Your plane is crashed, you survived, there are people death in the floor, in the middle of an Amazonas, suddenly you see a tiger, but he doesn't see you yeat, you RUN or you play DEATH? ")
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="RUN"):
            print("\nYou starting to RUN, the tiger see you like a prey! you see a cave in a few metters, you are so tired, and don't want to turn your head around, before the cave there is a tree, but you are not sure if you can climb it")
            print("\n the tiger is faster than you...you starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...you lose **GAME OVER**")
            ans = 'correct'
        elif(c1.upper()=="DEATH"):
            print("the tiger is close to you but he is starting to eat someone else, you see a CAVE not soo far away, but you are so afraid to run ")
            ans='correct'
            scene2()
        else:
            print("RUN or DEATH?")
            c1 = input()

def scene2():
    import time
    print("the time pass and if you want to survive you need to decide to enter in the CAVE or climb the TREE")
    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="CAVE"):
            print("\nYou are now in the cave, you cannot see anything, you starting to have an hiperventilation, you feel the mud in your shoes, you try to control your respiration, you hear the tiger but you don't know if start to pray or cry ")
            time.sleep(2)
            print("Your tears help you to feel better, you starting to feel bites, you cannot smell or hear the tiger, the bites make you crazy...you starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...you lose **GAME OVER**")
            ans = 'correct'
            
        elif(c1.upper()=='TREE'):
            print("You are in the tree, the tiger starting to eat someone else, you cut your self with a branch, you are safe but you are bleeding ")
            ans='correct'
            scene3()
            
        else:
            print("CAVE or TREE?")
            c1=input()

def scene3():
    import time
    print("You start to feel cold but you know you need to continue to fight, you need to do something else, but what? so you start to regreat of all your sins and Pray for help, YES or NOT?")
    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="YES"):
            print("\nSuddenly you see an helicoptere searching living people, they see you!! you are safe now!! Pray always is the answer!! ")
            time.sleep(2)
            ans = 'correct'
            
        elif(c1.upper()=="NOT"):
            print("You starting to see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...**GAME OVER** ")
            ans='correct'
            
        else:
            print("YES OR NOT?")
            c1=input()
            scene1()
           
scene1()
print("\n\n")
