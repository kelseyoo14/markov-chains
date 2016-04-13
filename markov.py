from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open file and .read() contents into string
    file_words = open(file_path).read()
    return file_words


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # Create list to hold each word in the text file
    text_string = text_string.split()
    text_string[-1]

    # Create a list of bi-grams that will be the keys of the dictionary of markov chains
    counter = 0

    while counter < (len(text_string) - 2):
        #create a tuple/bigram of words
        new_key = (text_string[counter], text_string[counter+1])
        new_value = text_string[counter + 2]

        # check if new_key in chain, if it is, append new_value, otherwise add new_key with new_value to chain
        if new_key in chains:

            #chains[first_word, second_word].append(word that follows second word(word 3))
            #in other words index1 =  1, index2 = value1 + 1, index3 = index2 + 1
            chains[new_key].append(new_value)

            #chains[("could", "you")]= "could you"
        else:
            chains[new_key] = [new_value]

        counter += 1

    # for testing 
    # for key in chains:
    #     print key, chains[key]

    return [chains, text_string]


def make_text(chains, text_string):
    """Takes dictionary of markov chains; returns random text."""

    # creates variable to hold first words and last word of text file
    first_words = (text_string[0], text_string[1])
    last_word = text_string[-1]

    # picks random key from dictionary
    # current_key = choice(chains.keys())

    # initialize current_key
    current_key = first_words

    # recreate current_key if it equals the last two words of the file
    # so that we get more than 2 words in our story.
    # while current_key[1] == last_word:
    #     current_key = choice(chains.keys())

    # creates start of text
    text = "{} {}".format(current_key[0], current_key[1])

    # loop through a range, grabbing a new current_key, generating a new random_word
    # add new random_word to text
    # if new random_word is 'am?' break, so that 'am?' is the end of text
    for i in range(1000):
        random_word = choice(chains[current_key])
        text = text + " " + random_word
        if random_word == last_word:
            break
        current_key = (current_key[1], random_word)

    return text


# -----------------------------------------------------------------

filename = sys.argv[1]

chains, text_string = make_chains(open_and_read_file(filename))
print make_text(chains, text_string)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text