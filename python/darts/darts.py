import math
def score(x, y):
    distance = math.sqrt(x*x + y*y)
    if distance > 10:
        return 0
    elif distance <= 10 and distance > 5 :
        return 1
    elif distance <= 5 and distance > 1:
        return 5
    else:
        return 10
