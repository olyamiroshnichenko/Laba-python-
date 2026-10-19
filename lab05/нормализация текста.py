#normalize.py
text = input("Введите строку: ")

original_length = len(text)

words = text.split()
normalized_text = " ".join(words)

new_length = len(normalized_text)
word_count = len(words)

print("Исходная длина:", original_length)
print("Новая длина:", new_length)
print("Нормализованный текст:", normalized_text)
print("Количество слов:", word_count)
