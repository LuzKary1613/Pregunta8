import numpy as np
import matplotlib.pyplot as plt

def function_valoresperado(N):
    R = np.random.uniform(0, 1, N)
    x = (3 ** R) / 2
    return x

N = 100000
x = function_valoresperado(N)
C = 500

plt.hist(x, bins=C)
plt.show()

print(f'Valor aproximado: {np.mean(x)}')
