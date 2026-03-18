import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X)
    filled_X = np.zeros_like(X)
    if X.ndim == 1:
        if strategy == 'mean':
            fill_value = np.nanmean(X)
        else:    
            fill_value = np.nanmedian(X)
        filled_X = np.where(np.isnan(X), fill_value, X)
        return filled_X
    # Calculate mean of each Feature column
    for i in range(X.shape[1]):
        if np.isnan(X[:,i]).all():
            continue
        if strategy == 'mean':
            fill_value = np.nanmean(X[:,i])
        else:    
            fill_value = np.nanmedian(X[:,i])
        filled_X[:,i] = np.where(np.isnan(X[:,i]), fill_value, X[:,i])
    return filled_X
    # 