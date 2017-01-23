'''
Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.
The list of banned words are as follows:
sum
import
for
while
reduce
Input: A list of numbers.
Output: The sum of numbers.
'''


def checkio(digits):
    i = 0
    def summa(digits):
        nonlocal i
        if digits:
            i += digits[0]
            digits.remove(digits[0])
            summa(digits)
            return i
    summa(digits)
    return i


print(checkio([1,2,3,4]))
print(checkio([2,2,2,2,2,2]))

#not my solution
'''
def checkio(data):
    if len(data) == 1:
        return data[0]
    data[-2] += data[-1]
    data.pop()
    return checkio(data)
'''
