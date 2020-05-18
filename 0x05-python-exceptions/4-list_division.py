#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listdiv = []
    for mv in range(list_length):
        try:
            div = 0
            div = my_list_1[mv] / my_list_2[mv]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            listdiv.append(div)
    return listdiv
