def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    hits = set(recommended[:k]).intersection(relevant)
    precision = len(hits) / k
    recall = len(hits) / len(relevant)
    return [precision, recall]
    