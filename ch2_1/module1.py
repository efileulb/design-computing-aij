def read_data(file_name):
    import csv
    reader = csv.reader(open(file_name, 'r'))
    X, Y = [], []
    for row in reader:
        X.append(row[0]), Y.append(row[1])
    return X, Y  # �f�[�^��Ԃ�


def draw_graph(X, Y, xmin, xmax, ymin, ymax, Lc, Ls, Lw, title, xlabel, ylabel):
    import matplotlib.pyplot as plt
    plt.xlim(xmin, xmax)  # X�͈̔͂̎w��
    plt.ylim(ymin, ymax)  # Y�͈̔͂̎w��
    plt.title(title)  # �O���t�^�C�g��
    plt.xlabel(xlabel)  # X���^�C�g��
    plt.ylabel(ylabel)  # Y���^�C�g��
    plt.plot(X, Y, color=Lc, linestyle=Ls, linewidth=Lw)  # �O���t����������ɍ쐬
    plt.show()  # �O���t�̕`��
