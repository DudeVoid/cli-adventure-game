import random

class Game:
  def __init__(self):
    # Put variables you need across the entire game here
    # Access them with self.var in any other function in the class
    # ALL class functions HAVE to have the `self` parameter at the start
    self.difficulty = 0

  def choice(self, choices: list, arg=""):
    choices_string = ""
    for choice in choices:
      # We add one so that the game visually doesn't start the list at '0'
      choices_string += f"{choices.index(choice) + 1}. {choice}\n"

    chosen = input(f"\nHere are your choices:\n{choices_string}")

    # This try/except is here because num can sometimes be a string since
    # people are stupid when they play CLI games and enter whatever they feel like
    try:
      num = int(chosen)
      # We subtract one here because we added one for the end user before ^
      num -= 1

      # Again subtracting one because lists start at 0
      if not num in range(0, len(choices) - 1):
        # This person either picked a negative number,
        # or something with a larger index than the list of choices xD
        print("Please choose something actually in the list.")
        return self.choice(choices)
    except ValueError:
      print("Please choose a number.")
      return self.choice(choices)
    
    # If nothing failed, we return the choice
    return choices[num]

  def quest(self):
    # Quest: part 1
    print("Part 1: Introduction")
    q_name = input("What is your name? ")
    q_quest = input("What is your quest? ")
    q_colour = input("What is your favorite colour? ")

    print(f"\nAh, so your name is {q_name}, your quest is {q_quest} and your favorite colour is {q_colour}.")

    # Quest: part 2
    print("\nPart 2: The decision")
    print("You are hit with a dangerous choice. You can only go one of three ways. Which do you choose?")

    # Get the choice back from the function when the user picks a valid one
    choice = self.choice([
      'Deadly cavern',
      'Mysterious cave waterfall',
      'The pathway to nowhere'
    ])

    print(f"\nYou have chosen {choice}. Let's hope that was the right way to go!")

# Initalize class
game = Game()

# Begin game. Very spicy.
game.quest()
