#profile.py

last_name = input('Фамилия: ')
first_name = input('имя: ')
group = input('введите группу: ')
city = input('введите город: ')
age = int(input('введите возраст: '))
subject = input('введите предмет: ')
hours = float(input('введите количество часов:'))

full_name = f'{first_name}{last_name}'
age_4 = age + 4
hours_weeks = hours * 4
hours_day = hours / 7

print('           КАРТОЧКА ПРОФИЛЯ')
print(f'Полное имя:{full_name}')
print(f'Возраст через четыре года:{age_4}')
print(f'Время подготовки за четыре недели:{hours_weeks:.2f}ч')
print(f'Среднее время подготовки в день за семидневную неделю:{hours_weeks:2f}ч')
print(f'часы подготовки:{hours_day}')
