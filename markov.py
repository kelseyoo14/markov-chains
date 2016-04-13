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


def make_chains(text_string, n_gram = 2):
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
    # text_string[-1]

    # Create a list of n-grams that will be the keys of the dictionary of markov chains
    for i in range((len(text_string) - n_gram)):
        #create a tuple/bigram of words
        new_key = tuple(text_string[i:(i + n_gram)])
        # print new_key


        # new_key = (text_string[i], text_string[i+1])
        new_value = text_string[i + n_gram]
        # print new_value

        # check if new_key in chain, if it is, append new_value, otherwise add new_key with new_value to chain
        if new_key in chains:

            #chains[first_word, second_word].append(word that follows second word(word 3))
            #in other words index1 =  1, index2 = value1 + 1, index3 = index2 + 1
            chains[new_key].append(new_value)

            #chains[("could", "you")]= "could you"
        else:
            chains[new_key] = [new_value]


    # for testing 
    # for key in chains:
    #     print key, chains[key]

    return [chains, text_string]


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

    
    # initialize random_word and punctuation_count
    random_word = ()
    # punctuation_count = 0

    # make sure program prints at least so many sentences before breaking
    # break program at the last_word of text_string
    # loop through a range, grabbing a new current_key, generating a new random_word
    # add new random_word to text
    # if new random_word is 'am?' break, so that 'am?' is the end of text
    while random_word != last_word:
        # create next random_word
        random_word = choice(chains[current_key])

        # add new random_word to text
        text = text + " " + random_word

        # check to see if word ends with punctuation
        # if random_word[-1] == "?" or random_word[-1] == "." or random_word[-1] == "!":
        #     punctuation_count += 1
        

        # rebind new current_key to all values except first from current_key and the new random_word
        current_key = current_key[1:n_gram]
        current_key = current_key + tuple([random_word])


    return text


# -----------------------------------------------------------------

filename = sys.argv[1]

chains, text_string = make_chains(open_and_read_file(filename), 2)
print make_text(chains, text_string)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text