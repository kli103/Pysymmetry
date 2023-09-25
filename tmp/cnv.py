from utils import exp_pi_i, frac, zero, plus_one, minus_one

class C3v():

    def __init__(self):
        self.elements = ['E', 'C3', 'C3\'', 'sigma_v', 'sigma_v\'', 'sigma_v\'\'']
        self.irrep_dims = [1,1,2]
        self.irrep_names = ['A1', 'A2', 'E']
        self.irreps = []
        self.irreps.append([plus_one, plus_one, plus_one, plus_one, plus_one, plus_one])
        self.irreps.append([plus_one, plus_one, plus_one, minus_one, minus_one, minus_one])
        epsilon = exp_pi_i(frac(2, 3), +1)
        irrep_E = []
        irrep_E.append([[plus_one, zero], [zero, plus_one]])
        irrep_E.append([[epsilon.conjugate(), zero], [zero, epsilon]])
        irrep_E.append([[epsilon, zero], [zero, epsilon.conjugate()]])
        irrep_E.append([[plus_one, zero], [zero, plus_one]])
        irrep_E.append([[plus_one, zero], [zero, plus_one]])
        irrep_E.append([[plus_one, zero], [zero, plus_one]])


print(1+1)
print(C3v().irreps[0])
