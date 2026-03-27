def wrapper(f):
    def fun(l):
        # 1. Создаем список отформатированных номеров
        formatted_list = []
        for s in l:
            # Берем последние 10 цифр номера
            clean = s[-10:]
            # Форматируем строку: +7 (xxx) xxx-xx-xx
            res = f"+7 ({clean[:3]}) {clean[3:6]}-{clean[6:8]}-{clean[8:]}"
            formatted_list.append(res)
        
        # 2. Передаем отформатированный список в функцию сортировки
        return f(formatted_list)
    return fun

@wrapper
def sort_phone(l):
    # Возвращаем отсортированный список строк
    return sorted(l)

if __name__ == '__main__':
    # Считываем количество N, затем N строк с номерами
    l = [input() for _ in range(int(input()))]
    # Выводим результат через распаковку списка с разделением новой строкой
    print(*sort_phone(l), sep='\n')