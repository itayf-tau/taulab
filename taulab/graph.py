import matplotlib.pyplot as plt

from taulab.datatypes import FitResult


class Graph:
    def __init__(self, fit_result: FitResult):
        self.fit_result = fit_result
        self.measurement = fit_result.measurement

    def plot(
        self,
        x_fit=None,
        ax=None,
        data_label=None,
        fit_label=None,
    ):
        if ax is None:
            _, ax = plt.subplots()
        x_fit = x_fit if x_fit is not None else self.measurement.x

        # Plot data with error bars if available
        if self.measurement.x_err is not None or self.measurement.y_err is not None:
            ax.errorbar(
                self.measurement.x,
                self.measurement.y,
                xerr=self.measurement.x_err,
                yerr=self.measurement.y_err,
                fmt="o",
                label=data_label,
            )
        else:
            ax.plot(self.measurement.x, self.measurement.y, "o", label=data_label)

        # Plot fit result if provided
        y_fit = self.fit_result.extrapolate(x_fit)
        ax.plot(x_fit, y_fit, color="red", label=fit_label)

        if data_label or fit_label:
            ax.legend()

        return ax

    def residuals_plot(self, ax=None, residuals_label=None):
        if ax is None:
            _, ax = plt.subplots()

        # Calculate residuals
        y_fit = self.fit_result.extrapolate(self.measurement.x)
        residuals = self.measurement.y - y_fit

        # Plot residuals
        ax.axhline(0, color="gray", linestyle="--")
        ax.errorbar(
            self.measurement.x,
            residuals,
            yerr=self.measurement.y_err,
            fmt="o",
            label=residuals_label,
        )
        if residuals_label:
            ax.legend()

        return ax
