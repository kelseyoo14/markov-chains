from random import choice


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

    # Create a list of bi-grams that will be the keys of the dictionary of markov chains
    counter = 0
    # while counter < len(text_string) -2:
    #     #create a tuple/bigram of words
    #     bigram_keys.append([(text_string[counter], text_string[counter+1])])
    #     counter += 1


    while counter < (len(text_string) - 2):
        #create a tuple/bigram of words
        if text_string[counter+1] in chains:
            chains[(text_string[counter], text_string[counter+1])].append(text_string[counter + 2])

            #chains[("could", "you")]= "could you"
        else:
            chains[(text_string[counter], text_string[counter+1])] = [text_string[counter + 2]]



        counter += 1








    for key in chains:
        print key, chains[key]
    return chains

make_chains(open_and_read_file("green-eggs.txt"))

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     text = ""

#     # your code goes here

#     return text


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text