import random

# get guess
def get_guess():
    return list(str(input("What is your guess? ")))

# generate computer code
def generate_code():
    digits = [str(num) for num in range(10)]
    # shuffle the digits
    random.shuffle(digits)
    # grab the first three
    return digits[:3]

# generate the clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

# run game logic
print("Welcome Code Wrecker!")
secret_code = generate_code()
clue_report = []
while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
