from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        numer, denom = Rational._get_lowest_terms(numer, denom)
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        sum_numer = self.numer * other.denom + other.numer * self.denom
        sum_denom = self.denom * other.denom
        sum_numer, sum_denom = Rational._get_lowest_terms(sum_numer, sum_denom)
        return Rational(sum_numer, sum_denom)

    def __sub__(self, other):
        sum_numer = self.numer * other.denom - other.numer * self.denom
        sum_denom = self.denom * other.denom
        sum_numer, sum_denom = Rational._get_lowest_terms(sum_numer, sum_denom)
        return Rational(sum_numer, sum_denom)

    def __mul__(self, other):
        sum_numer = self.numer * other.numer
        sum_denom = self.denom * other.denom
        sum_numer, sum_denom = Rational._get_lowest_terms(sum_numer, sum_denom)
        return Rational(sum_numer, sum_denom)

    def __truediv__(self, other):

        sum_numer = self.numer * other.denom
        sum_denom = self.denom * other.numer
        if sum_denom == 0:
            print("Divide by zero not possible")
        sum_numer, sum_denom = Rational._get_lowest_terms(sum_numer, sum_denom)
        return Rational(sum_numer, sum_denom)

    def __abs__(self):
        if self.numer < 0:
            self.numer *= -1
        if self.denom < 0:
            self.denom *= -1
        return self

    def __pow__(self, power):
        self.numer = pow(self.numer, power)
        self.denom = pow(self.denom, power)
        return self

    def __rpow__(self, base):
        return pow(base, (self.numer/self.denom))

    @staticmethod
    def _get_lowest_terms(numer, denom):

        if numer == 0:
            return 0, 1
        elif numer < 0 and denom < 0 or denom < 0:
            numer *= -1
            denom *= -1

        new_numer = abs(numer)
        new_denom = abs(denom)

        if new_numer < new_denom:
            lower = new_numer
        else:
            lower = new_denom

        while lower > 0:
            if numer % lower == 0 and denom % lower == 0:
                gsd = lower
                break
            lower -= 1
        return numer//gsd, denom//gsd
