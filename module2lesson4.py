numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for key in numbers:
    is_prime = True
    if key < 2:
        is_prime = False
    else:
        for i in range(2, key):
            if key % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(key)
    else:
        not_primes.append(key)
print("Простые числа:", primes)
print("Не простые числа:", not_primes)