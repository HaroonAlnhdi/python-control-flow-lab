# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()




# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    
    letter = input("Enter a letter (a-z or -A-Z): ").upper()
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            print(f"The letter ({letter}) is a vowel.")

    #  isalpha() method returns True if all the characters are alphabet letters (a-z).
    elif letter.isalpha() and letter not in "AEIOU":
        print(f'The letter ({letter}) is a consonant.')

    else:
        print("non-alphabetical or invalid entries.")

check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():

    vote = input("Please enter your age: ");
    vote = int(vote)
    if vote < 0:
        print("Invalid age.No negative numbers")
    elif vote >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dogAge = input("Enter a dog's age: ")
    dogAge = int(dogAge)
    if dogAge < 0:
        print("Invalid age.")
    elif dogAge == 1 or dogAge == 2:
        dogYears = dogAge * 10
        print(f"The dog's age in dog years is {dogYears}.")
    else:
        #  {2*10 : first two years  of dog } + {(dogAge - 2) : remaining years * 7}
        dogYears = 2 * 10 + (dogAge - 2) * 7
        print(f"The dog's age in dog years is {dogYears}.")

calculate_dog_years()