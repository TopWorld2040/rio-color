import numpy as np

# The type to be used for all intermediate math
# operations. Should be a float because values will
# be scaled to the range 0..1 for all work.

math_type = np.float32

epsilon = np.finfo(math_type).eps


def to_math_type(arr):
    """Convert an array from native integer dtype range to 0..1
    scaling down linearly
    """
    max_int = np.iinfo(arr.dtype).max
    return arr.astype(math_type) / max_int


def scale_dtype(arr, dtype):
    """Convert an array from 0..1 to dtype, scaling up linearly
    """
    max_int = np.iinfo(dtype).max
    return (arr * max_int).astype(dtype)