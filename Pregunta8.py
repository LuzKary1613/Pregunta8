import numpy as np
import matplotlib.pyplot as plt

def func_test(N):
    R = np.random.uniform(0, 1, N)
    x = (3 ** R) / 2
    return x

N = 100000
x = func_test(N)
C = 500

plt.hist(x, bins=C)
plt.show()

print(f'El valor aproximado es de {np.mean(x)}')
