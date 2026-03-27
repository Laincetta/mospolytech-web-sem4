def sum_and_sub(a, b):
    """Возвращает кортеж (сумма, разность)."""
    return (a + b, a - b)


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    s, d = sum_and_sub(a, b)
    print(s)
    print(d)