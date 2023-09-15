from utils import exp_pi_i, frac, exp_pi_i_zero, exp_pi_i_plus_one

class C3v():

    def __init__(self):
        self.elements = ['E', 'C3', 'C3\'', 'sigma_v', 'sigma_v\'', 'sigma_v\'\'']
        self.irrep_dims = [1,1,2]
        self.irrep_names = ['A1', 'A2', 'E']
        self.irreps = []
        self.irreps.append([1, 1, 1, 1, 1, 1])
        self.irreps.append([1, 1, 1, -1, -1, -1])
        epsilon = exp_pi_i(frac(2, 3), +1)
        irrep_E = []
        irrep_E.append([[exp_pi_i_plus_one, exp_pi_i_zero], [exp_pi_i_zero, exp_pi_i_plus_one]])
        irrep_E.append([[epsilon.conjugate(), exp_pi_i_zero], [exp_pi_i_zero, epsilon]])
        irrep_E.append([[epsilon, exp_pi_i_zero], [exp_pi_i_zero, epsilon.conjugate()]])
        irrep_E.append([[exp_pi_i_plus_one, exp_pi_i_zero], [exp_pi_i_zero, exp_pi_i_plus_one]])
        irrep_E.append([[exp_pi_i_plus_one, exp_pi_i_zero], [exp_pi_i_zero, exp_pi_i_plus_one]])
        irrep_E.append([[exp_pi_i_plus_one, exp_pi_i_zero], [exp_pi_i_zero, exp_pi_i_plus_one]])


print(1+1)
print(C3v().irreps[0])