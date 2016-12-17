# Let's teach the Robots to distinguish words and numbers.
# You are given a string with words and numbers separated by whitespaces (one space).
# The words contains only letters. You should check if the string contains three words in succession.
# For example, the string "start 5 one two three 7 end" contains three words in succession.
# Input: A string with words.
# Output: The answer as a boolean.

def checkio(words):
    i = 0
    for word in words.split(" "):
        if not word.isdigit():
            i += 1
            if i == 3:
                return True
        else:
            i = 0
    return False

print(checkio("start 5 one two three 7 end"))