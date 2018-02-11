#!/usr/bin/env python

class Infinity(object):
    def __init__(self, sign=1.0):
        self.sign = str(sign/abs(sign))[0]
        if self.sign.startswith('1'):
            self.sign = '+'
        else:
            self.sign = '-'

    def __add__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return self
            else: return 0.0
        else:
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return 0.0
            elif self.sign.startswith('-'): return self
            else: return Infinity(1.0)
        else:
            return self

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return Infinity(1.0)
            else: return Infinity(-1.0)
        else:
            if other == 0: return 0
            else: return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return 1.0
            else: return -1.0
        else:
            if other == 0: return 0
            else: return self

    def __rdiv__(self, other):
        return self.__div__(other)

    def __abs__(self):
        return Infinity(1.0)

    def __float__(self):
        return self

    def __neg__(self):
        if self.sign.startswith('-'):
            return Infinity(1.0)
        else:
            return Infinity(-1.0)

    def __pos__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return False
            elif self.sign == '+': return True
            else: return False
        else:
            return self.sign.startswith('+')

    def ___le__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return True
            elif self.sign == '+': return True
            else: return False
        else:
            return self.sign.startswith('+')

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.sign == other.sign: return True
            else: return False
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__()

    def __ge__(self, other):
        return not self.__lt__()

    def print_self(self):
        print "{0}Inf".format(self.sign)

class Undefined(object):
    def __init__(self):
        pass

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __mul__(self, other):
        if other == 0: return 0.0
        else: return self

    def __div__(self, other):
        if isinstance(other, type(self)): return 1.0
        else: return self

    def __abs__(self):
        return self

    def __float__(self):
        return self

    def __neg__(self):
        return self

    def __pos__(self):
        return self

    def __lt__(self, other):
        return self

    def ___le__(self, other):
        return self

    def __eq__(self, other):
        return self

    def __ne__(self, other):
        return self

    def __gt__(self, other):
        return self

    def __ge__(self, other):
        return self

    def print_self(self):
        print "Undefined"
