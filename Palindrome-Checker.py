# Palindrome Checker 

# Initializing variable to y

u_inp = "y"

while u_inp == "y":

    userInput = input("Please enter your palindrome : ").casefold()

    # Reversing the User Input

    reversedUserInput = reversed(userInput)

    if list(userInput) == list(reversedUserInput):
        print("This is a palindrome..! \n")
    else:
        print("This is not a palindrome \n")

    u_inp = input("Do you want to have another test ? [Y/N] ").lower()

print("\n Thanks for having Fun..")    