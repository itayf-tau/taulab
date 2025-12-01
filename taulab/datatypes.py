import numpy as np
import pandas as pd
import numpy.typing as npt
from dataclasses import dataclass
from collections.abc import Callable


@dataclass
class Measurement:
    x: npt.NDArray[np.float64]
    y: npt.NDArray[np.float64]
    x_err: npt.NDArray[np.float64] | None = None
    y_err: npt.NDArray[np.float64] | None = None


@dataclass
class FitResult:
    """Standard dataclass to hold results from a curve fitting operation."""

    params: npt.NDArray[np.float64]  # params in their order (a0, a1, a2, ...)
    error: npt.NDArray[np.float64]  # errors corresponding to each param
    covariance: npt.NDArray[np.float64]
    function: Callable
    measurement: Measurement

    def extrapolate(self, x):
        return self.function(self.params, x)


@dataclass
class ParseResult:
    data: pd.DataFrame
    metadata: dict


@dataclass
class PhysicalSize:
    value: float
    uncertainty: float
