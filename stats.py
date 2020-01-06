import scipy.stats as stats

# What probability distribution would you use to model the scenario outlined above?
# Binomial

# Calculate all the requested probabilities.
# 10 subjects, at least 5 remain
1 - (.1 ** 5) # .9999

# 10 subjects, only 1 leaves
.1 * (.9 ** 9) # .0387

# 10 subjects, all stay
.9 ** 10 # .3487

# 20 subjects, at least 10 remain
1 - (.1 ** 10) # .9999999999

p_list = [.9, .8, .7]
n_list = [10, 20]

def get_probs(n, p):
    inv = 1 - p
    results = {}
    results['half'] = 1 - (inv ** (n / 2))
    results['all_but_one'] = inv * (p ** (n - 1))
    results['all'] = inv ** n
    return results

probs = {}
for n in n_list:
    for p in p_list:
        probs[f'{n}, {p}'] = get_probs(n, p)