import numpy as np  # ���W���[��numpy��np�Ƃ������O�œǂݍ���
import csv  # ���W���[��csv�̓ǂݍ���
filename = 'out'  # �o�̓t�@�C����
writer = csv.writer(open(filename + '.csv', 'w'))  # �o�͂���csv�t�@�C���̐���
writer.writerow(['step', 'f(x)', 'x1', 'x2'])  # csv�t�@�C���ւ̃��x���̏�������


def f(x):  # �ړI�֐��̒�`
    return 0.50 * (x[0] - 3.0)**2 + (x[1] - 2.0)**2


def df(x):  # ���z�x�N�g���̒�`
    return np.array([x[0] - 3.0, 2.0 * (x[1] - 2.0)])


def line_search(xk):  # 2���@�ɂ�胉�C���T�[�`���s���֐�
    tau = 2.0
    xj1 = xk
    xj2 = xj1 - tau * df(xk)
    while abs(f(xj2) - f(xj1)) > eps:
        if f(xj2) < f(xj1):
            tau = tau
        else:
            tau = -tau / 2.0
        xj1 = xj2
        xj2 = xj1 - tau * df(xk)
    return xj1


x = [4.0, 3.0]  # �݌v�ϐ��̏����l
t = 0.10  # �т̏����l
itera = 1000  # �œK���̍ő唽����
eps = 1.0e-10  # �I�������̂��߂̎w��l
for k in range(itera):  # ��������ŋ}�~���@
    fx = f(x)
    writer.writerow([k, fx, x[0], x[1]])
    x_prev = x
    x = line_search(x)
    if abs(np.linalg.norm(x_prev - x)) < eps:
        break
