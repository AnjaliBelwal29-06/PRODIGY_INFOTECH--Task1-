import random


def guess_number_game():
    Random_number=random.randint(1,100)
    Attempts=0
    print("Welcome to the Guessing game...")


    Your_name=input("Enter your name: ")
    
    print("You think of a number between 1-100")


    while True:
      Your_guess=int(input("enter your guessing number: "))
      Attempts+=1

      if Your_guess<Random_number:
         print("Too low. Please Try again!!")



      elif Your_guess>Random_number:
        print("Too high. Please Try again!!")

        

      else:
        print(f"Congrats!,{Your_name} You won the game in {Attempts} Attempts")
        break
      

guess_number_game()
   


      

