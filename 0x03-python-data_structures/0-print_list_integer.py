#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
     print("{:d}".format(x))
my_list = [1,2,3,4,7,3]
print_list_integer(my_list)
