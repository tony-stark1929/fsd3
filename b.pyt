# find 5 unique and longest words
f=open('xyzz.txt')
words=f.read().split()
unique_words=set(words)
unique_words_sorted=sorted(unique_words, key=lambda x: len(x), reverse=True)
for i in range(5):
    print(unique_words_sorted[i])
            