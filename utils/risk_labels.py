def risk_label(prob: float):
    if prob < 0.20:
        return "Low", "green"
    elif prob < 0.40:
        return "Medium", "orange"
    else:
        return "High", "red"