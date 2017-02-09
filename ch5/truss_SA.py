# -*- coding: utf8 -*-
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
import random
import math
from scipy import optimize
E = 205000.0
L = 2.0 * 1.0e+3
P1 = 400.0 * 1.0e+3
P2 = 200.0 * 1.0e+3
sigma_bar = 235.0
u_bar = 5.0
a1 = L * 1.0
a2 = L * 1.0
penalty = 1.0e+10
A0 = np.array([3000.0, 3000.0])


def f(A):
    cons = g(A)
    return a1 * A[0] + a2 * A[1] + penalty * (max(-cons[0], 0) + max(-cons[1], 0) + max(-cons[2], 0) + max(-cons[3], 0) + max(-cons[4], 0))


def g(A):
    sigma1 = sigma_bar - (P1 + P2) / A[0]
    sigma2 = sigma_bar - P2 / A[1]
    u2 = u_bar - (P1 + P2) * L / A[0] / E - P2 * L / A[1] / E
    return np.array([sigma1, sigma2, u2, A[0], A[1]])
nstep = 1000  # �X�e�b�v��
cool = 0.99  # ���x�����炷����
shrink = 0.99  # �T���͈͂��k�����銄��
scale = 0.01  # �ϐ��̃X�P�[�����O�p�����[�^
temp = 1.0  # ���x�̏�����
delta = 3000.0  # �T���͈͂̏�����
nb = 10  # �ߖT���̐�
objopt = f(A0)  # �ړI�֐��̍œK�l�̏�����
random.seed(1000)  # �����̏�����
obj0 = f(A0)  # �ړI�֐��̌v�Z
# �݌v�ϐ��ƖړI�֐��̗���ۑ��p
A0_history = [A0[0]]
A1_history = [A0[1]]
f_history = [obj0]
for k in range(nstep):
    print('-------- �X�e�b�v: ', k)
    print('���x', temp, '�T���͈�', delta, '�ϐ�', A0, '�ړI�֐�', obj0, '�b��l', objopt)
    # �ߖT���̕]��
    obj1 = 1.0e10
    for n in range(nb):
        A = [A0[0] + (random.random() - 0.5) * delta,
             A0[1] + (random.random() - 0.5) * delta]
        obj = f(A)  # �ړI�֐��̌v�Z
        if(obj < obj1):  # �œK�ȋߖT����I��
            obj1 = obj
            A1 = list(A)
    print('�œK�ߖT��', A, '�ړI�֐�', obj1)
    A0_history.append(A[0])
    A1_history.append(A[1])
    f_history.append(obj1)
    diff = obj1 - obj0  # �ړI�֐��̑���
    if(diff < 0):  # ���������̂Ƃ��ړI�֐��Ɖ����X�V
        obj0 = obj1
        A0 = A1
    else:  # ������0�܂��͐��̂Ƃ�
        prob = math.exp(-diff / temp / scale)  # �X�V�m���̌v�Z
        ran = random.random()
        if(ran < prob):  # �������X�V�m����菬�����Ƃ��ړI�֐��Ɖ����X�V
            obj0 = obj1
            A0 = A1
    temp = temp * cool  # ���x�̍X�V
    delta = delta * shrink  # �T���͈͂̍X�V
    if(obj1 < objopt):  # �œK�l�̍X�V
        objopt = obj1
        optstep = k
        Aopt = A1
print('==========================')
print('�œK�ړI�֐��l', objopt, '�X�e�b�v', optstep, '�ϐ�', Aopt)
