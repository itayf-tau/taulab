import math
from taulab.datatypes import PhysicalSize

QuantityLike = PhysicalSize | tuple[float, float]


def nsigma(v1: QuantityLike, v2: QuantityLike):
    if isinstance(v1, tuple):
        v1 = PhysicalSize(*v1)
    if isinstance(v2, tuple):
        v2 = PhysicalSize(*v2)
    return abs(v1.value - v2.value) / math.sqrt(v1.uncertainty**2 + v2.uncertainty**2)
