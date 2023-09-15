import math

class frac():

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.modify_sign(self)

    def modify_sign(self):
        if self.numerator < 0 and self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def negative(self):
        self.numerator = -self.numerator
        self.modify_sign(self)


class exp_pi_i():

    def __init__(self, radian:frac, pm):
        self.radian = radian
        self.pm = pm

    def conjugate(self):
        self.radian = self.radian.negative()
        

# =======================
# real and compelx number
# =======================

class real_num():

    def __init__(self, c, sqrts):
        self.c = c
        self.sqrts = sqrts

    def calculate(self):
        return self.c * math.sqrt(self.sqrts)


class complex_num():

    def __init__(self, real_part, complex_part):
        # Both real part and complex part are arrays of real_num()
        # Array element representing addition relation
        self.real_part = real_part
        self.complex_part = complex_part


def real_multiply(x1: real_num, x2: real_num) -> real_num:
    x1_temp = x1.sqrts
    x2_temp = x2.sqrts
    extract = 1
    for sqrt1 in x1.sqrts:
        for sqrt2 in x2_temp:
            if sqrt1==sqrt2:
                x1_temp.remove(sqrt1)
                x2_temp.remove(sqrt2)
                extract *= sqrt2
                break
    return real_num(x1.c*x2.c*extract, x1_temp+x2_temp)


def complex_multiply(x1: complex_num, x2: complex_num) -> complex_num:
    return complex_num()


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True