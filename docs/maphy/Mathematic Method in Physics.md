# Mathematic Method in Physics

[TOC]

## Part I : Complex Variable Functions 复变函数

### 可导与解析

$f(z)$可导的必要条件：

$$
\begin{aligned}
f'(z) &= \frac{\partial f}{\partial x} = 
\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}\\
&= \frac 1i \frac{\partial f}{\partial y} = 
-i\frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}
\end{aligned}
$$

**Cauchy-Reiman Equation**

$$
\begin{cases}
\displaystyle{\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}} \\
\displaystyle{\frac{\partial u}{\partial y} =-\frac{\partial v}{\partial x}}
\end{cases}
$$

计算二阶微分有：

$$
\begin{aligned}
\nabla^2u &= \frac{\partial^2u}{\partial x^2}+ \frac{\partial^2u}{\partial y^2}\\
&= \frac{\partial}{\partial x}\frac{\partial u}{\partial y} + \frac{\partial}{\partial y}(-\frac{\partial u}{\partial x})\\
&=0
\end{aligned}
$$

同理有：

$$
\nabla^2v = 0
$$

这被称为 **(共轭)调和函数** 

同理还可证：

$$
\nabla^2(uv) =0
$$

---
### 解析复变函数

我们知道

$$
dv = \frac{\partial v}{\partial x}dx + \frac{\partial v}{\partial y}dy =
-\frac{\partial u}{\partial y}dx + \frac{\partial u}{\partial x}dy
$$

可通过积分求解

**Eg1:   $f(z)$解析且$\mathrm{Re} f = u(x,y) = 2xy$, 求$f(z)$**

观察有$dv = -2xdx + 2ydy = d(y^2-x^2)$，于是$v = y^2-x^2+C$

$$
f(z) = 2xy + i(y^2-x^2+C) = -i(x+iy)^2 + iC = -iz^2+iC
$$

---

采取共轭复数的求解：

$$
\begin{cases}
x= \displaystyle{\frac{z+z^*}{2}}\\
y= \displaystyle{\frac{z-z^*}{2i}}
\end{cases}
$$

于是

$$
\frac{\partial f}{\partial z^*} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial z^*} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial z^*} = \frac 12 \frac{\partial f}{\partial x} - \frac{1}{2i}\frac{\partial f}{\partial y} = 0
$$

又有

$$
\begin{aligned}
f(x+iy) &= u(x,y)+iv(x,y)\\
f^*(x-iy) &= u(x,y)-iv(x,y)
\end{aligned}
$$

于是

$$
u(x,y) = \frac{f(x+iy)+f^*(x-iy)}{2}
$$

若令：$x+iy = z, x-iy = 0$，则$x=\frac z2,y = \frac{z}{2i}$

$$
f(z) = 2u(\frac z2,\frac{z}{2i}) -f^*(0)
$$

!!! NOTE

	若函数在0处无定义，可取解析域内$x-iy = z_0$。eg：$u = \frac{x}{x^2+y^2}$

??? warning

	此处的$z$和$z^*$为“形式化推导”的产物，即两者并不存在数量关系（不一定同时等于0）

**Eg2:  $f(z)$解析且已知$u+v$，求$f(z) = u+iv$**
设

$$
F = u+v+\mathrm{Im}(F) = u+iv +v-iu = (1-i)f
$$

---
### 初等函数

**幂函数**

$$
f(z) = z^n,\quad n\in\mathbb{C}
$$

for $n = 1,2,3 ...$,$f(z)$在$\infty$不解析，但在$\mathbb{C}$解析

for $n = -1,-2,-3 ...$, $f(z)$在$\mathbb{C}/0$上解析

**指数函数**

$$
f(z) = e^z
$$

表现为周期函数且$e^x>0\quad if\quad x\in\mathbb{R}$
$e^z+1=0$在$\mathbb{R}$内无解但在$\mathbb{C}$内有无穷多解，since  $e^{i\pi + 2k\pi} = -1$
于是其解$z = i\pi + 2k\pi$

**三角函数**

$$
f(z) = \sin z, \cos z, \tan z, \cot z
$$

对于复数域可能有$|\sin z| > 1$
由欧拉公式我们有：

$$
\begin{aligned}
\sin z &= \frac{e^{iz} - e^{-iz}}{2i} \\
\cos z &= \frac{e^{iz} + e^{-iz}}{2}
\end{aligned}
$$

双曲函数形式：

$$
\begin{aligned}
\sinh z &= \frac{e^z - e^{-z}}{2} \\
\cosh z &= \frac{e^z + e^{-z}}{2}
\end{aligned}
$$

若要讨论函数在无穷远点的性质，取变量替换$t = \frac 1z$

**本性奇点**：既非极点，也不可去。eg：

$$
e^{1/z} \quad for \quad z=0
\
$$

---

### 多值函数

讨论函数：

$$
\begin{aligned}
w &= \sqrt{z-a}\\
w^2 &= z-a
\end{aligned}
$$

若令$w = \rho e^{i\phi}$, $z-a = r e^{i\theta}$

$$
\rho^2 e^{i2\phi} = re^{i\theta}
$$

于是

$$
\begin{cases}
r = \sqrt{\rho}\\
\theta = 2\phi + 2k\pi
\end{cases}
$$

即为$\mathrm{arg}(\sqrt{z-a}) = \frac 12 \mathrm{arg}(z-a)$