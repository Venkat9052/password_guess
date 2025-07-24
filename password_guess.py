import random
import time
history = "history.txt"
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
# function to show history-------------------------------------------------------------------------------------------

def show_history():
    data = open("history.txt","r")
    lines = data.readlines()
    if(len(lines) == 0 ):
        print("No History available")
    else:
        for line in lines:
            print(line) 
    data.close()
# function to save history ------------------------------------------------------------------------------------------

def save_history(secret_word,stmt):
    with open("history.txt","a") as file:
        file.write(f"Secret word is {secret_word} \n {stmt}\n")
    
# function to clear history ------------------------------------------------------------------------------------------

def clear():
    with open("history.txt","w"):
        print("")
    print("history is cleared..............................")

# function to choose secret password-----------------------------------------------------------------------------------

def computer_choice():
    level = input("Choose the level you want like Easy,Medium or Hard : ").strip()
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

# game function -----------------------------------------------------------------------------------------------------

def play_game(secret_word):
    attempts = 0
    while True:
        start = time.time()
        guess = input("Guess the password : ") 
        attempts +=1

        hint = ""     ## resets the hint for every new iteration
        if guess == secret_word:
            duration =round(time.time() - start) 
            stmt = f"Congratulations you guessed the password correctly in {attempts} attempts and duration is {duration} seconds"
            print("✅",stmt)
            save_history(secret_word,stmt)
            break
        else:
            for i in range(len(secret_word)):
                if i < len(guess) and guess[i] == secret_word[i]:
                    hint+=guess[i]
                else:
                    hint += "_"
        print("Hint : ",hint)

# our main loop of game --------------------------------------------------------------------------------------------

def main():
    while True:
        secret_word = computer_choice()
        play_game(secret_word)
        again = input("Do you want to play again (yes/no) : ").strip()
        if again != "yes":
            print("Game over ,Thank's for Playing")
            break


# User defining ---------------------------------------------------------------------------------------------------
print("Welcome to password guessing Game ")
print("Come on Let's play the game ")

while True:
    user_interest = input("Do you want to see history type ( history ), or clear history (clear)  or Exit  : ").strip()

    if user_interest.lower() =="history":
        show_history()
    elif user_interest.lower() =="clear":
        clear()
    elif user_interest.lower() =="exit":
        print("Game Over")
        break
    else:
        start_time = time.time()
        main()
        end_time = time.time()
        total_time = round((end_time - start_time),2)
        print(f"You guessed all the passwords in this span of {total_time} time in seconds")











    