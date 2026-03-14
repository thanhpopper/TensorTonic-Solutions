import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if x.ndim == 3:
        GAP = np.mean(x, axis=(1,2))
    else:
        GAP = np.mean(x, axis=(2,3))
    return GAP
            