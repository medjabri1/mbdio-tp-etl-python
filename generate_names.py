from random import choice, randint
from string import ascii_letters

# GENERATE RANDOM NAMES IN FILE

file = open('./output/random_names.txt', 'w')
data = ''

for i in range(100):

    current_line = ''

    current_line = ''.join(choice(ascii_letters)
                           for i in range(randint(5, 10)))

    current_line += ' '
    current_line += ''.join(choice(ascii_letters) for i in range(5))

    data += current_line
    data += '\n'

file.write(data)
