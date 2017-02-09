import simpy
import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, env, name, mu):
        self.env = env  # SimPy�̃V�~�����[�V������
        self.name = name  # �����̖��O
        # �p�𑫂��̂ɂ����鎞�Ԃ��A�[�������z�ŗ^����B
        k = 3.0
        lam_2 = k * mu  # ���Ғl1/mu=k/lam���lam=k*mu
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # �����̏�Ԃ�\���B

    def __repr__(self):  # print(self)���������̏o�͂����߂Ă����B
        return 'time: %6.2f, name: %s, status: %s' % (self.env.now, self.name, self.status)

    def behave(self, toilet):  # 1�X�e�b�v�ōs���C��A�̍s���B
        print(self)
        # SimPy�ɒǉ�����v���Z�X�Ƃ��āCgenerator�Ƃ��č쐬����B
        with toilet.request() as req:
            self.status = 'queueing'
            print(self)
            yield req  # request���ʂ�܂ő҂��C�ʂ����玟�̃v���Z�X�ցB
            self.status = 'relieving'
            print(self)
            yield self.env.timeout(self.relieve_time)
            self.status = 'leaving'  # �ޏo���B
            print(self)


def person_generator(env, toilet, lam, mu, person_Num=None):
    print('time: %6.2f, start' % env.now)
    i = 0
    if person_Num == None:
        def flag(i):
            return True #None�̂Ƃ��͖�����W�c�Ƃ��Ĉ����B
    else:
        def flag(i):
            return i < person_Num  # �L����W�c�B
            
    while flag(i):
        # �o�ꂷ�鎞�ԊԊu�͎w�����z
        yield env.timeout(npr.exponential(1.0 / lam, size=1))
        person = Person(env, 'person_%00d' % i, mu)
        i += 1
        env.process(person.behave(toilet))  # �V�~�����[�V�������Ɏ��s����v���Z�X��ǉ�


def simulation(lam=0.2, mu=0.2, capacity=1, until=100):
    ### �V�~�����[�V�������� ###
    # ����ݒ�
    env = simpy.Environment()  # SimPy�ɂ��V�~�����[�V���������쐬
    toilet = simpy.Resource(env, capacity=capacity)  # capacity�̐������g�C��������B
    # �l��ݒ�
    person_Num = 5  # �L����W�c
    env.process(person_generator(env, toilet,
                                 lam, mu, person_Num))  # �l���o��������v���Z�X�Ɠo�^
    ### �V�~�����[�V�����J�n ###
    env.run(until=until)

if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    npr.seed(RANDOM_SEED)
    simulation(lam=0.2, mu=0.2, capacity=1, until=100)
