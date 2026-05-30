# arctan-approx
Arctan Approximation Algorithm
**Author: chayedan1-a**

## Overview
A low-computation-cost fast approximation of the arctangent function (output in degrees), designed for real-time applications such as games and embedded systems.

## Definition
Given:
- $a$ = $|opposite side (focus)|$
- $b$ = $|adjacent side|$
- $x = a - b$
- $r = \dfrac{\min(a,b)}{\max(a,b)}$

> **Note**: The algorithm is defined for $(a, b) \neq (0, 0)$, which means $a$ and $b$ cannot both be zero.

## Core Formula
### Algorithm 1
Accuracy bound: $\le 0.09^\circ$
$$\theta = \left| 0^{\frac{|x|+x}{2}} \cdot 90 - \Bigl[45r - r \cdot (r-1) \cdot (14.02 + 3.79r)\Bigr] \right|$$

### Algorithm 2
Accuracy bound: $\le 0.08^\circ$
$$\theta = \left| \left( 0^{\frac{|x|+x}{2}} \cdot 90^\circ \right) - \Bigl[45r - r \cdot (r-1) \cdot (13.982 + 3.828r + 0.084r^2)\Bigr] \right|$$

### Important Notes on Behavior
1. The formula as written is equivalent to $\arctan(b/a)$.  
   To match the standard definition $\arctan(a/b)$, replace $\dfrac{|x|+x}{2}$ with $\dfrac{|x|-x}{2}$ in the exponent.

2. The expression $0^{\frac{|x|+x}{2}}$ relies on the language's handling of $0^0$:
   - If your language defines $0^0 = 1$ (e.g., Lua), the formula works as written.
   - If your language does not support $0^0 = 1$, remove the exponent term and use conditional judgment:
     - If $a \ge b$: use $\left| 0 - \bigl(45r - r(r-1)(14.02+3.79r)\bigr) \right|$
     - If $a < b$: use $\left| 90 - \bigl(45r - r(r-1)(14.02+3.79r)\bigr) \right|$

## Usage
1. Ensure $(a, b) \neq (0, 0)$.
2. Compute $r = \dfrac{\min(a,b)}{\max(a,b)}$.
3. Substitute into the formula above (or use the conditional form if needed).
4. The result is the approximated angle $\theta$ in degrees.

# On Algorithms: Proximal Fitting Form

## Proximal Fitting Form

### I. Definition

- $a$ = $opposite side$
- $b$ = $adjacent side$
- $x = |a| - |b|$ — first-order angle discriminator
- $r = \dfrac{\min(|a|,|b|)}{\max(|a|,|b|)}$ — input ratio

---

### II. Core Formulas

**First-Order Processor**

$v = \left| 0^{\frac{|x| + x}{2}} \cdot 90 - \Bigl[45r - r \cdot (r-1) \cdot (13.982 + 4.02r)\Bigr] \right|$

- **Function:** Polynomial angle approximation, output range $0 \sim 90^\circ$.

**Second-Order Full-Quadrant Definition (Sign Conversion)**

$p = 0^{|b|-b} - 0^{|b|+b}$
$q = 0^{|a|-a} - 0^{|a|+a}$

- **Purpose:** Convert the signs of $a$ and $b$ to $-1$, $0$, or $1$.

**In-place Correction**

$p = p + 0^{|p|} \cdot q$
$q = q + 0^{|q|} \cdot p$

*(The following $p$ and $q$ are the corrected values.)*

**Convert to $0$ or $1$**

$A = 0^{q + |q|}$
$B = 0^{p + |p|}$

**Second-Order Full-Quadrant Mapper**

$C = \Bigl[360 \cdot \bigl(B \cdot 0.5 + (1 - B) \cdot A\bigr)\Bigr] + \Bigl[(p + 0^{|p|}) \cdot q \cdot v\Bigr]$

---

### III. Interpreters (Coordinate System Conversion) & Modules

**Third-Order Interpreter (Optional):**

$C - 0^{|C-180| - (C-180)} \cdot 360$

- **Description:** Folds the angle to $\pm 180^\circ$.

**Second-Order Interpreter (Compass Angle, Optional):**

$90 - C + 360$

**First-Order Discriminator:**

$0^{\frac{|x| + x}{2}}$

**Zero-Order Protector (Optional):**

$0^{|a|+|b|}$

---

### IV. Configuration for Output Coordinate Systems

- **Mathematical Coordinates ($0 \sim 360^\circ$):**
  First-Order Discriminator: $-$, Interpreter: None required

- **Compass Angle ($0 \sim 360^\circ$):**
  First-Order Discriminator: $-$, Second-Order Interpreter: Required

- **Folded Angle ($\pm 180^\circ$):**
  Third-Order Interpreter: Required

---

### V. Protector & Discriminator Usage

- When $a = b = 0$, direct calculation returns $180$.

- **Modified $r$ (to prevent division by zero):**

$r = \dfrac{\min(|a|,|b|)}{\max(|a|,|b|) + 0^{|a|+|b|}}$

- **To return $0$ instead of $180$ for $(0, 0)$:**

$0^{0^{|a|+|b|}} \cdot C$

- **Discriminator symbol switching:**

$0^{\frac{|x| + x}{2}}$

(The symbol inside $+$ can be switched to $-$ to change logic: $-$ corresponds to atan2(a, b), $+$ corresponds to atan2(b, a).)

---

### VI. Performance Specifications

- **Accuracy:** $\le 0.09^\circ$, converges to exact values at extreme ratios
- **Speed:** Very fast (based on special power operations)
- **Efficiency:** Extremely high (branchless architecture)
- **Storage:** Byte-level footprint
- **Stability:** Tested without issues
- **Limitation:** Depends on $0^0 = 1$ (only weakness; natively compatible with Python, Lua)

## License
Apache License 2.0
