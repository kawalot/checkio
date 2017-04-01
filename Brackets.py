"""
Input: An expression with different of types brackets as a string (unicode).
Output: A verdict on the correctness of the expression in boolean (True or False).
"""


def checkio(expression):
    stack = []
    try:
        for char in expression:
            if char == '(':
                stack.append(char)
            if char == '{':
                stack.append(char)
            if char == '[':
                stack.append(char)
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    except IndexError:
        return False
    if stack:
        return False
    else:
        return True

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside g {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
