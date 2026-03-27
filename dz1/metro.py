n = int(input())
passengers = []

for _ in range(n):
    a, b = map(int, input().split())
    passengers.append((a, b))

t = int(input())

count = 0
for a, b in passengers:
    if a <= t <= b:
        count += 1

print(count)