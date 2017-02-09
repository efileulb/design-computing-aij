import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import os


def orthogonal_transformation(zfront, zback):  # �`��̎�@�𓧎����e���畽�s���e�ɕύX
    a = 2 / (zfront - zback)
    b = -1 * (zfront + zback) / (zfront - zback)
    c = zback
    return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, a, b], [0, 0, 0, c]])


def plot_shape3D(r, ijt, ijc, xmin, xmax, ymin, ymax, zmin, zmax):  # �`��̕`��
    proj3d.persp_transformation = orthogonal_transformation
    fig = plt.figure()
    ax = Axes3D(fig)
    for e in ijt:
        i, j = e[0], e[1]
        ax.plot([r[i, 0], r[j, 0]], [r[i, 1], r[j, 1]], [
                r[i, 2], r[j, 2]], c='r', lw=1)  # �����ނ̕`��
    for e in ijc:
        i, j = e[0], e[1]
        ax.plot([r[i, 0], r[j, 0]], [r[i, 1], r[j, 1]], [
                r[i, 2], r[j, 2]], c='b', lw=5)  # ���k�ނ̕`��
    ax.plot(r[:, 0], r[:, 1], r[:, 2], c='gray',
            ls='none', marker='o', ms=10)  # �ߓ_�̕`��
    ax.set_xlim(xmin, xmax), ax.set_ylim(
        ymin, ymax), ax.set_zlim(zmin, zmax)  # �`��͈͂̎w��
    ax.set_aspect('equal'), ax.set_axis_off()  # �c����𓙂������C���W���͕\�����Ȃ�
    plt.show()
