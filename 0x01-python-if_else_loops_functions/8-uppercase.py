#!/usr/bin/python3
def uppercase(str):
    a = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            a += chr(ord(i) - 32)
        else:
            a += i
    print("{}".format(a))
