import numpy as np

A1 = np.array([[1], [1], [1], [1], [1], [1]])
A2 = np.array([[1], [1], [1], [-1], [-1], [-1]])
Exy = np.array([[[1,0],[0,1]],
                [[-1/2,-np.sqrt(3)/2],[np.sqrt(3)/2,-1/2]],
                [[-1/2,np.sqrt(3)/2],[-np.sqrt(3)/2,-1/2]],
                [[1,0],[0,-1]],
                [[-1/2,-np.sqrt(3)/2],[-np.sqrt(3)/2,1/2]],
                [[-1/2,np.sqrt(3)/2],[np.sqrt(3)/2,1/2]]])

# $$
# P_R \varphi_\kappa^{(j)}=\sum_{\lambda=1}^{l_j} \varphi_\lambda^{(j)} \Gamma^{(j)}(R)_{\lambda \kappa}
# $$
# $$
# \mathcal{P}_{\lambda \kappa}^{(j)}=\frac{l_j}{h} \sum_R \Gamma^{(j)}(R)_{\lambda \kappa}^* P_R
# $$
# $$
# \varphi_\lambda^{(j)}=\mathcal{P}_{\lambda \kappa}^{(j)} \varphi_\kappa^{(j)}=\frac{l_j}{h} \sum_R \Gamma^{(j)}(R)_{\lambda \kappa}^* P_R \varphi_\kappa^{(j)}
# $$

Sigma = np.array([[1,2,3,4],
                  [2,3,1,4],
                  [3,1,2,4],
                  [1,3,2,4],
                  [3,2,1,4],
                  [2,1,3,4]])

irreps = [A1, A2, Exy]
proj_bond = []
for irrep in irreps:
    if len(irrep[0])==1:
        proj_bond.append(irrep.squeeze())
    else:
        li = len(irrep[0])
        for i in range(li):
            irrep_i = []
            for matrix in irrep:
                irrep_i.append(sum(matrix.T[i]))
            proj_bond.append(np.array(irrep_i))
proj_bond = np.array(proj_bond)
# print(proj_bond)

# print(Sigma.T)
# print(len(A2[0]))
# print(len(Exy[0]))

def avoid_same_array(arrays, new_array):
    same = False
    for array in arrays:
        array_same = True
        for idx, x in enumerate(array):
            if not array[idx] == new_array[idx]:
                array_same = False
                break
        if array_same == True:
            same = True
    return same


bond2spws = []
for i in range(len(proj_bond)):
    num_bonds = len(Sigma.T)
    bond2spw = []
    for s in Sigma.T:
        coeffs = [0 for i in range (num_bonds)]
        for idj, j in enumerate(s):
            coeffs[j-1] += proj_bond[i, idj]
        denominator = np.where(sum(np.abs(coeffs))==0, 1, sum(np.abs(coeffs)))
        # print(coeffs)
        coeffs = [float(k)/denominator for k in coeffs]
        # print(denominator)
        # print(coeffs)
        # same = avoid_same_array(bond2spw, coeffs)
        # neg_same = avoid_same_array(bond2spw, -np.array(coeffs))
        # if not same and neg_same:
        #     bond2spw.append(coeffs)
        bond2spw.append(coeffs)
    # print("0"*30)
    bond2spws.append(bond2spw)

print(bond2spws)
# print(bond2spws[0])

e_x = np.array([1,0])
e_y = np.array([0,1])
e_x = e_x.reshape(2,1)
e_y = e_y.reshape(2,1)
# print(Exy[0].shape)
# print(e_x.shape)
e_x_sy = []
e_y_sy = []
for sy_op in Exy:
    # print(np.dot(sy_op, e_x))
    # print(np.dot(sy_op, e_y))
    e_x_sy.append(np.dot(sy_op, e_x))
    e_y_sy.append(np.dot(sy_op, e_y))

e_x_sy = np.array(e_x_sy).reshape(6,2)
e_y_sy = np.array(e_y_sy).reshape(6,2)
# print(e_x_sy.shape)
# print(e_x_sy)
# print(e_y_sy)

num_electron = 2

xx_sys = []
for i in range(len(e_x_sy)):
    xx_sy = [0 for i in range(num_electron*len(e_x))]
    # print(xx_sy)
    index = 0
    for j in range(len(e_x)):
        for k in range(len(e_x)):
            # print(e_x_sy[i][j])
            xx_sy[index] = e_x_sy[i][j] * e_x_sy[i][k]
            index += 1
    xx_sy = np.array(xx_sy)
    # print(xx_sy)
    xx_sys.append(xx_sy)
xx_sys = np.array(xx_sys)
# print(xx_sys)

xy_sys = []
for i in range(len(e_x_sy)):
    xy_sy = [0 for i in range(num_electron*len(e_x))]
    # print(xx_sy)
    index = 0
    for j in range(len(e_x)):
        for k in range(len(e_x)):
            # print(e_x_sy[i][j])
            xy_sy[index] = e_x_sy[i][j] * e_y_sy[i][k]
            index += 1
    xy_sy = np.array(xy_sy)
    # print(xx_sy)
    xy_sys.append(xy_sy)
xy_sys = np.array(xy_sys)
# print(xy_sys)

yx_sys = []
for i in range(len(e_x_sy)):
    yx_sy = [0 for i in range(num_electron*len(e_x))]
    # print(yx_sy)
    index = 0
    for j in range(len(e_x)):
        for k in range(len(e_x)):
            # print(e_x_sy[i][j])
            yx_sy[index] = e_y_sy[i][j] * e_x_sy[i][k]
            index += 1
    yx_sy = np.array(yx_sy)
    # print(yx_sy)
    yx_sys.append(yx_sy)
yx_sys = np.array(yx_sys)
# print(yx_sy)

yy_sys = []
for i in range(len(e_x_sy)):
    yy_sy = [0 for i in range(num_electron*len(e_x))]
    # print(yx_sy)
    index = 0
    for j in range(len(e_x)):
        for k in range(len(e_x)):
            # print(e_x_sy[i][j])
            yy_sy[index] = e_y_sy[i][j] * e_y_sy[i][k]
            index += 1
    yy_sy = np.array(yy_sy)
    # print(yx_sy)
    yy_sys.append(yy_sy)
yy_sys = np.array(yy_sys)
# print(yx_sy)

# print(xx_sys.T)
# print(yy_sys.T)
# print(xy_sys.T)
# print(yx_sys.T)

multiw2singlew = []
for i in range(len(proj_bond)):
    for xx in xx_sys:
        coeffs = [0 for i in range (num_bonds)]
        for idj, j in enumerate(s):
            coeffs[j-1] += proj_bond[i, idj]
        denominator = np.where(sum(np.abs(coeffs))==0, 1, sum(np.abs(coeffs)))
        # print(coeffs)
        coeffs = [float(k)/denominator for k in coeffs]
        bond2spw.append(coeffs)
    bond2spws.append(bond2spw)