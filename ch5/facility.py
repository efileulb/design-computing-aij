import numpy as np  # ���W���[��numpy��np�Ƃ������O�œǂݍ���
import csv  # ���W���[��csv�̓ǂݍ���
from scipy import optimize  # scipy����optimize���W���[����ǂݍ���
filename = 'out2'  # �o�̓t�@�C����
writer = csv.writer(open(filename + '.csv', 'w'))  # �o�͂���csv�t�@�C���̐���
writer.writerow(['step', 'f(x)', 'x1', 'x2'])  # csv�t�@�C���ւ̃��x���̏�������


def f(x):  # �ړI�֐��̒�`
    return ((2 - x[0])**2 + (4 - x[1])**2)**0.5 + ((3 - x[0])**2 + (2 - x[1])**2)**0.5


def h(x):  # ��������̒�`(>0)
    return np.array([-2 * x[0] - 3 * x[1] + 7, x[0], -x[0] + 2, x[1], -x[1] + 2])


def callbackF(x):  # �œK���̊e�X�e�b�v�Ōv�Z���ʂ��L�^����֐�
    global step
    step += 1
    writer.writerow([step, f(x), x[0], x[1]])

    
x = np.array([0.0, 0.0])
step = 0
writer.writerow([step, f(x), x[0], x[1]])
optimize.fmin_slsqp(f, x, f_ieqcons=g, iprint=2, callback=callbackF)  # ����2���v��@
