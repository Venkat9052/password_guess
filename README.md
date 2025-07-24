# password_guesser game
📌 Description
This is a simple password guessing game built with Python. The game challenges players to guess a randomly selected word from a hidden list, with difficulty levels including Easy, Medium, and Hard. After each incorrect guess, a hint is displayed showing the correctly guessed letters in their correct positions.

The game also tracks and saves your successful attempts, including the guessed word, number of attempts, and time taken to guess it. You can view past game history, clear history, or just play the game directly.

🎮 Features
🔢 Multiple difficulty levels: Easy, Medium, and Hard word banks.

🕹️ Interactive hint system: Reveals correct letters in correct positions.

📝 Game history: View previously guessed words and your performance.

🧹 Clear history option for fresh gameplay.

⏱️ Tracks time taken per game and total session duration.

📁 File Structure
main.py - The core game script.

history.txt - A text file to store previous game results (auto-created if not present).

▶️ How to Run
Make sure you have Python installed.

Run the script:

bash
Copy
Edit
python main.py
Follow the prompts to:

Choose difficulty

Guess the password

View hints

Replay or exit

View or clear history

🧠 Example
text
Copy
Edit
Welcome to password guessing Game 
Come on Let's play the game 
Choose the level you want like Easy,Medium or Hard : medium
Guess the password : plane
Hint : pl___
Guess the password : planet
✅ Congratulations you guessed the password correctly in 2 attempts and duration is 5 seconds

💡 Future Improvements
Add leaderboard with high scores.

GUI version with Tkinter or PyQt.

Import custom word lists.

Add multiplayer mode.
