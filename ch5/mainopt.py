import numpy as np
import truss3                    # truss3.py�����W���[���Ƃ��ăC���|�[�g
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from scipy import sparse
from scipy import optimize
filename = 'model2.csv'
r, nod, ij, nel, A, E, fix, p = truss3.input(filename)


def plot_shape(r, ij, nel, a, scale):
    a = a / max(a) * scale
    [plt.plot([r[ij[e][0], 0], r[ij[e][1], 0]], 
              [r[ij[e][0], 1], r[ij[e][1], 1]], 
              c='b', lw=round(a[e], 2)) for e in range(nel)]
    plt.xlim([min(r[:, 0]) - 0.1, max(r[:, 0]) + .1])
    plt.ylim([min(r[:, 1]) - .1, max(r[:, 1]) + .1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(filename + '.eps')
    plt.show()
plot_shape(r, ij, nel, A, 1)  # �����`��̊m�F
lgh = truss.length(r, ij, nel)
v_bar = 0.02
remove = truss.boundary_condition(fix)
p = truss.np.delete(p, remove, 0)  # ���E�������l�������׏d�x�N�g���ƍ����s��W��
nf = len(p)  # ���R�x
b = truss.global_b(r, nod, ij, nel, lgh, remove)


def f(x, nel, p, b, E, lgh):        # �ړI�֐�
    K = sparse.csr_matrix(truss.make_k(E, x, lgh, b, nel))
    u = sparse.linalg.spsolve(K, p)
    return p.dot(u)


def df(x, nel, p, b, E, lgh):       # �ړI�֐��̔����W��
    K = sparse.csr_matrix(truss.make_k(E, x, lgh, b, nel))
    u = sparse.linalg.spsolve(K, p)
    print(p.dot(u))
    return [-u.dot(E[e] / lgh[e] * b[:, e].dot(b[:, e].T)).dot(u) for e in range(nel)]


def h(x, nel, lgh, v_bar):          # ����֐�
    v = sum([lgh[e] * x[e] for e in range(nel)])
    return [v_bar - v]


def dh(x, nel, lgh, v_bar):         # ����֐��̔����W��
    return -lgh


bnd = np.zeros([nel, 2])
for i in range(nel):
    bnd[i, 0], bnd[i, 1] = 1.0e-10, 1.0e+10
A = optimize.minimize(f, A, args=(nel, p, b, E, lgh), jac=df, method='SLSQP', 
    constraints=({'type': 'ineq', 'fun': h, 'jac': dh, 
    'args': (nel, lgh, v_bar)}), bounds=bnd, options={'eps': 1e-10, 'ftol': 1e-10, 
    'maxiter': 100000, 'disp': True}).x
plot_shape(r, ij, nel, A, 10)
