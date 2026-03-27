import os
import sys

# python files_sort.py ~/Documents/web/dz2
def list_files(directory_path):
    """
    Возвращает отсортированный список имён файлов в директории.
    При ошибке возвращает None.
    """
    try:
        if not os.path.isdir(directory_path):
            return None

        all_items = os.listdir(directory_path)
        files = [f for f in all_items if os.path.isfile(os.path.join(directory_path, f))]
        files.sort(key=lambda f: (os.path.splitext(f)[1], f))
        return files
    except Exception:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        result = list_files(path)
        if result is not None:
            for f in result:
                print(f)
        else:
            print(f"Ошибка: Путь '{path}' не найден или не является директорией.")
    else:
        print("Использование: python files_sort.py <путь_к_директории>")