## assignment.py
"""Lab July 2 — core functions to implement.

Edit *only* the bodies that contain `raise NotImplementedError()`.
Do **not** rename functions: the autograder expects these names.
"""

from __future__ import annotations
from typing import Iterable, Dict, List
import math


def _validate_numeric(nums: Iterable[float]) -> List[float]:
    """Return a concrete list after validating elements are numeric."""
    nums = list(nums)
    if not nums:
        raise ValueError("Input sequence is empty.")
    for x in nums:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Non‑numeric element detected: {x!r}")
    return nums


def mean_loop(nums: Iterable[float]) -> float:
    """Compute arithmetic mean using an explicit *for* loop.

    Args:
        nums: Sequence of int/float values.
    Returns:
        The mean of the inputs.
    """
    raise NotImplementedError


def median_loop(nums: Iterable[float]) -> float:
    """Return the median value without using `statistics` or `numpy`."""
    raise NotImplementedError


def summary_stats(nums: Iterable[float]) -> Dict[str, float]:
    """Return mean, median, min, and max as a dictionary."""
    raise NotImplementedError


def quantile(nums: Iterable[float], q: float) -> float:
    """Compute the *q*‑quantile (0 ≤ q ≤ 1) via linear interpolation."""
    raise NotImplementedError
