import json
import os


SCORE_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "scores.json"
)


def load_scores():

    try:

        with open(SCORE_FILE, "r") as file:
            scores = json.load(file)

            if isinstance(scores, list):
                return scores

            return []

    except (FileNotFoundError, json.JSONDecodeError):

        return []


def save_scores(scores):

    os.makedirs(
        os.path.dirname(SCORE_FILE),
        exist_ok=True
    )

    with open(SCORE_FILE, "w") as file:

        json.dump(scores, file, indent=4)


def add_score(result):

    scores = load_scores()

    scores.append(result)

    save_scores(scores)


def display_scoreboard():

    scores = load_scores()

    print("\n" + "=" * 55)
    print("                 LEADERBOARD")
    print("=" * 55)

    if not scores:

        print("No scores recorded yet.")

        return

    winners = [
        score for score in scores
        if score.get("won") is True
    ]

    winners.sort(
        key=lambda score: score.get("score", 0),
        reverse=True
    )

    if not winners:

        print("No winning scores yet.")

        return

    print(
        f"{'PLAYER':<15}"
        f"{'LEVEL':<12}"
        f"{'SCORE':<10}"
        f"{'ATTEMPTS':<10}"
    )

    print("-" * 55)

    for player in winners[:10]:

        print(
            f"{player['player']:<15}"
            f"{player['difficulty']:<12}"
            f"{player['score']:<10}"
            f"{player['attempts']:<10}"
        )

    print("=" * 55)