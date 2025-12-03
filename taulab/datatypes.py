import numpy as np
import pandas as pd
import numpy.typing as npt
from dataclasses import dataclass


@dataclass
class Measurement:
    x: npt.NDArray[np.float64]
    y: npt.NDArray[np.float64]
    x_err: npt.NDArray[np.float64] | None = None
    y_err: npt.NDArray[np.float64] | None = None


@dataclass
class ParseResult:
    data: pd.DataFrame
    metadata: dict


@dataclass
class PhysicalSize:
    value: float
    uncertainty: float
