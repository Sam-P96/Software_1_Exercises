import random
import math

n = 0 #number of times point lands in circle
N = 1000000 #number of tries

for i in range(N):
    x = random.random()
    y = random.random()
    if (x ** 2) + (y ** 2) < 1:
            n += 1

expected = math.pi
print(f"The expected value is {expected:.4f}")
print(f"Number of points inside the circle is {n}.")
pi_a = (4 * n) / N
print(f"Approximation of Pi is {pi_a:.4f}")
