"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Text-based adventure game, the user is presented a scenario with different options.

"""
print()
print()
print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"""                                   SURVIVING GAME: LIVE OR DEATH                                         """')
print('"""                                                                                                         """')
print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print()
print()


op1=input("Your plane is crashed, you survived, there are people death in the floor, in the middle of  Amazonas, suddenly you see a tiger, but he doesn't see you yet, you RUN or you play DEATH? ")


if (op1.upper()=='RUN'):
   op2=input("You are starting to RUN, the tiger see you like a prey! you see a cave in a few metters, you are so tired, and don't want to turn your head around, before the cave there is a tree, but you are not sure if you can climb it, what do you do? TREE or CAVE? ")
   print()
   print()
   
   if (op2.upper()=='TREE'):
    op3=input("You are in the top of the tree, but you were cutted by a branch, you are bleeding, what do going to do? PRAY or WAIT? ")
    print()
    print()
    
    if (op3.upper()=='PRAY'):
        print("After you prayed, you see an helicoptere that is looking survived people,  and the see you... you WIN, pray is always the key ")
        print("END OF THE GAME")
    elif (op3.upper()=='WAIT'):
        print("You starting to feel dizzy and suddendly you see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...")
        print("**GAME OVER**")
    else:
        print("OPTION INVALID")
        

   
   elif (op2.upper()=='CAVE'):
    
    op4=input("You are now in the cave, you cannot see anything, you starting to have an hiperventilation, you feel the mud in your shoes, you try to control your respiration, you hear the tiger, what do you do? PRAY or CRY? ")
    print()
    print()

    if (op4.upper()=='PRAY'):
        print("After you prayed, you see an helicoptere that is looking surviving people,  and the see you... you WIN, pray is always the key")
    
    elif (op4.upper()=='CRY'):
        print("Your tears help you to feel better, you starting to feel bites, you cannot smell or hear the tiger, but the bites make you crazy, one of them was a posoinous spider..You starting to feel dizzy and suddendly you see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too...")  
        print("YOU LOSE") 
        print("**GAME OVER**")
    
    else:
        print("OPTION INVALID")  
   
   else:  
     print("OPTION INVALID") 

elif (op1.upper()=='DEATH'):
    op5=input("You are playing that you are death, you see the tiger is eating someone else, so you crawl like a snake, you hear water like a RIVER near of you, but before there is TUNNEL which one are you going to choose? RIVER or TUNNEL ")
    print()
    print()
    if (op5.upper()=='RIVER'):
        op6=input("You are in the river now, you know how to swim, but is dark but you have faith, but it will be enough? Suddenly, you see a BOAT, but you are not sure if they are a good people because you are in the middle of the amazonas dont't forget that! so you see a little house on the side of the river, you are so tired, so you pick? HOUSE or BOAT")
        
        if (op6.upper()=='BOAT'):
            print("You are in the boat, they are a good people, fiu! you are safe now, you ...WIN ")
            print("END OF THE GAME")
        elif (op6.upper()=='HOUSE'):
            print("You are in the house, the people seems to be normal, but you noticed they are CANIVALES!! OH NO!! and suddendly you see your grand grandma, she tells you: why you are here my dear? and you got it, you are dead too..")
            print("YOU LOSE...")
            print("**GAME OVER**")
        else:
            print("OPTION INVALID ")   
    
    elif (op5.upper()=='TUNNEL'):
        op7=input("You are in the TUNNEL, you can't see well, you feel the mud heavy, the air, smells like something burnt, in the end of the tunnel you see a TRIBE, you are not sure if they are good people, if you continue, in the mud, you going to arrive to a village, you are so tired and hungry, what do you choose? TRIBE or VILLE ") 
        print()
        print()
        if (op7.upper()=='VILLE'):
            print("You are so tired, but you arrived to a VILLE, they are the survivors of the crash...you are safe now...you WIN ")  
            print("END OF THE GAME ")
        elif (op7.upper()=='TRIBE'):
            print("You arrived with the tribe, they don't speak your language, but they are good with you, you are safe now, sometimes you need to trust...you WIN ")
            print("END OF THE GAME")
        else: 
             print("OPTION INVALID ")

else:
     print("OPTION INVALID ")
     


