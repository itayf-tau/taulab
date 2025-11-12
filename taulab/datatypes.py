import numpy.typing as npt
import pandas as pd
from dataclasses import dataclass
from collections.abc import Callable


@dataclass
class FitResult:
    """Standard dataclass to hold results from a curve fitting operation."""
    params: npt.ArrayLike  # params in their order (a0, a1, a2, ...)
    error: npt.ArrayLike  # errors corresponding to each param
    covariance: npt.ArrayLike
    function: Callable

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
