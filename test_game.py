import unittest
from unittest.mock import patch
from main import pick_word, display_word

class TestWordGame(unittest.TestCase):

    def test_pick_word_is_string(self):
        word = pick_word()
        self.assertIsInstance(word, str)
        self.assertTrue(len(word) > 0)

    def test_display_word_partial_guess(self):
        with patch('builtins.print') as mock_print:
            display_word("burger", ['b', 'r', 'e'])
            mock_print.assert_called_with("b _ r _ e r")

    def test_display_word_all_letters_guessed(self):
        with patch('builtins.print') as mock_print:
            display_word("burger", ['b', 'u', 'r', 'g', 'e'])
            mock_print.assert_called_with("b u r g e r")


if __name__ == '__main__':
    unittest.main()