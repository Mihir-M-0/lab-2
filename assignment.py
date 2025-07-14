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
    total = 0.0
    nums = _validate_numeric(nums)
    length = len(nums)
    if length == 0:
        raise ValueError

    else:
        for i in range(length):
            total += nums[i]
        return total/length




def median_loop(nums: Iterable[float]) -> float:
    """Return the median value without using `statistics` or `numpy`."""
    
    nums = _validate_numeric(nums)
    length = len(nums)
    if length == 0:
        raise ValueError
    nums.sort()
    if(length %2 == 0):
        half = length//2
        sumOne = nums[half -1]
        sumTwo = nums[half]
        total = sumOne + sumTwo
        return total/2
    else:
        half = (length//2)
        return nums[half]
   


def summary_stats(nums: Iterable[float]) -> Dict[str, float]:
    """Return mean, median, min, and max as a dictionary."""
    collection = {}
    nums = _validate_numeric(nums)
    length = len(nums)
    if(length == 0):
        raise ValueError
    else:
        nums.sort()
        mean = mean_loop(nums)
        collection["mean"] = mean
        median = median_loop(nums)
        collection["median"] = median
        collection["min"] = nums[0]
        collection["max"] = nums[length - 1]
        return collection





def quantile(nums: Iterable[float], q: float) -> float:
    """Compute the *q*‑quantile (0 ≤ q ≤ 1) via linear interpolation."""
    nums = _validate_numeric(nums)
    length = len(nums)
    if(length == 0):
        raise ValueError
    
    else:
        nums.sort()
        index = (length - 1) * q
        print(index)
        if index == int(index):
            index = int(index)
            return nums[index]
        else:
            lower = int(index)
            higher = min(lower + 1, length - 1)
            fraction = (length - 1) * q - lower
            return (1-fraction) * nums[lower] + fraction * nums[higher]


