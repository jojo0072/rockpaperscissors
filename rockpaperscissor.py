def game():
    import random
    title=print("\nRock, paper, scissor")
    user_action=input("\n\nChoose rock, paper or scissor: ").lower()
    possible_actions=("rock", "paper", "scissor")
    computer_action=random.choice(possible_actions)
    
    if user_action not in possible_actions:
        print("Invalid input. Please choose rock, paper, or scissor.")
        game()
        
    pc_a=print(f"Computer choose {computer_action}!")    

    if (user_action == "rock" and computer_action == "scissor") or \
    (user_action=="paper" and computer_action == "rock") or \
    (user_action =="scissor" and computer_action == "paper"):
        print("You win!!!")
    elif user_action == computer_action:
        print("It's a tie!!!")
    else:
        print("You lose!!!")
    play_again=input("Wanna play again (y/n)?: ")
    if play_again.lower()== "y":
        print("_________________________________________")
        game()
game()