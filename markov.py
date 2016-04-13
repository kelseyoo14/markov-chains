from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and returns
    the file's contents as a list with all the file's words
    """

    # Open file and .read() contents into string
    file_words = open(file_path).read()

    # Create list to hold each word in the text file
    file_words = file_words.split()

    return file_words


def make_chains(text_string, n_gram = 2):
    """Takes n_gram input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # Create a list of n-grams that will be the keys of the dictionary of markov chains
    for i in range((len(text_string) - n_gram)):
        #create a tuple/bigram of words
        new_key = tuple(text_string[i:(i + n_gram)])
        new_value = text_string[i + n_gram]

        # check if new_key in chain, if it is, append new_value
        # otherwise add new_key with new_value to chain
        if new_key in chains:
            chains[new_key].append(new_value)

        else:
            chains[new_key] = [new_value]


    return chains


def make_text(chains, text_string):
    """Takes dictionary of markov chains and text_string of file words; returns random text."""

    # variable to hold last word of text file
    last_word = (text_string[-1])


    # picks random key from dictionary
    current_key = choice(chains.keys())
    n_gram = len(current_key)

    # make sure current_key starts with upper case letter and doesn't inclue last_word
    while current_key[0][0].islower() or current_key[n_gram - 1] == last_word:
        current_key = choice(chains.keys())


    # creates start of text
    text = " ".join(current_key)

    # initialize random_word
    random_word = ()

    # while random_word isn't equal to last_word, continue adding more words to 'text'
    while random_word != last_word:
        # create next random_word
        random_word = choice(chains[current_key])

        # add new random_word to text
        text = text + " " + random_word
        
        # rebind new current_key to all values except first from current_key and the new random_word
        current_key = current_key[1:n_gram]
        current_key = current_key + tuple([random_word])


    return text


# -----------------------------------------------------------------

filename = sys.argv[1]

text_string = open_and_read_file(filename)
chains = make_chains(text_string, 2)
print make_text(chains, text_string)
