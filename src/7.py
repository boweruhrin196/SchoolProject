import random

def random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)

print(random_word())
