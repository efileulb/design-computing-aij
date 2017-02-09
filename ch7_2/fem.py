import numpy as np
import csv
import math


def input(fname):
    r, ijt, ijc = [], [], []
    reader = csv.reader(open(fname, 'r'))
    for row in reader:  # �ߓ_�̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        r.append([float(row[0]), float(row[1]), float(row[2])])
    nod, r = len(r), np.array(r)  # �ߓ_��,����array�ϊ�
    for row in reader:  # �v�f�ߓ_�֌W�̓ǂݍ���
        break  # �擪�s�͓ǂݔ�΂�
    for row in reader:
        if row[0] == '':
            break
        if int(row[2]) == 0:
            ijc.append([int(row[0]), int(row[1])])
        else:
            ijt.append([int(row[0]), int(row[1])])
    nelt, nelc = len(ijt), len(ijc)  # ���k/�����ނ̐�
    return r, ijt, ijc, nod, nelt, nelc


def output(fname, r, nod, ijt, ijc, nelt, nelc, b, lam):
    writer = csv.writer(open(fname, 'w'))
    writer.writerow(['X', 'Y', 'Z'])  # �^�C�g���s
    [writer.writerow([r[i, 0], r[i, 1], r[i, 2]])
     for i in range(nod)]  # �ߓ_���W�̏�������
    writer.writerow([])  # 1�s������
    writer.writerow(['I', 'J', 'CorT', 'Axial Force'])  # �^�C�g���s
    [writer.writerow([ijc[e][0], ijc[e][1], 0, lam[e]])
     for e in range(nelc)]  # ���k�ޏ��̏�������
    [writer.writerow([ijt[e][0], ijt[e][1], 1, b[e]])
     for e in range(nelt)]  # �����ޏ��̏�������


def length(r, ijt, ijc, nelt, nelc):
    lght, lghc = [], []  # ���k/�����ނ̒����̃��X�g
    for e in range(nelt):
        i, j = ijt[e][0], ijt[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        lght.append(math.sqrt(xl**2 + yl**2 + zl**2))  # �����ނ̕��ޒ��v�Z
    for e in range(nelc):
        i, j = ijc[e][0], ijc[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        lghc.append(math.sqrt(xl**2 + yl**2 + zl**2))  # ���k�ނ̕��ޒ��v�Z
    return np.array(lght), np.array(lghc)  # ���X�g��array�ɕϊ����ėv�f������Ԃ�


def dlengthtc(r, ijt, ijc, nod, lght, lghc, nelt, nelc):
    nablaLt, nablaLc = np.zeros([nod * 3, nelt]), np.zeros([nod * 3, nelc])
    for e in range(nelt):  # �����ނ̒�����r�Ɋւ���Δ����̌v�Z
        i, j = ijt[e][0], ijt[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        nablaLt[i, e], nablaLt[j, e] = xl / lght[e], -xl / lght[e]
        nablaLt[nod + i, e], nablaLt[nod + j, e] = yl / lght[e], -yl / lght[e]
        nablaLt[nod * 2 + i, e], nablaLt[nod *
                                         2 + j, e] = zl / lght[e], -zl / lght[e]
    for e in range(nelc):  # ���k�ނ̒�����r�Ɋւ���Δ����̌v�Z
        i, j = ijc[e][0], ijc[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        nablaLc[i, e], nablaLc[j, e] = xl / lghc[e], -xl / lghc[e]
        nablaLc[nod + i, e], nablaLc[nod + j, e] = yl / lghc[e], -yl / lghc[e]
        nablaLc[nod * 2 + i, e], nablaLc[nod *
                                         2 + j, e] = zl / lghc[e], -zl / lghc[e]
    return nablaLt, nablaLc
