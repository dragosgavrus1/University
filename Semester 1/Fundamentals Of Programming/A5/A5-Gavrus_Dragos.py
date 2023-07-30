import math


def create_c(real, img):
    """
    Create complex number
    :param real: the real part of the complex number
    :param img: the imaginary part of the complex number
    :return: the list/dictionary containing the complex number
    """
    return [real, img]
    # return {'real': real, "img": img}


def add_complex():
    """
    Creating a complex number
    :return: the complex number (list or dictionary)
    """
    real = int(input("Enter real part: "))
    img = int(input("Enter imaginary part: "))

    c = create_c(real, img)
    return c


def get_real(c):
    return c[0]
    # return c["real"]


def get_img(c):
    """

    param c: the complex number (list or dictionary)
    :return: the imaginary part
    """
    return c[1]
    # return c["img"]


def read_list(arr):
    # reading the list
    n = int(input("Numbers in the list: "))
    for i in range(n):
        num = add_complex()
        arr.append(num)


def get_str(c):
    real = get_real(c)
    img = get_img(c)
    if img == 0:
        return str(real)
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + "-" + str(img) + "i"


def display_list(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            print(get_str(arr[i]))
        else:
            print(get_str(arr[i]), end=", ")


def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


def modulus(c1):
    # calculate the modulus of the complex number
    real = get_real(c1)
    img = get_img(c1)
    return math.sqrt(real * real + img * img)


def consecutive_prime_modules(arr):
    """
    Find the longest subarray with the difference between two consecutive elements moduli is prime
    param arr: The list
    :return: the maximum length and the starting and ending indexes
    """
    # the longest subarray of numbers where the difference between the modulus of consecutive numbers is a prime number
    maxlen = 0  # max length
    maxi = 0  # index of the start of the max subarray
    maxj = 0  # index of the end
    okay = False  # check if the previous numbers are in a subarray
    l = 0  # current start index
    r = 0  # current end index

    for i in range(len(arr) - 1):
        dif = modulus(arr[i]) - modulus(arr[i + 1])  # calculate the difference of the moduli
        if int(dif) == dif:  # if the difference is an integer
            if prime(int(dif)):  # if its prime
                if not okay:  # if the difference of the previous numbers is not prime
                    if r - l > maxlen:  # check if the previous length is the max one
                        maxlen = r - l + 1  # change the indexes
                        maxi = l
                        maxj = r
                    l = i  # start the new ones
                    r = i + 1
                    okay = True
                else:  # if the number before also has the difference a prime number
                    r = r + 1
        else:
            okay = False  # if the subarray does not continue

    if r - l + 1 > maxlen:
        maxlen = r - l + 1
        maxi = l
        maxj = r
    return maxlen, maxi, maxj


def print_prime_modulus(maxlen, maxi, maxj):
    print("Length of the longest subarray where the difference between the modulus of consecutive numbers is prime: ",
          maxlen)
    for i in range(maxi, maxj + 1):
        if i == maxj:
            print(get_str(arr[i]))
        else:
            print(get_str(arr[i]), end=", ")


def max_subarray_sum(arr):
    """
    Find the subarray with the maximum sum between the real parts of the elements
    param arr: The list
    :return: the maximum length, first elem of the subarray and last elem
    """
    maximum = get_real(arr[0])  # the max sum
    starting_index = 0  # the first element of the subarray
    end_index = 0  # the last element of the subarray
    curr_start = 0  # the current start
    curr_max = 0  # the max sum up to this point

    for i in range(len(arr)):
        curr_max = curr_max + get_real(arr[i])  # we add the real part to the sum

        if maximum < curr_max:  # we update the max sum if necessary
            maximum = curr_max
            starting_index = curr_start
            end_index = i
        if curr_max < 0:  # if the current sum is less than 0 we start from the next index a new subarray
            curr_max = 0
            curr_start = i + 1
    return maximum, starting_index, end_index


def print_max_subarray(maximum, starting, end):
    print("Max sum: ", maximum)
    print("Length: ", end - starting + 1)
    for i in range(starting, end + 1):
        if i == end:
            print(get_str(arr[i]))
        else:
            print(get_str(arr[i]), end=", ")


def print_menu():
    print("1. Read list ")
    print("2. Display list")
    print("3. Properties ")
    print("4. Exit application")


def start():
    while True:
        print_menu()
        opt = int(input("Option: "))
        if opt == 4:
            break
        if opt == 1:
            arr = []
            read_list(arr)
        if opt == 2:
            display_list(arr)
        if opt == 3:
            maxl, maxi, maxj = consecutive_prime_modules(arr)
            print_prime_modulus(maxl, maxi, maxj)
            print("")
            maximum, start_ind, end = max_subarray_sum(arr)
            print_max_subarray(maximum, start_ind, end)
        print("")


arr = [[15, 8], [8, 6], [-40, 2], [1, 2], [-3, 5], [12, 5], [6, 8], [3, 4], [7, 1], [-1, 2]]
start()
