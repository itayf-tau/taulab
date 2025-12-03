import numpy as np
import numpy.typing as npt
import scipy.stats
from collections.abc import Callable
from taulab.datatypes import Measurement
from scipy.odr import Output


class FitResult:
    """Standard dataclass to hold results from a curve fitting operation."""

    def __init__(self, output: Output, function: Callable, measurement: Measurement):
        # params in their order (a0, a1, a2, ...)
        self._params: npt.NDArray[np.float64] = output.beta
        # errors corresponding to each param
        self._error: npt.NDArray[np.float64] = output.sd_beta
        self._covariance: npt.NDArray[np.float64] = output.cov_beta
        self._function: Callable = function
        self._raw_output: Output = output
        self._measurement: Measurement = measurement

    @property
    def params(self) -> npt.NDArray[np.float64]:
        return self._params.copy()

    @property
    def error(self) -> npt.NDArray[np.float64]:
        return self._error.copy()

    @property
    def measurement(self) -> Measurement:
        return self._measurement

    def extrapolate(self, x):
        return self._function(self._params, x)

    def params_report(self):
        lines = []
        lines.append("Fit Parameters:")
        for i, (param, err) in enumerate(zip(self._params, self._error)):
            lines.append(
                f"  a{i}: {param:.6g} ± {err:.6g} ({((err / param) * 100):.2g}%)"
            )
        return "\n".join(lines)

    def metrics_report(self):
        lines = []
        dof = len(self.measurement.x) - len(self._params)
        chi2_red = self._raw_output.sum_square / dof  # type: ignore
        p_value = scipy.stats.chi2.sf(chi2_red, dof)
        lines.append(f"Degrees of Freedom: {dof}")
        lines.append(f"Reduced Chi-Squared: {chi2_red:.6g}")
        lines.append(f"P-Value: {p_value:.6g}")
        return "\n".join(lines)

    def __str__(self) -> str:
        return f"{self.metrics_report()}\n\n{self.params_report()}"

    def print(self) -> None:
        print(self.__str__())
