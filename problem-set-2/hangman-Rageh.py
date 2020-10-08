# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/Users/gharseldin/Documents/pythonTraining/MIT Course/problem-set-2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # secret_word = choose_word()
    # letters_guessed = []
    secret_word_list = set()
    # [ a, a , r , a , p]
    for x in secret_word:
        secret_word_list.add(x)
    x = 0
    for guess in letters_guessed:
        if guess in secret_word_list:
            x += 1
    # n
    # for char in secret_word:
    #     # 5 + n
    #     if not (char in letters_guessed):
    #         return False
    # return True

    is_word_guessed.secret_word_list = secret_word_list
    return(x == len(secret_word_list))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # letters_to_guess_f = letters_to_guess[:]
    # for x in range(len(secret_word)):
    #   letters_to_guess.append('_ ')

    # letters_to_guess = hangman(secret_word).letters_to_guess

    hangman.letters_to_guess = list(hangman.letters_to_guess)
    x = 0
    y = 0
    for letter_w in secret_word:
        if letters_guessed[-1] == letter_w:
            hangman.letters_to_guess[x] = (letters_guessed[-1]+' ')
            y += 1
        x += 1

    for x in range(len(hangman.letters_to_guess)):
        hangman.letters_to_guess[x] = str(hangman.letters_to_guess[x])

    if y == 0:
        if letters_guessed[-1] in ['a', 'e', 'i', 'o', 'u']:
            hangman.guesses_remaining -= 2
        else:
            hangman.guesses_remaining -= 1
        print('Oops! That letter is not in my word:',
              ''.join(hangman.letters_to_guess))
    else:
        print('Good guess:', ''.join(hangman.letters_to_guess))

    print('-'*20)
    if hangman.guesses_remaining > 0:
        print('You have', hangman.guesses_remaining, 'guesse(s) left.')
        print('Available letters', get_available_letters(letters_guessed))

    if hangman.guesses_remaining <= 0:
        print('Sorry, you ran out of guesses. The word was', secret_word + '.')
        return False
    else:
        return True

    # if y == len(secret_word):
    #  break


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    import string
    available_letters = list(string.ascii_lowercase)
    for i in letters_guessed:
        for x in available_letters:
            if i == x:
                available_letters.remove(i)
                break

    for i in range(len(available_letters)):
        available_letters[i] = str(available_letters[i])
    return(''.join(available_letters))


def warnings_remaining(guess, letters_guessed):

    # x = guess.isalpha()
    # if x == False:
    hangman.warnings -= 1

    if guess not in string.ascii_lowercase or len(guess) > 1 and hangman.warnings >= 0:
        print('Oops! That is not a valid letter. You have', hangman.warnings,
              'warning(s) left:',  ''.join(hangman.letters_to_guess))

    elif letters_guessed.count(guess) > 1 and hangman.warnings >= 0:
        print('Oops! That letter has already been guessed. You have',
              hangman.warnings, 'warning(s) left:',  ''.join(hangman.letters_to_guess))

    if hangman.warnings < 0 and hangman.guesses_remaining > 1:
        print('You are out of warnings:', ''.join(hangman.letters_to_guess))
        hangman.guesses_remaining -= 1
    elif hangman.warnings < 0 and hangman.guesses_remaining == 1:
        print('You are out of warnings and guesses.')
        hangman.guesses_remaining -= 1
        return False

    print('-'*20)
    print('You have', hangman.guesses_remaining, 'guesse(s) left.')
    print('Available letters', get_available_letters(letters_guessed))
    letters_guessed.pop()

    # else:
    #   return True


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    import string
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word),
          'letters long.\n--------------------\nYou have 3 warnings left\nYou have 6 guesses left.\nAvailable letters:', string.ascii_lowercase)
    # secret_word = 'pineapple'
    hangman.letters_to_guess = []
    for _ in range(len(secret_word)):
        hangman.letters_to_guess.append('_ ')
    print(*hangman.letters_to_guess, sep='')

    hangman.warnings = 3
    hangman.guesses_remaining = 6
    letters_guessed = []

    while True:

        guess = input('Please guess a letter: ')
        # guess = guess.lower()
        guess = guess.casefold()
        letters_guessed.append(guess)
        # print(letters_guessed)
        # hangman.letters_guessed = letters_guessed
        if guess not in string.ascii_lowercase or len(guess) > 1 or guess in letters_guessed[0:-1]:
            if warnings_remaining(guess, letters_guessed) == False:
                print('word was', secret_word)
                break

        elif not get_guessed_word(secret_word, letters_guessed):
            # print('word was', secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!\nYour total score for this game is:',
                  hangman.guesses_remaining*len(is_word_guessed.secret_word_list))
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    for x in range(len(my_word)):
        my_word[x] = my_word[x].strip()
    matches = []

    if len(my_word) != len(other_word):
        return False
    else:
        i = 0
        for i in range(len(my_word)):
            if my_word[i] == '_':
                matches.append(my_word[i])
            else:
                if my_word[i] != other_word[i]:
                    break
                else:
                    matches.append(my_word[i])
    if len(matches) == len(my_word):
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    # my_word = hangman.letters_to_guess
    matches = []
    x = 0
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            matches.append(other_word)
            x += 1
    if x == 0:
        print('No matches found')
    else:
        print(*matches, sep=' ')

    for x in range(len(my_word)):
        my_word[x] = my_word[x]+' '


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    import string
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word),
          'letters long.\n--------------------\nYou have 3 warnings left\nYou have 6 guesses left.\nAvailable letters:', string.ascii_lowercase)
    # secret_word = 'pineapple'
    hangman.letters_to_guess = []
    for x in range(len(secret_word)):
        hangman.letters_to_guess.append('_ ')
    print(*hangman.letters_to_guess, sep='')

    hangman.warnings = 3
    hangman.guesses_remaining = 6
    letters_guessed = []

    while True:

        guess = input('Please guess a letter: ')
        # guess = guess.lower()
        guess = guess.casefold()
        letters_guessed.append(guess)
        # print(letters_guessed)
        # hangman.letters_guessed = letters_guessed
        if guess != '*':
            if guess not in string.ascii_lowercase or len(guess) > 1 or guess in letters_guessed[0:-1]:
                if warnings_remaining(guess, letters_guessed) == False:
                    print('word was', secret_word)
                    break

            elif not get_guessed_word(secret_word, letters_guessed):
                # print('word was', secret_word)
                break

            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!\nYour total score for this game is:',
                      hangman.guesses_remaining*len(is_word_guessed.secret_word_list))
                break

        else:
            show_possible_matches(hangman.letters_to_guess)
            # print(hangman.letters_to_guess)
            # print(secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)

print(is_word_guessed("aaarap", ['a', 'r', 'p']))


# F(string) = F(string[0]) AND F(string[1:len])
def is_word_guessed_recursive(secret_word, letters_guessed):
    if len(secret_word) == 0:
        return True
    else:
        char = secret_word[0]
        return char in letters_guessed and is_word_guessed_recursive(secret_word[1:], letters_guessed)


print(is_word_guessed_recursive("aaarap", ['a', 'r', 'p']))
