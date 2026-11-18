import random


DIFFICULTIES = {
    "1": {
        "name": "Easy",
        "minimum": 1,
        "maximum": 50,
        "attempts": 10
    },

    "2": {
        "name": "Medium",
        "minimum": 1,
        "maximum": 100,
        "attempts": 7
    },

    "3": {
        "name": "Hard",
        "minimum": 1,
        "maximum": 200,
        "attempts": 5
    }
}


def display_welcome():
    print("\n" + "=" * 45)
    print("          NUMBER GUESSING GAME")
    print("=" * 45)
    print("Welcome! Try to guess the secret number.")
    print("=" * 45)


def select_difficulty():

    print("\nSELECT DIFFICULTY")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    while True:

        choice = input("\nChoose difficulty (1-3): ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice. Please select 1, 2 or 3.")


def get_player_name():

    while True:

        name = input("\nEnter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")


def generate_secret_number(minimum, maximum):

    return random.randint(minimum, maximum)


def get_guess(minimum, maximum):

    while True:

        try:

            guess = int(
                input(f"Enter your guess ({minimum}-{maximum}): ")
            )

            if minimum <= guess <= maximum:
                return guess

            print(f"Enter a number between {minimum} and {maximum}.")

        except ValueError:

            print("Invalid input! Enter a whole number.")


def calculate_score(attempts_used, total_attempts, difficulty):

    remaining_attempts = total_attempts - attempts_used

    difficulty_bonus = {
        "Easy": 10,
        "Medium": 30,
        "Hard": 50
    }

    score = (
        remaining_attempts * 10
        + difficulty_bonus[difficulty]
    )

    return max(score, 10)


def play_game(player_name, difficulty):

    minimum = difficulty["minimum"]
    maximum = difficulty["maximum"]
    total_attempts = difficulty["attempts"]

    secret_number = generate_secret_number(minimum, maximum)

    guesses = []

    print("\n" + "=" * 45)
    print(f"PLAYER: {player_name}")
    print(f"DIFFICULTY: {difficulty['name']}")
    print(f"NUMBER RANGE: {minimum}-{maximum}")
    print(f"AVAILABLE ATTEMPTS: {total_attempts}")
    print("=" * 45)

    for attempt in range(1, total_attempts + 1):

        print(f"\nAttempt {attempt} of {total_attempts}")

        guess = get_guess(minimum, maximum)

        guesses.append(guess)

        if guess == secret_number:

            score = calculate_score(
                attempt,
                total_attempts,
                difficulty["name"]
            )

            print("\n" + "=" * 45)
            print("CONGRATULATIONS! YOU WON!")
            print(f"Secret number: {secret_number}")
            print(f"Attempts used: {attempt}")
            print(f"Your score: {score}")
            print("=" * 45)

            return {
                "player": player_name,
                "difficulty": difficulty["name"],
                "won": True,
                "score": score,
                "attempts": attempt,
                "guesses": guesses
            }

        elif guess < secret_number:

            print("Too LOW! Try a higher number.")

        else:

            print("Too HIGH! Try a lower number.")

        remaining = total_attempts - attempt

        print(f"Attempts remaining: {remaining}")

    print("\n" + "=" * 45)
    print("GAME OVER! YOU RAN OUT OF ATTEMPTS.")
    print(f"The secret number was: {secret_number}")
    print("=" * 45)

    return {
        "player": player_name,
        "difficulty": difficulty["name"],
        "won": False,
        "score": 0,
        "attempts": total_attempts,
        "guesses": guesses
    }