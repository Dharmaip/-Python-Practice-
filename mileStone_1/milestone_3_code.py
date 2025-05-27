print("Wellcome to the quiz game!I wil ask you some questions and you will have to answer them correctly to win the game!")
print("There will be 20 questions you have to answer. Let's start!")
print("What is the capital of France? ")
#"Answer"" is where the input is going to be stored
answer = input().lower()
while answer not in ["paris", "Paris", "paris france"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["paris", "p", "Paris", "paris france"]:
    print("Correct! Paris is the capital of France.")
print("Question number 2!")
print("What is the largest planet in our solar system? ")
answer = input().lower()
while answer not in ["jupiter", "Jupiter"]:
        print("Incorrect! Please try again.")
        answer = input().lower()
if answer in ["jupiter", "Jupiter"]:
    print("Correct! Jupiter is the largest planet in our solar system.")
print("Question number 3!")
print("What is the chemical symbol for water? ")
answer = input().lower()
while answer not in ["h2o", "H2O"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["h2o", "H2O"]:
    print("Correct! The chemical symbol for water is H2O.")
print("Question number 4!")
print("What is the capital of Japan? ")
answer = input().lower()
while answer not in ["tokyo", "Tokyo"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["tokyo", "Tokyo"]:
    print("Correct! Tokyo is the capital of Japan.")
print("Question number 5!")
print("What is the largest mammal in the world? ")
answer = input().lower()
while answer not in ["blue whale", "Blue Whale"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["blue whale", "Blue Whale"]:
    print("Correct! The blue whale is the largest mammal in the world.")
print("Question number 6!")
print("What is the smallest country in the world? ")
answer = input().lower()
while answer not in ["vatican city", "Vatican City"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["vatican city", "Vatican City"]: 
    print("Correct! Vatican City is the smallest country in the world.")
print("Question number 7!")
print("What is the largest desert in the world? ")
answer = input().lower()
while answer not in ["sahara", "Sahara"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["sahara", "Sahara"]:
    print("Correct! The Sahara is the largest desert in the world.")
print("Question number 8!")
print("What is the longest river in the world? ")
answer = input().lower()
while answer not in ["nile", "Nile"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["nile", "Nile"]:
    print("Correct! The Nile is the longest river in the world.")
print("Question number 9!")
print("What is the largest ocean in the world? ")
answer = input().lower()
while answer not in ["pacific", "Pacific"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["pacific", "Pacific"]:    
    print("Correct! The Pacific Ocean is the largest ocean in the world.")
print("Question number 10!")
print("What is the capital of Italy? ")
answer = input().lower()
while answer not in ["rome", "Rome"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["rome", "Rome"]:
    print("Correct! Rome is the capital of Italy.")
print("Question number 11!")
print("What is the largest continent in the world? ")
answer = input().lower()
while answer not in ["asia", "Asia"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["asia", "Asia"]:
    print("Correct! Asia is the largest continent in the world.")
print("Question number 12!")
print("What is the capital of Spain? ")
answer = input().lower()
while answer not in ["madrid", "Madrid"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["madrid", "Madrid"]:
    print("Correct! Madrid is the capital of Spain.")
print("Question number 13!")
print("What is the largest country in the world? ")
answer = input().lower()
while answer not in ["russia", "Russia"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["russia", "Russia"]:
    print("Correct! Russia is the largest country in the world.")
print("Question number 14!")
print("Who created the first computer? ")
answer = input().lower()
while answer not in ["charles babbage", "Charles Babbage"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
    if answer in ["charles babbage", "Charles Babbage"]:
        print("Correct! Charles Babbage is considered the father of the computer.")
print("Question number 15!")
print("What is the most abundant element in the universe? ")
answer = input().lower()
while answer not in ["hydrogen", "Hydrogen"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
    if answer in ["hydrogen", "Hydrogen"]:
        print("Correct! Hydrogen is the most abundant element in the universe.")
print("Question number 17!")
print("Who created Google? ")
answer = input().lower()
while answer not in ["larry page and sergey brin", "Larry Page and Sergey Brin", "Larry Page", "Sergey Brin", "larry page", "sergey brin"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["larry page and sergey brin", "Larry Page and Sergey Brin", "Larry Page", "Sergey Brin", "larry page", "sergey brin"]:
    print("Correct! Larry Page and Sergey Brin created Google.")
print("Question number 18!")
print("What is the capital of Germany? ")
answer = input().lower()
while answer not in ["berlin", "Berlin"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["berlin", "Berlin"]:
    print("Correct! Berlin is the capital of Germany.")
print("Question number 19!")
print("What produces the most oxygen on Earth? ")
answer = input().lower()
while answer not in ["phytoplankton", "Phytoplankton"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["phytoplankton", "Phytoplankton"]:
    print("Correct! Phytoplankton produces the most oxygen on Earth.")
print("Question number 20!")
print("What is the largest organ in the human body? ")
answer = input().lower()
while answer not in ["skin", "Skin"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["skin", "Skin"]:
    print("Correct! The skin is the largest organ in the human body.")
print("Congratulations! You have completed the quiz game!")
print("You answered all questions correctly! You are a genius!")