import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = [rock, paper, scissors]

computer = random.randint(0,2)

computer_choice = choice[computer]






def game():
  player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
  print(f"You chose: {choice[int(player)]}")
  print(f"Computer chose: {computer_choice}")
  if int(player) == int(computer):
    print("Draw!")
  elif int(player) ==0 and int(computer) ==2:
    print("You won!")
  elif int(player) ==1 and int(computer) ==0:
     print("You won!")
  elif int(player) ==2 and int(computer) ==1:
     print("You won!")
  else:
    print("You lose!")


game()

 






  





  



