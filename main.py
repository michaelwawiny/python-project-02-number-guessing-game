from game import (
    display_welcome,
    select_difficulty,
    get_player_name,
    play_game
)

from scoreboard import (
    add_score,
    display_scoreboard
)


def display_menu():

    print("\nMAIN MENU")
    print("1. Start New Game")
    print("2. View Leaderboard")
    print("3. Exit")


def main():

    display_welcome()

    player_name = get_player_name()

    while True:

        display_menu()

        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":

            difficulty = select_difficulty()

            result = play_game(
                player_name,
                difficulty
            )

            add_score(result)

            print("\nGame result saved successfully!")

        elif choice == "2":

            display_scoreboard()

        elif choice == "3":

            print("\nThank you for playing!")
            print("Goodbye!")

            break

        else:

            print("Invalid option. Choose 1, 2 or 3.")


if __name__ == "__main__":

    main()