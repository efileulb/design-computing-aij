import numpy as np
import csv
import math


def input(fname):  # �g���X�̓ǂݍ���
    reader = csv.reader(open(fname, 'r'))
    r, ij, A, E, fix, p = [], [], [], [], [], []  # �ߓ_���W,�v�f�ߓ_�֌W,�f�ʐ�,�����O�W��,���E����,�׏d�x�N�g��
    for row in reader:  # �ߓ_�̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        r.append([float(row[0]), float(row[1])])
    nod, r = len(r), np.array(r)  # �ߓ_��,list��array�ϊ�
    for row in reader:  # �v�f�ߓ_�֌W�̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        ij.append([int(row[0]), int(row[1])])
        A.append(float(row[2]))
        E.append(float(row[3]))
    nel, A, E = len(ij), np.array(A), np.array(
        E)  # �v�f��,list��array�ϊ�,list��array�ϊ�
    for row in reader:  # ���E�����̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        fix.append([int(row[0]), int(row[1]), int(row[1])])
    p = np.zeros(nod * 2)
    for row in reader:  # �W���׏d�̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        p[int(row[0]) * 2:(int(row[0]) + 1) * 2] =\
            [float(row[1]), float(row[2])]
    return r, nod, ij, nel, A, E, fix, p


def length(r, ij, nel):  # �v�f�������v�Z
    lgh = [math.sqrt((r[ij[i][0], 0] - r[ij[i][1], 0])**2 +
                     (r[ij[i][0], 1] - r[ij[i][1], 1])**2) for i in range(nel)]
    return np.array(lgh)


def transmatrix(l, r1, r2):  # ���W�ϊ��s������߂�
    tr = np.matrix([[0.0] * 4] * 4)
    lx, ly = r2[0] - r1[0], r2[1] - r1[1]
    cos, sin = lx / l, ly / l
    tr[0, 0], tr[1, 1], tr[2, 2], tr[3, 3] = cos, cos, cos, cos
    tr[1, 0], tr[3, 2], tr[0, 1], tr[2, 3] = -sin, -sin, sin, sin
    return tr


def boundary_condition(fix):  # ���E�����̎w��
    remove = []
    for i in fix:
        if i[1] == 1:
            remove.append(i[0] * 2)
        if i[2] == 1:
            remove.append(i[0] * 2 + 1)
    return remove


def global_b(r, nod, ij, nel, lgh, remove):  # �S�̍��W�n�ł�b�x�N�g���쐬
    b0, b_g = np.zeros([4]), np.zeros([2 * nod, nel])
    b0[0], b0[2] = 1.0, -1.0
    eln = 0
    for i_j in ij:
        ni, nj = i_j[0], i_j[1]
        trans = transmatrix(lgh[eln], r[ni, :], r[nj, :])
        b = np.dot(trans.T, b0)  # �S�̍��W�n�ɕϊ�
        b_g[ni * 2:(ni + 1) * 2, eln] += [b[0, 0], b[0, 1]]  # i�ߓ_�̎��R�x�ԍ��ʒu�Ɋi�[
        b_g[nj * 2:(nj + 1) * 2, eln] += [b[0, 2], b[0, 3]]  # j�ߓ_�̎��R�x�ԍ��ʒu�Ɋi�[
        eln += 1
    return np.delete(np.matrix(b_g), remove, 0)  # �S���ߓ_���R�x�ɑΉ�����s������


def make_k(E, a, l, b, nel):  # �S�̍����s��̍쐬
    K = sum([E[e] * a[e] / l[e] * b[:, e].dot(b[:, e].T) for e in range(nel)])
    return K
