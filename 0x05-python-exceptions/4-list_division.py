#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                val1 = my_list_1[i]
                val2 = my_list_2[i]
                if not isinstance(val1, (int, float)) or \
                   not isinstance(val2, (int, float)):
                    raise TypeError
                if val2 == 0:
                    raise ZeroDivisionError
                result = val1 / val2
            except IndexError:
                print("out of range")
                result = 0
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by zero")
                result = 0
            finally:
                result_list.append(result)
    except TypeError:
            print("out of range")
    finally:
            return result_list
