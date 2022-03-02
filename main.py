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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

pc_choice = random.randint(0, 2)
print(game_images[pc_choice])


if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
  
elif user_choice==0 and pc_choice==1:
  print('You are loser, you chose rock and your opponent chose paper')
  
elif user_choice==0 and pc_choice==1:
  print('You are loser, you chose rock and your opponent chose paper')

elif user_choice==0 and pc_choice==2:
  print('You are winner, you chose rock and your opponent chose scissors')
elif user_choice==2 and pc_choice==0:
  print('You are loser, you chose scissors and your opponent chose rock')
elif user_choice>pc_choice:
  print('You are winner')
elif pc_choice>user_choice:
  print('You are loser')
elif pc_choice==user_choice:
  print('Draw')

  
  
