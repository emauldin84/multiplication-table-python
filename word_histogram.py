# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary
#  containing the tally of how many times each word in the sentence was used in the text

# recieve input from user
string = input('Please enter a sentence: ')

def letter_histogram(word):
    tally = {}
    my_string = word.lower().split()
    for i in my_string:
        if i not in tally:
            tally[i] = 1
        elif i in tally:
            tally[i] = tally[i] + 1
    print(tally)

letter_histogram(string)