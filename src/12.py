import random

def roll_dice(num_sides):
    """Roll a number of dice."""
    if num_sides <= 0:
        raise ValueError("number of sides must be positive")
    return sum([random.randint(1, num_sides) for _ in range(num_dice)])

def get_roll():
    """Get a random roll."""
    return roll_dice(6)

if __name__ == "__main__":
    print("Rolling the dice...")
    print("Result:", get_roll())
