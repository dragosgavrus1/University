#
# The program's functions are implemented here.
# There is no user interaction in this file, therefore no input/print statements.
# Functions here communicate via function parameters, the return statement and raising of exceptions.
#

import datetime


def create_transaction(day, value, type, description):
    return {"day": day, "value": value, "type": type, "description": description}


def get_day(transaction):
    ans = int(transaction["day"])
    return ans


def set_day(transaction, day):
    transaction["day"] = day


def get_value(transaction):
    ans = int(transaction["value"])
    return ans


def set_value(transaction, value):
    transaction["value"] = value


def get_type(transaction):
    return transaction["type"]


def set_type(transaction, type):
    transaction["type"] = type


def get_description(transaction):
    return transaction["description"]


def set_description(transaction, description):
    transaction["description"] = description


def to_str(transaction):
    return str(get_day(transaction)) + " " + str(get_value(transaction)) + " " + str(get_type(transaction)) + " " + str(
        get_description(transaction))


# A
def add_transaction(all_transactions, value, type, description):
    # Add a new transaction at the current day
    curr_date = datetime.datetime.now()
    transaction = create_transaction(curr_date.day, value, type, description)
    all_transactions.append(transaction)
    return all_transactions


def insert_transaction(all_transactions, day, value, type, description):
    # Insert a new transaction at any day of the month
    try:
        if day > 30 or day < 1:
            raise Exception("Day should be between 1 and 30")
        transaction = create_transaction(day, value, type, description)
        all_transactions.append(transaction)
        return all_transactions, None
    except Exception as e:
        return all_transactions, e


def test_add():
    trns = [create_transaction(20, 11, "in", "rnd")]
    trns2 = []
    add_transaction(trns2, 11, "in", "rnd")
    assert trns == trns2


def test_insert():
    trns = [create_transaction(20, 11, "in", "rnd")]
    trns2 = []
    insert_transaction(trns2, 20, 11, "in", "rnd")
    assert trns == trns2


# B
def remove_day(all_transactions, day):
    """
    Remove all transactions from a day
    :param all_transactions: all transactions
    :param day: the day for removing the transactions
    :return: the new list
    """
    try:
        if day > 30 or day < 1:
            raise Exception("Day should be between 1 and 30")
        c = []
        for i in range(len(all_transactions)):
            transaction = all_transactions[i]
            if get_day(transaction) != day:
                c.append(transaction)
        return c, None
    except Exception as e:
        return all_transactions, e


def test_remove_day():
    trns = [{"day": 2, "value": 10, "type": "in", "description": "na"}]
    trns2 = trns
    trns2 = remove_day(trns2, 2)
    assert trns2 == []


def remove_days(all_transactions, start_day, end_day):
    """
    Remove elements between the days given in the parameters
    :param all_transactions: the transactions
    :param start_day:
    :param end_day:
    :return: the new list
    """
    try:
        for i in range(start_day, end_day + 1):
            all_transactions, exception = remove_day(all_transactions, i)  # Use remove day function for the days
            if exception is not None:
                raise Exception("Day should be between 1 and 30")
        return all_transactions, None
    except Exception as e:
        return all_transactions, e


def test_remove_days():
    trns = [{"day": 2, "value": 10, "type": "in", "description": "na"},
            {"day": 5, "value": 10, "type": "in", "description": "na"}]
    trns2 = trns
    trns2 = remove_days(trns2, 2, 5)
    assert trns2 == []


def remove_type(all_transactions, type):
    """
    Remove all elements of the type from the list
    :param all_transactions: the transactions
    :param type: the type
    :return: the new list
    """
    try:
        if type != "in":
            if type != "out":
                raise Exception("There are no such types")
        c = []
        for i in range(len(all_transactions)):
            trans = all_transactions[i]
            if get_type(trans) != type:
                c.append(trans)
        return c, None
    except Exception as e:
        return all_transactions, e


def test_remove_type():
    trns = [{"day": 2, "value": 10, "type": "in", "description": "na"},
            {"day": 5, "value": 10, "type": "in", "description": "na"}]
    trns2 = trns
    trns2 = remove_type(trns2, "in")
    assert trns2 == []


def replace_value(all_transactions, day, type, description, new_value):
    # Replace a value from a transaction by giving the details of the transaction
    try:
        if day > 30 or day < 1:
            raise Exception("Day should be between 1 and 30")
        for i in range(len(all_transactions)):
            trans = all_transactions[i]
            if get_day(trans) == day and get_type(trans) == type and get_description(trans) == description:
                set_value(trans, new_value)
        return all_transactions, None
    except Exception as e:
        return all_transactions, e


def test_replace():
    trns = [{"day": 2, "value": 10, "type": "in", "description": "na"},
            {"day": 5, "value": 10, "type": "in", "description": "na"}]
    trns2 = [{"day": 2, "value": 10, "type": "in", "description": "na"},
             {"day": 5, "value": 23, "type": "in", "description": "na"}]
    replace_value(trns2, 5, "in", "na", "10")
    assert trns2 == trns


# D
def filter_type(all_transactions, type):
    """
    Filter all elements of the specified type
    :param all_transactions: the current transactions
    :param type: the type
    :return: the filtered list
    """
    c = []
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if get_type(trans) == type:
            c.append(trans)
    return c


def filter_smaller(all_transactions, type, value):
    """
    Filter all elements of the specified type and lesser value
    :param all_transactions: the current transactions
    :param type: the type
    :param value: the max value
    :return: the filtered list
    """
    c = []
    for i in range(len(all_transactions)):
        trans = all_transactions[i]
        if get_type(trans) == type or get_value(trans) < value:
            c.append(trans)
    return c


# E
def undo(history):
    """
    Undo
    :param history: the history list
    :return: the previous lists
    """
    if len(history) > 1:
        history.pop()
        all_transactions = history[-1]
        return history, all_transactions
    else:
        return history, history[-1]
