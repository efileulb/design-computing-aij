import numpy as np
a = np.array([[1, 2], [3, 4]])  # �s��̒�`
b = np.array([5, 11])  # �x�N�g���̒�`
x = np.linalg.solve(a, b)  # �A��1���������̉�
print(x)
