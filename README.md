# arctan-approx
Arctan Approximation Algorithm

## Overview
A low-computation-cost fast approximation of the arctangent function (output in degrees), designed for real-time applications such as games and embedded systems.

## Definition
Given:
- $a$: opposite side (focus)
- $b$: adjacent side
- $x = a - b$
- $r = \dfrac{\min(a,b)}{\max(a,b)}$

> **Note**: The algorithm is defined for $a, b \neq 0$.

## Core Formula
$$
\theta = \left|
0^{\frac{|x|+x}{2}} \cdot 90
- \bigl(45r - r(r-1)(14.02 + 3.79r)\bigr)
\right|
$$

### Important Notes on Behavior
1. The formula as written is equivalent to $\arctan(b/a)$.  
   To match the standard definition $\arctan(a/b)$, replace $\dfrac{|x|+x}{2}$ with $\dfrac{|x|-x}{2}$ in the exponent.

2. The expression $0^{\frac{|x|+x}{2}}$ relies on the language's handling of $0^0$:
   - If your language defines $0^0 = 1$ (e.g., Lua), the formula works as written.
   - If your language does not support $0^0 = 1$, remove the exponent term and use conditional judgment:
     - If $a \ge b$: use $\left| 0 - \bigl(45r - r(r-1)(14.02+3.79r)\bigr) \right|$
     - If $a < b$: use $\left| 90 - \bigl(45r - r(r-1)(14.02+3.79r)\bigr) \right|$

## Usage
1. Ensure $a, b \neq 0$.
2. Compute $r = \dfrac{\min(a,b)}{\max(a,b)}$.
3. Substitute into the formula above (or use the conditional form if needed).
4. The result is the approximated angle $\theta$ in degrees.

## License
Apache License 2.0
