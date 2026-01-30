# 微积分概要

> 说明：这份资料本质上是**对结论的总结**，供快速阅览和查找用。不适合任何形式的高等数学考试。

## 1. 极限与导数

### Stolz定理

若数列 $\{a_n\}$ 和 $\{b_n\}$ 满足：

- $\displaystyle \lim_{n\to+\infty} b_n = \infty$ 且 $\{b_n\}$ 严格单调递增
- $\displaystyle \lim_{n\to+\infty} a_n = \infty$

或者满足：

- $\displaystyle \lim_{n\to+\infty} b_n = 0$ 且 $\{b_n\}$ 严格单调递减
- $\displaystyle \lim_{n\to+\infty} a_n = 0$

则：

$$
\lim_{n\to\infty} = \frac{a_n - a_{n-1}}{b_n - b_{n-1}} = L\quad \Rightarrow \quad \lim_{n\to\infty} = \frac{a_n}{b_n}
$$

> 相当于是离散版本的L' Hospital定理。

---

### 一阶导数的传递性质

$$
\dv{y}{x} = \dv{y}{u}\dv{u}{x} \qc \dv{x}{y} = \frac{1}{\dv{y}{x}}
$$

> 一阶导数可以类似于商进行传递，但二阶导数不行。

---

### 高阶导数（Leibniz 公式）

$$
(f(x)g(x))^{(n)}(x) = \sum_{k=0}^n \mqty(k\\n) f^{(k)}(x)g^{(n-k)}(x)
$$

---

## 2. 单变量积分

### 分部积分

$$
\int u\dd v = vu - \int v \dd u
$$

---

### 幂函数的Taylor展开

$$
(1+x)^\alpha = \sum_{k=0}^\infty \mqty(\alpha\\k)x^k
$$

> 常结合柯西乘积：
>
> $$
> \pqty{\sum_{n=0}^\infty a_nx^n}\pqty{\sum_{n=0}^\infty b_nx^n} = \sum_{n=0}^{\infty}\pqty{\sum_{k=0}^n a_k b_{n-k}}x^n
> $$

---

## 3. 多变量积分

### 偏导的可交换性

$$
\pdv[2]{f}{x}{y} = \pdv[2]{f}{y}{x}
$$

---

### 梯度，散度，旋度

$$
\begin{gathered}
\grad f(x,y,z) = \pqty{\pdv{f}{x} , \pdv{f}{y}, \pdv{f}{z}} \\
\div \vb f(x,y,z) = \pdv{f_x}{x} + \pdv{f_y}{y}+ \pdv{f_z}{z}\\
\curl \vb f(x,y,z) = \mqty|i&j&k\\\pdv{x}&\pdv{y}&\pdv{z}\\f_x&f_y&f_z|
\end{gathered}
$$

---

### 二阶Taylor展开

$$
f(x,y) = \sum_{n=0}^\infty \frac{1}{n!}\pqty{\Delta x\pdv{x}+\Delta y\pdv{y}}^n f(x_0,y_0)
$$

---

### 隐函数问题

对于写成隐函数 $F(x,y) = 0$ 的函数 $y = f(x)$ 求导有：

$$
f'(x) = -\frac{\partial_xF(x,y)}{\partial_yF(x,y)}
$$

其中，隐函数存在的条件是 $\partial_y F(x,y) \neq 0$ 。

如果对于方程组：

$$
\begin{cases}
F_1(x,u,v) = 0 \\
F_2(x,u,v) = 0
\end{cases}
$$

则需要分别求偏导得到：

$$
\begin{cases}
\pdv{F_1}{x} + \pdv{F_1}{u}u'(x) + \pdv{F_1}{v}v'(x) = 0 \\
\pdv{F_2}{x} + \pdv{F_2}{u}u'(x) + \pdv{F_2}{v}v'(x) = 0 \\
\end{cases}
$$

其中，隐函数存在的条件是 Jacobi 行列式：

$$
J = \frac{D(F,G)}{D(u,v)} = \mqty|\partial_u F_1(u,v) & \partial_v F_1(u,v) \\ \partial_u F_2(u,v) & \partial_v F_2(u,v)| \neq 0
$$

---

### 极值问题

令

$$
A = \pdv[2]{f}{x} \qc B = \pdv[2]{f}{x}{y} \qc C  =\pdv[2]{f}{y}
$$

那么对函数 $f(x,y)$ :

- 一阶必要性：

$$
\pdv{f}{x} = \pdv{f}{y} =0
$$

- 二阶充分性：对于判别式 $B^2 - AC$ 有
  - 如果 $B^2 - AC < 0$ :
    - $A>0$ 为极小值点；
    - $A>0$ 为极大值点；
  - 如果 $B^2 - AC> 0$ ，为非极值点的鞍点
  - 如果 $B^2 - AC = 0$ 则需要进一步判断。

如果有限制条件 $\varphi(x,y) = 0$ ，则构建函数 $F(x,y,\lambda) = f(x,y) + \lambda \varphi(x,y)$ 求稳定点。

---

## 4. 级数

### 一般级数的判别法

判断 $\sum_{n=1}^\infty a_nb_n $的收敛性：

|                |          Dirichlet 判别法          |           Abel 判别法            |
| :------------: | :--------------------------------: | :------------------------------: |
| $\{a_n\}$ 满足 |         $a_n \to 0$ 且单调         |         $a_n$ 有界且单调         |
| $\{b_n\}$ 满足 | $\sum_{n=1}^\infty b_n$ 部分和有界 |   $\sum_{n=1}^\infty b_n$ 收敛   |
|      结论      |  $\sum_{n=1}^\infty a_nb_n $ 收敛  | $\sum_{n=1}^\infty a_nb_n $ 收敛 |

同样对于函数项级数：

|                   |               Dirichlet 判别法               |                Abel 判别法                 |
| :---------------: | :------------------------------------------: | :----------------------------------------: |
| $\{a_n(x)\}$ 满足 | $a_n(x) \rightrightarrows 0$ 且关于 $n$ 单调 |      $a_n(x)$ 一致有界且关于 $n$ 单调      |
| $\{b_n(x)\}$ 满足 |  $\sum_{n=1}^\infty b_n(x)$ 部分和一致有界   |    $\sum_{n=1}^\infty b_n(x)$ 一致收敛     |
|       结论        |  $\sum_{n=1}^\infty a_n(x)b_n(x) $ 一致收敛  | $\sum_{n=1}^\infty a_n(x)b_n(x) $ 一致收敛 |


---

### Abel 变换

$$
\sum_{k=1}^n a_kb_k = \sum_{k=1}^{n-1} (a_k - a_{k+1})B_k + a_nB_n \qc B_k = \sum_{l=1}^k b_l
$$

> 某种意义上的“分部求和”（Summation by parts）。

---

### 离散傅里叶展开

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos(nx) + b_n\sin(nx))
$$

其中：

$$
\begin{cases}
a_n = \frac1\pi \int_{-\pi}^{\pi} f(x)\cos(nx) \dd x \\
b_n = \frac1\pi \int_{-\pi}^{\pi} f(x)\sin(nx) \dd x
\end{cases}
$$

对于一个以 $2\pi$ 为周期的函数 $f(x)$，傅里叶级数满足：

$$
\frac{a_0^2}{2} + \sum_{k=1}^{\infty}(a_k^2 + b_k^2) = \frac{1}{\pi}\int_{-\pi}^{\pi}f^2(x)\dd x
$$

---

## 5. 多重积分

### Gauss 矩公式

$$
\begin{gathered}
\int_0^\infty e^{-x^2}\dd x  = \frac{\sqrt{\pi}}{2} \\
\int_0^\infty x^ne^{-x^2}\dd x = \frac12\Gamma\pqty{\frac{n+1}{2}} = \begin{cases}
\frac{(2k)!}{2\cdot4^{k}k!}\sqrt{\pi}, &n=2k \\
\frac{k!}{2}, &n=2k + 1
\end{cases}
\end{gathered}
$$

---

### Cauchy-Schwarz 不等式

$$
\pqty{\int_a^b f(x)g(x)\dd x}^2 \leq \int_a^b f^2(x)\dd x\int_a^b g^2(x)\dd x
$$

---

### 多重积分换元

$$
\dd x \dd y \dd w = \abs{\frac{D(x,y,z)}{D(u,v,w)}}\dd u \dd v \dd w
$$

---

## 6. 路径积分

### 曲线积分

- 第一类曲线积分

$$
\int_L f(x,y) \dd s = \int_a^b f(x,y(x))\sqrt{1+y'(x)^2} \dd x
$$

- 第二类曲线积分

$$
\int_L \vb F(x,y) \cdot \dd{\vb r} = \int_a^b \bqty{P(x,y) + Q(x,y)y'(x)}\dd x
$$

---

### 曲面积分

- 第一类曲面积分

$$
\iint_S f(x,y,z)\cdot \dd S = \iint_D f(x,y,g(x,y))\sqrt{1+(g'_x)^2+(g'_y)^2} \dd x \dd y
$$

- 第二类曲面积分

$$
\begin{aligned}
\iint_S \vb F(x,y,z)\cdot \dd{\vb S} &= \iint_S  \vb F(x,y,z)\cdot\vb n(x,y,z) \dd S \\
&= \iint_S (P\cos(\vb n,x) + Q\cos(\vb n,y) + R\cos(\vb n,z))\dd S\\
&= \iint_S P\dd y \dd z + Q \dd z \dd x + R \dd x \dd y
\end{aligned}
$$

可转化成第一类：

$$
\begin{aligned}
\iint_S \vb F(x,y,z)\cdot\vb n(x,y,z) \dd S &= \pm\iint_S \frac{1}{\sqrt{1+(g'_x)^2+(g'_y)^2}}(P(-g_x') + Q(-g_y') + R)\dd S \\
&= \pm \iint_D (P(-g_x') + Q(-g_y') + R)\dd x \dd y
\end{aligned}
$$

---

### Green 公式

- 二维情况

  - 函数 $P$ 和 $Q$ 在区域 $D$ 内没一点都有定义且**有连续偏导数**；

  - $D$ 为有界闭区域。

$$
\oint_{L^+} P\dd x + Q\dd y = \iint_D \pqty{\pdv{Q}{x} - \pdv{P}{y}} \dd x \dd y
$$

用单位外法向量 $\vb n$ 来表示课得到散度定理：

$$
\oint_{L^+} (P,Q)\cdot \vb nds = \iint_D \pqty{\pdv{Q}{x} + \pdv{P}{y}} \dd x \dd y = \iint_D \pqty{\div\vb F} \dd x \dd y
$$

- 三维情况

$$
\begin{gathered}
\iint_S P\dd y \dd z + Q \dd z \dd x + R \dd x \dd y = \iiint_\Omega \pqty{\pdv{P}{x} + \pdv{Q}{y} + \pdv{R}{z}} \dd V \\
\iint_S (\vb F \cdot \vb n)\dd S = \iiint_\Omega (\div\vb F) \dd V
\end{gathered}
$$

---

### Stokes 公式

$$
\begin{gathered}
 \oint_L P\dd x + Q\dd y + R\dd z = \iint_S \mqty|\dd y \dd z & \dd z \dd x & \dd x \dd y \\ \pdv{x} & \pdv{y} & \pdv{z} \\ P&Q&R| \\
 \oint_L \vb F \dd{\vb r}=\iint_S(\curl\vb F)\cdot \vb n \dd S
\end{gathered}
$$

---

## 7. 无穷积分 瑕积分

### 收敛判别

|             |           Dirichlet 判别法           |             Abel 判别法              |
| :---------: | :----------------------------------: | :----------------------------------: |
| $a(x)$ 满足 |  $\lim_{x\to\infty} a(x)=0$ 且单调   |          $a(x)$ 有界且单调           |
| $b(x)$ 满足 |   $\int_1^Xb(x)\dd x$ 部分积分有界   |   $\int_1^{+\infty}b(x)\dd x$ 收敛   |
|    结论     | $\int_1^{+\infty}a(x)b(x)\dd x$ 收敛 | $\int_1^{+\infty}a(x)b(x)\dd x$ 收敛 |

---

## 8. 常微分方程

### Wronski 行列式

$$
W(x) = \mqty|\varphi_1(x) & \varphi_2(x) \\ \varphi'_1(x) & \varphi_2'(x)|
$$

对于一个通解 $C_1\varphi_1(x) + C_2\varphi_2(x)$，则 $\varphi_1(x)$ 和 $\varphi_2(x)$ 线性无关的充分条件是**区间上存在一点** $W(x) \neq 0$ （可证明一点非零则区间上均非零）。

---

### 二阶常数变易法

对二阶齐次方程有特解 $y(x) = C_1(x)\varphi_1(1)$，一般设：

$$
\begin{cases}
C_1'(x)\varphi_1(x) + C_2'(x)\varphi_2(x) = 0 \\
C_1'(x)\varphi'_1(x) + C_2'(x)\varphi'_2(x) = f(x)
\end{cases}
$$

---

### Bernoulli方程

$$
y' + P(x)y = Q(x)y^{\alpha}
$$

一般换元 $z = y^{1-\alpha}$，之后有：

$$
z' = (1-\alpha)\frac{y'}{y^\alpha} = (1-\alpha)\pqty{Q(x) - P(x)z}
$$

之后按一阶方法求解。

---

