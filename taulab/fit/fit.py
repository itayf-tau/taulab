import numpy.typing as npt
import numpy as np
from scipy.odr import Model, ODR, RealData
from taulab.datatypes import Measurement
from taulab.fit.fit_result import FitResult


def odr_fit(
    fit_func,
    init_values,
    x_data: npt.ArrayLike,
    x_err: npt.ArrayLike,
    y_data: npt.ArrayLike,
    y_err: npt.ArrayLike,
) -> FitResult:
    model = Model(fit_func)
    odr_data = RealData(x_data, y_data, sx=x_err, sy=y_err)
    odr = ODR(odr_data, model, beta0=init_values)
    output = odr.run()

    measurement = Measurement(
        x=np.array(x_data),
        y=np.array(y_data),
        x_err=np.array(x_err),
        y_err=np.array(y_err),
    )
    return FitResult(output, fit_func, measurement)
