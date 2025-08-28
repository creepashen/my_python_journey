name = input('Enter the of file ->')

Fhand = open(name)

count = dict()

for line in Fhand:
    line = line.split()
    
    for words in line:
        count[words] = count.get(words, 0 ) + 1

what_word = ''
counts = 0

for word, count in count.items():
    if count >= counts:
        counts = count
        what_word = word

print(f'The word is --> {what_word.upper()}', counts,'Times')
