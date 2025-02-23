import numpy as np

# Simulate 1000 coin tosses (0 for Tails, 1 for Heads)
coin_tosses = np.random.randint(0, 2, 1000)
heads_probability = np.sum(coin_tosses) / len(coin_tosses)
print(f"Estimated Probability of Heads: {heads_probability:.2f}")
