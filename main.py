import random

case = 0

# Main list sequences, only one word no sentences
words = ['Horse']

# Find the first letter
word = random.choice(words)
let = len(word) - (len(word) - 1)
first_let = word[:let]
if case = 0:
    first_let = first_let.lower()
elif case = 1:
    first_let = first_let.upper()

# Remove first letter
word_noLet = word[let:]

# Check if letter is vowel
if first_let == 'a' or first_let == 'e' or first_let == 'i' or first_let == 'o' or first_let == 'u':
    first_letVow = True
    confo = ' '
else:
    first_letVow = False
    confo = ' not '

# Convert to pig latin
if first_letVow == True:
    reos = word + '-yay'
elif first_letVow == False:
    reos = word_noLet + '-' + first_let + 'ay'

# Main Section
print('Original word: ' + word)
print('First letter: ' + first_let)
print('Letter is' + confo + 'a vowel')
print('\n')
print('Pig Latin: ' + reos)
