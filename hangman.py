import string
from words import choose_word
from images import IMAGES

'''
Important instruction
* function and variable name snake_case -> is_prime
* constant variable upper case PI
'''


def get_unique_letters(s):
    st = set()
    ans = ""
    for c in s:
        if c not in st:
            ans += c
            st.add(c)
    return ans


def is_word_guessed(secret_guess_word, letters_guessed):
    """
    secret_guess_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns:
      return True (if user guess the world correctly )
      return False (wrong selection)
    """

    counts = [0] * 26
    for c in secret_guess_word:
        counts[ord(c) - ord('a')] += 1
    for c in letters_guessed:
        counts[ord(c) - ord('a')] -= 1
    for i in range(26):
        if counts[i] != 0:
            return False

    return True


# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_guess_word, letters_guessed):
    """
    secret_guess_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns:
      return string which contain all the right guessed characters
      Example :-
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    """
    index = 0
    guessed_word = ""
    while index < len(secret_guess_word):
        if secret_guess_word[index] in letters_guessed:
            guessed_word += secret_guess_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list contains all guessed characters
    returns:
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    """
    letters_left = string.ascii_lowercase
    return letters_left


def hangman(secret_guess_word):
    """
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word

    * In each round user will guess one character

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word
    """
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_guess_word))), end='\n\n')

    letters_guessed = ''
    total_attempts = len(IMAGES)
    attempt = 0
    unique_secret_word = get_unique_letters(secret_guess_word)
    while attempt < total_attempts - 1:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter != '' and letter in secret_guess_word:
            if letter not in letters_guessed:
                letters_guessed += letter
            print("Good guess: {} ".format(
                get_guessed_word(secret_guess_word, letters_guessed)))

            if is_word_guessed(unique_secret_word, letters_guessed):
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_guess_word, letters_guessed)))
            print("")
            print(IMAGES[attempt])
            attempt += 1
        if attempt == total_attempts - 1:
            print("\n * * GAME OVER! * * ", end='\n\n')


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
if __name__ == '__main__':
    secret_word = choose_word()
    hangman(secret_word)
