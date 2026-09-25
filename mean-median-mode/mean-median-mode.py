from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    result = {}
    """
    Returns a dictionary with mean, median, and mode.
    """
    cnt = Counter(x)
    mode = cnt.most_common(1)
    result.update({"mean": float(np.mean(x))})
    result.update({"median": float(np.median(x))})
    result.update({"mode": float(mode[0][0])})
    return result
    pass