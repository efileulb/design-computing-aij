def grow(s, r):  # ������s�ƌJ��Ԃ���r�����
    n = len(s)  # ���͂���������̒���
    ss = ' '  # �o�͂��镶�����������
    for i in range(n):
        if s[i] == 'f':  # ' f'  �� ' fg'  �ɏ�������
            ss = ss + 'fg'
        else:
            if s[i] == 'g':  # ' g'  �� ' gh'  �ɏ�������
                ss = ss + 'gh'
            else:
                ss = ss + 'h'  # ���̑��̕����ih�j�̂Ƃ����̂܂�
    print(ss)
    r -= 1  # �c��̌J�Ԃ��񐔂�1���炷
    if r > 0:  # �J�Ԃ��񐔂�0�łȂ����C�������g���Ăяo��
        grow(ss, r)
    return ss

grow('fgh', 2)  # grow��2����s