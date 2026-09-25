import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    
    
    
    return {
        "variance": float(np.var(x, ddof=1)),
        "standard_deviation": float(np.std(x, ddof=1)) 
        #ddof = 0 mean cal for population or random variable
        #ddof = 1 mean cal for sample 
    }
    pass