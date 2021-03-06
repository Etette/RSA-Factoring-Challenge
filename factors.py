#!/usr/bin/python3

""" Module that factorize as many numbers
as possible into product of 2 smaller numbers"""

from sys import argv


def factorize(value):
    """print a descomposition of an integer"""
    i = 2

    if value < 2:
        return
    while value % i:
        i += 1
    print("{:0f}={:0f}*{:0f}".format(value, value / i, i))


if len(argv) != 2:
    exit()
try:
    with open(argv[1]) as file:
        line = file.readline()
        while line != "":
            value = int(line.split('\n')[0])
            factorize(value)
            line = file.readline()
except IndexError:
    pass
