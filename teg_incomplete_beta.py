import numpy as np
import math

def teg_nchoosek(x, y):
    try:
        return math.gamma(x + 1) / (math.gamma(y + 1) * math.gamma(x - y + 1))
    except:
        return 0

def teg_incomplete_beta_comb_series(x, a, b):
    # From https://dlmf.nist.gov/8.17
    N = 200
    Ix = (1-x)**b * np.sum(np.array([teg_nchoosek(b + (a+j) - 1, (a+j)) * x**(a+j) for j in range(0, N)]))
    return Ix

def teg_incomplete_beta(x, a, b):
    if x > a/(a + b):
        Ix = 1 - teg_incomplete_beta_comb_series(1-x, b, a)
    else:
        Ix = teg_incomplete_beta_comb_series(x, a, b)
    return Ix
