# -*- coding: utf-8 -*-
f1 = open('data1_utf8.dat', 'r')  # data1.dat ����͂̂��߂�open
f2 = open('data2.dat', 'w')  # data2.dat ���o�͂̂��߂�open
content = f1.read()  # �t�@�C���S�Ă�str�^�C�v�œǂݍ���
contents = content.split(';')  # �Z�~�R�����ŋ�؂�
for kk in contents:
    k1, k2 = kk.split(',')  # �J���}����؂�Ƃ��ă��X�g�ɕ���
    k1, k2 = int(k1), float(k2)  # �e�v�f�𐔒l�ɕϊ�
    f2.write(str(k1) + ' ' + str(k2**2) + '\n')  # 2��l�Ƌ󔒁C���s�R�[�h����������
f1.close()  # data1.dat ���N���[�Y
f2.close()  # data2.dat ���N���[�Y
