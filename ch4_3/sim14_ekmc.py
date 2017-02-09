import simpy
import numpy.random as npr
import matplotlib.pyplot as plt
import sim13_many as mysim  # �����ō쐬�������W���[����ǂݍ��݁B
RANDOM_SEED = 5


def monitor(env, toilet, data):  # �L�^�p��
    while True:
        tup = [
            env.now,  # ���ݎ���
            toilet.count,  # �g�p�l��
            len(toilet.queue)  # �s��l��
        ]
        data.append(tup)
        yield env.timeout(1)


def simulation(lambd=0.3, mu=0.2, capacity=1, until=100):
    ### �V�~�����[�V�������� ###
    # ����ݒ�
    env = simpy.Environment()  # SimPy�ɂ��V�~�����[�V���������쐬
    toilet = simpy.Resource(env, capacity=capacity)
    # �l���o��������v���Z�X�Ɠo�^ # ������W�c
    env.process(mysim.person_generator(env, toilet,
                                       lambd, mu))  
    # �L�^�p����ݒ�
    data = []  # �L�^�p
    env.process(monitor(env, toilet, data))
    # �f�[�^��ݒ�
    ### �V�~�����[�V�����J�n ###
    env.run(until=until)
    ### �V�~�����[�V�����I�� ###
    print(data)
    ### ���� ###
    x = [tup[0] for tup in data]  # ����
    y = [tup[2] for tup in data]  # �҂��l��
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(x, y, color='gray')
    ax.set_title(r'length of queue, $\lambda=%4.2f, \mu=%4.2f, c=%d$' %
                 (lambd, mu, capacity))
    ax.set_xlabel('steps')
    ax.set_ylabel('queue length')
    plt.show()


if __name__ == '__main__':  # ���̃X�N���v�g���̂����s���ꂽ�Ƃ��ɂ݈̂ȉ������s
    npr.seed(RANDOM_SEED)
    simulation(lambd=1.0, mu=0.2, capacity=5, until=100)
