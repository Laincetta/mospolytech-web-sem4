def my_sum(*args):
    result = 0
    for i in range(0, len(args)):
        result += int(args[i])
    return result


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(my_sum(*sys.argv[1:]))
    else:
        n = input().split(" ")
        print(my_sum(*n))