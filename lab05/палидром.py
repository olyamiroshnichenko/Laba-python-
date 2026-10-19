#palidrome.py
text = input()

text = text.replace(" ", "").lower()

if text == "":
    print("Нет текста")
elif text == text[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
