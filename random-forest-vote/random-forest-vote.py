import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.array(predictions)
    trees, samples = predictions.shape
    major_vote = []
    for sample in range(samples):
        counts = np.bincount(predictions[:, sample].ravel())
        major_vote.append(np.argmax(counts))
    return major_vote
        