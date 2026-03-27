str1 = input().strip()
str2 = input().strip()
if sorted(str1) == sorted(str2):
    print("YES")
else: 
    print("NO")