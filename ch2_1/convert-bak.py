# -*- coding: utf-8 -*-
f1 = open('data1.dat', 'rb')  # data1.dat を入力のためにopen
f2 = open('data2.dat', 'wb')  # data2.dat を出力のためにopen
for ii in f1:
    jj = ii.rsplit('\r')  # 改行コードを区切りとしてリストに分割

for kk in jj:
    ll = kk.rsplit(' ')  # 空白を区切りとしてリストに分割
    k1, k2 = float(ll[0]), float(ll[1])  # リストの各要素を実数に変換
    f2.write(str(k1**2) + ' ' + str(k2**2) + '\n')  # 2乗値と空白，改行コードを書き込み
f1.close()  # data1.dat をクローズ
f2.close()  # data2.dat をクローズ
