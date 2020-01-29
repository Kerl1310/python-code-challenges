import sys


def calculate(number):
    '''
    Calculate the value using the formula provided in the scenario.
    '''
    number_as_string = str(number)
    sum_of_digits = calculateSumOfDigits(number_as_string)

    result = number * sum_of_digits
    result -= int(number_as_string[::-1])

    if result > 0 and (result % 10) != 0 and (result % 1) == 0:
        return result
    return 0


def calculateSumOfDigits(number_as_string):
    '''
    Calculate the sum of all the digits of the number.
    '''
    sum_of_digits = 0
    for digit in number_as_string:
        sum_of_digits += int(digit)
    return sum_of_digits


if len(sys.argv) > 0:
    print(calculate(sys.argv[1]))
