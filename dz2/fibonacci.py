cube = lambda x: x**3 # Возводит число x в степень 3


def fibonacci(n):
    # Возвращаем список чисел Фибоначчи
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))