import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X)
    filled_X = np.zeros_like(X)
    dim = X.ndim
    if dim == 1:
        filled_X = filled_X.reshape(-1,1)
        X = X.reshape(-1,1)
    # Calculate mean of each Feature column
    for i in range(X.shape[1]):
        if np.isnan(X[:,i]).all():
            continue
        if strategy == 'mean':
            fill_value = np.nanmean(X[:,i])
        else:    
            fill_value = np.nanmedian(X[:,i])
        filled_X[:,i] = np.where(np.isnan(X[:,i]), fill_value, X[:,i])
    if dim == 1:
        filled_X = filled_X.flatten()
        X = X.flatten()
    return filled_X
    # 