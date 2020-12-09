#!/usr/bin/env python3
# dec2hex.py 

def def2bin(dec):
	binValue = bin(dec)
	binS = str(bin(dec))
	b = binS.replace('0b','')
	print(dec,binValue,b) #debug
	return b
	
def main():
	print("* Decimal to Binary ******")
	binString = dec2bin(10)
	print(10,binString)
	binString = dec2bin(245)
	print(245,binString)
	
main()
