import numpy as np
from scipy import integrate as itgr  # scipy����integrate�֐����C���|�[�g


def pi(x):  # ��ϕ��֐��̒�`
    return 4.0 / (1.0 + x**2)
answer = itgr.quad(pi, 0, 1)  # (��ϕ��֐�,�ϕ���ԉ�,�ϕ���ԏ�)
print(answer)
