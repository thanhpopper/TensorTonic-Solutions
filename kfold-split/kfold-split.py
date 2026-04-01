import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    indices = np.arange(N)
    k_fold = []
    if rng:
        indices = rng.permutation(N)
    elif shuffle == True:
        indices = np.random.shuffle(N)
    sizes = np.array([N//k] * k)
    if N % k != 0:
        sizes[:(N%k)] = sizes[:(N%k)] + 1
    fold_indices = [sum(sizes[:i]) for i in range(1,k+1)]
    for i in range(k):
        if i == 0:
            val = indices[:fold_indices[i]]
        else:
            val = indices[fold_indices[i-1]: fold_indices[i]]
        train = np.array([i for i in indices if i not in val])
        k_fold.append((train,val))
    return k_fold
        