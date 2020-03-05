def convert(number):
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)

    sound = ""
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"

    return sound
