#You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
#For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
#Input: A positive integer.
#Output: The product of the digits as an integer.


def checkio(number):
	eval = 1
	for digit in str(number):
		if int(digit) == 0:
			continue
		else:
			eval = eval * int(digit)
	return eval
print(checkio(123405))
print(checkio(999))
print(checkio(1000))
print(checkio(1111))