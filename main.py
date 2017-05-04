#!/usr/bin/env python3
"""
This is a compressor 

"""
import string

alphabets = list(string.printable)
input_string = input("Input String: ")
compressed_string = ''
file = open("compress.txt", "w")

for char in input_string:
    if char in alphabets:
        compressed_string += bin(alphabets.index(char) + 1)[2:] + " "

x = compressed_string.split()

print("Compressed string: ", x)


def UnComp():
    original_string = ''
    uncompress = open("uncompress.txt", "w")
    for i in x:
        original_string += alphabets[int(i, 2) - 1]
    uncompress.write(original_string)


UnComp()

file.write(compressed_string)
file.close()
