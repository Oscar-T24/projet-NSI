# Create an empty dictionary.
python_words = {}

# Fill the dictionary, pair by pair.
python_words['list'] = 'A list'
python_words['dictionary'] = 'A collection of key-value pairs.'
python_words['function'] = 'A named set of instructions that defines a set of actions in Python.'

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print("\nWord: %s" % word)
    print("Meaning: %s" % meaning)