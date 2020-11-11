import re

words = {}
regex = re.compile("[^a-z]")

# read all words from the example.txt text file and count how often they occur
with open("example.txt", "r") as f:
    for line in f:
        for word in line.split():
            # convert word to lowercase as we don't care about case
            word = word.lower()
            # remove any superfluous comma's and full stops etc.
            word = regex.sub("", word)
            # add one tot he count if we've seen the word before, else set count to 1
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

print("unique words:")

# print words that only occur once
for word in words:
    if words[word] == 1:
        print(">> " + word)
