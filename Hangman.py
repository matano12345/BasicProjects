import string


def check_win(secret_word, old_letters_guessed):
    """Checks if a given word contains specific letters.
        :param secret_word: given word
        :param old_letters_guessed: specific letters
        :type secret_word: str
        :type old_letters_guessed: list
        :return: The result of whether or not the word has all the letters
        :rtype: bool
        """
    counter = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            counter += 1
    return counter == len(secret_word)


def show_hidden_word(secret_word, old_letters_guessed):
    """Prints the letters that were guessed successfully so far.
        Letters that haven't been guessed will be presented as '_'
        :param secret_word: given word
        :param old_letters_guessed: guessed letters
        :type secret_word: str
        :type old_letters_guessed: list
        :return: String representation of guessed letters and blank spaces
        :rtype: str
        """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + ' '
        else:
            hidden_word += '_ '
    return hidden_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the input is valid AND wasn't guessed yet.
        :param letter_guessed: the input that was entered by the user
        :param old_letters_guessed: guessed letters
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: If the input was a single letter that wasn't guessed yet, function will return 'True'
                and 'False' otherwise
        :rtype: bool
        """
    return (len(letter_guessed) == 1) and letter_guessed.isalpha() and (letter_guessed not in old_letters_guessed[::])


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Updates the guessed letters pool (if the input is valid).
            :param letter_guessed: the input that was entered by the user
            :param old_letters_guessed: guessed letters
            :type letter_guessed: str
            :type old_letters_guessed: list
            :return: If the input was valid, function will update 'old_letters_guessed and return 'True'
                    Otherwise, function will print 'X' and the letters that were guessed and return 'False'
            :rtype: bool
            """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += letter_guessed
        return True
    else:
        old_letters_guessed.sort()
        print("X\n" + "-> ".join(old_letters_guessed))
        return False


def choose_word(file_path, index):
    """Returns the word located in a specified index. (If 'index' is larger the number of words inside the file,
    the function will reduce the amount needed for it to run correctly).
                :param file_path: location of the file that needs to be checked
                :param index: number (int) which represent the location of a word inside the file
                :type file_path: str
                :type index: int
                :return: The word located in the specified index.
                :rtype: str
                """
    file = open(file_path, "r")
    file_content = file.read()
    file_content = file_content.split(' ')
    while index > len(file_content):
        index -= len(file_content)
    index -= 1
    chosen_word = file_content[index]
    file.close()
    return chosen_word.lower()


def print_hangman():
    """The function prints the Hangman banner.
    :return: None
    """
    HANGMAN_ASCII_ART = """\
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART)


def create_photos():
    """The function creates a set of hangman positions and returns them as a dictionary.
    :return: set of hangman position, with keys range from 1-6
    :rtype: dict
    """
    hangman_dict = {"0": "    x-------x",
                    "1": """    x-------x
    |
    |
    |
    |
    |""",
                    "2": """    x-------x
    |       |
    |       0
    |
    |
    |""",
                    "3": """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
                    "4": """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
                    "5": """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
                    "6": """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    return hangman_dict


def main():
    """This program is a game of hangman.
    The user uses a text file that contain words separated by a blank space.
    He is then required to guess, which word was chosen and to guess the different letters
    that combines it.
    :rtype: None
    """
    HANGMAN_PHOTOS = create_photos()  # create the different looks of the hangman
    MAX_TRIES, num_of_tries = 6, 0
    print_hangman()
    file_path = input("Enter file path: ")  # The location of the text file
    index = int(input("Enter index: "))  # The index number of the word to be played
    secret_word = choose_word(file_path, index)  # 'secret word' is the word selected from the file
    old_letters_guessed = []
    print("Let's Start!")
    print(HANGMAN_PHOTOS[str(num_of_tries)])
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries <= MAX_TRIES:
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed.lower(), old_letters_guessed):  # if letter pass and wasn't guessed
            if letter_guessed in secret_word:  # if the guess was correct
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed):  # if all letters were guessed
                    print("WIN")
                    break
            else:
                num_of_tries += 1
                print(":(")
                if num_of_tries <= MAX_TRIES:
                    print(HANGMAN_PHOTOS[str(num_of_tries)])
                    print(show_hidden_word(secret_word, old_letters_guessed))
                if num_of_tries == MAX_TRIES:  # when there are no more tries left
                    print("LOSE")
                    break


if __name__ == "__main__":
    main()
