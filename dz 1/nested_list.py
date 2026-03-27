n = int(input())
a = []
for i in range(0, n):
    b = []
    b.append(input())
    b.append(float(input()))
    a.append(b)

# Получаем уникальные оценки и сортируем по возрастанию
grades = []
for student in a:
    if student[1] not in grades:
        grades.append(student[1])

grades.sort()  # Сортируем по возрастанию

if len(grades) >= 2:
    second_lowest = grades[1]  # вторая наименьшая
else:
    second_lowest = grades[0]

# Собираем имена студентов с этой оценкой
result = []
for student in a:
    if student[1] == second_lowest:
        result.append(student[0])

# Сортируем имена в алфавитном порядке
result.sort()
for name in result:
    print(name)