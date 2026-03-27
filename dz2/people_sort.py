import operator

def person_lister(f):
    def inner(people):
        # 1. Сортируем список по возрасту (индекс 2). 
        people.sort(key=lambda x: int(x[2]))
        
        # 2. Применяем функцию форматирования f к каждому человеку в отсортированном списке.
        return map(f, people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # Считываем данные
    people = [input().split() for i in range(int(input()))]
    # Выводим результат
    print(*name_format(people), sep='\n')