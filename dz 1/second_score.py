n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])
a.sort(reverse=True)
for i in range(0,n):
    if a[0] != a[i]:
        print(a[i])
        break;