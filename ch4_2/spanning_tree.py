import copy
import math
import bpy

def make_path(c,e): # ��e ���p�Xc �ɒǉ�
    c.append(e)

def search(a,e,i,m,comp,c,n): # �ǉ�����ӂ̒T��
    if len(e)==n-1:# �S��؂̕ӂ̐���(���_��)-1�Ȃ̂ŕӂ̐���n-1�ƂȂ�Ώo�͂���
        b=copy.deepcopy(e)
        make_path(c,b)
    for j in range(i,m):
        a_0=a[j][0]#head
        a_1=a[j][1]#tail
        if comp[a_0]!=comp[a_1]:# �o�b�N�g���b�N�@�ɂ��S��؂�T��
            comp2=copy.deepcopy(comp)
            e.append(j)
            t=min(comp[a_0],comp[a_1])# �A�������ԍ��̍ŏ��l
            s=max(comp[a_0],comp[a_1])# �A�������ԍ��̍ő�l
            for k in range(len(comp)):# �ő�l���ŏ��l�Œu��������
                if comp[k]==s:
                    comp[k]=t
            search(a,e,j+1,m,comp,c,n)
            comp=comp2
            e.pop()

def make_edges(c,a,d,n): # �`��̂��߂̕Ӄf�[�^�̍쐬
    for i in range(len(c)):
        f=[]
        for j in range(n-1):
            f.append(a[c[i][j]])
        d.append(f)

def make_verts(verts_n,n,k): # �`��̂��߂̒��_�f�[�^�̍쐬
    p=k//10+1
    for l in range(9):
        verts_i=copy.deepcopy(verts_n[-1])
        for i in range(n):
            verts_i[i][0]+=15
        verts_n.append(verts_i)
    verts_m=copy.deepcopy(verts_n)
    verts_m_0=copy.deepcopy(verts_m)
    for j in range(p):
        for q in range(10):
            for i in range(n):
                verts_m_0[q][i][1]+=15*(j+1)
        for i in range(10):
            verts_n.append(verts_m_0[i])
        verts_m_0=copy.deepcopy(verts_m)

def cylinder(o_0, o_1):  # �`��̂��߂̉~���̒�`

    x_0 = o_0[0] #���W�̐ݒ�
    y_0 = o_0[1]
    z_0 = o_0[2]
    x_1 = o_1[0]
    y_1 = o_1[1]
    z_1 = o_1[2]

    x_c = x_0 + ((x_1-x_0)/2) #�~���̒��S�̓_��ݒ�
    y_c = y_0 + ((y_1-y_0)/2)
    z_c = z_0 + ((z_1-z_0)/2)

    x_t = x_1-x_c
    y_t = y_1-y_c
    z_t = z_1-z_c

    r = math.sqrt( (x_t*x_t) + (y_t*y_t) + (z_t*z_t) )
    theta = math.acos( z_t/r )
    phi = math.atan2( (y_t), (x_t) )

    bpy.ops.mesh.primitive_cylinder_add(location = (x_c, y_c, z_c),
        depth = r*2,radius = 0.2,rotation = (0, theta, phi))

#################################################
# �����̂̒��_���W�ƕӁE���_�̐ڑ��֌W
verts=[[0,0,0], [10,0,0], [10,10,0], [0,10,0],
[0,0,10], [10,0,10], [10,10,10], [0,10,10]]

a = [(0,1),(1,2),(2,3),(0,3),
(0,4),(1,5),(2,6),(3,7),
(4,5),(5,6),(6,7),(4,7)]

#################################################

n=len(verts)# ���_�̐�
m=len(a)# �ӂ̐�

comp=[i for i in range(n)]

e=[]# �ϐ��̏�����
c=[]
d=[]

search(a,e,0,m,comp,c,n) #�S��؂̒T��

# ���ʂ̕`��
make_edges(c,a,d,n)
verts_n=[verts]
k=len(c)
make_verts(verts_n,n,k)
for j in range(k):
    e=d[j]
    for i in range(n-1):
        cylinder(verts_n[j][e[i][0]],verts_n[j][e[i][1]])
