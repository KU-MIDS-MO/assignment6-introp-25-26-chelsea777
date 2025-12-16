import numpy as np
def random_unit_vectors(num_vectors, dim):
    m = np.random.randn(num_vectors,dim)
    norms = np.linalg.norm(m,axis = 1)
    u = m/norms[:,np.newaxis]
    return u
