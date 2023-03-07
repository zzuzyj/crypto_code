
# @author: Nev8r
# @date: 2023-03-07 21:55:17

import numpy as np
from numpy.linalg import *
from inverse import inverse
def int_mat(mat):
    x = np.zeros(mat.shape, dtype=np.int16)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            x[i, j] = int(round(mat[i, j]))
    return x
def inv_mat_mod(a):
    a_inv = a.I
    a_det = det(a)
    a_adju = a_inv * a_det % 26
    a_det_inv = inverse(int(round((a_det % 26))), 26)
    aa_inv = (a_det_inv * a_adju)%26
    return aa_inv
if __name__=='__main__':
    a = np.mat([[11, 2, 19], [5, 23, 25], [20, 7, 17]])
    b = np.mat([[0], [0], [0]])
    m = np.mat([[24, 17, 13, 8, 14], [14, 15, 13, 18, 20], [20, 8, 14, 5, 17]])
    c = (a * m + b)%26
    a_mod_inv = inv_mat_mod(a)
    m = (a_mod_inv * (c - b)) %26
    print(int_mat(m))