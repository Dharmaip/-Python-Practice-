name = input("What is your name?")
#asking the user age
age = int(input("How old are you?"))
#added by 1 for next year's age
number = age + 1 
print("Hello {}!, you will be {} next year!".format(name.title(), number))
print("Anyways, do you have any pets? Answer with yes or no")
answer = input().lower()
#Added a loop to keep asking until a valid answer is received
while answer not in ["yes", "no", "y", "n"]:
    print("Invalid input. Please answer with yes or no.")
    answer = input().lower()

if answer == "yes" or "y" or "yeah":
    pet_type = input("What type of pet do you have? ")
    print("Oh nice! A {} must be a great companion!".format(pet_type))
else:
    print("Thanks for letting me know!")
pet_name = input("What is your pet's name? ")
pet_age = input("How old is your pet? ")
print("Your pet's name is {} and they are {} years old.".format(pet_name, pet_age))
