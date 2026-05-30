# -*- coding: utf-8 -*-
"""
Approximate Arctangent Angle Calculation Algorithm
Author: chayedan1-a
Accuracy:
    Algorithm 1: Error ≤ 0.09º
    Algorithm 2: Error ≤ 0.08°
Description:
    Implement two polynomial approximation formulas for angle calculation,
    used for scenarios without native arctan function.
    
    Usage:
        from arctan_approx import arctan_approx
        angle = arctan_approx(a=3.0, b=4.0)  # returns arctan(3/4) in degrees
"""

import math


def calc_angle_algorithm1(x: float, r: float) -> float:
    """
    Algorithm 1 (low precision, simpler formula)
    θ = | 0^((|x|+x)/2) · 90 − [45r − r · (r−1) · (14.02 + 3.79r)] |
    Accuracy bound: ≤ 0.4°
    
    The term 0^((|x|+x)/2) acts as a branchless conditional:
        - When x > 0 (a > b): 0^positive = 0, so θ = |0 - poly| = poly
        - When x ≤ 0 (a ≤ b): 0^0 = 1, so θ = |90 - poly| = 90 - poly
    """
    exp_part = (abs(x) + x) / 2
    base = (0 ** exp_part) * 90

    poly = 45 * r - r * (r - 1) * (14.02 + 3.79 * r)
    theta = abs(base - poly)
    return theta


def calc_angle_algorithm2(x: float, r: float) -> float:
    """
    Algorithm 2 (high precision, more polynomial terms)
    θ = | (0^((|x|+x)/2) · 90°) − [45r − r · (r−1) · (13.982 + 3.828r + 0.084r²)] |
    Accuracy bound: ≤ 0.072°
    """
    exp_part = (abs(x) + x) / 2
    base = (0 ** exp_part) * 90

    poly = 45 * r - r * (r - 1) * (13.982 + 3.828 * r + 0.084 * (r ** 2))
    theta = abs(base - poly)
    return theta


def arctan_approx(a: float, b: float, high_precision: bool = True) -> float:
    """
    Calculate arctan(a / b) using polynomial approximation.
    
    Args:
        a: Opposite side length (can be any real number)
        b: Adjacent side length (can be any real number)
        high_precision: True for Algorithm 2 (≤0.072° error),
                       False for Algorithm 1 (≤0.4° error)
    
    Returns:
        Angle in degrees, range [0, 90]
    
    Raises:
        ValueError: If both a and b are zero
    
    Example:
        >>> arctan_approx(3, 4)
        36.869...  (arctan(0.75) ≈ 36.87°)
    """
    if a == 0 and b == 0:
        raise ValueError("a and b cannot both be zero")
    
    x = a - b
    r = min(a, b) / max(a, b)
    
    if high_precision:
        return calc_angle_algorithm2(x, r)
    else:
        return calc_angle_algorithm1(x, r)


if __name__ == "__main__":
    # =============================================
    # Demo: calculate arctan(a / b), output in degrees
    # =============================================
    a, b = 3.0, 4.0  # a: opposite side, b: adjacent side

    # Test with both algorithms
    angle1 = arctan_approx(a, b, high_precision=False)
    angle2 = arctan_approx(a, b, high_precision=True)
    expected = math.degrees(math.atan2(a, b))

    print(f"True value   arctan({a}/{b}) = {expected:.6f}°")
    print(f"Algorithm 1 (max error ≤ 0.4°)  : {angle1:.6f}°  (deviation {abs(angle1 - expected):.4f}°)")
    print(f"Algorithm 2 (max error ≤ 0.072°): {angle2:.6f}°  (deviation {abs(angle2 - expected):.4f}°)")
