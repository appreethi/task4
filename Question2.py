'''Write a python code using lambda function to check every element of a list is an integer or a string'''

mylist = [ 1, 2.3 , "Hello", 65,"Preethi",78965,9.098, 2+6j,"sequence"]

#filter integers
filter_integers = list(filter(lambda x : isinstance(x, int),mylist))

#filter strings
filter_strings = list(filter(lambda x : isinstance(x,str),mylist))

#printing results
print("list of integers:",filter_integers)
print("list of strings:",filter_strings)

