def get_random_number(n):
    return randint(0, n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_random_prime(n):
    while True:
        prime = get_random_number(n)
        if is_prime(prime):
            return prime

get_random_prime(100)
