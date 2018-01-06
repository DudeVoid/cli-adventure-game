# Quest: part 1
print("Part 1: Introduction")
question_name = input("What is your name? ")
question_quest = input("What is your quest? ")
question_color = input("What is your favorite color? ")

print("\nAh, so your name is '{}', your quest is '{}' and your favorite color is '{}'.".format(question_name, question_quest, question_color)) 

# Quest: part 2
print("\nPart 2: The decision")
print("You are hit with a dangerous choice. You can only go one of three ways. Which do you choose?")
question_choice = input("\nHere are your choices\n1. Deadly Cavern\n2. Mysterious cave waterfall\n3. The pathway to nowhere\n")

print("\nYou have chosen {}. Let's hope that was the right way to go!".format(question_choice))
