import random
import math

print("""This program can approximate the value of pi using random 
points on a graph. Enter a high number for more accurate results.
Something like a million or so!""")
n = 0 #number of times point lands in circle
N = int(input("Enter number of points to generate: "))

for i in range(N):
    x = random.random()
    y = random.random()
    if (x ** 2) + (y ** 2) < 1:
            n += 1

expected = math.pi
print(f"The expected value is {expected:.4f}")
print(f"Number of points inside the circle was {n}, while {N - n} "
      f"landed outside.")
pi_a = (4 * n) / N
print(f"Approximation of Pi is {pi_a:.4f}")
