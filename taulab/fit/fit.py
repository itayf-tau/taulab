import numpy.typing as npt
import numpy as np
from scipy.odr import Model, ODR, RealData
from taulab.datatypes import FitResult, Measurement


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

    fit_params = output.beta
    fit_params_err = output.sd_beta
    fit_cov = output.cov_beta
    measurement = Measurement(
        x=np.array(x_data),
        y=np.array(y_data),
        x_err=np.array(x_err),
        y_err=np.array(y_err),
    )
    return FitResult(fit_params, fit_params_err, fit_cov, fit_func, measurement)
