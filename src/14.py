import random

def get_random_code():
  num = random.randint(100, 999)
  letters = ['a', 'b', 'c', 'd', 'e']
  letter = random.choice(letters)
  return f"{num}{letter}"
