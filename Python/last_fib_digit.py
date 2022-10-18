def fib_digit(n):
    a = b = 1
    for _ in range(n - 2):
        a, b = (a + b) % 10, a

    return a


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()