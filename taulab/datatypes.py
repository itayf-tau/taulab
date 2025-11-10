import numpy.typing as npt
import pandas as pd
from dataclasses import dataclass


@dataclass
class FitResult:
    """Standard dataclass to hold results from a curve fitting operation."""

    params: npt.ArrayLike  # params in their order (a0, a1, a2, ...)
    error: npt.ArrayLike  # errors corresponding to each param
    covariance: npt.ArrayLike


@dataclass
class ParseResult:
    data: pd.DataFrame
    metadata: dict | None = None
