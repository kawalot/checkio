# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.


def checkio(digit):
    roman = ''
    dictionary = {
        1: "I", 2: "II", 3: "III",
        4: "IV", 5: "V", 6: "VI",
        7: "VII", 8: "VIII", 9: "IX",
        10: "X", 20: "XX", 30: "XXX",
        40: "XL", 50: "L", 60: "LX",
        70: "LXX", 80: "LXXX", 90: "XC",
        100: "C", 200: "CC", 300: "CCC",
        400: "CD", 500: "D", 600: "DC",
        700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M", 2000: "MM", 3000: "MMM",
        4000: "MMMM"
    }
    string = str(digit)
    if len(string) == 1:
        roman = (dictionary.get(int(string[-1]), "Nothing"))
        return roman
    elif len(string) == 2:
        if string[-1] == '0':
            roman = (dictionary.get(int(string[-2] + '0'), "Nothing"))
        else:
            roman = (dictionary.get(int(string[-2] + '0'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
        return roman
    elif len(string) == 3:
        if string[-1] == '0' and string[-2] == '0':
            roman = (dictionary.get(int(string[-3] + '00'), "Nothing"))
            return roman
        elif string[-1] == '0' and string[-2] != '0':
            roman = (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            return roman
        elif string[-1] != '0' and string[-2] == '0':
            roman = (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
        else:
            roman = (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
    elif len(string) == 4:
        if string[-1] == '0' and string[-2] == '0' and string[-3] == '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            return roman
        elif string[-1] == '0' and string[-2] == '0' and string[-3] != '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-3] + '00'), "Nothing"))
            return roman
        elif string[-1] == '0' and string[-2] != '0' and string[-3] != '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            return roman
        elif string[-1] != '0' and string[-2] != '0' and string[-3] != '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
        elif string[-1] != '0' and string[-2] == '0' and string[-3] != '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-3] + '00'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
        elif string[-1] != '0' and string[-2] == '0' and string[-3] == '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
        elif string[-1] != '0' and string[-2] != '0' and string[-3] == '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            roman += (dictionary.get(int(string[-1]), "Nothing"))
            return roman
        elif string[-1] == '0' and string[-2] != '0' and string[-3] == '0':
            roman = (dictionary.get(int(string[-4] + '000'), "Nothing"))
            roman += (dictionary.get(int(string[-2] + '0'), "Nothing"))
            return roman
print(checkio(9))
print(checkio(13))
print(checkio(201))
print(checkio(3903))
print(checkio(999))
