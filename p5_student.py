def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word]=counts[word]+1
        else:
            counts[word]=1
    return counts

print(count_words("a b a c"))
print(count_words(""))
