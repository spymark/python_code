__author__ = 'spyros'
import string
import random

goal = "methinks it is like a weasel"
letters = string.letters[0:26]


def ran_word(wordlen):
    word = []
    for i in range(1,wordlen+1):
        word.append(random.choice(letters))
    return "".join(word)

test = ran_word(6)
while(test != 'weasel'):
    print test
    test = ran_word(6)
    continue
print test



# print random.choice(letters)
