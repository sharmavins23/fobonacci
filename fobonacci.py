import functools
import math

from matplotlib import pyplot as plt


@functools.cache
def fobonacci(n, k):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return (fobonacci(n-1, k) * fobonacci(n-2, k)) % k


xValues = list(range(0, 1000))
k = 2300
yValues = [fobonacci(x, k) for x in xValues]

# Plot these values
plt.plot(xValues, yValues)
plt.title(f"Fobonacci mod {k}")
plt.savefig(f"plots/fobonacci_{k}.png")
