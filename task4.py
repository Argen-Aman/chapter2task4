a = input('Write me any sentence, and I will try to count the words in it separated by spaces:\n')
x = int(a.count (' '))
y = int(a.count ('  '))
z = int(a.count ('   '))
v = int(a.count ('    '))
w = int(a.count ('  '))

print('The sentence has ' + str(1 + v + w + x + y + z) + ' word(s).')
