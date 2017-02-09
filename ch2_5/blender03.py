import bpy

# �����̂̒��_���W�ƕӁE���_�̐ڑ��֌W
nodes=[[0,0,0], [1,0,0], [1,1,0], [0,1,0],
       [0,0,1], [1,0,1], [1,1,1], [0,1,1]]

faces=[[0,1,2,3], [4,5,6,7], [0,4,5,1],
       [1,2,6,5], [3,2,6,7], [0,3,7,4]]

mesh_data = bpy.data.meshes.new('cube_mesh_data')   #���b�V���f�[�^���쐬
cube_object = bpy.data.objects.new('cube_object', mesh_data) #�����̃I�u�W�F�N�g���쐬

scene = bpy.context.scene                #�V�[�����쐬
scene.objects.link(cube_object)          #�I�u�W�F�N�g�����݂̃V�[���Ƀ����N

mesh_data.from_pydata(nodes, [], faces)  #���_�Ɩʂ̃��X�g�����b�V���f�[�^�ɒǉ�
mesh_data.update()                       #�ҏW�����f�[�^���X�V