import random
import timeit


def generate_n_numbers(n):
    nlist = []
    for i in range(n):
        # adding random generated numbers between 0 and 100 to the list
        nlist.append((random.randint(1, 99)))
    return nlist


def insert_sort(nlist):
    k = 0
    # we start from the second element on the list because insert sort compares the current element to the elements
    # in front of it while they are bigger and move them up a position and insert the element where it is bigger than
    # the predecessor or the firs one in the list
    for i in range(1, len(nlist)):
        a = nlist[i]
        j = i - 1

        # we move the elements greater than nlist[i] one position up
        while j >= 0 and a < nlist[j]:
            nlist[j + 1] = nlist[j]
            j = j - 1

        if j + 1 != i:
            nlist[j + 1] = a

    return nlist

# comb sort is an improved bubble sort by making the gap between the two numbers it compares larger and by doing that
# the small numbers at the end of the list are swapped and

def comb_sort(nlist):
    # the initial gap for comb sort is the list length divided by the shrink factor witch is generally 1.3
    gap = len(nlist)
    is_sorted = False
    shrink = 1.3

    while is_sorted == False:
        # the gap is divided again
        gap = int(gap / shrink)

        if gap < 1:
            # if the gap is less than 1 the algorithm will check the list again and if there are no other swaps the
            # list is sorted
            gap = 1
            is_sorted = True

        for i in range(len(nlist) - gap):

            # normal bubble sort swaps with the added gap
            if nlist[i] > nlist[i + gap]:
                nlist[i], nlist[i + gap] = nlist[i + gap], nlist[i]
                is_sorted = False

    return nlist


def run_menu():
    print("Menu : ")
    print("1. Generate random numbers ")
    print("2. Insert sort ")
    print("3. Comb sort")
    print("4. Best case")
    print("5. Worst case")
    print("6. Average case")
    print("0. Exit")
    while True:
        option = int(input("Option = "))
        if option == 0:
            break
        if option == 1:
            n = int(input("n : "))
            nlist = generate_n_numbers(n)
            print(nlist)
        if option == 2:
            nlist = insert_sort(nlist)
            print("The sorted list : ", nlist)

        if option == 3:
            nlist = comb_sort(nlist)
            print("The sorted list : ", nlist)
            x = int(input("Case = "))

        if option == 4:
            print("1. Insert sort")
            print("2. Comb sort")
            x = int(input("x = "))
            if x == 1:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    nlist.sort()
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    insert_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2

            if x == 2:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    nlist.sort()
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    comb_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2

        if option == 5:
            print("1. Insert sort")
            print("2. Comb sort")
            x = int(input("x = "))
            if x == 1:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    nlist.sort(reverse=True)
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    insert_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2

            if x == 2:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    nlist.sort(reverse=True)
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    comb_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2

        if option == 6:
            print("1. Insert sort")
            print("2. Comb sort")
            x = int(input("x = "))
            if x == 1:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    insert_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2

            if x == 2:
                leng = 10000
                for i in range(5):
                    nlist = generate_n_numbers(leng)
                    print("Length : ", leng)
                    startime = timeit.default_timer()
                    comb_sort(nlist)
                    print("Time : ", timeit.default_timer() - startime)
                    leng = leng * 2


run_menu()
