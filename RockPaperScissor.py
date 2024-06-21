import random
user_score = 0
computer_score = 0

while True:

    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)


    user_choice = input("enter your choice(Rock/Paper/Scissors): ").lower()
    if user_choice not in ["rock","paper","scissors"]:
        print("Invalid.try again with valid choice")
        print()
        continue

    print(f"your choice is {user_choice}")
    print(f"computer choice is {computer_choice}")
    
    if computer_choice == user_choice :
        print("Match Tie")

    elif (user_choice == 'rock' and computer_choice == 'scissors') or\
       (user_choice == 'scissors' and computer_choice == 'paper') or\
       (user_choice == 'paper' and computer_choice == 'rock'):
        print("you won")

        user_score+=1

    else:
        print("you loose")
        computer_score+=1

    print(f"SCORES - You : {user_score} , computer score : {computer_score}")

    user_dec=input("Do you want to play another round? (yes/no): ").lower()
    if user_dec != "yes":
        break
print()

print(f"SCORES - You : {user_score} , computer score : {computer_score}")
if user_score>computer_score:
    print("You have highest score. So,You won the game!!")
elif user_score == computer_score:
    print("The game is tie")    
else :
    print("You loose!!.Because Computer has highest score. ")

print()

print("Thanks for playing!")