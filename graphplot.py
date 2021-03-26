import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1, 6, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, ls="-.")
# plt.plot(x, y2)

# plt.show()

def AND(x1, x2):
    w1, w2, theta = 1.0, 2.0, 5.0
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

if __name__ == "__main__":
    print(__name__)
    print(AND(2, 3))

