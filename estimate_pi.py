import numpy as np

def estimate_pi(num_samples):
    points = np.random.rand(num_samples,2)
    x = points[:,0]
    y = points[:,1]
    ds = x*x + y*y
    inside = 0
    for value in ds:
        if value <=1:
            inside +=1
    pi_hat = 4*inside/num_samples
    return float(pi_hat)
    

