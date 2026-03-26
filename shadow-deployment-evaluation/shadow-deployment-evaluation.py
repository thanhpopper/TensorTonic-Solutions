import math
def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    ## initialize metrics
    promotion = {}
    metrics = {}
    accuracy_count_shadow = 0
    accuracy_count_prod = 0
    agreement_count = 0
    
    latency_shadow = []
    #latency_prod = []    

    n = len(shadow_log)

    for s, p in zip(shadow_log, production_log):
        if s["actual"] == s["prediction"]:
            accuracy_count_shadow += 1
        if p["actual"] == p["prediction"]:
            accuracy_count_prod += 1
        if s["prediction"] == p["prediction"]:
            agreement_count += 1
        latency_shadow.append(s["latency_ms"])

    # Accuracy
    metrics["shadow_accuracy"] = accuracy_count_shadow / n
    metrics["production_accuracy"] = accuracy_count_prod / n
    metrics["accuracy_gain"] = metrics["shadow_accuracy"] - metrics["production_accuracy"]

    #Agreement
    metrics["agreement_rate"] = agreement_count / n

    #latency
    metrics["shadow_latency_p95"] = sorted(latency_shadow)[math.ceil(0.95 * n) - 1]
    #max_latency_p95 = latency_prod.sort[ceil(0.95 * n) - 1]

    # Conditions for deployment of shadow
    cond1 = (metrics["accuracy_gain"] >= criteria["min_accuracy_gain"])
    cond2 = (metrics["shadow_latency_p95"] <= criteria["max_latency_p95"])
    cond3 = (metrics["agreement_rate"] >= criteria["min_agreement_rate"])

    if cond1 & cond2 & cond3:
        promotion["promote"] = True
    else: 
        promotion["promote"] = False
    promotion["metrics"] = metrics

    return promotion
            
            
            
    