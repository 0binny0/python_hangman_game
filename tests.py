from unittest import TestCase, main
from unittest.mock import patch, Mock, PropertyMock
from classes import Player, Guess
from main import Game

class TestPlayerLetterGuess(TestCase):
    '''Verify that an error is raised if the provided
    guess is not a single letter of the alphabet.'''

    def setUp(self):
        self.player = Player()

    @patch("classes.input", side_effect=["%", 'a'])
    def test_player_guess_invalid_character(self, mock_guess):
        guessed_letter = self.player.guess_attempt()
        self.assertEqual(guessed_letter, 'a')
        self.assertEqual(mock_guess.call_count, 2)


class TestLetterAgainstWord(TestCase):
    '''Verify that a player guess is marked as missed if the letter
    guessed is not in the mystery word and not previously guessed.'''

    def setUp(self):
        self.game = Game()

    @patch("classes.input", return_value="b")
    @patch("main.choice", return_value="Hello")
    def test_guessed_letter_is_miss(self, mock_word, mock_letter):
        guess = self.game.get_player_guess()
        self.assertIsInstance(guess, Guess)
        self.assertEqual(guess.play, "miss")


class TestSomeLettersGuessed(TestCase):
    '''Verify that the game word string shows only
    those letters that are guessed if the game is ongoing.'''

    def setUp(self):
        self.game = Game()
        self.game.guesses = [
            Guess('e', "miss"), Guess('p', 'hit')
        ]
        self.game.word = "python"
        self.guess = Guess('o', 'hit')

    def test_hangman_revealed_letter_matches(self):
        updated_hangman_string = self.game.update_guessed_word(self.guess)
        self.assertEqual(updated_hangman_string, "p***o*")


class TestAllLettersGuessed(TestCase):
    '''Verify that the game word string shows all
    letters that are guessed if the game is ongoing.'''

    def setUp(self):
        self.game = Game()
        self.game.guesses = [
            Guess('y', "hit"), Guess('p', 'hit'), Guess('o', 'hit'),
            Guess('n', "hit"), Guess('h', "hit")
        ]
        self.game.word = "python"
        self.guess = Guess("t", "hit")

    def test_hangman_revealed_letter_matches(self):
        updated_hangman_string = self.game.update_guessed_word(self.guess)
        self.assertEqual(updated_hangman_string, "python")



if __name__ == "__main__":
    main()
