import numpy as np


def softmax(x):
    e_x = np.exp(x)
    print(e_x)
    e_x_sum = np.sum(e_x)
    print(e_x_sum)
    return e_x / e_x_sum


x = np.array([100, 100])
print(softmax(x))