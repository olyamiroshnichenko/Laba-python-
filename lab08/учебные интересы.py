def common_topics(first, second):
    return sorted(set(first) & set(second))
def all_topics(first, second):
    return sorted(set(first) | set(second))
first = input("Введите темы первого студента: ").lower().split()
second = input("Введите темы второго студента: ").lower().split()
print("Общие темы:", common_topics(first, second))
print("Все темы:", all_topics(first, second))
