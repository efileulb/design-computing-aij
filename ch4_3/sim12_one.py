import simpy
import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, env, name, lam, mu):
        self.env = env  # SimPy�̃V�~�����[�V������
        self.name = name  # �����̖��O
        #�@��������܂ł̎��Ԃ̊��Ғl��1/������
        self.arrive_time = npr.exponential(1. / lam)
        # �p�𑫂��̂ɂ����鎞�Ԃ��A�[�������z�ŗ^����B
        k = 3.0
        lam_2 = k * mu # ���Ғl1/mu=k/lam���lam=k*mu
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # �����̏�Ԃ�\���B

    def __repr__(self):  # print(self)���������̏o�͂����߂Ă����B
        return 'time: %6.2f, name: %s, status: %s' % (self.env.now, self.name, self.status)

    def behave(self):  # 1�X�e�b�v�ōs���C��A�̍s���B
        # SimPy�ɒǉ�����v���Z�X�Ƃ��āCgenerator�Ƃ��č쐬����B
        # �����̖��O��print���� %s�̂Ƃ����self.name�������Ă���B
        self.status = 'arrival'
        print(self)       
        yield self.env.timeout(self.arrive_time)
        self.status = 'relieving'
        print(self)
        yield self.env.timeout(self.relieve_time)
        self.status = 'leaving'  # �ޏo���B
        print(self)


def simulation(lam, mu):
    ### �V�~�����[�V�������� ###
    # ����ݒ�
    env = simpy.Environment()  # SimPy�ɂ��V�~�����[�V���������쐬
    # �l��ݒ�
    person = Person(env, 'Yasuda', lam, mu)
    env.process(person.behave())  # �v���Z�X�Ɠo�^
    ### �V�~�����[�V�����J�n ###
    env.run(until=100)


if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    npr.seed(RANDOM_SEED)
    simulation(1.0/30.0, 1/5.0)
