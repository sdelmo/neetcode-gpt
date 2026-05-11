import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        
        # Subtract maximum value from all elements before computing
        # This prevents overflow when input values are large
        mx_z = np.max(z)

        sf_mx = np.round(((np.exp(z-mx_z) / (np.sum(np.exp(z-mx_z))))), 4)

        return sf_mx
