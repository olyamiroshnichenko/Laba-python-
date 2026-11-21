# collections_lab.py

records = [
    {"title": "Борщ", "category": "суп", "amount": 6},
    {"title": "Щи", "category": "суп", "amount": 4},
    {"title": "Оливье", "category": "салат", "amount": 8},
    {"title": "Цезарь", "category": "салат", "amount": 2},
    {"title": "Наполеон", "category": "десерт", "amount": 10},
    {"title": "Чизкейк", "category": "десерт", "amount": 8},
]

def totals_by_category(records):
    """Словарь: категория -> сумма порций."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record.get("amount", 0)
    return totals

def unique_categories(records):
    """Множество уникальных категорий."""
    categories = set()
    for record in records:
        categories.add(record["category"])
    return categories

def titles_by_category(records):
    """Словарь: категория -> список названий."""
    result = {}
    for record in records:
        result.setdefault(record["category"], []).append(record["title"])
    return result

def best_recipe(records):
    """Кортеж (название, порции) для записи с максимумом порций."""
    best = max(records, key=lambda r: r["amount"])
    return (best["title"], best["amount"])

if __name__ == "__main__":
    totals = totals_by_category(records)
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    print("Категории:", sorted(unique_categories(records)))

    groups = titles_by_category(records)
    for category, titles in sorted(groups.items()):
        print(f"{category}: {', '.join(titles)}")

    name, amount = best_recipe(records)
    print(f"Пара: {name}, {amount}")
