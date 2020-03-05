def is_armstrong_number(number):
    if number < 10:
        return True
    power = len(str(number))
    sm = 0
    test_number = number
    while test_number != 0:
        sm += pow(test_number % 10, power)
        test_number = test_number // 10
    if number != sm:
        return False
    else:
        return True
