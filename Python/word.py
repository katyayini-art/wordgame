import random

# List of cleaned player names (replace with full list if external)
player_names = [
    "Avery Bradley", "Jae Crowder", "John Holland", "R.J. Hunter", "Jonas Jerebko",
    # ... add more from your cleaned dataset
]

# Pick a random player name
target = random.choice(player_names).lower()
target_simple = target.replace(".", "").replace(" ", "")  # Remove special chars

print("🏀 Welcome to NBA Wordly!")
print(f"Guess the NBA player! The name has {len(target_simple)} letters (no spaces or dots).")
print("You have 6 attempts.")

def get_feedback(guess, target):
    feedback = []
    for i in range(len(target)):
        if i < len(guess) and guess[i] == target[i]:
            feedback.append("🟩")  # correct position
        elif guess[i] in target:
            feedback.append("🟨")  # wrong position
        else:
            feedback.append("⬜")  # not in name
    return feedback

attempts = 6
while attempts > 0:
    user_input = input(f"\nAttempt {7 - attempts}/6: ").lower()
    guess = user_input.replace(".", "").replace(" ", "")  # Normalize input

    if len(guess) != len(target_simple):
        print(f"❗ Enter exactly {len(target_simple)} letters (no spaces or dots).")
        continue

    feedback = get_feedback(guess, target_simple)
    print(" ".join(feedback))

    if guess == target_simple:
        print("🎉 You guessed it right! The player is:", target.title())
        break

    attempts -= 1

if guess != target_simple:
    print(f"❌ Out of attempts. The correct player was: {target.title()}")
