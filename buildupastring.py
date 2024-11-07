import random

# Step 1: Ask the user for a string
user_input = input("Enter a string that is exactly 10 characters long: ")

# Step 2: Check the string length
if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")

    # Step 3: Print the first and last characters
    print("First character:", user_input[0])
    print("Last character:", user_input[-1])

    # Step 4: Construct the string character by character
    constructed_string = ""
    for char in user_input:
        constructed_string += char
        print(constructed_string)

    # Step 5 (Bonus): Shuffle the string and print it
    shuffled_string = list(user_input)
    random.shuffle(shuffled_string)
    print("".join(shuffled_string))
