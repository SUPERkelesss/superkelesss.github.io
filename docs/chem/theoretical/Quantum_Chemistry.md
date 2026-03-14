# 量子化学 Quantum Chemistry

## 1. 数学快速准备

### 1.1 线性代数

> 推荐教材：
>
> - Gilbert Strang, Introduction to Linear Algebra 5th-ed (Wellesley, 2016).
> - 丘维声，《简明线性代数》(北京大学出版社，2002).
> - F.W. Byron, Jr. and R. W. Fuller, Mathematics of Classical and Quantum  Physics (Dover 1992)
> - R. A. Horn, C. R. Johnson, Matrix Analysis (2nd ed.) (Cambridge Uni. Press 2012).

---

一些简单定义：

- 单位矩阵 $I$：$I_{ij} = \delta_{ij} =
  \begin{cases}
  1&,i=j\\
  0&,i\neq j
  \end{cases}$

- 矩阵的逆：$(AB)^{-1} = B^{-1}A^{-1}$
- 矩阵的转置：$\mathbf{A}^{\mathsf{T}}_{ij} = A_{ji}$
- 矩阵的厄米共轭：$(\mathbf{A})_{ij}^{\dagger} = A_{ji}^*$
- 厄米（Hermitian）矩阵：$\mathbf{A}^{\dagger} = \mathbf{A}$
- 幺正（unitary）矩阵：$\mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A} \mathbf{A}^{\dagger} = \mathbf{I}$
- 正交矩阵：$\sum_k A^*_{ki} A_{kj} = \sum_k A^*_{ik} A_{jk} = \delta_{ij}$
- 矩阵的迹：$\operatorname{Tr} \mathbf{A} = \sum_i A_{ii}$，$\operatorname{Tr}(\mathbf{A}\mathbf{B}) = \operatorname{Tr}(\mathbf{B}\mathbf{A})$
- 相似/幺正/正交变换：$\mathbf{A} = \mathbf{T}^{-1} \mathbf{B} \mathbf{T}$
- 矢量的内积：$\boldsymbol{u} \cdot \boldsymbol{v} = \boldsymbol{u}^{\dagger} \boldsymbol{v}$
- 幂等矩阵：$\mathbf{P}^2 = \mathbf{P}$

---

排列算符（将矩阵元素排列为一种形式）：

$$
\mathcal P_I(1,2,\cdots,n) = (I_1, I_2, \cdots ,I_n)
$$

互换算符（排列算符的分解，包含奇数/偶数次互换的排列称为奇/偶排列）：

$$
\mathcal P_{ij}(\cdots,i,\cdots,j,\cdots) = (\cdots,j,\cdots,i,\cdots)
$$

一般定义：

$$
\abs{\vb A} =
$$

---

中道崩殂了。明年再战！

---





































