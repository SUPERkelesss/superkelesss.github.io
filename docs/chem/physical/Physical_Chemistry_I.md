# 物理化学(一) 笔记 Physical Chemisnbtry I

## PART I QUANTUM THEORY

## Lecture 1

### 1.1 经典力学

我们先考虑动量 $\vb p$，很明显有 $\vb p = m\vb v$。这于是有：

$$
\dv{\vb p}{t} = m \dv{\vb v}{t} = m\vb a = \vb F_{ext}
$$

接下来考虑能量 $E = T+U = \frac 12 m \abs{\vb v}^2 + U(\vb r)$ ：

$$
\begin{aligned}
\dv{E}{t} &= \frac12m\dv{v^2}{t} + \dv{U(x)}{t} = mv\dv{v}{t} + v\dv{U}{x}
\end{aligned}
$$

于是当能量守恒时得到：

$$
\dv{p}{t} = -\pdv{U}{x} \Rightarrow \dv{\vb p}{t} = -\pdv{U}{\vb r}\hat r
$$

在*Newton*力学体系，相空间内的一个点 $(\vb r(0), \vb v(0))$ 的演化遵从：

$$
\begin{cases}
\dv{\vb r}{t} = \vb v\\
\dv{\vb v}{t} = -\frac1m \pdv{U(\vb r)}{\vb r}
\end{cases}
$$

 这就确定了从 $(\vb r(0), \vb v(0))$ 到 $(\vb r(t), \vb v(t))$ 的唯一一条演化路径。怎么证明路径唯一呢？

---

我们定义**拉格朗日量**（Lagrangian）：

$$
 L(\dot x,\dot y,\dot z,x,y,z,t) = T-U
$$

规定**作用量**（action）$S$ 为连接相空间两个点所有轨迹的泛函：

$$
S = \int_{t_1}^{t_2} L(\dot x,\dot y,\dot z,x,y,z,t)\dd
$$


**最小作用量原理**认为，相空间的真实运动轨迹是一阶变分 $\delta S = 0$ 的轨迹。

我们规定 $\dv{ L}{t} = 0$ ，这样对于静势能有：

$$
\begin{aligned}
\delta S&=\delta \int_0^t  L(\dot x,\dot y,\dot z,x,y,z,t) \dd t'\\
&= \int \dv{ L}{x}\delta x \dd t + \int \dv{ L}{\dot x} \dd \delta x + \cdots \\
&= \int \dv{ L}{x}\delta x \dd t + \eval{\dv{ L}{x}\delta x}_0^t - \int \dv{t} \dv{ L}{\dot x}\delta x \dd t +\cdots\\
&= \int_0^t (\dv{ L}{x} - \dv{t} \dv{ L}{\dot x})\delta x \dd t' \cdots
\end{aligned}
$$

这需要：

$$
\boxed{\dv{ L}{x} = \dv{t} \dv{ L}{\dot x}}
$$

这被称为**Euler-Lagrange方程**。

如果是正交坐标系，这和牛顿第二定律等价。但Langrange力学的先进之处其坐标可以换成任意一个广义坐标 $q_i$。比如对于球坐标系 $(r,\phi,\theta)$：

$$
\dv{ L}{\theta} = \dv{t} \dv{ L}{\dot \theta}
$$

当我们选取广义坐标 $q_j$ 时，其对应的动量 $p_j$ 被称为**共轭动量**（conjuncted momentum）。例如 $x\sim p_x$，$\theta \sim p_\theta$ 。我们有：

$$
p_j = \pdv{ L}{\ddot q_j}
$$

---

我们定义*Hamilton*量：

$$
H =\sum_J p_j\dot q_j -  L(\dot q, q)
$$

例如对于单个粒子，当 $q_j = x$ 时，可以计算得到 $H = T+V = E$ 。

我们同样考虑微分：

$$
\begin{aligned}
\dd H &= \sum_j p_j \dd{\dot q_j} +  \sum_j \dot q_j \dd{p_j} - \sum_j \pdv{ L }{\dot q_j}\dd{\dot q_j} - \sum_j \pdv{ L }{q_j}\dd{q_j} \\
&= \sum_j \dot q_j \dd{p_j} - \sum_j \dot p_j \dd {q_j}
\end{aligned}
$$

又可以由全微分得到：

$$
\dd H = \sum_j\pdv{H}{p_j} \dd p_j + \sum_j\pdv{H}{q_j} \dd q_j
$$

对应系数得到：

$$
\begin{cases}
\dot q_j = \pdv{H}{p_j} \\
\dot p_j = -\pdv{H}{p_j}
\end{cases}
$$

这被称为**Hamilton方程组**。

这时候考虑哈密顿量的导数：

$$
\dv{H}{t} = \sum_j \dot q_j \dot{p_j} - \sum_j \dot p_j \dot {q_j} =0
$$

即**哈密顿量不随时间改变**。

---

考虑相空间内的一个区域 $((p,p+\dd p),(q,q+\dd q))$ ，我们定义**流量**(flux)) $f(p,q,t)$，表示这个微小区域进出粒子的梯度。

$$
\begin{aligned}
\dv{f}{t} &= \pdv{f}{t} + \pdv{f}{p}\dv{p}{t} + \pdv{f}{q}\dv{q}{t}\\
 &= \pdv{f}{t} - \pdv{f}{p}\pdv{H}{q} + \pdv{f}{q}\dv{H}{p}
\end{aligned}
$$

于是这个相空间内的粒子数：

$$
\begin{aligned}
N = \pdv{f}{t}\dd q \dd p &= \bqty{-f(q+\dd q)\dot q(q+\dd q) + f(q)\dot q(q)}\dd p \\
&=-\pqty{\pdv{f}{q}\dot q + f\pdv{\dot q}{q}}\dd p\dd q
\end{aligned}
$$

第二步忽略了高阶项。分别约去得到：

$$
\begin{aligned}
\pdv{f}{t} &= -\pqty{\pdv{f}{q}\dot q + f\pdv{\dot q}{q}}-\pqty{\pdv{f}{p}\dot p + f\pdv{\dot p}{p}} \\
&= -\pqty{\pdv{f}{q}\dot q + f\pdv{H}{p}{q}}-\pqty{\pdv{f}{p}\dot p - f\pdv{H}{p}{q}} \\
&= - \pdv{f}{q}\dot q - \pdv{f}{p}\dot p
\end{aligned}
$$

代入第一个式子，得到：

$$
\boxed{\dv{f}{t} = 0}
$$

这就是**刘维尔定理**，也就是相流是不可压缩的，也就是相空间体积元在演化过程中保持不变。

---

### 1.2 量子理论

我们都知道平面波的表达式 $e^{i(\vb k \cdot \vb r - \omega t)}$，其中 $\vb k = \vb p/\hbar$，$\omega = E/\hbar$。我们定义一个波函数 $\Psi(r,t)$ 为若干各平面波的叠加，它们的系数为 $f(k)$ ：

$$
\begin{aligned}
\Psi(r,t) &= \int f(k')e^{i(k'r - \omega t)} \dd k' \\
&=\int F(p)e^{i\frac{pr - Et}{\hbar}} \dd p
\end{aligned}
$$

我们把波函数对时间求一次导数：

$$
i\hbar \pdv{t}\Psi(r,t) = \int EF(p)e^{i\frac{pr - Et}{\hbar}} \dd p
$$

也可以对空间求一次导数：

$$
-i\hbar \pdv{r}\Psi(r,t) = \int pF(p)e^{i\frac{pr - Et}{\hbar}} \dd p
$$

好像只有动量的一次方弄不出能量，因此我们再求一次导数：

$$
\begin{aligned}
-\hbar^2 \pdv{r}\Psi(r,t) &= \int p^2F(p)e^{i\frac{pr - Et}{\hbar}} \dd p \\
&= \int 2m(E-U)F(p)e^{i\frac{pr - Et}{\hbar}} \dd p
\end{aligned}
$$

化简之后就可以得到：

$$
\boxed{\hat H \psi = (-\frac{\hbar^2}{2m}\pdv[2]{r} +U)\psi = E\psi}
$$

这就是**定态Schrodinger方程**。

再带入到时间导数的表达式里，我们有：

$$
\boxed{i\hbar\pdv{t}\Psi(r,t) = \hat H \Psi}
$$

这就是**含时Schrodinger方程**。

---

我们进入到原子层面。假设一个体系由很多个原子，需要考虑原子核和电子的相互作用。假设原子核坐标是 $R_I$ ，电子坐标是 $r_i$ ，用薛定谔方程写出就是：

$$
\hat H = -\sum_I \frac{\hbar^2}{2m} \nabla_I^2 -\sum_i \frac{\hbar^2}{2m} \nabla_i^2 + 一大堆库伦项
$$

其中，电子动能项和一大堆库伦项都可以全部视为电子有关项。

我们分离核和电子的运动，假设我们可以解出核坐标 $R_I$ 对应的电子能量 $E(R)$ ，我们定义一个新的波函数：

$$
\phi(r;R) = \sum_l \psi_l(r;R)\chi_l(R;t)
$$

由含时薛定谔方程得到：

$$
i\hbar\pdv{t} \sum_l \psi_l\chi_l = \hat H(\sum_l \psi_l\chi_l) =-\sum_I \frac{\hbar^2}{2m} \nabla_I^2 + E(R)
$$

---

## Lecture 2 量子力学 Quantum Mechanics

### 波函数 Wavefunction

我们定义一个一维里的自由的电子，也就是 $V(x) = 0$，这样就有：

$$
-\frac{\hbar^2}{2m}\dv[2]{x} \psi = E \psi \Rightarrow \psi(x) = e^{i\frac{\sqrt{2mR}}{\hbar}x}
$$

对于这一项我们可以继续定义，我们知道动量 $p = \sqrt{2mE}$，波矢 $k = p/\hbar$，这样就是：

$$
\psi(x) = e^{ikx}
$$

对于这样一个粒子而言，是没有特定的“量子化能级”的。也就是说在量子力学里其实不必有量子化。

那么波函数到底是什么呢？我们可以认为波函数**包含了一个系统的所有信息**，而这一信息是通过**概率幅**（Probability Amplitude）来显示的。我们定义：

$$
\dd{P(\vb{r},t)} = \psi^*(\vb{r},t)\psi(\vb{r},t)\dd{\vb r}
$$

由于归一化限制，概率密度满足：

$$
\int \psi^*(\vb{r},t)\psi(\vb{r},t)\dd{\vb r} = 1 \Rightarrow \ip{\psi}{\psi} =1
$$

如何从波函数得到宏观物理量？我们认为宏观的物理量是一个算符对波函数的本征值。比如：

$$
\begin{gathered}
\hat{X}\ket{\psi} = x\ket{\psi} \\
\hat{P}\ket{\psi} = \frac{\hbar}{i}\grad\ket{\psi} = p\ket{\psi}
\end{gathered}
$$

对于一个算符 $\hat A$，如果它存在多个本征值 $a$ 和对应本征向量 $\phi_a$，我们就可以分解这个波函数：

$$
\psi(\vb r,t) = \sum_a c_a \phi_a
$$

这就引出了**正交性**：$\ip{\phi_i}{\phi_j} = 0$。把他们合并在一起就是正交归一性：

$$
\ip{\phi_i}{\phi_j} = \delta_{ij}
$$

我们可以计算 $\psi$ 处于 $\phi_i$ 时的概率：

$$
\mel{\psi}{c_i}{\phi_i} = \sum_n c_i c_n^* \ip{\phi_n}{\phi_i} = c_ic_i^*\ip{\phi_i} = |c_i|^2
$$

由于已经归一化 $\ip{\psi} = 1$，我们就能得到这个概率 $P_i = |c_i|^2$。

---

### 波包和不确定性原理

我们假设知道有这样一个z周期函数，他的形式像傅里叶级数，以 $L$ 为周期：

$$
f(x) = \sum_{-\infty}^{\infty} c_n e^{ik_n x}\qc k_n = \frac{2\pi n}{L}
$$

我们有：

$$
c_n = \frac{1}{L}\int_{x_0}^{x_0 + L}\dd{x}e^{-ik_n x}f(x)
$$

> 我们可以通过直接代入证明这个式子：
>
> $$
> \begin{aligned}
> \frac{1}{L}\int_{x_0}^{x_0 + L}\dd{x}e^{-ik_n x}f(x) &= \frac{1}{L}\int_{x_0}^{x_0 + L}\dd{x}e^{-ik_n x}\sum_{-\infty}^{\infty} c_p e^{ik_p x}\\
> &= \frac{1}{L}\sum_{-\infty}^{\infty}c_p\int_{x_0}^{x_0+L}e^{i(k_p - k_n)x} \dd{x}\\
> &= \frac{1}{L}\cdot  c_nL = c_n
> \end{aligned}
> $$

（不严谨地）取 $L\to\infty$，就不用管是不是周期函数了。这就是连续傅里叶变换。

$$
F(k) = \frac{1}{\sqrt{2\pi}}\int f(x)e^{-ikx}\dd{x}
$$

---

对于自由粒子 $f(x) = e^{ipx/\hbar}$，我们有：

$$
\frac{\hbar}{i} \pdv{f(x)}{x} = pf(x) \Rightarrow \hat{p} = \frac{\hbar}{i}\grad
$$

这就是动量算子的来源。

再代入含时Schrodinger方程，解自由粒子的波函数：

$$
\begin{gathered}
i\hbar\pdv{t}\Psi(r,t) = -\frac{\hbar^2}{2m}\grad^2 \Psi(r,t) \\
\Rightarrow \Psi(r,t) = Ae^{i(kr-\omega t)}\qc \omega = \frac{\hbar k^2}{2m}
\end{gathered}
$$

这和平面波的表达式是类似的，说明自由粒子波函数可以用平面波表示。

---

对于平面波而言，由于 $\hbar/i\ \grad \psi(x) = 0$，所以波峰是在空间内均匀分布的。

现在我们假设有很多个自由粒子，用叠加原理（Principle of superposition）累加在一起，并且用 $g(k)$ 控制权重，这样就改变的均匀分布：

$$
\psi(x,t) = \frac{1}{\sqrt{2\pi}}\int g(k)e^{ikx}\dd{k}
$$

运用傅里叶变换就可以得到权重：

$$
g(k) = \frac{1}{\sqrt{2\pi}}\int \psi(x,t)e^{-ikx}\dd{x}
$$

> 比如建立下面的权重：
>
> $$
> \begin{cases}
> \frac12 g(k_0)&,k = k_0 - \Delta k/2 \\
> g(k_0)&,k=k_0\\
> \frac12 g(k_0)&,k = k_0 + \Delta k/2
> \end{cases}
> $$
>
> 于是累加得到：
>
> $$
> \begin{aligned}
> \psi(x) &= g(k_0)\qty[e^{ik_0x} + \frac12 e^{i(k-\Delta k/2)}+\frac12 e^{i(k+\Delta k/2)}]\\
> &= g(k_0)e^{ik_0x}\qty[1+\cos(\Delta k/2\  x)]
> \end{aligned}
> $$
>
> 可以看到有两种波动模式。在一个周期内有：
>
> $$
> \frac{\Delta k\Delta x}{2} = 2\pi \Rightarrow \Delta k \cdot \Delta x = 4\pi
> $$

对于一个更加general的case：

![image-20260314114251204](Physical_Chemistry_I.assets/image-20260314114251204.png)

可以看到波在一定的部分里看起来在 $g(k)$ 的范围内，这就叫波包。

---

对于**高斯波包**（Gaussian wavepackets），也就是 $g(k)$ 按高斯分布形成的波函数，我们有：

$$
\psi(x) = \frac{\sqrt{a}}{(2\pi)^{3/4}}\int_{-\infty}^{\infty}e^{-\frac{a^2}{4}(k-k_0)^2}e^{ikx}\dd{k}
$$

这就有：

$$
\Delta x \cdot \Delta p = \frac{\hbar}{2}
$$

这就是 **Heisenberg不确定性原理**（Heisenberg uncertainty principal）。

---

### 势箱中的粒子

由一维势箱我们可以解得：

$$
\psi_n(x) = \sqrt{\frac{2}{a}}\sin[2](\frac{n\pi x}{a})
$$

我们可以认为 $\ket{\psi(x)} = \sum_n c_n \ket{\psi_n(x)}$。这之后，我们可以求能量的期望值。

$$
\mqty[\dmat{E_1, E_2, \ddots, E_n}]\mqty[c_1\\c_2\\\vdots\\c_n] = \mqty[c_1E_1\\c_2E_2\\\vdots\\c_nE_n] \Rightarrow \hat{H}\ket{\psi} = E\ket{\psi}
$$

能量的期望值可以表示为：

$$
\begin{aligned}
\ev{E} &= \frac{\mel{\psi}{\hat H}{\psi}}{\ip{\psi}} = \frac{\smqty[c_1&c_2&\cdots&c_n]\smqty[\dmat{E_1, E_2, \ddots, E_n}]\smqty[c_1\\c_2\\\vdots\\c_n]}{\smqty[c_1&c_2&\cdots&c_n]\smqty[c_1\\c_2\\\vdots\\c_n]}\\
&= \frac{\sum_i E_n|c_i|^2}{\sum_i |c_i|^2} = \sum_i P_i E_i
\end{aligned}
$$

---

### 对易子

对易子（Commutation）可以表示为：

$$
[A,B] = AB - BA
$$

如果对易子等于0，我们就说这两个算符对易，**这意味着 $\ket{\psi}$ 和 $B\ket{\psi}$ 具有相同的特征值**。

一个典型的例子是 $[x,p_x] = i\hbar$。

---

### 测量（Measurement）

对于一次测量，会使体系坍缩至其中一种可能的状态。需要注意的是，**测量的先后顺序可能会影响测量结果**。

<img src="Physical_Chemistry_I.assets/image-20260310172456282.png" alt="image-20260310172456282" style="zoom:67%;" />

对于两个不对易的算符对应的物理量而言，比如 $\ket{u}$ 和 $\ket{v}$ ，先测量 $\ket{u}$ 会使波函数有一定概率坍缩到 $\ket{u_1}$ 上，有一定概率坍缩到 $\ket{u_2}$ 上，之后再测定 $v$ 结构就是坍缩之后的向量继续向 $\ket{v}$ 坍缩。

---

### 三维的情况

由于三个方向上的波函数都是线性无关的，我们可以把能量拆成：（假设边长为 $L$）：

$$
E = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_y^2)
$$

右边这一项有点像欧氏距离的平方……为了展示这一点，我们把空间坐标画出来：

![image-20260310173445375](Physical_Chemistry_I.assets/image-20260310173445375.png)

这样，图中的每一个点就代表了一个可能的量子态。我们把表达式化简成：

$$
E = \frac{h^2R^2}{8mV^{2/3}} \Rightarrow R^2 = \frac{8mEV^{2/3}}{h^2}
$$

这样这个空间内1/8球的体积就是：

$$
\phi(E) = \frac18 \cdot \frac43\pi R^3 = \frac{\pi}{6}(\frac{8mE}{h^2})^{3/2}V
$$

如果最高能量 $E=kT$，定义热波长，就有：

$$
\phi(E)\sim\frac{V}{\Lambda^3}\qc \Lambda = (\frac{h}{2\pi mkT})^{1/2}
$$

（怎么感觉这个证明略显奇怪……还是按配分函数的想法来吧）

---

### Schrodinger方程与求导

接下来我们关注含时薛定谔方程。尝试对 $\ip{\psi(t)}$ 进行求导：

$$
\begin{aligned}
\dv{t}\ip{\psi(t)} &= [\dv{t}\bra{\psi(t)}]\ket{\psi(t)} + \bra{\psi(t)}[\dv{t}\ket{\psi(t)}] \\
&= -\frac{1}{ih}\mel{\psi(t)}{\hat H}{\psi(t)} + \frac{1}{ih}\mel{\psi(t)}{\hat H}{\psi(t)} = 0
\end{aligned}
$$

这意味着含时的波函数对应的概率是保持不变的。

接下来我们考虑对于 $\ev{A}{\psi(t)}$ 求导（此处假设算符 $A$ 对时间线性无关）：

$$
\begin{aligned}
\dv{t}\ev{A}{\psi(t)} &= [\dv{t}\bra{\psi(t)}]A\ket{\psi(t)} + \bra{\psi(t)}A[\dv{t}\ket{\psi(t)}]\\
&= -\frac{1}{i\hbar}\mel{\psi(t)}{\hat HA}{\psi(t)} + \frac{1}{i\hbar}\mel{\psi(t)}{A\hat H}{\psi(t)} = 0\\
&= \frac{1}{i\hbar}\ev{[A,H]}
\end{aligned}
$$

这被称为 **Ehvenfest 定理**。

---

对于带幂次的对易子而言，比如：

$$
\begin{gathered}
\comm{x}{p^2} = \comm{x}{p}p +p\comm{x}{p} = 2i\hbar p\\
\comm{x}{p^3} = \comm{x}{p^2}p +p^2\comm{x}{p} = 3i\hbar p^2
\end{gathered}
$$

由此我们可以总结出：

$$
\comm{x}{p^n} = ni\hbar p^{n-1}
$$

如果是一个函数，我们也可以作Taylor展开：

$$
\begin{aligned}
\comm{x}{F(p)} &= \comm{x}{\sum_n f_ip^n} \\
&= \sum_nf_n\comm{x}{p^n} \\
&= \sum_nni\hbar p^{n-1} = i\hbar F'(p)
\end{aligned}
$$

以此为基础，我们尝试对位矢的期望值求导：

$$
\begin{aligned}
\dv{\ev{R}}{t} &= \frac{1}{i\hbar}\ev{[R,H]}\\
&= \frac{1}{i\hbar}\ev{[R,\frac{p^2}{2m} + V]}\\
&= \frac{1}{i\hbar}\ev{[R,\frac{p^2}{2m}]}=\ev{\frac{p}{m}} = \ev{v}
\end{aligned}
$$

这正好符合我们在经典力学里的定义。也可以对动量求导：

$$
\begin{aligned}
\dv{\ev{P}}{t} &= \frac{1}{i\hbar}\ev{\comm{p}{H}}\\
&= \frac{1}{i\hbar}\ev{[p,\frac{p^2}{2m} + V]}\\
&= \frac{1}{i\hbar}\ev{[p,V(R)]}\\
&= -\ev{\grad_RV(R)}
\end{aligned}
$$

这也和经典力学相同。

---

