def is_leap(a):
    if (a % 4 == 0 and not(a % 100 == 0)) or a % 400 == 0:
        return True
    else:
        return False
    
a = int(input())
print(is_leap(a))
