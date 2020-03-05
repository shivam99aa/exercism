def is_armstrong_number(number):

    power = len(str(number))
    return number == sum([int(i) ** power for i in str(number)])
