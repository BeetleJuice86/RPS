import random


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

#player input is int in relation to shape
player_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' Scissors:\n"))
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[player_choice])
    #random number for shape
    comp_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[comp_choice])

    if player_choice == 0 and comp_choice == 2:
        print("You win!")
    elif comp_choice == 0 and player_choice == 2:
        print("You lose!")
    elif comp_choice > player_choice:
        print("You lose!")
    elif player_choice > comp_choice:
        print("You win!")
    elif comp_choice == player_choice:
        print("Draw, try again!")
    else:
        print("What is going on?")
