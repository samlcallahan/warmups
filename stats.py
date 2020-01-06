import scipy.stats as stats
import itertools as it
import pandas as pd

# What probability distribution would you use to model the scenario outlined above?
# Binomial

# Calculate all the requested probabilities.

p_list = [.9, .8, .7]
n_list = [10, 20]

def get_probs(n, p):
    inv = 1 - p
    results = {}
    results['half or more'] = 0
    for i in range((n // 2) + 1):
        results['half or more'] += 1 - (inv  ** i)
    results['all but one'] = (p ** (n - 1))
    results['all'] = p ** n
    return results

probs = {}
for n in n_list:
    for p in p_list:
        probs[f'{n}, {p}'] = get_probs(n, p)

# stats rework

def get_stats(n, p):
    return {
        'n': n,
        'p': p,
        'half or more': stats.binom(n, p).sf(n / 2),
        'all but one': stats.binom(n, p).pmf(n - 1),
        'all': stats.binom(n, p).pmf(n)
    }

stats = pd.DataFrame([get_stats(n, p) for n, p in it.product(n_list, p_list)])