import math


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def real_num(c, sqrts):
    return [RealNum(c, sqrts)]


def neg_real_num(c, sqrts):
    return [RealNum(c, sqrts).negative()]


def real_nums(cs, sqrtss):
    ret = []
    for i in range(len(cs)):
        ret.append(RealNum(cs[i], sqrtss[i]))
    return ret


def neg_real_nums(cs, sqrtss):
    ret = []
    for i in range(len(cs)):
        ret.append(RealNum(cs[i], sqrtss[i]).negative())
    return ret


def reals_add(x1, x2):
    return x1+x2


def real_mcl(r1, r2):
    sqrts1 = r1.sqrts
    sqrts2 = r2.sqrts
    extract = 1
    for sqrt1 in r1.sqrts:
        for sqrt2 in sqrts2:
            if sqrt1==sqrt2:
                sqrts1.remove(sqrt1)
                sqrts2.remove(sqrt2)
                extract *= sqrt2
                break
    sqrts = sqrts1+sqrts2
    return RealNum(r1.c*r2.c*extract, sqrts.sort())



def reals_mcl(x1, x2):
    mcl_ret = []
    flag = True
    for r1 in x1:
        for r2 in x2:
            r1r2 = real_mcl(r1, r2)
            for r in mcl_ret:
                if r.sqrts == r1r2.sqrts:
                    r.c = r.c + r1r2.c
                    flag = False
                    break
            if flag:
                mcl_ret.append(r1r2)
            else:
                flag = True
    return mcl_ret


class RealNum():

    def __init__(self, c, sqrts):
        self.c = c
        self.sqrts = sqrts

    def calculate(self):
        return self.c * math.sqrt(self.sqrts)
    
    def negative(self):
        self.c = -self.c
