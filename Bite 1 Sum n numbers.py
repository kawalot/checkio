# def sum_numbers(numbers=None):
#     sum = 0
#     if numbers or numbers==[]:
#         for i in numbers:
#             sum += i
#     else:
#         return 5050
#     return sum

def sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)