import random

def generate_random_code(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(characters) for i in range(length))

generate_random_code(10)
