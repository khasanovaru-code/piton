data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g') 

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
        
letters.reverse()

numbers.remove(6.13)
numbers.insert(1, 2)
numbers.sort()

word = []
letters.extend(word)
letters [2] = "g"
letters [3] = "o"
letters [4] = "o"
letters [5] = "l" 

letters.remove ("C")
letters.remove ("T")
letters.remove ("h")
letters.remove ("k")

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)


