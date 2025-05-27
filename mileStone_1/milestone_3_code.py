print("Wellcome to the quiz game!I wil ask you some questions and you will have to answer them correctly to win the game!")
print("There will be 10 questions you have to answer. Let's start!")
print("What is the capital of France? ")
answer = input().lower()
while answer not in ["paris", "Paris", "paris france"]:
    print("Incorrect! Please try again.")
    answer = input().lower()
if answer in ["paris", "p", "Paris", "paris france"]:
    print("Correct! Paris is the capital of France.")
print("Next question!")
print("What is the largest planet in our solar system? ")
answer = input().lower()
while answer not in ["jupiter", "Jupiter"]:
        print("Incorrect! Please try again.")
        answer = input().lower()
if answer in ["jupiter", "Jupiter"]:
    print("Correct! Jupiter is the largest planet in our solar system.")