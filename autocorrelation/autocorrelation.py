def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    correlations = []
    avg = sum(series) / len(series)
    var = sum([(x - avg)**2 for x in series])
    if var == 0:
        correlations = [1.0] + [0.0] * max_lag
        return correlations
        
    for lag in range(max_lag+1):
        r = sum([(series[i] - avg)*(series[i + lag] - avg) for i in range(len(series) - lag)])/var 
        correlations.append(r)
    return correlations
        
        