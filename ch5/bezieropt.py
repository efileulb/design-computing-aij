import bezier
import csv  # bezier.py����у��W���[��csv�̓ǂݍ���
import numpy as np  # ���W���[��numpy��np�Ƃ������O�œǂݍ���
import scipy as sp  # ���W���[��scipy��sp�Ƃ������O�œǂݍ���
from scipy import optimize  # scipy����optimize���W���[����ǂݍ���
from scipy import integrate  # scipy����integrate���W���[����ǂݍ���


filename = 'input1'  # ����_���W�����i�[�������̓t�@�C����
reader = csv.reader(open(filename + '.csv', 'r'))  # ���̓t�@�C���̓ǂݍ���
next(reader)  # �擪�s�͓ǂݔ�΂�
row = next(reader)[0:2]
nu, nv = int(row[0]), int(row[1])  # u,v�����̐���_��
next(reader)  # 1�s�ǂݔ�΂�
cp = []
for row in reader:
    cp.append([float(row[0]), float(row[1]), float(row[2])])  # ����_���W�ǂݍ���
cp = np.array(cp)
limit = [np.min(cp), np.max(cp), np.min(cp), np.max(cp),
         np.min(cp), np.max(cp)]  # �`��͈�
bezier.plot_shape(nu, nv, cp, limit)


def f(x):  # �ړI�֐��̒�`
    global cp, nu, nv
    cp[:, 2] = x[:]  # ����_���W�̍X�V
    return integrate.nquad(lambda u, v: bezier.EGF(nu, nv, u, v, cp), [[0, 1], [0, 1]],
                           opts={'epsabs': 1.0e-6, 'epsrel': 1.0e-6})[0]  # ���l�ϕ�


k = 0
b = []  # �݌v�ϐ��͈̔͂̐ݒ�

for i in range(nu):
    for j in range(nv):
        if i == 0 or i == nu - 1 or j == 0 or j == nv - 1:
            b.append([cp[k, 2], cp[k, 2]])  # ���E�͓������Ȃ�
        else:
            b.append([-1.0e+10, 1.0e+10])
        k += 1

x = cp[:, 2]
optimize.fmin_slsqp(f, x, fprime=None, bounds=b,
                    iprint=2, full_output=True)  # �����񎟌v��@
bezier.plot_shape(nu, nv, cp, limit)  # ���ʂ̕`��
