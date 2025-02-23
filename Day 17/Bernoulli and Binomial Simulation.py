from scipy.stats import bernoulli, binom
import matplotlib.pyplot as plt

# Bernoulli: Single trial with p=0.6
p = 0.6
bernoulli_sample = bernoulli.rvs(p, size=1000)
print(f"Bernoulli sample (first 10 outcomes): {bernoulli_sample[:10]}")

# Binomial: 10 trials with p=0.6
n = 10
binomial_sample = binom.rvs(n, p, size=1000)

# Plot histogram of binomial outcomes
plt.figure(figsize=(8, 4))
plt.hist(binomial_sample, bins=np.arange(n+2)-0.5, density=True, color='skyblue', edgecolor='black')
plt.title("Binomial Distribution (n=10, p=0.6)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()