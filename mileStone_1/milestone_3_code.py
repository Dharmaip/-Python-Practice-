print("Wellcome to the quiz game!I wil ask you some questions and you will have to answer them correctly to win the game!")
print("There will be 15 questions you have to answer. Let's start!")
print("What is the capital of France? ")
#"Answer"" is where the input is going to be stored
answer = input().lower()
attempts = 0
while answer not in ["paris", "Paris", "paris france"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["paris", "Paris", "paris france"]:
    print("Correct! Paris is the capital of France.")
else:
    print("Incorrect! The correct answer is Paris.")

print("Question number 2!")
print("What is the largest planet in our solar system? ")
attempts = 0
answer = input().lower()
while answer not in ["jupiter", "Jupiter"] and attempts < 2:
        print("Incorrect! Please try again.")
        answer = input().lower()
        attempts += 1
if answer in ["jupiter", "Jupiter"]:
    print("Correct! Jupiter is the largest planet in our solar system.")
else:
    print("Incorrect! The correct answer is Jupiter.")

print("Question number 3!")
print("What is the chemical symbol for water? ")
attempts = 0
answer = input().lower()
while answer not in ["h2o", "H2O"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["h2o", "H2O"]:
    print("Correct! The chemical symbol for water is H2O.")
else:
    print("Incorrect! The correct answer is H2O.")

print("Question number 4!")
print("What is the capital of Japan? ")
answer = input().lower()
attempts = 0
while answer not in ["tokyo", "Tokyo"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts +- 1
if answer in ["tokyo", "Tokyo"]:
    print("Correct! Tokyo is the capital of Japan.")
else: 
    print("Incorrect! The correct answer is Tokyo ")

print("Question number 5!")
print("What is the largest mammal in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["blue whale", "Blue Whale"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts +- 1
if answer in ["blue whale", "Blue Whale"]:
    print("Correct! The blue whale is the largest mammal in the world.")
else:
    print("Incorrect! The correct answer is Blue Whale ")

print("Question number 6!")
print("What is the smallest country in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["vatican city", "Vatican City"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["vatican city", "Vatican City"]: 
    print("Correct! Vatican City is the smallest country in the world.")
else:
    print("Incorrect! The correct answer is Vatican City.")

print("Question number 7!")
print("What is the largest desert in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["sahara", "Sahara"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["sahara", "Sahara"]:
    print("Correct! The Sahara is the largest desert in the world.")
else:
    print("Incorrect! The correct answer is Sahara.")

print("Question number 8!")
print("What is the longest river in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["nile", "Nile"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["nile", "Nile"] and attempts < 2:
    print("Correct! The Nile is the longest river in the world.")
else:
    print("Incorrect! The correct answer is Nile river.")

print("Question number 9!")
print("What is the largest ocean in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["pacific", "Pacific"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["pacific", "Pacific"]:    
    print("Correct! The Pacific Ocean is the largest ocean in the world.")
else:
    print("Incorrect! The correct answer is Pacific Ocean.")

print("Question number 10!")
print("What is the capital of Italy? ")
answer = input().lower()
attempts = 0
while answer not in ["rome", "Rome"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["rome", "Rome"]:
    print("Correct! Rome is the capital of Italy.")
else:
    print("Incorrect! The correct answer is Rome.")

print("Question number 11!")
print("What is the largest continent in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["asia", "Asia"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["asia", "Asia"]:
    print("Correct! Asia is the largest continent in the world.")
else:
    print("Incorrect! The correct answer is Asia.")

print("Question number 12!")
print("What is the capital of Spain? ")
answer = input().lower()
attempts = 0
while answer not in ["madrid", "Madrid"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["madrid", "Madrid"]:
    print("Correct! Madrid is the capital of Spain.")
else:
    print("Incorrect! The correct answer is Madrid")

print("Question number 13!")
print("What is the largest country in the world? ")
answer = input().lower()
attempts = 0
while answer not in ["russia", "Russia"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["russia", "Russia"]:
    print("Correct! Russia is the largest country in the world.")
else:
    print("Incorrect! The correrct answer is Russia.")

print("Question number 14!")
print("Who created the first computer? ")
answer = input().lower()
attempts = 0
while answer not in ["charles babbage", "Charles Babbage"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["charles babbage", "Charles Babbage"]:
    print("Correct! Charles Babbage is considered the father of the computer.")
else:
    print("Incorrect! The correct answer is Charles Babbage.")

print("Question number 15!")
print("What is the most abundant element in the universe? ")
answer = input().lower()
attempts = 0
while answer not in ["hydrogen", "Hydrogen"] and attempts < 2:
    print("Incorrect! Please try again.")
    answer = input().lower()
    attempts += 1
if answer in ["hydrogen", "Hydrogen"]:
    print("Correct! Hydrogen is the most abundant element in the universe.")
else:
    print("Incorrect! The correct answer is Hydrogen.")

print("Congratulations! You have completed the quiz game!")
print("You answered all questions correctly! You are a genius!")