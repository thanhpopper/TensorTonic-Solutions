import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    # 1-d array
    X = np.array(X)
    y = np.array(y)
    indices = np.arange(len(y))
    if rng is None:
        rng = np.random.Generator()
    rng.shuffle(indices)

    for i in range(0,len(y),batch_size):
        if (i + batch_size > len(y)):
            if drop_last == False:
                batch = (X[indices[i:len(y)]], y[indices[i:len(y)]])
                yield batch
                break
            else:
                break
        else:
            batch = (X[indices[i:i+batch_size]], y[indices[i:i+batch_size]])
            yield batch
        
        