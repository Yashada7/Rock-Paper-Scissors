#Code by Yashada Tembe

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

game_images=[rock,paper,scissors]

a=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
print("You choose: ")
print(game_images[a])

computer=random.randint(0, 2)
print("Computer chose:")
print(game_images[computer])

if a>=3 or a<0:
    print("You typed an invalid number. You lose.")
elif a==0 and computer==2:
  print("You win!")
elif computer>a:
  print("You lose.")
elif computer==a:
  print("It's a draw.")
elif a>computer:
  print("You win!")
