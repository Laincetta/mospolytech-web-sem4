import string
with open('example.txt', 'r' , encoding="utf-8") as file:
    words = [word.strip(string.punctuation) for word in file.read().split()]
    max_len = max(len(word) for word in words) if words else 0
    
    for word in words:
        if len(word) == max_len:
            print(word)