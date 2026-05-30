# arctan-approx
Arctan Approximation Algorithm
**Author: chayedan1-a**

## Overview
A low-computation-cost fast approximation of the arctangent function (output in degrees), designed for real-time applications such as games and embedded systems.

## Definition
Given:
- $a$ = $|opposite side (focus)|=|X-axis|$
- $b$ = $|adjacent side|=|Y-axis|$
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

- $a$ = $opposite side=X-axis$
- $b$ = $adjacent side=Y-axis$
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

$C = \Bigl[360 \cdot \bigl(A \cdot 0.5 + (1 - A) \cdot B\bigr)\Bigr] + \Bigl[(p + 0^{|p|}) \cdot q \cdot v\Bigr]$

---

### III. Interpreters (Coordinate System Conversion) & Modules

**Third-Order Interpreter (Optional):**

$C - 0^{|C-180| - (C-180)} \cdot 360$

- **Description:** Folds the angle to $\pm 180^\circ$.

**Second-Order Interpreter (Compass Angle, Optional):**

$90 - C + 360$
Note: Variable C must output the mathematical angle for this to work.

**Second-Order Mapper**

$360 * ( A * 0.5 + (1 - A) * B )$

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

- **Discriminator vs. Mapper Mode Switching**:
Mapper:360 * ( **A** * 0.5 + (1 - **A**) * **B** )
Discriminator:0^[(|x| **+** x) / 2]
(The symbol inside '**+**','**AAB**' can be switched to '**-**','**BBA**' to change logic)

When Argument order'**AAB**''**+**' is used with $a=x, b=y$:
It outputs the mathematical angle.
That is, under this condition, '**AAB**''**+**' is equivalent to $atan2(y, x)$.
Invariantly, AAB+ is always equal to atan2(b, a).

When '**BBA**''**-**' is used with $a=x, b=y$:
It outputs the compass angle.
That is, under this condition, '**BBA**''**-**' is equivalent to $atan2(x, y)$.
Invariantly, BBA- is always equal to atan2(a, b).

---
If the axes are swapped (i.e., $a=y-axis$, $b=x-axis$):

When Argument order'**AAB**''**+**' is used with $a=y, b=x$:
It outputs the compass angle.
That is, under this condition, '**AAB**''**+**' is equivalent to $atan2(x, y)$.
Invariantly, AAB+ is always equal to atan2(b, a).

When '**BBA**''**-**' is used with $a=y, b=x$:
It outputs the mathematical angle.
That is, under this condition, '**BBA**''**-**' is equivalent to $atan2(y, x)$.
Invariantly, BBA- is always equal to atan2(a, b).

---

### VI. Performance Specifications

- **Accuracy:** $\le 0.09^\circ$, converges to exact values at extreme ratios
- **Speed:** Very fast (based on special power operations)
- **Efficiency:** Extremely high (branchless architecture)
- **Storage:** Byte-level footprint
- **Stability:** Tested without issues
- **Limitation:** Depends on $0^0 = 1$ (only weakness; natively compatible with Python, Lua)

## Original text without Markdown formatting

Proximal Fitting Form

I. Definition

a = opposite side =x-axis
b = adjacent side =y-axis
x = |a| - |b| -- first-order angle discriminator
r = min(|a|, |b|) / max(|a|, |b|) -- input ratio

---

II. Core Formulas

First-Order Processor
v = | 0^[(|x| + x) / 2] * 90 - [ 45r - r(r-1)(13.982 + 4.02r) ] |
Function: Polynomial angle approximation, output range 0 ~ 90 degrees.

Second-Order Full-Quadrant Definition (Sign Conversion)
p = 0^(|b|-b) - 0^(|b|+b)
q = 0^(|a|-a) - 0^(|a|+a)
Purpose: Convert the signs of a and b to -1, 0, or 1.

In-place Correction
p = p + 0^(|p|) * q
q = q + 0^(|q|) * p

(The following p and q are the corrected values.)
Convert to 0 or 1
A = 0^(q + |q|)
B = 0^(p + |p|)

Second-Order Full-Quadrant Mapper
C = [ 360 * ( A * 0.5 + (1 - A) * B ) ] + [ (p + 0^|p|) * q * v ]

---

III. Interpreters (Coordinate System Conversion) & Modules

Third-Order Interpreter (Optional):
C - 0^(|C-180| - (C-180)) * 360
Description: Folds the angle to ±180 degrees.

Second-Order Interpreter (Compass Angle, Optional):
90 - C + 360

Second-Order Mapper

360 * ( A * 0.5 + (1 - A) * B )

First-Order Discriminator:
0^[(|x| + x) / 2]

Zero-Order Protector (Optional):
0^(|a|+|b|)

---

IV. Configuration for Output Coordinate Systems

Mathematical Coordinates (0 ~ 360):
First-Order Discriminator: +, Interpreter: None required

Compass Angle (0 ~ 360):
First-Order Discriminator: -, Second-Order Interpreter: Required

Folded Angle (±180):
Third-Order Interpreter: Required

---

V. Protector & Discriminator Usage

When a = b = 0, direct calculation returns 180.

Modified r (to prevent division by zero):
r = min(|a|, |b|) / ( max(|a|, |b|) + 0^(|a|+|b|) )

To return 0 instead of 180 for (0, 0):
0^(0^(|a|+|b|)) * C

- **Discriminator vs. Mapper Mode Switching**:
Mapper:360 * ( **A** * 0.5 + (1 - **A**) * **B** )
Discriminator:0^[(|x| **+** x) / 2]
(The symbol inside '**+**','**AAB**' can be switched to '**-**','**BBA**' to change logic)

When Argument order'AAB''+' is used with a=x, b=y:
It outputs the mathematical angle.
That is, under this condition, 'AAB''+' is equivalent to atan2(y, x).
Invariantly, AAB+ is always equal to atan2(b, a).

When 'BBA''-' is used with a=x, b=y:
It outputs the compass angle.
That is, under this condition, 'BBA''-' is equivalent to atan2(x, y).
Invariantly, BBA- is always equal to atan2(a, b).

---
If the axes are swapped (i.e., a=y-axis, b=x-axis):

When Argument order'AAB''+' is used with a=y, b=x:
It outputs the compass angle.
That is, under this condition, 'AAB''+' is equivalent to atan2(x, y).
Invariantly, AAB+ is always equal to atan2(b, a).

When 'BBA''-' is used with a=y, b=x:
It outputs the mathematical angle.
That is, under this condition, 'BBA''-' is equivalent to atan2(y, x).
Invariantly, BBA- is always equal to atan2(a, b).
---

VI. Performance Specifications

Accuracy: ≤ 0.09°, converges to exact values at extreme ratios
Speed: Very fast (based on special power operations)
Efficiency: Extremely high (branchless architecture)
Storage: Byte-level footprint
Stability: Tested without issues
Limitation: Depends on 0^0 = 1 (only weakness; natively compatible with Python, Lua)

## Chinese 中文

**近态拟合式**
一、定义

a = 对边 = x轴
b = 邻边 = y轴
x = |a| - |b| -- 一阶角度判断器
r = min(|a|, |b|) / max(|a|, |b|) -- 输入比例

---

二、核心公式

一阶处理器
v = | 0^[(|x| + x) / 2] * 90 - [ 45r - r(r-1)(13.982 + 4.02r) ] |
功能：多项式角度逼近，输出范围 0 ~ 90 度。

二阶全象限定义（符号转换）
p = 0^(|b|-b) - 0^(|b|+b)
q = 0^(|a|-a) - 0^(|a|+a)
作用：将 a、b 的符号转换为 -1、0、1。

原地修正
p = p + 0^(|p|) * q
q = q + 0^(|q|) * p

（以下 p、q 均为修正后的值。）

转换为 0 或 1
A = 0^(q + |q|)
B = 0^(p + |p|)

二阶全象限映射器
C = [ 360 * ( A * 0.5 + (1 - A) * B ) ] + [ (p + 0^|p|) * q * v ]

---

三、解释器（坐标系转换）与模块

三阶解释器（可选）：
C - 0^(|C-180| - (C-180)) * 360
说明：将角度折叠至 ±180 度。

二阶解释器（罗盘角，可选）：
90 - C + 360
—若需使用则变量C需要为输出数学角

二阶映射器
360 * ( A * 0.5 + (1 - A) * B )

一阶判断器：
0^[(|x| + x) / 2]

零阶保护器（可选）：
0^(|a|+|b|)

---

四、输出坐标系配置

数学坐标（0 ~ 360）：
一阶判断器：+，无需解释器

罗盘角（0 ~ 360）：
一阶判断器：-，无需解释器

折叠角（±180）：
三阶解释器必装

---

五、保护器与判断器用法

当 a = b = 0 时，直接计算返回 180。

修正 r（防止除零）：
r = min(|a|, |b|) / ( max(|a|, |b|) + 0^(|a|+|b|) )

若 (0, 0) 需返回 0 而非 180（依然要使用零阶保护器，否则(a=b=0)时r返回NaN）：
0^(0^(|a|+|b|)) * C

---

判断器与映射器模式切换：

映射器：360 * ( A * 0.5 + (1 - A) * B )
判断器：0^[(|x| + x) / 2]
（**+**、**AAB** 内部的符号可切换为 **-**、**BBA** 以改变逻辑）

当参数顺序 'AAB' '+' 配合 a=x, b=y 使用时：
输出数学角。
即此条件下，'AAB' '+' 等价于 atan2(y, x)。
不变性：AAB+ 始终等于 atan2(b, a)。

当 'BBA' '-' 配合 a=x, b=y 使用时：
输出罗盘角。
即此条件下，'BBA' '-' 等价于 atan2(x, y)。
不变性：BBA- 始终等于 atan2(a, b)。

---
若坐标轴交换（即 a=y轴, b=x轴）：

当参数顺序 'AAB' '+' 配合 a=y, b=x 使用时：
输出罗盘角。
即此条件下，'AAB' '+' 等价于 atan2(x, y)。
不变性：AAB+ 始终等于 atan2(b, a)。

当 'BBA' '-' 配合 a=y, b=x 使用时：
输出数学角。
即此条件下，'BBA' '-' 等价于 atan2(y, x)。
不变性：BBA- 始终等于 atan2(a, b)。

---

六、性能指标

精度：≤ 0.09°，极端比值下收敛接近至精确值
速度：极快（基于特殊幂运算）
效率：极高（无分支架构）
存储：字节级占用
稳定性：经测试无问题
限制：依赖 0^0 = 1（唯一弱点；Python、Lua 原生兼容）

## License
Apache License 2.0
