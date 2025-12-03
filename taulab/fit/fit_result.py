import numpy as np
import numpy.typing as npt
from collections.abc import Callable
from taulab.datatypes import Measurement
from scipy.odr import Output


class FitResult:
    """Standard dataclass to hold results from a curve fitting operation."""

    def __init__(self, output: Output, function: Callable, measurement: Measurement):
        # params in their order (a0, a1, a2, ...)
        self.params: npt.NDArray[np.float64] = output.beta
        # errors corresponding to each param
        self.error: npt.NDArray[np.float64] = output.sd_beta
        self.covariance: npt.NDArray[np.float64] = output.cov_beta
        self.function: Callable = function
        self.measurement: Measurement = measurement
        self.raw_output: Output = output

    def extrapolate(self, x):
        return self.function(self.params, x)
