import bpy
import copy              # �I�u�W�F�N�g���R�s�[���邽�߂̃��W���[��copy���C���|�[�g

def move(box,l,stack,s,t):  # �}�`���R�s�[���Ĉړ����鑀��

    box_2 =copy.deepcopy(box)  # box��box_2�ɃR�s�[
    n=len(box_2)

    for i in range(n):
        for j in range(8):
            box_2[i][j][s]+=l    # s������ l �����ړ�
            box_2[i][j][t]+=l    # t������ l �����ړ�

    stack.extend(box_2)         # �X�^�b�N�ɃR�s�[

########################################
# �����̂̒��_���W�ƕӁE���_�̐ڑ��֌W
verts=[[[0,0,0], [1,0,0], [1,1,0], [0,1,0],
        [0,0,1], [1,0,1], [1,1,1], [0,1,1]]]

faces=[[0, 1, 2, 3], [4, 5, 6, 7], [0, 4, 5, 1],
       [1, 2, 6, 5], [3, 2, 6, 7], [0, 3, 7, 4]]

stack=[]     # �����̂�ۑ����邽�߂̃X�^�b�N�̏�����

l=1         # �����̂��ړ�����ʂ̏����l
########################################

#�t���N�^���}�`�̐����C�����l�ł�3��J��Ԃ�
for i in range(3):
    move(verts,l,stack,1,2)
    move(verts,l,stack,0,1)
    move(verts,l,stack,0,2)
    verts.extend(stack)
    stack=[]
    l=l*2

# �ϐ��̏�����
m_d=[]
c_m_d=[]
c_o=[]
C_O=[]

n=len(verts)

#blnder��ɐ}�`��`�悷�邽�߂̐ݒ�
for i in range(n):
    m_d.append("mesh_data_"+str(i))
    c_m_d.append("cube_mesh_data_"+str(i))
    c_o.append("cube_object"+str(i))
    C_O.append("Cube_Object"+str(i))

    m_d[i] = bpy.data.meshes.new(c_m_d[i])
    m_d[i].from_pydata(verts[i], [], faces)
    m_d[i].update()
    c_o[i] = bpy.data.objects.new(C_O[i], m_d[i])

scene = bpy.context.scene

for i in range(n):
    scene.objects.link(c_o[i])