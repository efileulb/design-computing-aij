import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, name, expected, ahead=None):
        self.name = name  # �����̖��O
        self.ahead = ahead  # �����̑O�ɂ���l
        # �p�𑫂��̂ɂ����鎞�Ԃ��A�[�������z�ŗ^����B
        k = 3.0
        lam_2 = k / expected  # ���ҒlE=k/lam���lam=k/E
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.queueing_time = 0  # �ݐς̑҂�����
        self.status = 'initial'  # �����̏�Ԃ�\���BNone�͑��݂��Ȃ����Ƃ�\���B

    def __repr__(self):  # print(self)���������̏o�͂����߂Ă����B
        return 'name: %s, status: %s' % (self.name, self.status)

    def behave(self):  # 1�X�e�b�v�ōs���C��A�̍s���B
        ### ��������𓾂� ###
        # �O�ɂ���l�̏�Ԃ����ē���Bahead_status�����肷��B
        if self.ahead != None:
            ahead_status = self.ahead.status
        else:
            ahead_status = 'leaving'

        ### �ӎv��������čs������ ###
        if ahead_status != 'leaving':  # �O�ɐl��������s��ɕ��ԁB
            self.queueing_time += 1
            self.status = 'queueing for %d' % self.queueing_time
            print(self)
        else:  # �O�ɐl�����Ȃ���΁C�p�������B
            self.relieve_time += -1
            self.status = 'relieving rest:%-2.2f' % self.relieve_time
            print(self)
            if self.relieve_time <= 0:  # �����p�𑫂��I������C�ޏo����B
                self.status = 'leaving'  # �ޏo���B
                print(self)


def person_generator(expected):  # next�ŌĂяo�����т�person�𐶐�
    i = 0
    ahead = None
    while True: 
        person = Person('person_%02d' % i, expected, ahead=ahead)
        ahead = person
        i += 1
        yield person # yeild�́C���ɌĂ΂ꂽ�Ƃ��ɂ܂����̈ʒu���珈�������B


def simulation(lam, mu, person_Num):
    ### �V�~�����[�V�������� ###
    person_list_queueing = []  # �V�X�e�����ɂ���l�̃��X�g�B
    person_list_worked = [] # �V�~�����[�V�����I�������l���߂��ރ��X�g
    gen = person_generator(1./mu) # �p�𑫂����Ԃ̊��Ғl=1/�P�ʎ��Ԃ�����ɗp�𑫂��l��
    time = -1

    ### �V�~�����[�V�����J�n ###
    # �S�����ޏo����܂ŃV�~�����[�V����������B
    while len(person_list_worked) < person_Num:  # �w�肵���l�����I�������烋�[�v�I��
        time += 1
        print('time:%d, queue:%d' % (time, len(person_list_queueing)))
        # �o���̏���
        num = npr.poisson(lam) # �P�ʎ��Ԃ�����̓����l���̊��Ғl=������(�l)�B
        if num:
            for i in range(num):
                person_list_queueing.append(next(gen))  # next(gen)��person�𐶐�

        # �V�X�e�����ɂ���l���ꂼ��̍s���̏���
        # python�̎d�l�ŁCperson_list�̃��[�v���Ƀ��X�g�̓��e��ύX�����
        # �\�����Ȃ������������̂ŁC[:]�̃X���C�X�ŃR�s�[����B
        for person in person_list_queueing[:]:  # ��l���s������
            person.behave()
            if person.status == 'leaving':  # �ޏo�ɂȂ��Ă���person�����X�g�����菜��
                person_list_queueing.remove(person)
                person_list_worked.append(person)

        if time > 100:
            break

    ### �V�~�����[�V�����I����܂Ƃ� ###
    print('report')
    for person in person_list_worked:
        print('name: %s, queueing time: %s' %
              (person.name, person.queueing_time))

if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    npr.seed(RANDOM_SEED)
    simulation(lam=0.2, mu=0.2, person_Num=5)
