
# @author: Nev8r
# @date: 2023-03-07 21:38:18

from mul_table_replace import inv_mat_mod,int_mat
import numpy as np
A = np.mat([[11,2],
     [5,23]])
A_inv_mod = inv_mat_mod(A)

print(int_mat(A_inv_mod))
