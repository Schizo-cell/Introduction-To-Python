total = 0
for n in range(2, 1000):
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
           is_prime = False
        break
    if is_prime:
        total += n
print("Sum of primes below 1000:", total)