import simpy


class Person:

    def __init__(self, env, name):
        self.env = env  # SimPy�̃V�~�����[�V������
        self.name = name  # �����̖��O

    def behave(self):  # 1�X�e�b�v�ōs���C��A�̍s���B
        # SimPy�ɒǉ�����v���Z�X�Ƃ��āCgenerator�Ƃ��č쐬����B
        while True:
            print('time[%02d] My name is %s' % (self.env.now, self.name))
            yield self.env.timeout(1)


def simulation():
    ### �V�~�����[�V�������� ###
    # ����ݒ�
    env = simpy.Environment()  # SimPy�ɂ��V�~�����[�V���������쐬
    # �l��ݒ�
    person = Person(env, 'Yasuda')
    env.process(person.behave())  # �v���Z�X�Ɠo�^
    ### �V�~�����[�V�����J�n ###
    env.run(until=5)


if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    simulation()
