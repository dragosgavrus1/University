import numpy


def recursive_partitions(arr, n, set1, set2, sum1, sum2, poz):
    if poz == n:
        if sum1 == sum2:
            print("Subset 1: ", set1)
            print("Subset 2: ", set2)
            return True
        else:
            return False

    set1.append(arr[poz])
    rez = recursive_partitions(arr, n, set1, set2, sum1 + arr[poz], sum2, poz + 1)
    if rez:
        return rez

    set1.pop()
    set2.append(arr[poz])
    rez = recursive_partitions(arr, n, set1, set2, sum1, sum2 + arr[poz], poz + 1)

    if not rez:
        set2.pop()
    return rez


def naive_partition(arr, n):
    sum_arr = sum(arr)
    if sum_arr % 2 == 1:
        print("The array can't be partitioned into two subsets with equal sum")
        return
    subset1 = []
    subset2 = []
    return recursive_partitions(arr, n, subset1, subset2, 0, 0, 0)


def partition_dp(arr, n):
    sum_arr = sum(arr)
    if sum_arr % 2 == 1:
        print("The array can't be partitioned into two subsets with equal sum")
        return

    k = sum_arr // 2
    dp = numpy.zeros((n + 1, k + 1))

    for i in range(1, k + 1):
        dp[0][i] = False  # No sum can be obtained if num of elements is 0
    for i in range(n + 1):
        dp[i][0] = True  # Sum 0 can be obtained by not selecting any elements

    # Fill the DP table
    for i in range(1, n + 1):
        for cur_sum in range(1, k + 1):
            dp[i][cur_sum] = dp[i - 1][cur_sum]
            if arr[i - 1] <= cur_sum:
                dp[i][cur_sum] = dp[i][cur_sum] or dp[i - 1][cur_sum - arr[i - 1]]
                # if cur_sum - arr[i-1] can be computed so can cur_sum

    subset1 = []
    subset2 = []
    if not dp[n][k]:
        print("The array can't be partitioned into two subsets with equal sum")
        return

    i = n
    cur_sum = k

    while i > 0 and cur_sum >= 0:
        if dp[i - 1][cur_sum]:
            i = i - 1
            subset2.append(arr[i])

        elif dp[i - 1][cur_sum - arr[i - 1]]:
            i = i - 1
            cur_sum = cur_sum - arr[i]
            subset1.append(arr[i])

    print("Subset 1: ", subset1)
    print("Subset 2: ", subset2)


A = [1, 1, 1, 1, 2, 3, 5]
n = len(A)
partition_dp(A, n)
# naive_partition(A, n)
