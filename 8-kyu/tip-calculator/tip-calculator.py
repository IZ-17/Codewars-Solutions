import math
​
def calculate_tip(amount, rating):
    rate = {
        "terrible": 0,
        "poor": 0.05,
        "good": 0.1,
        "great": 0.15,
        "excellent": 0.2
    }
    rating_lower = rating.lower()
    if rating_lower in rate:
        return math.ceil(amount * rate[rating_lower])
    return "Rating not recognised"