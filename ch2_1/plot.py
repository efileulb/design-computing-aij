import module1  # �쐬�������W���[�� module1.py�̓ǂݍ���

file_name = 'data3.csv'  # �t�@�C����
x, y = module1.read_data(file_name)  # module1���̊֐�read_data�ɂ��f�[�^���擾
xmin, xmax, ymin, ymax = 0, 10, 0, 10  # �`��͈�
lc, ls, lw = 'black', '-', 2.0  # �`��I�v�V����
title, xl, yl = 'LineGraph', 'X-Axis', 'Y-Axis'  # �^�C�g���C���x��
module1.draw_graph(x, y, xmin, xmax, ymin, ymax, lc,
                   ls, lw, title, xl, yl)  # module1����
# �֐�draw_graph�ɂ��O���t�`��
