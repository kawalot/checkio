'''
Write a function that finds the longest palindromic substring of a given string. 
Try to be as efficient as possible!
If you find more than one substring you should return the one which is closer to the beginning.
Input: A text as a string.
Output: The longest palindromic substring. 
'''


def longest_palindromic(text):
    d = []
    def ispalindrom(text):
        for i in range(0, len(text)):
            temp = text[:i]
            if temp == ''.join(reversed(temp)):
                d.append(temp)
    

    if text == ''.join(reversed(text)):
        return text
    for i in range(0, len(text)):
        ispalindrom(text[i:])
    lengths = [len(i) for i in d]
    index = lengths.index(max(lengths))
    return d[index]

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"