from tkinter import *
from tkinter import messagebox
import random

word_dict = {
    "Abundant": "Existing in large quantities; plentiful.",
    "Benevolent": "Kind and generous.",
    "Candid": "Honest and straightforward.",
    "Diligent": "Showing care and effort in work.",
    "Eloquent": "Fluent and persuasive in speaking or writing.",
    "Frugal": "Careful with money; thrifty.",
    "Gratify": "To please or satisfy.",
    "Hinder": "To delay or obstruct.",
    "Imminent": "About to happen very soon.",
    "Jubilant": "Extremely joyful and happy.",
    "Keen": "Eager or enthusiastic.",
    "Lucid": "Clear and easy to understand.",
    "Mundane": "Ordinary or boring.",
    "Notorious": "Famous for something bad.",
    "Obsolete": "No longer in use.",
    "Persevere": "To keep going despite difficulty.",
    "Quaint": "Charming in an old-fashioned way.",
    "Reckless": "Without thinking about the consequences.",
    "Serene": "Calm, peaceful, and untroubled.",
    "Tedious": "Boring and too long.",
    "Ubiquitous": "Present everywhere at once.",
    "Vivid": "Bright, distinct, and clear.",
    "Witty": "Clever and humorous.",
    "Yearn": "To long for something.",
    "Zealous": "Very enthusiastic and devoted.",
    "Amicable": "Friendly and without disagreement.",
    "Brisk": "Quick and active.",
    "Clandestine": "Secretive, especially for wrongdoing.",
    "Dexterous": "Skillful with hands or mind.",
    "Empathy": "The ability to understand others' feelings."
}


used_words = []
hint_level = 0
current_word = ""
current_meaning = ""
score = 0
attempts_left = 3


window = Tk()
window.geometry("850x550")
window.title("🌟 Fictionary Word Guess Game 🌟")
window.configure(bg="#fff3e0")

title_label = Label(window, text="🎯 Guess the Word!", font=("Arial", 24, "bold"), bg="#fff3e0", fg="#ef6c00")
title_label.pack(pady=10)

meaning_label = Label(window, font=("Arial", 16), wraplength=700, bg="#fff3e0", fg="#4e342e")
meaning_label.pack(pady=20)

entry = Entry(window, font=("Arial", 18), width=30, justify="center", bg="#fbe9e7")
entry.pack(pady=10)
entry.focus_set()

hint_label = Label(window, text="", font=("Arial", 14, "italic"), bg="#fff3e0", fg="#00838f")
hint_label.pack(pady=10)

score_label = Label(window, text="Score: 0", font=("Arial", 16, "bold"), bg="#fff3e0", fg="#2e7d32")
score_label.pack(pady=5)


def start_game():
    global current_word, current_meaning, hint_level, used_words, attempts_left

    try:
        if len(used_words) == len(word_dict):
            messagebox.showinfo("Game Over", "🎉 You've guessed all words! Click Reset to play again.")
            return

        hint_level = 0
        attempts_left = 3
        entry.delete(0, END)
        hint_label.config(text="")

        remaining_words = [word for word in word_dict if word not in used_words]
        current_word = random.choice(remaining_words)
        current_meaning = word_dict[current_word]
        used_words.append(current_word)
        meaning_label.config(text="Guess the word for:\n\n" + current_meaning)
        entry.focus_set()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while starting the game:\n{e}")


def show_hint():
    global hint_level

    try:
        if not current_word:
            messagebox.showwarning("Start Game", "Click Reset or Submit to begin.")
            return

        if hint_level == 0:
            hint_label.config(text=f"Hint 1: The word starts with '{current_word[0]}'.")
        elif hint_level == 1:
            hint_label.config(text=f"Hint 2: The word has {len(current_word)} letters.")
        elif hint_level == 2:
            hint_label.config(text=f"Hint 3: The word ends with '{current_word[-1]}'.")
        else:
            hint_label.config(text=f"No more hints!")
        hint_level += 1
    except Exception as e:
        messagebox.showerror("Hint Error", f"Error showing hint:\n{e}")


def check_answer():
    global score, attempts_left

    try:
        user_input = entry.get().strip().lower()
        correct_word = current_word.lower()

        if not current_word:
            messagebox.showwarning("Start Game", "Click Reset or Submit to begin.")
            return

        if not user_input:
            messagebox.showwarning("Input Required", "Please enter a word before submitting.")
            return

        if user_input == correct_word:
            if hint_level == 0:
                points = 100
            elif hint_level == 1:
                points = 80
            elif hint_level == 2:
                points = 60
            else:
                points = 40

            score += points
            score_label.config(text=f"Score: {score}")
            messagebox.showinfo("Correct ✅", f"Great! You got it.\nPoints earned: {points}\n\nThe word was '{current_word}'.")
            start_game()
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showinfo("Try Again ❌", f"Wrong guess!\nYou have {attempts_left} chances left.")
                entry.delete(0, END)
            else:
                messagebox.showinfo("Out of Chances ❌", f"You used all attempts!\nThe word was: '{current_word}'.")
                start_game()
    except Exception as e:
        messagebox.showerror("Answer Error", f"Error checking your answer:\n{e}")


def reset_game():
    global score, used_words
    try:
        score = 0
        used_words = []
        score_label.config(text="Score: 0")
        start_game()
    except Exception as e:
        messagebox.showerror("Reset Error", f"Could not reset the game:\n{e}")


def show_game_info():
    try:
        messagebox.showinfo("📘 How to Play", 
            "🎮 Fictionary Word Guess Game Rules:\n\n"
            "1️⃣ A word definition will be displayed.\n"
            "2️⃣ Type the correct word and press Submit.\n"
            "3️⃣ You have 3 chances to guess each word.\n"
            "4️⃣ Click the Hint button to get up to 3 hints:\n"
            "    • Hint 1: First letter\n"
            "    • Hint 2: Word length\n"
            "    • Hint 3: Last letter\n"
            "5️⃣ Scoring System:\n"
            "    • 0 hints used = 100 points\n"
            "    • 1 hint used = 80 points\n"
            "    • 2 hints used = 60 points\n"
            "    • 3 hints used = 40 points\n"
            "6️⃣ If you fail all attempts, the word is revealed.\n\n"
            "🏁 Try to get the highest score!"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Error displaying game info:\n{e}")


btn_frame = Frame(window, bg="#fff3e0")
btn_frame.pack(pady=15)

check_btn = Button(btn_frame, text="Submit", font=("Arial", 14), command=check_answer, bg="#4fc3f7", fg="black", width=10)
check_btn.grid(row=0, column=0, padx=10)

hint_btn = Button(btn_frame, text="Hint", font=("Arial", 14), command=show_hint, bg="#aed581", fg="black", width=10)
hint_btn.grid(row=0, column=1, padx=10)

reset_btn = Button(btn_frame, text="Reset Game", font=("Arial", 14), command=reset_game, bg="#ff8a65", fg="black", width=12)
reset_btn.grid(row=0, column=2, padx=10)

info_btn = Button(btn_frame, text="Game Info", font=("Arial", 14), command=show_game_info, bg="#90caf9", fg="black", width=12)
info_btn.grid(row=0, column=3, padx=10)

start_game()
window.mainloop()
