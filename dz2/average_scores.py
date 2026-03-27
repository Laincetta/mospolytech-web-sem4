def compute_average_scores(scores):
    # zip(*scores) группирует элементы всех кортежей по индексам.
    # Таким образом, мы получаем оценки каждого студента в отдельном наборе.
    averages = []
    for student_marks in zip(*scores):
        avg = sum(student_marks) / len(student_marks)
        averages.append(avg)
    
    return tuple(averages)

if __name__ == '__main__':
    # Читаем N (студенты) и X (предметы)
    n, x = map(int, input().split())
    
    # Собираем данные: список из X кортежей
    all_scores = []
    for _ in range(x):
        subject_scores = tuple(map(float, input().split()))
        all_scores.append(subject_scores)
    
    # Получаем результат через функцию
    result = compute_average_scores(all_scores)
    
    # Выводим каждое среднее значение с точностью до 1 десятичного знака
    for avg in result:
        print(f"{avg:.1f}")