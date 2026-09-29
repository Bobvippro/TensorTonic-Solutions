import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = 0
    probabilitis = [
        math.comb(n, i) * p**i * (1-p)**(n-i) 
        for i in range(k+1)
    ]    
    return {
        "pmf": float(probabilitis[k]),
        "cdf": float(sum(probabilitis))
        
    }
    
    pass