# 固体物理学 Solid State Physics

## Lecture 1: 晶体结构 Structure of Crystals

### 1.1 Lattice 点阵

点阵有三种定义：

- 由**线性无关的基矢集合** (set of linearly independent primitive lattice vectors) 的整数倍加和构成的**无限点集**；
- 一个无限向量集，其中任意两个向量加和得到的向量仍在集合中；
- 无限点集，任意两点环境相同。

一系列关于向量的定义：

- **格矢** (lattice vector)：任意一个从一个点阵点指向另一点阵点的矢量；
- **基矢** (primitive lattice vectors)：可产生点阵的最少数量格矢集合（线性无关）；
- **最短基矢** (shortest primitive lattice vectors)：基矢集合中矢量长度最短的一个。

---

### 1.2 Unit Cell 晶胞

晶胞是可通过平移堆积完全填满整个空间并表示点阵结构的**空间区域**。

- **素晶胞** (primitive unit cell)：晶胞内仅含一个点阵点；
- **正当晶胞** (conventional unit cell)：满足正当晶胞原则；
- **Wegner-Seitz 原胞** (Wegner-Seitz unit cell)：由垂直平分面/线围成（对于一个点阵点周围的W-S原胞区域是满足到该点阵点距离小于任意一个其他点阵点的所有点构成的轨迹 (locus) ）。

关于晶胞的具体分类已在结构化学晶体讲义中提到。

---

## Lecture 2：晶体的衍射表征 Diffraction by crystals

### 2.1 倒易点阵(resiprocal lattice)

定义：如果一个点阵是R，那么对于点G，满足 $e^{iG\cdot R} = 1$ 的所有点G在倒易点阵内。也可以看作是原点阵的傅里叶变换。倒易空间实际上是由波矢 $k$ 构建的空间 ，因此数量维度是长度的倒数。

另一种更加直观的定义方法：对于素晶胞的三个基矢 $a_1, a_2, a_3$，倒易点阵的三个基矢 $b_1, b_2, b_3$ 满足：

$$
a_i \cdot b_j = 2\pi \delta_{ij}
$$

例如：对于基矢为 $a$ 的直线点阵，晶格矢量为 $na$ ，这对应倒易空间内基矢为 $2\pi / a$ ；对于简单立方点阵，会得到边长为 $2\pi/a$ 的简单立方倒易点阵，体心立方和面心立方倒易点阵互换。

<img src="Solid_State_Physics.assets/960px-Superstructures_in_low-energy_electron_diffraction_(LEED).svg.png" alt="undefined" style="zoom:33%;" />

六方点阵的倒易点阵也是六方点阵：

<img src="Solid_State_Physics.assets/image-20260306160733858.png" alt="image-20260306160733858" style="zoom:50%;" />

对于菱面体晶胞，它的倒易点阵也是菱面体晶胞，但是形状不同。

对于三维情况，有公式：

$$
\begin{cases}
b_1 = \frac{2\pi a_2\times a_3}{V}\\
b_2 = \frac{2\pi a_3\times a_1}{V}\\
b_3 = \frac{2\pi a_1\times a_2}{V}
\end{cases}
\qc V = a_1 \cdot(a_2\times a_3)
$$

在倒易点阵内定义的一个晶胞被称为布里渊区（Brillouin zone）。按照通常点阵方法画出的Wigner-Zeise晶胞被称为第一布里渊区（first Brillouin zone）。

![image-20260306160906969](Solid_State_Physics.assets/image-20260306160906969.png)

---

### 2.2 晶面(lattice plane)和晶向(lattice direction)

参考晶体讲义。

对于六方晶胞，有时也采取四轴定向的方法。

<img src="Solid_State_Physics.assets/image-20260304151020751.png" alt="image-20260304151020751" style="zoom:33%;" />

---

### 2.3 衍射 (Diffraction)定律

在结构化学里，我们已经知道Bragg衍射定律：

$$
2d\sin\theta = n\lambda
$$

<img src="Solid_State_Physics.assets/image-20260305222010811.png" alt="image-20260305222010811" style="zoom: 67%;" />

不幸的是，这只给出了类似“反射”的单角度衍射。对于晶体来说，在其他方向上也可能存在衍射峰，我们假设入射光的波矢是 $\vb k$，出射光的波矢是 $\vb k'$，这两个波矢方向不同的大小相等（弹性散射不改变能量）。

我们从Fermi黄金法则出发：

$$
\Gamma(k',k) = \frac{2\pi}{\hbar}\abs{\mel{k'}{V}{k}}^2\delta(E_{k'} - E_k)
$$

代入平面波函数的表达式：

$$
\psi_k(r) = \frac{1}{\sqrt{L^3}}e^{ikr}
$$

于是内部矩阵元变为：

$$
\mel{k'}{V}{k} = \frac{1}{L^3}\int\dd r V(r) e^{-i(k'-k)r}
$$

这也就是势能函数的傅里叶变换。

由于平移对称性，我们假设一个晶胞内部的坐标是 $\vb x$，格矢为 $\vb R$，即可以设 $\vb r = \vb R+\vb x$ 。由于环境完全相同，这两个点的势能完全相同，也就是 $V(\vb x)=V(\vb x+\vb R)$。我们带入到原式，把它转化成一个晶胞内的积分：

$$
\begin{aligned}
\mel{k'}{V}{k} &= \frac{1}{L^3}\int\dd r V(r) e^{-i(k'-k)r} \\
&= \frac{1}{L^3}\sum_{\vb R}\int_{cell}\dd x\ e^{-i(k'-k)(\vb x + \vb R)}V(\vb x + \vb R) \\
&= \frac{1}{L^3}\pqty{\sum_{\vb R}e^{-i(k'-k)\vb R}}\pqty{\int_{cell}\dd x\ e^{-i(k'-k)\vb x}V(\vb x)} \\
\end{aligned}
$$

注意看第一项括号 $\pqty{\sum_{\vb R}e^{-i(k'-k)\vb R}}$。由于Poisson求和，有：

$$
\sum_{\vb R}e^{-i(k'-k)\vb R} \propto \sum_{\vb G}\delta(k'-k-G)
$$

这意味着只有当 $k' - k = G$ 时，原式才不为0. 这被称为**Laun方程**（Laun condition）。这同时也告诉我们在晶体内散射动量不守恒，也就是 $k' = k + G$，这被称为**晶体动量守恒**。

回到Bragg方程。考虑一束光从 $\hat x$ 方向射入：

![image-20260309132512878](Solid_State_Physics.assets/image-20260309132512878.png)

这个时候晶胞的倒易点阵：

$$
\vb G = 2\pi n \hat x /d
$$

从纯几何的考虑，我们知道向量点乘：

$$
\vb G \cdot \vb k = \vb G \cdot \vb k' = |\vb G||\vb k|\sin \theta
$$

于是我们有：

$$
\begin{aligned}
|\vb G|^2 &= \vb G \cdot \vb G = \vb G \cdot (\vb k - \vb k')\\
&= \vb G \cdot \vb k - \vb G \cdot \vb k'\\
&= 2|\vb G||\vb k|\sin \theta
\end{aligned}
$$

这也就是说：

$$
\frac{2\pi n}{d} = 2\frac{2\pi}{\lambda}\sin\theta
$$

化简之后就能得到 Bragg 方程。

---

### 2.4 结构因子 (Structure factor)

我们来看第二项括号 $\pqty{\int_{cell}\dd x\ e^{-i(k'-k)\vb x}V(\vb x)}$ 。在固体物理里，我们一般用**结构因子** (Structure Factor) 称呼它：

$$
S(\vb G) = \int_{cell}\dd{\vb x}\ e^{-i\vb G \cdot \vb x}V(\vb x)
$$

我们考虑把势能分解成晶胞内各个原子的函数：

$$
V(\vb x) = \sum_{\text{all j in cell}} f_jg(\vb x - \vb x_j)
$$

进一步化简得到：

$$
\begin{aligned}
S(\vb G) &= \int_{cell}\dd {\vb x}\ \pqty{\sum_{\text{all j in cell}} f_jg(\vb x - \vb x_j)}e^{-i\vb G \cdot \vb x} \\
&= \sum_{\text{all j in cell}} \pqty{\int_{cell}\dd{\vb x}  f_jg(\vb x - \vb x_j) e^{-i\vb G \cdot \vb x}}\\
&= \sum_{\text{all j in cell}} \pqty{\int_{cell}\dd{(\vb x - \vb x_j)}  f_jg(\vb x - \vb x_j) e^{-i\vb G \cdot \vb (\vb x - \vb x_j)}}e^{i\vb G \cdot \vb x_j} \\
&= \sum_{\text{all j in cell}} f_j(\vb G) e^{i\vb G \cdot \vb x_j}
\end{aligned}
$$

这也就是说，假设我们知道晶胞内原子的分数坐标 $(n_j , m_j, p_j)$，我们就可以得到：

$$
\begin{aligned}
S(\vb G) &= \sum_{\text{all j in cell}} f_j(\vb G) e^{i\vb G \cdot \vb x_j} \\
&= \sum_{\text{all j in cell}} f_j(\vb G) e^{i(h\vb b_1 + k \vb b_2 + l \vb b_3) \cdot (n_j \vb a_1 + m_j \vb a_2 + p_j \vb a_3)} \\
&= \sum_{\text{all j in cell}} f_j(\vb G) e^{2\pi i(hn_j + km_j + lp_j)}
\end{aligned}
$$

这就是结构因子的最终表达式。将晶胞内各原子的 $f_j(\vb G) e^{2\pi i(hn_j + km_j + lp_j)}$ 加起来，得到的结构因子回合衍射强度成正比：

$$
\Gamma(k',k) \propto S(\vb G)
$$

> 求 $\ce{CsCl}$ 晶体的结构因子。原子坐标：Cs: (0, 0, 0) ; Cl: (1/2, 1/2, 1/2)。
>
> ![image-20260309142644371](Solid_State_Physics.assets/image-20260309142644371.png)
>
> 直接代入各原子坐标：
>
> $$
> \begin{aligned}
> S(\vb G) &= f_{\ce{Cs}} + f_{\ce{Cl}} e^{2\pi i(h/2 + k/2 + l/2)}\\
> &=  f_{\ce{Cs}} + f_{\ce{Cl}} e^{\pi i(h + k + l)}
> \end{aligned}
> $$
>
> 这意味着当 $(h+k+l)$ 为偶数时，$S(\vb G) = f_{\ce{Cs}} + f_{\ce{Cl}}$，得到一个强衍射峰；而当 $(h+k+l)$ 为奇数时，$S(\vb G) = f_{\ce{Cs}} - f_{\ce{Cl}}$，得到一个较弱的衍射峰。特别的，如果对于一个晶体体心和顶点原子相同，就有 $S(\vb G) = 0$，对应没有衍射峰。这种现象也被叫做**系统消光**（systematic extinction）。

---

### 2.5 Ewald 球 (Ewald's sphere)

前面我们知道，入射和出射波矢的矢量差就对应倒易点阵里的一个格矢，并且由于弹性散射，它们的模相同。假设我们有一个端点在倒易点阵点上的入射波矢 $\vb k_0$ ，入射方向固定，画一个球：

<img src="Solid_State_Physics.assets/Ewald3.png" alt="undefined" style="zoom: 33%;" />

在这个球面上还存在另一个球心到球面且正好在倒易点阵点上的矢量 $\vb k_1$，这里就能满足 $\vb k_1 - \vb k_0 = \vb G$ 且模相同了。这个时候就能在 $\vb k_1$ 的位置观测到一个衍射峰。

如何获得多组数据呢？

- **Laue 法**：固定晶体位置和入射光方向，改变入射光能量（也就是 $|\vb k_0|$），这个时候对应 Ewald 球的半径不断增大，就能找到不同半径对应的出射向量。

  <img src="Solid_State_Physics.assets/image-20260309141118395.png" alt="image-20260309141118395" style="zoom: 67%;" />

- **旋转晶体法**：固定入射光方向和波长，旋转单晶，对应倒易点阵发生旋转（相对来看，也就是Ewald球发生旋转）。这就能得到不同角度对应的衍射峰。

  <img src="Solid_State_Physics.assets/image-20260309141253064.png" alt="image-20260309141253064" style="zoom: 67%;" />

- **粉末法**：直接用晶体粉末进行衍射，这样就相当于有很多各个方向的微小单晶同时进行衍射了。

  <img src="Solid_State_Physics.assets/image-20260309141432395.png" alt="image-20260309141432395" style="zoom:67%;" />

---

## Lecture 3：点阵的对称性与群 Symmetry of Lattice

### 3.1 对称操作(Symmetry transformation)

具体已在结构化学中提及，包括：

- 平移（Translation）；
- 旋转（Rotation）；
- 反映（Reflection）；
- 反演（Inversion）；
- 滑移反映（Glide Reflection）和 反映旋转（Improper Rotation）。

---

### 群 (Group)

> 对于一个集合 $G$ 和一个运算 $*$ （称为**群乘积**(group multiplication)），满足：
>
> - 任意两个集合中的元素 $a,b$，满足 $(a*b) \in G$
> - 结合律（Associative）：$(a*b)*c = a*(b*c)$
>
> - 单位元素（Identity）：$\exist\ e \in G, \ a*e = a$
> - 逆元素（Inversion）：$\exist\ a^{-1} \in G, \ a*a^{-1} = e$
>
> 这样 $G(*)$ 就被称为一个**群**（Group）。集合中元素的数量被称为群的**势**（cardinalty）。

---

（接下来基本都是对称性相关的简单内容，略过。）

---

