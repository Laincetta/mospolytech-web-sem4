import time
import sys

# 1. Увеличиваем лимит рекурсии с запасом
sys.setrecursionlimit(3000000)


def fact_rec(n):
    """Рекурсивное вычисление факториала."""
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)


def fact_it(num):
    """Итеративное вычисление факториала."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == "__main__":
    try:
        line = input("Введите целое число n: ").strip()
        if not line:
            print("Ошибка: Ввод пуст")
            sys.exit(1)

        n = int(line)

        # Замер итерации
        start_it = time.perf_counter()
        _ = fact_it(n)  # Считаем, но не выводим само число (оно может быть огромным)
        end_it = time.perf_counter()
        time_it = end_it - start_it

        # Замер рекурсии
        start_rec = time.perf_counter()
        _ = fact_rec(n)
        end_rec = time.perf_counter()
        time_rec = end_rec - start_rec

        # Вывод результатов
        print(f"\n--- Результаты для n = {n} ---")
        print(f"Итерация: {time_it:.10f} сек")
        print(f"Рекурсия: {time_rec:.10f} сек")

        if time_it < time_rec:
            print(f"Итерация быстрее рекурсии в {time_rec / time_it:.2f} раз")

    except ValueError:
        print("Ошибка: Введите корректное целое число")
    except RecursionError:
        print("Ошибка: Слишком большое число для рекурсии (Stack Overflow)")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")