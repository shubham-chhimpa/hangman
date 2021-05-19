import unittest
from hangman import get_unique_letters, is_word_guessed


class TestHangman(unittest.TestCase):

    def test_get_unique_letters(self):
        self.assertEqual(get_unique_letters("good"), "god", "Should be god")
        self.assertEqual(get_unique_letters("kiet"), "kiet", "Should be kiet")

    def test_is_word_guessed(self):
        self.assertEqual(is_word_guessed("learning", "lreanngi"), True, "Should be True")
        self.assertEqual(is_word_guessed("learning", "lreanng"), False, "Should be False")
        self.assertEqual(is_word_guessed("god", "god"), True, "Should be True")


if __name__ == '__main__':
    unittest.main()
