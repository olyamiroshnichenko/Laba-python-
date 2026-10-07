# workload.py

subject1 = input("Название первого предмета: ")
count1 = int(input(f"Количество занятий по предмету «{subject1}» за неделю: "))
duration1 = int(input(f"Продолжительность занятия по предмету «{subject1}» (мин): "))

subject2 = input("Название второго предмета: ")
count2 = int(input(f"Количество занятий по предмету «{subject2}» за неделю: "))
duration2 = int(input(f"Продолжительность занятия по предмету «{subject2}» (мин): "))

minutes1 = count1 * duration1
minutes2 = count2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

available_hours = float(input("Доступное время на неделю (часы): "))
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4


print("            НАГРУЗКА ЗА НЕДЕЛЮ")
print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка:      {total_minutes} мин = {total_hours:.2f} ч")
print(f"Свободное время:     {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч")
