# 线性代数概要

> 说明：这份资料本质上是**对结论的总结**，供快速阅览和查找用。不适合任何形式的线性代数考试。

## 1. 线性方程组

### 行列式



---

### Cramer 法则

如果有 $n$ 个方程的 $n$ 元线性方程组有唯一解时，系数矩阵满足：

$$
\abs{A} = \mqty|a_{11}& a_{12}& \cdots &a_{1n} \\ a_{21} &a_{22}&\cdots&a_{2n} \\ \vdots&\vdots&\vdots&\vdots\\a_{n1}&a_{n2}&\cdots&a_{nn}| \neq 0
$$

且解集为：

$$
\qty(\frac{|B_1|}{|A|},\frac{|B_2|}{|A|},\cdots,\frac{|B_n|}{|A|})
$$

其中：

$$
\abs{B_j} = \mqty|a_{11}& \cdots& a_{1,(j-1)}&b_1&a_{1,(j-1)}&\cdots &a_{1n}  \\ a_{21}& \cdots& a_{2,(j-1)}&b_2&a_{2,(j-1)}&\cdots &a_{2n}\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\a_{n1}& \cdots& a_{n,(j-1)}&b_n&a_{n,(j-1)}&\cdots &a_{nn}|
$$

---

