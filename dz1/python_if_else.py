n = int(input())
if n < 1 or n > 100:
    print("Error");
elif n % 2 == 1:
    print("Weird")
elif (2 <= n <= 5):
    print("Not Weird")
elif (6 <= n <= 20):
    print("Weird")
elif (20 < n):
    print("Not Weird")