#!/usr/bin/env python3
"""
This is a compresser 

"""
import string
alphabets=list(string.ascii_lowercase)
String=input("Input String: ")
compressedString=' '
file=open("compress.txt","w")

for i in range(len(String)):
	for y in range(len(alphabets)):
		if alphabets[y]==String[i]:
			compressedString+=bin(y+1)[2:]+" "
		
	

x=compressedString.split()	
print("compressedString",x)			
def UnComp():
	answer=" "
	uncompress=open("uncompress.txt","w")
	for i in x:
		answer+=alphabets[int(i,2)-1]
	uncompress.write(answer)	
UnComp()
file.write(compressedString)
file.close()