import random

# list of easy words to guess
easy_words = [
    "cat", "dog", "sun", "book", "tree","tiger","dice","can","meat",
    "ball", "fish", "milk", "car", "hat","hen","solar","boat","fat"
]

# list of medium words to guess

medium_words = [
    "planet", "castle","country", "bridge","break", "flower","friends", "guitar","godzilla",
    "pencil", "window","wheel", "rocket","random", "camera","cameron", "monkey","mitochondria"
]

# list of hard words to guess

hard_words = [
    "philosophy","photographer", "algorithm", "architecture", "revolution","rocket", "hypothesis","hypocritic",
    "metaphor","monopoly", "cryptography", "hemisphere","hindustan", "oscillation","ointment", "photosynthesis","hemoglobin"
]


print("Welcome to password guessing game  ! \n")


def computer_choice():
    level = input("Choose the level you want like Easy,Medium or Hard : ").strip().lower()
    if level == "easy":
        secret = random.choice(easy_words)
        return secret
    elif level == "medium":
        secret = random.choice(medium_words)
        return secret
    elif level == "hard":
        secret = random.choice(hard_words)
        return secret
    else:
        print("Invalid input defaulting to Easy level:......")
        secret = random.choice(easy_words)
        return secret



def play_game(secret_word):
    attempts = 0
    while True:
        guess = input("Guess the password : ") 
        attempts +=1

        hint = ""     ## resets the hint for every new iteration
        if guess == secret_word:
            print(f"Congratulations you guessed the password correctly in {attempts} attempts")
            break
        else:
            for i in range(len(secret_word)):
                if i < len(guess) and guess[i] == secret_word[i]:
                    hint+=guess[i]
                else:
                    hint += "_"
        print("Hint : ",hint)

def main():
    while True:
        secret_word = computer_choice()
        play_game(secret_word)

        again = input("Do you want to play again (yes/no) : ").strip()
        if again != "yes":
            print("Game over ,Thank's for Playing")
            break

main()







    