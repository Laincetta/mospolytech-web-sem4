import datetime
from functools import wraps

def function_logger(path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 1. Фиксируем время начала
            start_time = datetime.datetime.now()
            
            # 2. Выполняем функцию
            result = func(*args, **kwargs)
            
            # 3. Фиксируем время окончания и считаем длительность
            end_time = datetime.datetime.now()
            duration = end_time - start_time
            
            # 4. Формируем запись для лога
            log_lines = [
                func.__name__,
                start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], # С микросекундами как в примере
                str(args) if args else None,
                str(kwargs) if kwargs else None,
                str(result) if result is not None else '-',
                end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                str(duration)
            ]
            
            # 5. Записываем в файл (режим 'a' — append, создаст файл если его нет)
            with open(path, 'a', encoding='utf-8') as f:
                for line in log_lines:
                    if line is not None:
                        f.write(f"{line}\n")
            
            return result
        return wrapper
    return decorator

# Пример использования:
@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

if __name__ == "__main__":
    print(greeting_format('John'))