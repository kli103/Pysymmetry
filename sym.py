import numpy as np

class Symmetry():

    def __init__(self, name, symmetries, irrep_names, irreps, characters):
        self.name = name
        self.symmetries = symmetries
        self.irrep_names = irrep_names
        self.irreps = irreps


C3v = Symmetry('C3v', ['E', 'C3', 'C3\'', 'sigma_v', 'sigma_v\'', 'sigma_v\'\''], ['A1', 'A2', 'E'], [
  [[1, 1, 1, 1, 1, 1]],
  [[1, 1, 1, -1, -1, -1]],
  [[[]]]
])


# zero = real_num(0, [])
# one = real_num(1, [])
# one_half = real_num(1/2, [])
# one_half_sqrt3 = real_num(1/2, [3])


# neg_one = real_num(-1, [])
# neg_one_half = real_num(-1/2, [])
# neg_one_half_sqrt3 = real_num(-1/2, [3])


# C3v = Symmetry('C3v',
#                ['E', 'C3', 'C3\'', 'sigma_v', 'sigma_v\'', 'sigma_v\'\''],
#                ['A1', 'A2', 'E'],
#                [[one, one, one, one, one, one],
#                 [one, one, one, neg_one, neg_one, neg_one],
#                 [[[one,zero],[zero,one]],
#                  [[neg_one_half,one_half_sqrt3],[neg_one_half_sqrt3,neg_one_half]],
#                  [[neg_one_half,neg_one_half_sqrt3],[one_half_sqrt3,neg_one_half]],
#                  [[one,zero],[zero,neg_one]],
#                  [[neg_one_half,neg_one_half_sqrt3],[neg_one_half_sqrt3,one_half]],
#                  [[neg_one_half,one_half_sqrt3],[one_half_sqrt3,one_half]]]],
#                [[1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, -1, -1, -1],
#                 [2, -1, -1, 0, 0, 0]])
