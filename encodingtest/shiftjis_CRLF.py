# shiftjis_CRLF
class Person:

    def __init__(self, name):  # �N���X���Ăяo���ꂽ�Ƃ��ɔ����iinitialize�j�B
        # __init__��Python�ōŏ������`����Ă���B
        self.name = name  # �����̖��O

    def behave(self):  # 1�X�e�b�v�ōs���C��A�̍s���B
        # �����̖��O��print���� %s�̂Ƃ����self.name�������Ă���B
        print('My name is %s' % self.name)


def simulation():
    ### �V�~�����[�V�������� ###
    person = Person("shiftjis_CRLF")  # �l��ݒ�
    time = -1
    ### �V�~�����[�V�����J�n ###
    while time < 3:  # ���Ԃ�3�ȏ�̂Ƃ���False�ƂȂ��ă��[�v���I������B
        time += 1
        print('����:%d' % time)
        person.behave()  # ���\�b�hbehave�����s����
    else:  # while���[�v�̏�������False��Ԃ����Ƃ��iwhile���[�v�I�����j�ɔ���
        print('����:%d, finished' % time)

if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    simulation()
