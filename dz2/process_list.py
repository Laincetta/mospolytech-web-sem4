import timeit

# List Comprehension
def process_list(arr):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]

# Функция-генератор
def process_list_gen(arr):
    for i in arr:
        yield i ** 2 if i % 2 == 0 else i ** 3

if __name__ == "__main__":
    test_arr = list(range(1000))

    # Замеряем время (1000 повторений)
    t_comp = timeit.timeit(lambda: process_list(test_arr), number=1000)
    print(t_comp)
    t_gen = timeit.timeit(lambda: list(process_list_gen(test_arr)), number=1000)
    print(t_gen)
