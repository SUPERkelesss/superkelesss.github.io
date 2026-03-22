# 数学物理方程 Partial Differential Equations

## 1. 定解问题

### 弦振动问题

考虑一根绷紧的**完全柔软**的均匀**轻质**弦，激发后在平面内的微小振动。考虑弦平衡时的微元：

- 选取 $y$ 方向位移物理量 $u(x,t)$，表示在 $t$ 时刻位于 $x$ 的位移。
- **轻弦**：忽略重力；
- **完全柔软**：弹力只沿切向。

对于一段在 $(x, x+\dd x)$ 上的一小段弦，在两个端点上拉力的角度不同：

![image-20260303113038024](PDE.assets/image-20260303113038024.png)

由于弦仅有 $y$ 方向上的运动，我们有：

$$
\begin{cases}
T_1\cos\theta_1 = T_2\cos\theta_2 \\
T_2\sin\theta_2-T_1\sin\theta_1 = \rho\dd x \cdot\overline{\pdv[2]{u}{t}}
\end{cases}
$$

由于振动很微小，我们近似这段弦为一条直线段。也就是：

$$
\frac{u_2-u_1}{(x+\dd x) - x} \ll 1 \Rightarrow \pdv{u}{x}  =\tan\theta \ll 1
$$

> 即为底边长 $\dd x$ 高为 $u_2 - u_1$ 的直角三角形。

于是忽略高阶项认为 $\sin \theta = \tan\theta = \pdv{u}{x},\cos\theta=1$。由第一个方程可得：

$$
T_1 = T_2
$$

统一为 $T$ 代入方程2：

$$
T(\eval{\pdv{u}{x}}_{x+\dd x} - \eval{\pdv{u}{x}}_{x}) = \rho\dd x \cdot\overline{\pdv[2]{u}{t}}
$$

同除 $\dd x$ 得到：

$$
T\pdv[2]{u}{x} = \rho\pdv[2]{u}{t}
$$

定义 $a = \sqrt{T/\eta}$ ，得到**弦的自由振动方程**：

$$
\boxed{\pdv[2]{u}{t} -a^2\pdv[2]{u}{x} = 0}
$$

> 分析量纲 $\sqrt{MLT^{-2}/ML^{-3}} = L/T$，得到 $a$ 为速度单位。

弹力和时间有关吗？由于hook定理，对于弹性弦，只要长度不变弹力就保持不变。分析微元段的长度：

$$
\dd s = \sqrt{(\dd u)^2 + (\dd x)^2} = \dd x \sqrt{1+\pqty{\pdv{u}{x}}^2}  \approx \dd x
$$

也就是 $\dd s - \dd x = 0$，即长度始终保持不变，也就是**弹力不随时间变化**。

接下来考虑受外力作用的形式。如果在 $u$ 方向上单位长度受力为 $f$ ，初始条件改为：

$$
\begin{cases}
T_2\cos\theta_2 - T_1\cos\theta_1 = 0 \\
T_2\sin\theta_2-T_1\sin\theta_1 + f\dd x = \rho\dd x \cdot\pdv[2]{u}{t}
\end{cases}
$$

用相同方法解得：

$$
\boxed{\pdv[2]{u}{t} -a^2\pdv[2]{u}{x} = \frac{f}{\rho}}
$$

这被称为**弦的受迫振动方程**。右侧的 $f/\rho$ 可以认为是单位质量受力。

---

### 杆纵振动问题

考虑一个**均匀轻细杆**沿杆长方向的**微小振动**。同样取一段微元 $(x,x+\dd x)$ 进行分析。

![image-20260305080931930](PDE.assets/image-20260305080931930.png)

- 均匀：认为处处截面积相等；
- 轻：忽略重力；
- 微小振动：忽略因振动引起的截面积变化。

由 *Newton* 第二定律：

$$
\begin{gathered}
\rho S \dd x \overline{\pdv[2]{u}{t}} = [P(x+\dd x, t) - P(x,t)]S \\
\rho \pdv[2]{u}{t} = \pdv{P}{x}
\end{gathered}
$$

由 *Young* 模量得到：$P = E\pdv{u}{x}$，于是：

$$
\boxed{\pdv[2]{u}{t} -a^2\pdv[2]{u}{x} = 0}\  \qc a = \sqrt{\frac{E}{\rho}}
$$

形如此的方程被称为**波动方程**。拓展成三维空间就是：

$$
\pdv[2]{u}{t} - a^2\grad^2u = 0
$$

---

## 热传导方程

假设一块连续介质，用 $u(x,y,z,t)$ 表示 $(x,y,z)$ 处 $t$ 时刻的温度。如果沿 $x$ 方向由温度梯度，由于能量守恒定律，在 $x$ 方向一定存在热量传递。由 *Fourier* 定律得：

$$
q_x = -k_x\pdv{u}{x}
$$

其中 $q$ 为热流密度，$k$ 为导热率。同样也有：

$$
q_y = -k_y\pdv{u}{y}\qc q_z = -k_z\pdv{u}{z}
$$

如果材料是各向同性的，那么三个方向上的导热率 $k$ 应该都相同。我们合并写成：

$$
\vb q = -k\grad u
$$

而如果是各向异性的就变成矩阵乘积：

$$
\vb q = -\vb K\cdot\grad u
$$

我们取出一个平行六面体：

![image-20260305092116360](PDE.assets/image-20260305092116360.png)

沿 $x$ 方向的流入的热量：

$$
(q_x - q_{x+\dd x})\dd y \dd z \dd t = -\pdv{q_x}{x}\dd x\dd y \dd z \dd t
$$

其他两个方向也是同理，于是把他们相加得到 $-\div \vb q \dd x\dd y \dd z \dd t$，又因为对应温度上升：

$$
-\div \vb q \dd x\dd y \dd z \dd t =  \dd (\rho c u) \cdot\dd x\dd y \dd z
$$

得到：

$$
\pdv{(\rho cu)}{t} + \div \vb q = \pdv{(\rho cu)}{t} - \div \vb K \cdot \grad u = 0
$$

而如果是各向同性介质，$\rho c$ 是常数，进一步化简得：

$$
\boxed{\pdv{u}{t} - \kappa\grad^2u = 0}\ \qc \kappa = \frac{k}{\rho c}
$$

其中 $\kappa$ 被称为**扩散率**。这类方程被称为**热扩散方程**。

如果体系中还有单位时间单位体积产生的热量 $f$，进一步携程：

$$
(f-\div \vb q) \dd x\dd y \dd z \dd t =  \dd (\rho c u) \cdot\dd x\dd y \dd z
$$

最终可以化简成：

$$
\pdv{u}{t} - \kappa\grad^2u = \frac{f}{\rho c}
$$

对于扩散问题，由于扩散过程和热传导类似，定义扩散率 $D$，也有：

$$
\pdv{u}{t} - D\grad^2 u = 0
$$

---

### 稳态情况

现在我们考虑当热传导体系达到稳定的状态，此时 $\pdv{u}{t} = 0$。也就是：

$$
\boxed{\grad^2u = \frac{f}{\kappa\rho c}}
$$

这被称为**Poisson方程**。特别的当 $f=0$ 时，得到：

$$
\boxed{\grad^2u = 0}
$$

这被称为**Laplace方程**。

同样也可以对弦振动作一样的考虑。假设有一个特别的振动 $u(x,y,z,t) = v(x,y,z)e^{i\omega t}$，这是一个周期性的振动。带入到振动公式：

$$
-\omega^2 v - a^2\grad^2v = 0
$$

于是有：

$$
\boxed{\grad^2 v + k^2v = 0} \qc k = \frac{\omega}{a}
$$

这被称为**Helmholtz方程**。

---

总结以上三种方程的性质：

|             波动方程              |            热传导方程             |       稳态方程        |
| :-------------------------------: | :-------------------------------: | :-------------------: |
| $\pdv[2]{u}{t} -a^2\grad^2 u = 0$ | $\pdv{u}{t} - \kappa\grad^2u = 0$ | $\grad^2u  + k^2u= 0$ |
|            双曲形方程             |            抛物线方程             |       椭圆方程        |

---

## 2. 行波法

### 定解条件的条件

假设对于一个二阶偏微分方程的问题，已经求出其通解，需要用已知条件消解未知数：

- 初始条件（Initial Condition，IC）：关注对时间 $t$ 微商的最高阶数。

- 边界条件（Boundary Condition，BC）：对于不同维度的问题，边界条件也不同。例如对于一维问题的边界条件：

  - 弦的横振动（第一类边界条件）： $\eval{u}_{x=0} = \eval{u}_{x=l} = 0$；

  - 杆的纵振动（第二类边界条件）：$\eval{u}_{x=0} = 0$，$x=l$ 单位面积受外力 $F(t)$。通过微元法分析：

    $$
    FS - P(l-\epsilon , t)S = \rho S \epsilon \overline{\pdv[2]{u}{t}}
    $$

    当 $\epsilon \to 0$ 时：

    $$
    F - E\eval{\pdv{u}{t}}_{x=l} = 0
    $$

    于是边界条件变为：

    $$
    \begin{cases}
    \eval{u}_{x=0} = 0\\ E\eval{\pdv{u}{t}}_{x=l} = F
    \end{cases}
    $$

  - 一段连接轻弹簧的轻杆（第三类边界条件）：$\eval{u}_{x=0} = 0$，且对于一端的弹簧有：

    $$
    FS = -k(u-u_0)
    $$

    其中 $u_0$ 为平衡位置杆末端位移，$u$ 为任意时刻杆末端位移。于是有：

    $$
    \begin{gathered}
    E\eval{\pdv{u}{t}}_{x=l} = -\frac{k}{S}(u-u_0)\\
    \eval{\pqty{E\eval{\pdv{u}{t}}_{x=l} + \frac{k}{S}u}}_{x=l} = \frac{k}{S}u_0
    \end{gathered}
    $$

    这里边界条件就是一阶微商和二阶微商的线性组合。

> 对热传导方程，由于是一个三维问题，我们需要通过曲面确定边界条件，例如：
>
> - 给定两曲面的温度：$\eval{u}_{x=\Sigma_0} =0,\ \eval{u}_{x=\Sigma} = f(\Sigma)$。这是第一类边界条件。
>
> - 如果表面单位时间通过单位面积散热为 $\psi$。取表面上的一个微元：
>
>   <img src="PDE.assets/image-20260310112715964.png" alt="image-20260310112715964" style="zoom:33%;" />
>
>   $$
>   q = -k\pdv{u}{n}
>   $$
>
>   其中 $n$ 为法向量。进一步得到：
>
>   $$
>   -k\pdv{u}{n} S\Delta t - \psi S\Delta t + 四个侧面的q\cdot四个侧面面积\cdot\Delta t = \rho S \epsilon \Delta t
>   $$
>
>   考虑 $\epsilon \to 0$，就有：
>
>   $$
>   \psi = -k\eval{\pdv{u}{n}}_{\Sigma}
>   $$
>
>   这是第二类边界问题。
>
> - 如果 $\psi$ 和外界环境与体系的温度差成正比：
>
>   $$
>   \begin{gathered}
>   -k\eval{\pdv{u}{n}}_{\Sigma} = H(\eval{u}_{\Sigma} - u_0)\\
>   \eval{\pqty{k\pdv{u}{n} + Hu}}_{\Sigma} = Hu_0
>   \end{gathered}
>   $$
>
>   这是第三类边界问题。
>

---

### 照搬常微分方程

假设我们有无限长的弦，考虑初值问题：

$$
\begin{cases}
\pdv[2]{u}{t} - a^2 \pdv[2]{u}{x} = 0&,-\infty < x < \infty,\ t > 0\\
\eval{u}_{t=0} = \psi(x)\\
\eval{\pdv{u}{t}}_{t=0} = \phi(x)
\end{cases}
$$

我们常识把第一个式子看成：

$$
(\pdv{u}{t} - a\pdv{u}{x})(\pdv{u}{t} + a\pdv{u}{x}) = 0
$$

我们得到了两个一阶方程。尝试作变换：

$$
\begin{cases}
\xi = x+at\\
\eta = x-at
\end{cases}\Rightarrow
\begin{cases}x = \frac{\xi + \eta}{2}\\t = \frac{\xi - \eta}{2a}\end{cases}
$$

然后我们努努力把偏微分都求出来：

$$
\begin{gathered}
\pdv{u}{t} = \pdv{\xi}{t}\pdv{u}{\xi} + \pdv{\eta}{t}\pdv{u}{\eta} = a\pqty{\pdv{u}{\xi} - \pdv{u}{\eta}} \\
\pdv{u}{x} = \pdv{\xi}{x}\pdv{u}{\xi} + \pdv{\eta}{x}\pdv{u}{\eta} = \pdv{u}{\xi} + \pdv{u}{\eta} \\

\end{gathered}
$$

还有二阶微分：

$$
\begin{aligned}
\pdv[2]{u}{t} &= \pdv{\xi}{t}\pdv{\xi}\pdv{u}{t} + \pdv{\eta}{t}\pdv{\eta}\pdv{u}{t}\\
&= a^2\pqty{\pdv[2]{u}{\eta}-2\pdv{u}{\xi}{\eta} + \pdv[2]{u}{\eta}}
\end{aligned}
$$

$$
\begin{aligned}
\pdv[2]{u}{x} &= \pdv{\xi}{x}\pdv{\xi}\pdv{u}{x} + \pdv{\eta}{x}\pdv{\eta}\pdv{u}{x}\\
&= \pdv[2]{u}{\eta}+2\pdv{u}{\xi}{\eta} + \pdv[2]{u}{\eta}
\end{aligned}
$$

全部代入原方程，可得：

$$
\pdv{u}{\xi}{\eta} = 0
$$

于是这个波动方程的通解是：

$$
u(x,t) = f(x-at) + g(x+at)
$$

由此可见：这个微分方程的解是由**两个函数相互叠加组成**（区别于常微分方程，是由两个常数组成的）。从物理角度来看，这代表的就是以恒定速度 $a$ 向左和向右传播的两个波的叠加。

接下来我们代入初值：

$$
\begin{cases}
\eval{u}_{t=0} = \psi(x) \Rightarrow f(x) + g(x) = \psi(x)\\
\eval{\pdv{u}{t}}_{t=0} = \phi(x)\Rightarrow -af'(x) + ag'(x) = \phi(x)
\end{cases}
$$

对后项积分也就是：

$$
f(x) - g(x) = -\frac{1}{a}\int_0^x \phi(s)\dd s + C
$$

这就可以解出：

$$
\begin{cases}
f(x) = \frac12 \psi(x) - \frac{1}{2a}\int_0^x\phi(s)\dd s + \frac{C}{2} \\
g(x) = \frac12 \psi(x) + \frac{1}{2a}\int_0^x\phi(s)\dd s - \frac{C}{2}
\end{cases}
$$

带回通解就是：

$$
u(x,t) = \frac{1}{2}\pqty{\psi(x-at) + \psi(x+at)} + \frac{1}{2a}\int_{x-at}^{x+at}\phi(s)\dd s
$$

从物理意义来看，第一项代表初始位移激发的波，其分成两份独立向左向右传播；第二项代表初始速度激发的波，其左右对称地扩展到 $(x-at, x+at)$。它们的传播速率均为 $a$。通过这样求解的方法称为**行波法**。

---

## 3. 分离变量法

### 得到本征方程

回到热传导问题的初始问题：

$$
\begin{cases}
\pdv{u}{t} - \kappa \pdv[2]{u}{x} = 0&, t > 0\\
\eval{u}_{t=0} = \psi(x)\\
u(0,t) = u(l,t) = 0
\end{cases}
$$

我们不妨认为通解满足：

$$
u(x,t) = X(x)T(t)
$$

这样原式子就满足：

$$
\frac{T'(t)}{T(t)} - \kappa \frac{X''(x)}{X(x)} = 0
$$

于是我们可以设：

$$
\frac{T'(t)}{\kappa T(t)} = \frac{X''(x)}{X(x)} = -\lambda
$$

其中 $T(t)$ 与 $x$ 无关，$X(x)$ 与 $t$ 无关，而常数 $\lambda$ 和两者都无关。我们把 $X(x)$ 的分式拆开，结合边界条件可以得到：

$$
\begin{cases}
X''(x) + \lambda X(x) = 0\\
X(0) = X(l) = 0
\end{cases}
$$

这个问题我们称为**本征值问题**。

同理对于 $T(t)$ ：

$$
T'(t) + \kappa\lambda T(t) = 0
$$

这就完成了分离变量。

---

同理可以看看两端固定的弦振动问题：

$$
\begin{cases}
\pdv{u}{t} - a^2 \pdv[2]{u}{x} = 0&, t > 0\\
u(0,t) = u(l,t) = 0\\
\eval{u}_{t=0} = \phi(x)\\
\eval{\pdv{u}{t}}_{t=0} = \psi(x) \\
\end{cases}
$$

设 $u = T(t)X(x)$ 得到：

$$
\frac{T''(t)}{T(t)} - a^2 \frac{X''(x)}{X(x)} = 0
$$

得到的本征值问题就是：

$$
\begin{cases}
X''(x) + \lambda X(x)=0\\ X(0)=X(l)=0
\end{cases}\qc T''(t) + a^2\lambda T(t) = 0
$$

> eg：氢原子的Schrodinger方程：
>
> $$
> \mathrm{i}\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2\mu} \left[ \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial \psi}{\partial r} \right) + \frac{1}{r^2 \sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial \psi}{\partial \theta} \right) + \frac{1}{r^2 \sin^2\theta} \frac{\partial^2 \psi}{\partial \phi^2} \right] - \frac{e^2}{4\pi\varepsilon_0 r} \psi
> $$
>
> 把波函数拆解为：
>
> $$
> \psi(r,\theta,\phi,t) = R(r)\Theta(\theta)\Phi(\phi)T(t)
> $$
>
> 代入得到：
>
> $$
> \mathrm{i}\hbar \frac{T'(t)}{T(t)} = -\frac{\hbar^2}{2\mu} \left[ \frac{[r^2R'(r)]'}{r^2R(r)} + \frac{[\sin\theta\Theta'(\theta)]'}{r^2 \sin\theta\Theta(\theta)} + \frac{\Phi''(\phi)}{r^2 \sin^2\theta\Phi(\phi)} \right] - \frac{e^2}{4\pi\varepsilon_0 r} = E
> $$
>
> 首先可以分离时间 $T$：
>
> $$
> \boxed{i\hbar T'(t) -ET(t) = 0}
> $$
>
> 原式化为：
>
> $$
> -\frac{\hbar^2}{2\mu} \left[ \frac{[r^2R'(r)]'}{r^2R(r)} +\frac1{r^2} (\frac{[\sin\theta\Theta'(\theta)]'}{ \sin\theta\Theta(\theta)} + \frac{\Phi''(\phi)}{ \sin^2\theta\Phi(\phi)}) \right] - \frac{e^2}{4\pi\varepsilon_0 r} = E
> $$
>
> 角度部分不含 $R(r)$，直接分离掉：
>
> $$
> \frac{[\sin\theta\Theta'(\theta)]'}{ \sin\theta\Theta(\theta)} + \frac{\Phi''(\phi)}{ \sin^2\theta\Phi(\phi)} = \lambda
> $$
>
> 之后再设：
>
> $$
> \boxed{\Phi''(\phi) + \mu\Phi(\phi) = 0}
> $$
>
> 原式化为：
>
> $$
> \frac{[\sin\theta\Theta'(\theta)]'}{ \sin\theta\Theta(\theta)} + \frac{\mu}{ \sin^2\theta} = \lambda
> $$
>
> 进一步化简为：
>
> $$
> \boxed{-\frac{1}{\sin^2\theta}\qty[\sin\theta\dv{\theta}(\sin\theta\dv{\theta})-\mu]\Theta(\theta) = \lambda\Theta(\theta)}
> $$
>
> 然后再回到径向的式子：
>
> $$
> -\frac{\hbar^2}{2\mu} \left[ \frac{[r^2R'(r)]'}{r^2R(r)} +\frac{\lambda}{r^2} \right] - \frac{e^2}{4\pi\varepsilon_0 r} = E
> $$
>
> 最后化简得到：
>
> $$
> \boxed{\qty[-\frac{\hbar^2}{2\mu r^2} \left[ \dv{r}(r^2\dv{r}R(r)) +\lambda \right] - \frac{e^2}{4\pi\varepsilon_0 r}]R(r) = ER(r)}
> $$
>
> 这就完成了分离变量。可以看到，引入常数数量是独立变量数-1。

---

### 求解本征值问题

先来看本征值问题，如果 $X''(x) = 0$，就意味着这是一个线性方程，而由于边界条件：

$$
b=kl+b = 0
$$

这意味着 $\lambda = 0$，也就是只有零解。我们说0不是本征值。

如果 $\lambda \neq 0$，这意味着：

$$
X(x) = A\sin\sqrt{\lambda}x + B\cos\sqrt{\lambda}x
$$

代入边界条件：

$$
B= A\sin\sqrt{\lambda}l = 0
$$

这意味着必有：

$$
\begin{cases}
\lambda_n = \qty(\frac{n\pi}{l})^2\\
X_n(x) = \sin(\frac{n\pi x}{l})
\end{cases}
$$

其中 $\lambda_n$ 称为本征值， $X_n(x)$ 称为本征函数。$n$ 为所有正整数。

这个时候 $T(t)$ 也很容易求，我们结合在一起：

$$
u(x,t)=X(x)T(t) = C_n e^{-\kappa \lambda_n t}\sin(\frac{n\pi x}{l})
$$

这个解我们叫做**特解**，将特解叠加可以得到**一般解**：

$$
u(x,t) = \sum_{n=1}^\infty C_n e^{-\kappa \lambda_n t}\sin(\frac{n\pi x}{l})
$$

要得到通解就要利用到初值条件了。我们有：

$$
u(x,0) = \sum_{n=1}^\infty C_n \sin(\frac{n\pi x}{l}) = \psi(x)
$$

我们知道本征函数具有正交性，现在我们再叠加一个本征函数并积分，尝试把常数表示出来：

$$
\int_0^l\sum_{n=1}^\infty C_n \sin(\frac{n\pi x}{l})\sin(\frac{m\pi x}{l}) \dd{x} = \int_0^l\psi(x)\sin(\frac{m\pi x}{l})\dd{x}
$$

交换积分和求和（这是一个平均收敛的函数）：

$$
\begin{aligned}
&\int_0^l\sum_{n=1}^\infty C_n \sin(\frac{n\pi x}{l})\sin(\frac{m\pi x}{l}) \dd{x} \\
&= \sum_{n=1}^\infty C_n \int_0^l\sin(\frac{n\pi x}{l})\sin(\frac{m\pi x}{l}) \dd{x}\\
&= \sum_{n=1}^\infty \frac{l}{2}C_n\delta_{nm} = \frac{l}{2}C_m
\end{aligned}
$$

这样就可以得到 $C_n$ 的值了。

> 总结：
>
> 1. 分离变量；
> 2. 求解本征值问题；
> 3. 求出特解，叠加得到一般解；
> 4. 通过正交性得到通解。

同理我们求解本征值问题：

$$
\begin{cases}
X''(x) + \lambda X(x)=0\\ X(0)=X(l)=0
\end{cases}\qc T''(t) + a^2\lambda T(t) = 0
$$

根据边界条件得到：

$$
X_n(x) = \sin(\sqrt{\lambda_n} x)\qc \lambda_n = \qty(\frac{n\pi}{l})^2
$$

又有：

$$
u(x,t) = T(t)X_n(x) = \qty(C_n \sin(\sqrt{\lambda_n} at) + D_n \cos(\sqrt{\lambda_n} at))\sin(\sqrt{\lambda_n} x)
$$

叠加得到一般解：

$$
u(x,t) = \sum_{n=1}^\infty\qty(C_n \sin(\sqrt{\lambda_n} at) + D_n \cos(\sqrt{\lambda_n} at))\sin(\sqrt{\lambda_n} x)
$$

之后同样乘正交值并积分，得到常数：

$$
\begin{gathered}
D_n = \frac{2}{l}\int_0^l \phi(x)\sin(\frac{n\pi x}{l})\dd{x}\\
C_n = \frac{2}{n\pi a}\int_0^l \psi(x)\sin(\frac{n\pi x}{l})\dd{x}
\end{gathered}
$$

---

### 本征值问题的性质

我们来看本征值问题的几个性质。

> **本征值问题的本征值一定是实数。**

我们不妨取复共轭

$$
\begin{cases}
X''^*(x) + \lambda^* X^*(x) = 0\\
X^*(0) = X^*(l) = 0
\end{cases}
$$

之后交叉相乘相减：

$$
[X^*(x)X''(x) - X(x)X''^*(x)] + (\lambda-\lambda^*)X^*(x)X(x) = 0
$$

积分得到：

$$
\begin{aligned}
&\int_0^l\qty[X^*(x)X''(x) - X(x)X''^*(x)] + (\lambda-\lambda^*)\int_0^lX^*(x)X(x)\\
&=\eval{\qty[X^*(x)X'(x) - X(x)X'^*(x)]}_0^l + (\lambda-\lambda^*)\int_0^lX^*(x)X(x)\\
&=  (\lambda-\lambda^*)\int_0^lX^*(x)X(x) = 0
\end{aligned}
$$

于是 $\lambda = \lambda^*$，即本征值为实数。

> **本征值问题的不同本征值对应本征函数正交。**

我们取另一个函数的复共轭：

$$
\begin{cases}
X_m''^*(x) + \lambda_m X_m^*(x) = 0\\
X_m(0) = X_m(l) = 0
\end{cases}
$$

交叉相乘相减：

$$
[X^*_m(x)X''_n(x) - X_n(x)X''^*_m(x)] + (\lambda_n-\lambda_m)X^*_m(x)X_n(x) = 0
$$

积分：

$$
\begin{aligned}
&\int_0^l[X^*_m(x)X''_n(x) - X_n(x)X''^*_m(x)] + (\lambda_n-\lambda_m)X^*_m(x)X_n(x)\\
&=\eval{\qty[X^*_m(x)X'_n(x) - X_n(x)X'^*_m(x)]}_0^l + (\lambda_n-\lambda_m)\int_0^lX^*_m(x)X_n(x)\\
&=  (\lambda_n-\lambda_m)\int_0^lX^*_m(x)X_n(x) = 0
\end{aligned}
$$

由于本征值不同，于是 $\int_0^lX^*_m(x)X_n(x) = 0$，即本征函数正交。

---

### 稳定方程

考虑一个矩形区域 $[0,a]\times[0,b]$ 的稳定问题：

$$
\begin{cases}
\pdv[2]{u}{x}+\pdv[2]{u}{y} = 0\\
\eval{u}_{x=0}=0\qc\eval{\pdv{u}{x}}_{x=a}=0\\
\eval{u}_{y=b}=0\qc\eval{\pdv{u}{y}}_{y=0}=f(x)\\
\end{cases}
$$

我们可以分离变量 $u(x,y) = X(x)Y(y)$，分离变量：

$$
\frac{X''(x)}{X(x)}+\frac{Y''(y)}{Y(y)}=0
$$

写出本征方程：

$$
\begin{cases}
X''(x) +\lambda X(x)=0\\
X(0) = X'(a) = 0
\end{cases}\qc Y''(y) -\lambda Y(y)=0
$$

先求解 $X(x)$，排除 $\lambda = 0$ 的零解，求得：

$$
X(x) = A\sin(\sqrt{\lambda}x) + B\cos(\sqrt{\lambda}x)
$$

代入边界条件：

$$
\begin{cases}
B=0\\
A\cos(\sqrt{\lambda}a)=0
\end{cases}
$$

又因为非零解，$A\neq0$，所以只能是：

$$
\sqrt{\lambda}a = \frac{\pi}{2}+n\pi\Rightarrow\lambda_n = \pqty{\frac{2n+1}{2a}\pi}^2
$$

于是：

$$
\boxed{X(x) = A\sin(\frac{2n+1}{2a}\pi x)}
$$

同理可以解得：

$$
Y(y) = A_n\sinh(\sqrt{\lambda_n}y)+B_n\cosh(\sqrt{\lambda_n}y)
$$

代入边界条件：

$$
A_n\sinh(\sqrt{\lambda_n}b)+B_n\cosh(\sqrt{\lambda_n}b)=0
$$

于是原式可以化为：

$$
\boxed{Y(y) = C_n\sinh(\frac{2n+1}{2a}\pi (y-b))}
$$

这样相乘并叠加得到一般解：

$$
u_n(x,y) =\sum_{n=0}^\infty C_n\sinh(\frac{2n+1}{2a}\pi (y-b))\sin(\frac{2n+1}{2a}\pi x)
$$

再根据边界条件：

$$
\eval{\pdv{u}{y}}_{y=0} =\sum_{n=0}^\infty C_n\frac{2n+1}{2a}\pi\cosh(\frac{2n+1}{2a}\pi b)\sin(\frac{2n+1}{2a}\pi x) = f(x)
$$

同样根据正交性积分：

$$
\begin{aligned}
&\int_0^a\sum_{n=0}^\infty C_n\frac{2n+1}{2a}\pi\cosh(\frac{2n+1}{2a}\pi b)\sin(\frac{2n+1}{2a}\pi x)\sin(\frac{2m+1}{2a}\pi x)\\
&= C_m\frac{2m+1}{2a}\pi\cosh(\frac{2m+1}{2a}\pi b) = \int_0^a f(x)
\end{aligned}
$$

这样就得到通解了。

---

### 非齐次方程——同时齐次化

对于受迫弦振动问题：

$$
\begin{cases}
\pdv[2]{u}{t} - a^2 \pdv[2]{u}{x} = f(x,t)&, t > 0\\
u(0,t) = u(l,t) = 0\\
\eval{u}_{t=0} = \eval{\pdv{u}{x}}_{t=0} =0\\
\end{cases}
$$

这里我们把 $u(x,t)$ 拆成两个函数：

$$
u(x,t) = v(x,t) + w(x,t)
$$

分别满足：

$$
\begin{cases}
\pdv[2]{v}{t} - a^2 \pdv[2]{v}{x} = f(x,t)\\
v(0,t) = v(l,t) = 0\\
\end{cases}\qc
\begin{cases}
\pdv[2]{w}{t} - a^2 \pdv[2]{w}{x} = 0\\
w(0,t) = w(l,t) = 0\\
\eval{w}_{t=0} = -\eval{v}_{t=0}\qc \eval{\pdv{w}{x}}_{t=0} = -\eval{\pdv{v}{x}}_{t=0}
\end{cases}
$$

> 特例1： $f(x)$ 与 $t$ 无关。可以设 $v(x,t) = v(x)$ 满足：
>
> $$
> \begin{cases}
> - a^2 \pdv[2]{v}{x} = f(x)\\
> v(0) = v(l) = 0\\
> \end{cases}
> $$
>
> 特例2：$f(x,t)=g(x)\sin\omega t$。可设 $v(x,t) = h(x)\sin\omega t$ ，此时有：
>
> $$
> \begin{cases}
> -\omega^2h(x)- a^2 h''(x) = g(x)\\
> h(0) = h(l) = 0\\
> \end{cases}
> $$

这样通过第一个式子，就可以把 $v(x,t)$ 解出来。之后解 $w(t)$ 就是经典的问题了。

---

### 非齐次方程——按本征函数展开

我们还是考虑齐次的问题：

$$
\begin{cases}
\pdv[2]{u}{t} - a^2 \pdv[2]{u}{x} = 0\\
u(0,t) = u(l,t) = 0\\
\end{cases}
$$

> 注意这里不能取初始条件 $\eval{u}_{t=0} = \eval{\pdv{u}{x}}_{t=0} =0\\$，因为该条件会得出原方程只有零解的结论。

对于齐次的情况我们知道：

$$
u(x,t) = \sum_{n=1}^\infty T_n(t)\sin\frac{n\pi}{l}x
$$

我们尝试将 $f(x,t)$ 也按这种方法展开：

$$
f(x,t) = \sum_{n=1}^\infty f_n(t)\sin\frac{n\pi}{l}x
$$

全部代入初始式子：

$$
\sum_{n=1}^\infty \qty[T''_n(t)\sin\frac{n\pi}{l}x+a^2\qty(\frac{n\pi}{l})^2T_n(t)\sin\frac{n\pi}{l}x-f_n(t)\sin\frac{n\pi}{l}x] = 0
$$

之后同样乘正交基并积分，最后这个方程就转化为：

$$
\begin{cases}
T''_n(t) +a^2\qty(\frac{n\pi}{l})^2T_n(t)-f_n(t)=0\\
T(0) = T'(0) = 0
\end{cases}
$$

这是一个二阶常微分方程，一定有解。这样理论上就可以把原方程解出来了。

---

### 非齐次边界条件

我们把边界条件改成这样：

$$
\begin{cases}
\pdv[2]{u}{t} - a^2 \pdv[2]{u}{x} =0\\
u(0,t) = \psi(t), u(l,t) = \phi(t)\\
\eval{u}_{t=0} = \eval{\pdv{u}{x}}_{t=0} =0\\
\end{cases}
$$

同样拆成两个函数：

$$
u(x,t) = v(x,t) + w(x,t)
$$

我们让 $v(x,t)$ 满足边界条件，这样 $w(x,t)$ 的边界条件就是齐次的了：

$$
v(0,t) = \psi(t), v(l,t) = \phi(t)
$$

> 一种可能的取法是取线性函数 $v(x,t) = \psi(t)+\frac{\phi(t)-\psi(t)}{l}x$.

这样 $w(x,t)$ 就满足：

$$
\begin{cases}
\pdv[2]{w}{t} - a^2 \pdv[2]{w}{x} = -\pdv[2]{v}{t} + a^2 \pdv[2]{v}{x} \\
w(0,t) = w(l,t) = 0\\
\eval{w}_{t=0} = -\eval{v}_{t=0}\qc \eval{\pdv{w}{x}}_{t=0} = -\eval{\pdv{v}{x}}_{t=0}
\end{cases}
$$

这就转化为了非齐次方程的情况，如果 $v(x,t)$ 选的好，使 $-\pdv[2]{v}{t} + a^2 \pdv[2]{v}{x} = 0$，那就转化成更简单的齐次方程了。

就算初始条件也是非齐次方程，只需要把后面一项改成 $-\pdv[2]{v}{t} + a^2 \pdv[2]{v}{x} + f(x,t)$ 即可。

$$
\begin{cases}
\pdv[2]{w}{t} - a^2 \pdv[2]{w}{x} = -\pdv[2]{v}{t} + a^2 \pdv[2]{v}{x}+f(x,t) \\
w(0,t) = w(l,t) = 0\\
\eval{w}_{t=0} = -\eval{v}_{t=0}\qc \eval{\pdv{w}{x}}_{t=0} = -\eval{\pdv{v}{x}}_{t=0}
\end{cases}
$$

> 特例：
>
> $$
> \begin{cases}
> \pdv[2]{u}{t} - a^2 \pdv[2]{u}{x} =0\\
> u(0,t) = \sin\omega t, u(l,t) = 0\\
> \eval{u}_{t=0} = \eval{\pdv{u}{x}}_{t=0} =0\\
> \end{cases}
> $$
>
> 可以设 $u = f(x)\sin\omega t$，就有：
>
> $$
> \begin{cases}
> -\omega^2f(x) - a^2 f''(x) =0\\
> f(0) = 1, f(1) = 0\\
> \end{cases}
> $$

---

