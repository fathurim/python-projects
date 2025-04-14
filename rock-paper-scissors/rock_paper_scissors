#Janken

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

##Input option
me = input("What do you choose? Rock, Paper or Scissors? ").lower()

##Picture result
if me != "rock" and me != "paper" and me != "scissors":
  print("You typed an invalid option, you lose!")

else:
  rps = ["rock", "paper", "scissors"]
  me_index = rps.index(me)
  import random
  computer_index = random.randint(0,2)
  computer = rps[computer_index]

  print(f"You chose {me}")
  if me == "rock":
    print(rock)
  elif me == "paper":
   print(paper)
  else:
   print(scissors)



  print(f"Computer chose {computer}")
  if computer == "rock":
    print(rock)
  elif computer == "paper":
    print(paper)
  else:
    print(scissors)

##The winner
  if me == computer:
    print("It's a draw")
  elif me == "rock" and computer == "scissors":
    print("You win")
  elif me == "paper" and computer == "rock":
    print("You win")
  elif me == "scissors" and computer == "paper":
    print("You win")
  else:
    print("You lose")
