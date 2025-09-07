print("This program prints all the prime numbers up to the number you entered.")
high = int(input("Please enter a number:"))
# high = 13 # using this for testing
none_prime = []
prime = []

for a in range(1, high + 1):
    for b in range(1, a + 1):
        if a % b == 0 and b != 1 and b != a:
            none_prime.append(a)

for x in range(1, high + 1):
        if x not in none_prime:
            prime.append(x)
print("The prime numbers are::")
print(prime)