class Rectangle:

    def __init__(self, dx, dy):  # �������֐�
        self.dx = dx
        self.dy = dy

    def cal_area(self):  # �ʐς��v�Z����֐�
        self.area = self.dx * self.dy
        return self.area
