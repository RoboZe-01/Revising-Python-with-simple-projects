
import  random

num_to_guess = random.randint(0,20)
ask = input(" Can u guess the number !! ( Y/n) : ").lower()
while True :
     if ask == "y":
            print("Let's do it then !! ")
            while True :
            

                    try :
                        guess = int(input(" Enter your Guess between  to 20 "))
                        if guess < num_to_guess :
                            print("Too low !!")
                        elif guess> num_to_guess :
                            print("Too high !!")    
                        else :
                            print(" Congratulations !! , You got it right . ")    
                            break
                    except ValueError :
                        print(" Enter valid Number . ")        


     elif ask == "n":
          print(" No Problem !! ")
     else :
          print("Invalid Answer ")     

                


