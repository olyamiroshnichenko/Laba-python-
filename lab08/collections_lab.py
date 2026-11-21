def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        word = word.strip(", . ! ? ; :")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts
def print_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
text = input("Введите текст: ")
counts = word_counts(text)
print_counts(counts)
