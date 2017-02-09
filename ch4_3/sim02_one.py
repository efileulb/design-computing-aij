import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, name):
        self.name = name  # �����̖��O
        #�@��������܂ł̎��Ԃ��w�����z�ŗ^����B
        expected_1 = 30.0
        lam_1 = 1.0 / expected_1  # ���Ғl=1/lam
        self.arrive_time = npr.exponential(1. / lam_1)
        # �p�𑫂��̂ɂ����鎞�Ԃ��A�[�������z�ŗ^����B
        # �A�[�������z�̓K���}���z�̊֐��ŕ\���ł���B
        k = 3.0
        expected_2 = 5.0
        lam_2 = k / expected_2  # ���ҒlE=k/lam���lam=k/E
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # �����̏�Ԃ�\���BNone�͑��݂��Ȃ����Ƃ�\���B

    def __repr__(self):  # print(self)���������̏o�͂����߂Ă����B
        return 'name: %s, status: %s' % (self.name, self.status)

    def behave(self):  # 1�X�e�b�v�ōs���C��A�̍s���B
        if self.status == 'initial':
            self.arrive_time -= 1  # �J�E���g�_�E������
            if self.arrive_time <= 0:
                self.status = 'relieving'
        elif self.status == 'relieving':
            self.relieve_time -= 1  # �J�E���g�_�E������
            if self.relieve_time <= 0:  # �����p�𑫂��I������C�ޏo����B
                self.status = 'leaving'  # �ޏo���B
        print(self)


def simulation():
    ### �V�~�����[�V�������� ###
    person = Person('Yasuda')  # �l��ݒ�
    time = 0
    ### �V�~�����[�V�����J�n ###
    while time < 1000:
        time += 1
        print('time:%d' % time)
        person.behave()
        if person.status == 'leaving':
            break  # �ޏo�����̂Ń��[�v���I���

    ### �V�~�����[�V�����I����܂Ƃ� ###
    print('report')
    print('simulation time: %d' % (time))


if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    npr.seed(RANDOM_SEED)
    simulation()
