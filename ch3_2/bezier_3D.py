import numpy as np  # ���W���[��numpy��ǂݍ���
import matplotlib.pyplot as plt  # ���W���[��matplotlib��pylab�֐���ǂݍ���
from mpl_toolkits.mplot3d import Axes3D  # matplotlib��Axes3D��ǂݍ���


def bernstein(t, n, i):  # bernstein���֐��̒�`
    cn, ci, cni = 1.0, 1.0, 1.0
    for k in range(2, n, 1):
        cn = cn * k
    for k in range(1, i, 1):
        if i == 1:
            break
        ci = ci * k
    for k in range(1, n - i + 1, 1):
        if n == i:
            break
        cni = cni * k
    j = t**(i - 1) * (1 - t)**(n - i) * cn / (ci * cni)
    return j


def bezierplot(nu, nv, uv, cp):  # bezier�Ȗʂ̒�`
    xyz = np.zeros([len(uv), 3])
    for k in range(len(uv)):
        u, v = uv[k, 0], uv[k, 1]
        sum1, sum2, sum3 = 0.0, 0.0, 0.0
        l = 0
        for i in range(1, nu + 1, 1):
            bu = bernstein(u, nu, i)
            for j in range(1, nv + 1, 1):
                bv = bernstein(v, nv, j)
                sum1 += cp[l, 0] * bu * bv
                sum2 += cp[l, 1] * bu * bv
                sum3 += cp[l, 2] * bu * bv
                l += 1
        xyz[k, :] = [sum1, sum2, sum3]
    return np.array(xyz)
u, v = np.arange(0, 1 + 0.1, 0.1), np.arange(0, 1 + 0.1, 0.1)  # �p�����[�^����
uv = [[i, j] for i in u for j in v]  # �p�����[�^���i�q��ɔz�u
uv = np.array(uv)  # ���X�g��array�ɕϊ�
nu, nv = 4, 3  # u,v�e�����̐���_��
cp = np.array([
    [-1, -1.5, -0.3], [0, -1.5, 0.4], [1, -1.5, 0.4],
    [-1, -0.5, -0.4], [0, -0.5, 1.2], [1, -0.5, -0.2],
    [-1, 0.5, 1.2], [0, 0.5, 0.6], [1, 0.5, 0.8],
    [-1, 1.5, 0.8], [0, 1.5, -0.5], [1, 1.5, 0.7]
])  # ����_����
s = bezierplot(nu, nv, uv, cp)  # bezier�Ȗʐ���
k = 0
x, y, z = [], [], []
for i in range(len(u)):  # ���������ߓ_���W�x�N�g�����s���Ƃɕ���
    xi, yi, zi = [], [], []
    for j in range(len(v)):
        xi.append(s[k, 0])
        yi.append(s[k, 1])
        zi.append(s[k, 2])
        k += 1
    x.append(xi)
    y.append(yi)
    z.append(zi)
cx, cy, cz = [], [], []
k = 0
for i in range(nu):  # ��������������W�x�N�g�����s���Ƃɕ���
    cxi, cyi, czi = [], [], []
    for j in range(nv):
        cxi.append(cp[k, 0])
        cyi.append(cp[k, 1])
        czi.append(cp[k, 2])
        k += 1
    cx.append(cxi)
    cy.append(cyi)
    cz.append(czi)
fig = plt.figure()
ax = Axes3D(fig)
ax.set_axis_off()
ax.set_aspect('equal')
ax.set_xlim(-np.max(cp), np.max(cp))
ax.set_ylim(-np.max(cp), np.max(cp))
ax.set_zlim(-np.max(cp), np.max(cp))
ax.plot_surface(x, y, z, rstride=1, cstride=1, color='yellow')  # bezier�Ȗʂ̕`��
ax.plot_wireframe(cx, cy, cz, color='red', linestyle='dashed')  # ���䑽�ʑ̕`��
ax.plot(cp[:, 0], cp[:, 1], cp[:, 2], color='green',
        lw=0, marker='o', ms=5)  # ����_�̕`��
plt.show()
