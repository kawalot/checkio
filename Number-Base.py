#You are given a positive number as a string along with the radix for it. 
#Your function should convert it into decimal form. The radix is less than 37 and greater than 1. 
#The task uses digits and the letters A-Z for the strings.
#Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
#Input: Two arguments. A number as string and a radix as an integer.
#Output: The converted number as an integer.


def checkio(str_number, radix):
	try:
		number = int(str_number,radix)
	except:
		return -1
	return number
	
print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))