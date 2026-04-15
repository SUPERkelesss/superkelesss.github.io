# Monte Carol 算法

## 1. Basis

由经典的统计力学得到，一个经典系统的可观测量满足：
$$
\ev{A} = \frac{\int \dd[3]{\va r^N} A(\va r^N) e^{-\beta U(\va r^N)}}{\int \dd[3]{\va r^N} e^{-\beta U(\va r^N)}}
$$
采取某个构象的概率密度为：
$$
P(\va r^N) = \frac{e^{-\beta U(\va r)}}{Z}
$$
考虑在构象空间（configuration-space）中，随机生成 $L$ 个点，则处于 $\va r^N$ 附近的一小片区域（子空间） $\Delta_{\dd{N}}$ 的点数目：
$$
n_j = LP(\va r^N) \Delta_{\dd{N}}
$$
如果有 $M$ 个子空间，并且平铺整个构象空间，这就有 $M = V^N /\Delta_{\dd{N}}$。当取得子空间体积 $\Delta_{\dd{N}}$ 足够小时，对应 $M$ 和 $L$ 足够大时有：
$$
\ev{A} \approx \frac1L \sum_{j=1}^M n_jA(\va r_j^N)
$$
相当于把构想空间划分成 $M$ 块，并对每一块取加权平均。类似于粗粒化操作。

当然我们也可以写成直接对每个点求平均的形式：
$$
\ev{A}\approx \frac1L \sum_{j=1}^L A(\va r_j^N)
$$
这样的好处是，我们不需要计算配分函数，因为 $\sum_j n_j = L$ 本身就是归一化的。然而这意味着生成的点必须满足 Boltzmann 权重。这一方法被称为**重要性采样** (Importance Sampling)。



