def fun(s):
    # Проверяем наличие символа '@'
    if '@' not in s:
        return False

    # Разделяем на локальную часть и домен
    parts = s.split('@')
    if len(parts) != 2:          # больше одного '@'
        return False
    username, domain = parts[0], parts[1]

    # Локальная часть не должна быть пустой
    if not username:
        return False

    # В домене должна быть хотя бы одна точка
    if '.' not in domain:
        return False

    # Делим домен на имя сайта и расширение по последней точке
    dot_index = domain.rfind('.')
    website = domain[:dot_index]
    extension = domain[dot_index + 1:]

    # Ни одна из частей не должна быть пустой
    if not website or not extension:
        return False

    # Длина расширения – от 1 до 3
    if len(extension) > 3:
        return False

    # Проверка символов в имени пользователя
    for ch in username:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ch.isdigit() or ch == '-' or ch == '_'):
            return False

    # Проверка символов в имени сайта
    for ch in website:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ch.isdigit()):
            return False

    # Проверка символов в расширении
    for ch in extension:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
            return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)