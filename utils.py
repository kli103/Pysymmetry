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

    def __init__(self, radian:frac, multi):
        self.radian = radian
        self.multi = multi

    def conjugate(self):
        self.radian = self.radian.negative()


exp_pi_i_zero = exp_pi_i(0, 0)
exp_pi_i_plus_one = exp_pi_i(0, 1)