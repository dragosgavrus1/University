#
# This is the program's UI module.
# The user interface and all interaction with the user (print and input statements) are found here
#
import copy

import src.functions


def read_command():
    args = input("Command: ")
    args = args.split()
    return args


def menu():
    print("add, insert, remove, replace, list, filter, undo, exit")


# C
def print_all(all_transactions):
    for i in range(len(all_transactions)):
        print(src.functions.to_str(all_transactions[i]))


def print_type(all_transactions, type):
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if src.functions.get_type(trans) == type:
            print(src.functions.to_str(all_transactions[i]))


def print_gr(all_transactions, value):
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if src.functions.get_value(trans) > value:
            print(src.functions.to_str(all_transactions[i]))


def print_ls(all_transactions, value):
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if src.functions.get_value(trans) < value:
            print(src.functions.to_str(all_transactions[i]))


def print_eq(all_transactions, value):
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if src.functions.get_value(trans) == value:
            print(src.functions.to_str(all_transactions[i]))


def print_balance(all_transactions, day):
    ans = 0
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if src.functions.get_day(trans) <= day:
            if src.functions.get_type(trans) == "in":
                ans = ans + src.functions.get_value(trans)
            elif src.functions.get_type(trans) == "out":
                ans = ans - src.functions.get_value(trans)
    print(ans)


def run_console():
    all_transactions = [{"day": 11, "value": 2000, "type": "in", "description": "salary"},
                        {"day": 19, "value": 13, "type": "in", "description": "change"},
                        {"day": 3, "value": 20, "type": "out", "description": "rd"},
                        {"day": 5, "value": 100, "type": "out", "description": "bread"},
                        {"day": 12, "value": 230, "type": "out", "description": "clothes"},
                        {"day": 8, "value": 500, "type": "out", "description": "rent"},
                        {"day": 2, "value": 50, "type": "in", "description": "gift"},
                        {"day": 22, "value": 100, "type": "in", "description": "win"},
                        {"day": 9, "value": 100, "type": "out", "description": "food"},
                        {"day": 11, "value": 77, "type": "out", "description": "water"}]
    history = [copy.deepcopy(all_transactions)]
    while True:
        menu()
        arguments = read_command()
        exception = None
        try:
            if arguments[0] == "undo":
                history, all_transactions = src.functions.undo(history)
            elif arguments[0] == "add":
                all_transactions = src.functions.add_transaction(all_transactions, int(arguments[1]), arguments[2],
                                                                 arguments[3])
                history.append(copy.deepcopy(all_transactions))
            elif arguments[0] == "insert":
                all_transactions, exception = src.functions.insert_transaction(all_transactions, int(arguments[1]),
                                                                               int(arguments[2]), arguments[3],
                                                                               arguments[4])
                if exception is not None:
                    print(exception)
                else:
                    history.append(copy.deepcopy(all_transactions))

            elif arguments[0] == "remove":
                if len(arguments) == 4:
                    all_transactions, exception = src.functions.remove_days(all_transactions, int(arguments[1]),
                                                                            int(arguments[3]))
                elif arguments[1].isdigit():
                    all_transactions, exception = src.functions.remove_day(all_transactions, int(arguments[1]))
                else:
                    all_transactions, exception = src.functions.remove_type(all_transactions, arguments[1])

                if exception is not None:
                    print(exception)
                else:
                    history.append(copy.deepcopy(all_transactions))

            elif arguments[0] == "replace":
                all_transactions, exception = src.functions.replace_value(all_transactions, int(arguments[1]),
                                                                          arguments[2], arguments[3],
                                                                          int(arguments[5]))
                if exception is not None:
                    print(exception)
                else:
                    history.append(copy.deepcopy(all_transactions))

            elif arguments[0] == "list":
                if len(arguments) == 3:
                    if arguments[1] == "<":
                        print_ls(all_transactions, int(arguments[2]))
                    elif arguments[1] == "=":
                        print_eq(all_transactions, int(arguments[2]))
                    elif arguments[1] == ">":
                        print_gr(all_transactions, int(arguments[2]))
                    elif arguments[1] == "balance":
                        print_balance(all_transactions, int(arguments[2]))
                elif len(arguments) == 2:
                    print_type(all_transactions, arguments[1])
                else:
                    print_all(all_transactions)

            elif arguments[0] == "filter":
                if len(arguments) == 3:
                    all_transactions = src.functions.filter_smaller(all_transactions, arguments[1], int(arguments[2]))
                else:
                    all_transactions = src.functions.filter_type(all_transactions, arguments[1])
                history.append(copy.deepcopy(all_transactions))

            elif arguments[0] == "exit":
                break

            else:
                print("There is no function called ", arguments[0])
            print("")

        except TypeError:
            print("Incorrect input, letters cannot be converted to integers")
            print("")

        except IndexError:
            print("Incorrect input")
            print("")
