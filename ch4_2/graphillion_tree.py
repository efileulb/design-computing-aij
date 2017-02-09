from graphillion import GraphSet         # graphillion�̃N���XGraphSet���C���|�[�g
import graphillion.tutorial as tl        # graphillion�̃��W���[��tutorial��tl�Ƃ������O�ŃC���|�[�g

universe = tl.grid(2, 2)           # 2x2�̃O���b�h�𐶐�
GraphSet.set_universe(universe)
# �K�����݂���ӂƕK�����݂��Ȃ��ӂ��`
lines = GraphSet({'include': [(8, 9), (5, 8), (4, 5)], 'exclude': [(6, 9)]})
# �S��؂𐶐�
trees = GraphSet.trees(is_spanning=True)
common = trees & lines
# ���ʂ̕`��
for path in common:
    tl.draw(path)
