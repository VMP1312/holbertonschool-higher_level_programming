#!/usr/bin/python3
def roman_to_int(roman_string):
    Rnum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    acum = 0
    prev = 0
    for Rmn in roman_string:
        if Rmn in roman_string:
            if prev < Rnum[Rmn]:
                acum += Rnum[Rmn] - prev * 2
            else:
                acum += Rnum[Rmn]
            prev = Rnum[Rmn]
    return acum
