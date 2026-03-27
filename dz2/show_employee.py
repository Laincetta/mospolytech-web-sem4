def show_employee(name, salary=100000):
    """Возвращает строку с информацией о сотруднике."""
    return name + ": " + str(salary) + " р"


if __name__ == "__main__":
    n = input()
    salary = input()
    if salary == "":
        print(show_employee(n))
    else:
        print(show_employee(n, int(salary)))
