import numpy as np #���W���[��numpy��np�Ƃ������O�œǂݍ���
import csv #���W���[��csv�̓ǂݍ���
import matplotlib.pyplot as plt #���W���[��matplotlib��pyplot�֐���plt
                                #�Ƃ������O�œǂݍ���
#**
reader = csv.reader(open('out2.csv', 'rb')) #��قǏo�͂���output.csv�̓ǂݍ���
f_history=[] #�ړI�֐��̗���
x1_history,x2_history=[],[] #�݌v�ϐ��̗���
#**
for row in reader:#1�s�ڂ̓��x���s�Ȃ̂œǂݔ�΂�
    break
for row in reader:
    f_history.append(float(row[1])) #�ړI�֐��̓ǂݍ���
    x1_history.append(float(row[2])) #�݌v�ϐ��̓ǂݍ���
    x2_history.append(float(row[3]))
plt.figure(figsize=(15,8)) #�O���t�`��L�����o�X�����c��15:8�Ő���
x1=np.arange(-0.5, 4.5, 0.1) #1.25�`4.75�܂�0.1���݂̃x�N�g��
x2=np.arange(-0.5, 4.5, 0.1) #0.25�`3.75�܂�0.1���݂̃x�N�g��
X1,X2=np.meshgrid(x1,x2) #x1,x2��g�ݍ��킹���s��
f=np.vectorize(lambda x1,x2: ((2.0-x1)**2+(4.0-x2)**2)**0.5+
((3.0-x1)**2+(2.0-x2)**2)**0.5) #x1,x2�������Ƃ���
                                                           #�ړI�֐���Ԃ��֐�
plt.subplot(1,2,1) #1�s�ڂ�2��̕��т�1��ڂɃO���t�𐶐�
plt.xlabel('x1') #���������̃��x��
plt.ylabel('x2') #���������̃��x��
C=plt.contour(X1,X2,f(X1,X2),20,colors='black') #�������f�[�^����
plt.clabel(C, inline=1, fontsize=10) #�������}����
plt.plot(x1_history,x2_history) #�ړI�֐��̒T���o�H����
#__
zero1=[0.0]*len(x1)
zero2=[0.0]*len(x2)
two1=[2.0]*len(x1)
two2=[2.0]*len(x2)
h=(-2.0*x1+7.0)/3.0
plt.plot(x1,zero1,'-',color='gray',label=r'$x_1=0$')
plt.plot(zero2,x2,'--',color='gray',label=r'$x_2=0$')
plt.plot(x1,two1,'-.',color='gray',label=r'$x_1-2=0$')
plt.plot(two2,x2,':',color='gray',label=r'$x_2-2=0$')
plt.plot(x1,h,'.',color='gray',label=r'$2x_1+3x_2-7=0$')
plt.fill([0,2,2,0.5,0],[0,0,1,2,2],alpha=0.1)
#__
plt.subplot(1,2,2) #1�s�ڂ�2��̕��т�2��ڂɃO���t�𐶐�
plt.xlabel('step') #���������̃��x��
plt.ylabel('f(x)') #���������̃��x��
plt.plot(f_history) #�ړI�֐��̗���}�̐���
                    #(x�������ȗ�����Ύ����I�ɉ�����step���ƂȂ�)
plt.show() #�O���t����ʂɕ\������