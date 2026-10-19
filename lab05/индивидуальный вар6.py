#variant.py
text = input()

count = 0

for word in text.split():
    word = word.strip(".,!?;:").lower()

    if word != "" and len(word) == 4:
        print(word)
        count += 1

if count == 0:
    print("Нет совпадений")

print(count)
