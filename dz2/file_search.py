import os
# python file_search.py test.tog

def find_file(start_dir, target_name):
    """
    Рекурсивный поиск файла. Возвращает полный путь или None.
    """
    for root, dirs, files in os.walk(start_dir):
        if target_name in files:
            return os.path.join(root, target_name)
    return None


def get_first_lines(path, n=5):
    """Возвращает первые n строк файла как список."""
    lines = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for _ in range(n):
                line = f.readline()
                if not line:
                    break
                lines.append(line.rstrip("\n"))
    except OSError:
        return None
    return lines


if __name__ == "__main__":
    target_file = input("Введите имя файла для поиска: ")
    start_dir = os.path.dirname(os.path.abspath(__file__))
    found_path = find_file(start_dir, target_file)

    if found_path:
        lines = get_first_lines(found_path, 5)
        if lines is not None:
            for line in lines:
                print(line)
        else:
            print(f"Файл {target_file} найден, но не удалось его прочитать")
    else:
        print(f"Файл {target_file} не найден")