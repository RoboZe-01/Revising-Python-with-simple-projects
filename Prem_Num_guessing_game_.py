


import random 
get_num = random.randint(0,100)
while True:
    ask = input(" DO wanna play num guessing game (Y/N) : ").lower()
    
    if ask == "y":
     while True:
      choice = int(input("Enter Your Guess : "))
      if choice >= 0 :
        
        if choice == get_num :
           print (" Congratulation You got the Correct number !!")
        elif choice >= get_num :
           print(" Too high ")
        elif choice <= get_num :
           print(" Too low ")  
     else :
        print(" Enter positive number !! ")   
    elif ask == "n"   :
       print(" Ok no Problem ") 
       break     
    else :
       print(" Invalid ")
          

        

     