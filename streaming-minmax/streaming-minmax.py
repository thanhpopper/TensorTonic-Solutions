import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here
    state = {}
    state["min"] = D * [np.inf]
    state["max"] = D * [-np.inf]
    return state

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    # Write code here
    X_batch = np.array(X_batch)
    for i in range(X_batch.shape[0]):
        state["min"] = np.minimum(state["min"], X_batch[i,:])
        state["max"] = np.maximum(state["max"], X_batch[i,:])
    normalized_batch = (X_batch - state["min"]) / (state["max"] - state["min"] + eps)
    return normalized_batch
    