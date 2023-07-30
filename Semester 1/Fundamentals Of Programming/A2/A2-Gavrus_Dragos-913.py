import random


def generate_n_numbers():
    n = int(input("The number of the elements in the list : "))
    nlist = []
    for i in range(n):
        # adding random generated numbers between 0 and 100 to the list
        nlist.append((random.randint(1, 99)))
    return nlist


def insert_sort(nlist, step):
    # we start from the second element on the list because insert sort compares the current element to the elements
    # in front of it while they are bigger and move them up a position and insert the element where it is bigger than
    # the predecessor or the firs one in the list

    k = 0
    for i in range(1, len(nlist)):
        # we start a counter for the steps and when k=step we display the list and reset the counter
        if k == step:
            print(nlist)
            k = 0

        a = nlist[i]
        j = i - 1

        # we move the elements greater than nlist[i] one position up
        while j >= 0 and a < nlist[j]:
            nlist[j + 1] = nlist[j]
            j = j - 1

        if j + 1 != i:
            nlist[j + 1] = a
            k = k + 1
    print("The sorted list : ", nlist)


# comb sort is an improved bubble sort by making the gap between the two numbers it compares larger and by doing that
# the small numbers at the end of the list are swapped and

def comb_sort(nlist, step):
    # the initial gap for comb sort is the list length divided by the shrink factor witch is generally 1.3
    gap = len(nlist)
    is_sorted = False
    shrink = 1.3
    k = 0  # the step counter

    while is_sorted == False:
        # the gap is divided again
        gap = int(gap / shrink)

        if gap < 1:
            # if the gap is less than 1 the algorithm will check the list again and if there are no other swaps the
            # list is sorted
            gap = 1
            is_sorted = True

        for i in range(len(nlist) - gap):

            if k == step:
                print(nlist)
                k = 0

            # normal bubble sort swaps with the added gap
            if nlist[i] > nlist[i + gap]:
                nlist[i], nlist[i + gap] = nlist[i + gap], nlist[i]
                is_sorted = False
                k = k + 1
    print("The sorted list : ", nlist)


def run_menu():
    print("Menu : ")
    print("1. Generate random numbers ")
    print("2. Insert sort ")
    print("3. Comb sort")
    print("0. Exit")
    nlist = []
    while True:
        option = int(input("Option = "))
        if option == 0:
            break
        if option == 1:
            nlist = generate_n_numbers()
            print(nlist)
        if option == 2:
            step = int(input("Step : "))
            insert_sort(nlist, step)
        if option == 3:
            step = int(input("Step : "))
            comb_sort(nlist, step)


run_menu()
