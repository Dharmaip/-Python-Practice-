name = input("What is your name?")
age = int(input("How old are you?"))
#Below is executed only if the user age is equal to or under 5
if age <= 5:
    recommended_sleep = "10 - 12 hours per night"
#Below is executed only if the user age is equal to or under 18
elif age <= 18:
    recommended_sleep = "7 - 9 hours per night"
#Below is executed only if the user age is equal to or under 30
elif age <= 30:
    recommended_sleep = "6 - 8 hours per night"
#Below is executed only if none of the above conditions are met
else:
    recommended_sleep = "7 - 8 hours per night"
print("Hello {}! Since you are {} years old, I recommend you to sleep at {} for better health".format(name.title(), age, recommended_sleep))

#Privacy implication
#We will not store any of your data in our local device. We wll do our best to protect your privacy