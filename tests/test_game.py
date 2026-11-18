import unittest

from game import (
    generate_secret_number,
    calculate_score,
    DIFFICULTIES
)


class TestNumberGuessingGame(unittest.TestCase):

    def test_random_number_range(self):

        number = generate_secret_number(1, 100)

        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 100)

    def test_easy_difficulty(self):

        self.assertEqual(
            DIFFICULTIES["1"]["attempts"],
            10
        )

    def test_medium_difficulty(self):

        self.assertEqual(
            DIFFICULTIES["2"]["attempts"],
            7
        )

    def test_hard_difficulty(self):

        self.assertEqual(
            DIFFICULTIES["3"]["attempts"],
            5
        )

    def test_score_calculation(self):

        score = calculate_score(
            attempts_used=2,
            total_attempts=7,
            difficulty="Medium"
        )

        self.assertEqual(score, 80)

    def test_minimum_score(self):

        score = calculate_score(
            attempts_used=10,
            total_attempts=10,
            difficulty="Easy"
        )

        self.assertEqual(score, 10)


if __name__ == "__main__":

    unittest.main()