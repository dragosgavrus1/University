def prime(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0

    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return 0
    return 1


def sum_of_prime_numbers_recursive(arr, pos, sum, n):
    if sum > n:
        return
    if sum == n:
        for i in range(pos):
            print(arr[i], end=" ")
        print("")
        return

    if pos == 0:
        start = 2
    else:
        start = arr[pos - 1]

    for i in range(start, n + 1):
        if prime(i) == 1:
            arr[pos] = i
            sum_of_prime_numbers_recursive(arr, pos + 1, sum + i, n)


def sum_of_prime_numbers_iterative(n):
    x = 2
    sum = 0
    arr = []
    end = False
    while not end:
        while sum + x <= n:
            if prime(x) == 1:
                sum += x
                arr.append(x)
                if sum == n:
                    print(arr)

                if sum <= n:
                    x = arr[-1]
            else:
                x = x + 1

        if len(arr) >= 1:
            x = arr.pop(-1)
            sum -= x
            x = x + 1
        else:
            end = True


# n = int(input("n: "))
# arr = [0] * n
# sum_of_prime_numbers_recursive(arr, 0, 0, n)
sum_of_prime_numbers_iterative(10)
