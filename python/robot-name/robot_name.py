import random
import string


class Robot:
    NameDict = {}

    def __init__(self):
        self.name = Robot.__name()

    def reset(self):
        new_name = Robot.__name()
        del Robot.NameDict[self.name]
        self.name = new_name

    @staticmethod
    def __name():
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + \
                   ''.join(random.choices(string.digits, k=3))
            if name in Robot.NameDict.keys():
                continue
            else:
                Robot.NameDict[name] = 1
                return name
