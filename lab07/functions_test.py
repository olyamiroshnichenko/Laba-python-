def sum_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    return " ".join(text.lower().split())

def select_numbers(numbers, threshold):
    result = []
    for number in numbers:
        if number == threshold:
            result.append(number)
    return result
