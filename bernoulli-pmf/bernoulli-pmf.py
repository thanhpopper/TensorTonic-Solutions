import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = []
    for i in x:
        if i == 1:
            pmf.append(p)
        else:
            pmf.append(1-p)
    pmf = np.array(pmf)
    mean = p
    var = p*(1-p)
    return pmf, mean, var