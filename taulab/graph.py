import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

from taulab.datatypes import FitResult


class Graph:
    def __init__(
        self,
        fit_result: FitResult,
        x_data: npt.NDArray[np.float64],
        y_data: npt.NDArray[np.float64],
        x_err: npt.NDArray[np.float64] | None = None,
        y_err: npt.NDArray[np.float64] | None = None,
    ):
        self.fit_result = fit_result
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.x_err = np.array(x_err) if x_err is not None else None
        self.y_err = np.array(y_err) if y_err is not None else None

    def plot(
        self,
        x_fit=None,
        ax=None,
        data_label=None,
        fit_label=None,
    ):
        if ax is None:
            _, ax = plt.subplots()
        x_fit = x_fit if x_fit else self.x_data

        # Plot data with error bars if available
        if self.x_err is not None or self.y_err is not None:
            ax.errorbar(
                self.x_data,
                self.y_data,
                xerr=self.x_err,
                yerr=self.y_err,
                fmt="o",
                label=data_label,
            )
        else:
            ax.plot(self.x_data, self.y_data, "o", label=data_label)

        # Plot fit result if provided
        y_fit = self.fit_result.extrapolate(x_fit)
        ax.plot(x_fit, y_fit, color="red", label=fit_label)

        ax.legend()

        return ax

    def residuals_plot(self, ax=None, residuals_label=None):
        if ax is None:
            _, ax = plt.subplots()

        # Calculate residuals
        y_fit = self.fit_result.extrapolate(self.x_data)
        residuals = self.y_data - y_fit

        # Plot residuals
        ax.axhline(0, color="gray", linestyle="--")
        ax.errorbar(
            self.x_data,
            residuals,
            yerr=self.y_err,
            fmt="o",
            label=residuals_label,
        )
        ax.legend()

        return ax
