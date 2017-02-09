import numpy as np
from scipy import optimize
import fem
import graph
import os


def lagrange(x, w, ijt, ijc, nod, nelt, nelc, lc_bar):  # �◯�����֐�
    r[:, 0], r[:, 1], r[:, 2] = x[:nod], x[nod:nod * 2], x[nod * 2:nod * 3]
    lam = x[nod * 3:]
    lght, lghc = fem.length(r, ijt, ijc, nelt, nelc)
    nablaLt, nablaLc = fem.dlengthtc(r, ijt, ijc, nod, lght, lghc, nelt, nelc)
    b = np.array([4.0 * w[e] * lght[e]**3 for e in range(nelt)])
    f1 = nablaLt.dot(b) + nablaLc.dot(lam)
    f2 = lghc - lc_bar
    return np.r_[f1, f2]

filename = '20_face_pieces'
inputfilename = 'datain/' + filename + '.csv'
r, ijt, ijc, nod, nelt, nelc = fem.input(inputfilename)  # �`��Ɨv�f�ߓ_�֌W�̓ǂݍ���
xmin, xmax, ymin, ymax, zmin, zmax =\
    np.min(r), np.max(r), np.min(r), np.max(r), np.min(r), np.max(r)
graph.plot_shape3D(r, ijt, ijc, xmin, xmax, ymin,
                   ymax, zmin, zmax)  # �����`��̕`��(�m�F�p)
lght, lghc = fem.length(r, ijt, ijc, nelt, nelc)  # ���ޒ��̌v�Z
lc_bar = lghc * 1.0  # ���k�ނ̒����̎w��l(�����ł͏����`��̒l�Ƃ���)
lam = np.zeros(nelc)
x = np.r_[r[:, 0], r[:, 1], r[:, 2], lam]
w = [1.0] * len(lght)
x = optimize.root(lagrange, x, args=(w, ijt, ijc, nod, nelt, nelc, lc_bar)).x
r[:, 0], r[:, 1], r[:, 2] = x[:nod], x[
    nod:nod * 2], x[nod * 2:nod * 3]  # �œK����ߓ_���W�֏�����
b, lam = np.array(
    [4.0 * w[e] * lght[e]**3 for e in range(nelt)]), x[nod * 3:]  # ���̓��[�h�v�Z
dir = 'dataout/'
outputfilename = dir + filename + '_opt.csv'

try:  # dataout�t�H���_�̑��ݗL���𒲂ׁC�Ȃ���ΐV�K�쐬����
    os.stat(dir)
except:
    os.mkdir(dir)
fem.output(outputfilename, r, nod, ijt, ijc,
           nelt, nelc, b, lam)  # �œK�`��Ǝ��̓��[�h�̏o��
xmin, xmax, ymin, ymax, zmin, zmax =\
    np.min(r), np.max(r), np.min(r), np.max(r), np.min(r), np.max(r)
graph.plot_shape3D(r, ijt, ijc, xmin, xmax, ymin, ymax, zmin, zmax)  # �œK�`��̕`��
