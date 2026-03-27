s = input().strip().upper()
vowels = "AEIOU"

kevin = 0
stuart = 0
n = len(s)

for i in range(n):
    if s[i] in vowels:
        kevin += n - i
    else:
        stuart += n - i

if stuart > kevin:
    print("Стюарт", stuart)
elif kevin > stuart:
    print("Кевин", kevin)
else:
    print("Draw")