import csv  # csv�t�@�C���̃C���|�[�g�B���̃t�@�C�����̂�csv.py�ɂ���Ƌ�������̂Œ��ӁB
f1 = open('data1.csv', 'r')  # data1.csv����͂̂��߂�open
f2 = open('data2.csv', 'w')  # data2.csv���o�͂̂��߂�open
reader = csv.reader(f1)  # data1.csv��csv�`���ŔF��
writer = csv.writer(f2)  # data2.csv��csv�`���ŔF��
for row in reader:  # csv�t�@�C���̓��e��1�s�����X�g�Ƃ��ēǂݍ���
    data1, data2 = float(row[0])**2, float(row[1])**2  # �����ɕϊ���2�悷��
    writer.writerow([data1, data2])  # 1�s����������
