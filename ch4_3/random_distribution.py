# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as npr
import scipy.stats as sps
import matplotlib.pylab as plt

RANDOM_SEED = 1  # random seed
SIZE = 10000  # ���s��
EXPECTED_V = 5  # ���Ғl


def x_uniform():
    # ��l���z
    #? a����b�܂ň�l�̊m���̂Ƃ����̊Ԃ�x��Ԃ��B
    a = 0
    b = EXPECTED_V * 2 - a
    return npr.uniform(a, b, SIZE)


def x_poisson():
    # �|�A�\�����z
    # �P�ʎ��Ԃ�����ɉ�N���鎖�ۂ����傤��k�񔭐�����Ƃ���k��Ԃ�
    lambd = EXPECTED_V  # ���Ғl=�ɂƂȂ�
    return npr.poisson(lambd, size=SIZE)


def x_exponential():
    # �w�����z
    # �P�ʎ��ԓ����蕽�σɉ�N���鎖�ہ�����1/�Ɏ��Ԃ�1�񔭐����鎖�ۂ̔����Ԋu��t���Ԃł���Ƃ���t��Ԃ�
    #�@���ϗ]���ȂǁB
    lambd = 1.0 / EXPECTED_V  # 1��������lambd�񔭐�����B= ����1/lambd���Ԃ̊Ԋu��1�񔭐�
    return npr.exponential(1. / lambd, size=SIZE)  # �����Ԋu�������_���ɕԂ�


def x_erlang():
    # �A�[�������z
    # �A�[�������z�̓K���}���z�̌`��ꐔk�𐳐����Ɍ��肵������
    k = 3
    lambd = k / EXPECTED_V  # ���Ғl = k/�ɂƂȂ�B
    return npr.gamma(k, 1. / lambd, size=SIZE)


def histogram(x_distribution, ax, title="histogram"):
    mean = np.mean(x_distribution)
    print("%s: mean:%f" % (title, mean))
    bins = np.arange(np.floor(np.amin(x_distribution)),
                     np.ceil(np.amax(x_distribution)) + 1.0, 1.)
    n, bins, patches = ax.hist(
        x_distribution, bins=bins, align='left', normed=1, color="gray")

    ax.set_title(title, fontsize=14)
    ax.set_xlabel('value')
    ax.set_ylabel('frequency / N')


if __name__ == '__main__':
    npr.seed(RANDOM_SEED)
    fig = plt.figure()
    fig.suptitle('Histogram: N=%d, E=%-4.2f' % (SIZE, EXPECTED_V), fontsize=16)
    fig.subplots_adjust(left=None, bottom=None, right=None,
                        top=None, wspace=0.3, hspace=0.4)

    ax1 = fig.add_subplot(221)
    histogram(x_uniform(), ax1, title="uniform")

    ax2 = fig.add_subplot(222)
    histogram(x_poisson(), ax2, title="poisson")

    ax3 = fig.add_subplot(223)
    histogram(x_exponential(), ax3, title="exponential")

    ax4 = fig.add_subplot(224)
    histogram(x_erlang(), ax4, title="erlang(k=3)")

    plt.show()
