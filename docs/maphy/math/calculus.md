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



























