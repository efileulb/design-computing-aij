from rect import *  # rect.py�̓��e���C���|�[�g����


class Square(Rectangle):

    def __init__(self, dx):
        self.dx = dx
        self.dy = self.dx  # 2�ӂ̒����𓙂�������
