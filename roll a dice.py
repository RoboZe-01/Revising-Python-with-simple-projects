

# Advancement 1: Modify the program so user can specify how many times the want to roll the dice 
# Advancement 2 : Keep track on how many times they rolled a dice 

import random
# loop 
    # Ask user for input either y/n 



        # if user put y 
        # give two random number 
        #if user choose n :
        # print ( thank you )
        # else terminate the program  

    
while True :

    choice = input ( " Do you want to roll a dice (y/n) : ").lower()


    if choice == "y" :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')



    elif choice == "n"    :
        print("Thank you so Much ")
        break
    else :
        print ("Invalid ")
    
