# `physics` 宏包常用命令

> 目前中文网络上关于 `physics` 包的资料比较少，尽管这个包现在已经停止维护了，但是确实大大方便了公式的输入，方便课堂笔记书写。于是我将一些常用的命令整理在这里。
>
> 本文档部分翻译自：[The Physics Package](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf)。

## 1. 自动括号

### 自动匹配括号 `\quantity`

|     简拼      |                效果                 | 注释                                     |
| :-----------: | :---------------------------------: | :--------------------------------------- |
|   `\qty()`    | $\displaystyle\qty(\frac{aa}{bb})$  | 自动匹配大小，效果相当于`\left( \right)` |
|   `\qty[]`    | $\displaystyle\qty[\frac{aa}{bb}]$  | `\qty`后面是什么括号就显示什么括号       |
|   `\qty{}`    | $\displaystyle\qty{\frac{aa}{bb}}$  |                                          |
| `\qty\big{}`  |      $\displaystyle\qty\big{}$      | 也可以手动调节大小                       |
| `\qty\Big{}`  |      $\displaystyle\qty\Big{}$      |                                          |
| `\qty\bigg{}` |     $\displaystyle\qty\bigg{}$      |                                          |
| `\qty\Bigg{}` |     $\displaystyle\qty\Bigg{}$      |                                          |
|   `\pqty{}`   | $\displaystyle\pqty{\frac{aa}{bb}}$ | 效果同`\qty()`；这种写法更$\LaTeX$ic一点 |
|   `\bqty{}`   | $\displaystyle\bqty{\frac{aa}{bb}}$ | 效果同`\qty[]`                           |
|   `\Bqty{}`   | $\displaystyle\Bqty{\frac{aa}{bb}}$ | 效果同`\qty{}`                           |

### 绝对值 `\absolutevalue`

|     简拼     |          效果          | 注释                 |
| :----------: | :--------------------: | :------------------- |
|   `\abs{}`   | $\displaystyle\abs{\frac{aa}{bb}}$ | 自动匹配大小 |
| `\abs\Big{}` |      $\displaystyle\abs\Big{}$      | 也可以手动调节大小   |
|  `\abs*{}`   | $\displaystyle\abs*{\frac{aa}{bb}}$ | 加星号不自动匹配大小 |

### 范数 `\norm`

|     简拼      |          效果           | 注释                 |
| :-----------: | :---------------------: | :------------------- |
|  `\norm{}`   | $\displaystyle\norm{\frac{aa}{bb}}$ |自动匹配大小   |
| `\norm\Big{}` |      $\displaystyle\norm\Big{}$      | 也可以手动调节大小，下同 |
|  `\norm*{}`   | $\displaystyle\norm*{\frac{aa}{bb}}$ | 加星号不自动匹配大小，下同 |

### 竖线求值 `\evaluated`

|      简拼      |      效果      | 注释                   |
| :------------: | :------------: | :--------------------- |
| `\eval{x}_a^b` | $\displaystyle\eval{x}_a^b$ | 自动匹配大小 |
| `\eval[|_a^b` | $\displaystyle\eval[\frac{aa}{bb}|_a^b$ | 自动匹配大小 |
| `\eval(x|_a^b` | $\displaystyle\eval(x|_a^b$ | 前加括号的形式         |
| `\eval[x|_a^b` | $\displaystyle\eval[x|_a^b$ | 前加括号的形式         |

### 阶次 `\order`

|     简拼      |     效果      | 注释               |
| :-----------: | :-----------: | :----------------- |
| `\order{x^2}` | $\displaystyle\order{x^2}$ |自动调节大小 |
| `\order{}` | $\displaystyle\order{\frac{aa}{bb}}$ |自动调节大小 |

### 对易子 `\commutator`

|     简拼      |                        效果                         | 注释         |
| :-----------: | :-------------------------------------------------: | ------------ |
| `\comm{A}{B}` |                    $\comm{A}{B}$                    | 自动调节大小 |
|  `\comm{}{}`  | $\displaystyle \comm{\frac{aa}{bb}}{\frac{cc}{dd}}$ | 自动调节大小 |

### 反对易子 `\anticommutator`

|      简拼      |                         效果                         | 注释                      |
| :------------: | :--------------------------------------------------: | ------------------------- |
| `\acomm{A}{B}` |                    $\acomm{A}{B}$                    | 自动调节大小，效果同`\pb` |
|  `\acomm{}{}`  | $\displaystyle \acomm{\frac{aa}{bb}}{\frac{cc}{dd}}$ | 自动调节大小              |

### 泊松括号 `\poissonbracket`

|    简拼     |                       效果                        | 注释                         |
| :---------: | :-----------------------------------------------: | ---------------------------- |
| `\pb{A}{B}` |                    $\pb{A}{B}$                    | 自动调节大小，效果同`\acomm` |
|  `\pb{}{}`  | $\displaystyle \pb{\frac{aa}{bb}}{\frac{cc}{dd}}$ | 自动调节大小                 |

---

## 2. 向量记号

### 向量（加粗） `\vectorbold`

|   简拼    |   效果    | 注释                   |
| :-------: | :-------: | ---------------------- |
| `\vb{a}`  | $\vb{a}$  | 正体+加粗 表示向量     |
| `\vb*{a}` | $\vb*{a}$ | 意大利体+加粗 表示向量 |

### 向量（箭头） `\vectorarrow`

|   简拼    |   效果    | 注释                       |
| :-------: | :-------: | -------------------------- |
| `\va{a}`  | $\va{a}$  | 正体+箭头加粗 表示向量     |
| `\va*{a}` | $\va*{a}$ | 意大利体+箭头加粗 表示向量 |

### 向量（基元） `\vectorunit`

|   简拼    |   效果    | 注释                           |
| :-------: | :-------: | ------------------------------ |
| `\vu{a}`  | $\vu{a}$  | 正体+加帽加粗 表示向量基元     |
| `\vu*{a}` | $\vu*{a}$ | 意大利体+加帽加粗 表示向量基元 |

### 点积 `\dotproduct`

|  简拼   |     效果      | 注释          |
| :-----: | :-----------: | ------------- |
| `\vdot` | ${a}\vdot{b}$ | 相当于`\cdot` |

### 外积/叉乘 `\crossproduct`

|   简拼   |      效果      | 注释           |
| :------: | :------------: | -------------- |
| `\cross` | ${a}\cross{b}$ | 相当于`\times` |
|  `\cp`   |    $a\cp b$    | 简拼版本       |

### 梯度 `\gradient`

|     简拼      |                    效果                     | 注释                     |
| :-----------: | :-----------------------------------------: | ------------------------ |
|    `\grad`    |                   $\grad$                   |                          |
| `\grad{\Psi}` |                $\grad{\Psi}$                |                          |
| `\grad(\Psi)` | $\displaystyle \grad(\Psi+\frac{\hbar}{i})$ | 自动匹配括号，并添加空格 |
| `\grad[\Psi]` | $\displaystyle \grad[\Psi+\frac{\hbar}{i}]$ | 自动匹配括号，并添加空格 |

### 散度 `\divergence`

|      简拼      |                       效果                        | 注释                     |
| :------------: | :-----------------------------------------------: | ------------------------ |
|     `\div`     |                      $\div$                       |                          |
| `\div{\vb{a}}` |                  $\div{\vb{a}}$                   |                          |
| `\div(\vb{a})` | $\displaystyle \div(\vb{a}+\frac{\hbar}{i}\vb b)$ | 自动匹配括号，并添加空格 |
| `\div[\vb{a}]` | $\displaystyle \div[\vb{a}+\frac{\hbar}{i}\vb b]$ | 自动匹配括号，并添加空格 |

### 旋度 `\curl`

|      简拼       |                        效果                        | 注释                     |
| :-------------: | :------------------------------------------------: | ------------------------ |
|     `\curl`     |                       $\div$                       |                          |
| `\curl{\vb{a}}` |                  $\curl{\vb{a}}$                   |                          |
| `\curl(\vb{a})` | $\displaystyle \curl(\vb{a}+\frac{\hbar}{i}\vb b)$ | 自动匹配括号，并添加空格 |
| `\curl[\vb{a}]` | $\displaystyle \curl[\vb{a}+\frac{\hbar}{i}\vb b]$ | 自动匹配括号，并添加空格 |

### Laplace算符 `\laplacian`

|        简拼        |                       效果                       | 注释                     |
| :----------------: | :----------------------------------------------: | ------------------------ |
|    `\laplacian`    |                   $\laplacian$                   |                          |
| `\laplacian{\Psi}` |                $\laplacian{\Psi}$                |                          |
| `\laplacian(\Psi)` | $\displaystyle \laplacian(\Psi+\frac{\hbar}{i})$ | 自动匹配括号，并添加空格 |
| `\laplacian[\Psi]` | $\displaystyle \laplacian[\Psi+\frac{\hbar}{i}]$ | 自动匹配括号，并添加空格 |

---

## 3. 运算

> `physics` 包把所有运算都加上了自动括号，所以可以直接方便的在后面打公式。原来没有自动括号的版本改成了其他命令。但是谁会拒绝自动括号呢？

### 三角运算

|     简拼     |            效果            | 注释                     |
| :----------: | :------------------------: | :----------------------- |
|  `\sin(x)`   |         $\sin(x)$          | 原命令为 `\sine`         |
|  `\cos(x)`   |         $\cos(x)$          | 原命令为 `\cosine`       |
|  `\tan(x)`   |         $\tan(x)$          | 原命令为 `\tangent`      |
|  `\csc(x)`   |         $\csc(x)$          | 原命令为 `\cosecant`     |
|  `\sec(x)`   |         $\sec(x)$          | 原命令为 `\secant`       |
|  `\cot(x)`   |         $\cot(x)$          | 原命令为 `\cotangent`    |
|  `\sinh(x)`  |         $\sinh(x)$         | 原命令为 `\sineh`        |
|  `\cosh(x)`  |         $\cosh(x)$         | 原命令为 `\cosineh`      |
|  `\tanh(x)`  |         $\tanh(x)$         | 原命令为 `\tangenth`     |
|  `\csch(x)`  |  $\operatorname{csch}(x)$  | 原命令为 `\cosecanth`    |
|  `\sech(x)`  |  $\operatorname{sech}(x)$  | 原命令为 `\secanth`      |
|  `\coth(x)`  |         $\coth(x)$         | 原命令为 `\cotangenth`   |
| `\arcsin(x)` |        $\arcsin(x)$        | 原命令为 `\arcsine`      |
| `\arccos(x)` |        $\arccos(x)$        | 原命令为 `\arccosine`    |
| `\arctan(x)` |        $\arctan(x)$        | 原命令为 `\arctangent`   |
| `\arccsc(x)` | $\operatorname{arccsc}(x)$ | 原命令为 `\arccosecant`  |
| `\arcsec(x)` | $\operatorname{arcsec}(x)$ | 原命令为 `\arcsecant`    |
| `\arccot(x)` | $\operatorname{arccot}(x)$ | 原命令为 `\arccotangent` |
|  `\asin(x)`  |        $\arcsin(x)$        | 原命令为 `\asine`        |
|  `\acos(x)`  |        $\arccos(x)$        | 原命令为 `\acosine`      |
|  `\atan(x)`  |        $\arctan(x)$        | 原命令为 `\atangent`     |
|  `\acsc(x)`  | $\operatorname{arccsc}(x)$ | 原命令为 `\acosecant`    |
|  `\asec(x)`  | $\operatorname{arcsec}(x)$ | 原命令为 `\asecant`      |
|  `\acot(x)`  | $\operatorname{arccot}(x)$ | 原命令为 `\acotangent`   |

### 其他运算

|   简拼   |   效果    | 注释                         |
| :------: | :-------: | ---------------------------- |
| `\exp()` | $\exp(x)$ | 原命令为 `\exponential`      |
| `\ln()`  | $\ln(x)$  | 原命令为 `\naturallogarithm` |
| `\log()` | $\log(x)$ | 原命令为 `\logarithm`        |
| `\det()` | $\det(M)$ | 原命令为 `\determinant`      |
| `\Pr()`  | $\Pr(x)$  | 原命令为 `\Probability`      |

### 迹运算 `trace`

|  简拼   |   效果   | 注释 |
| :-----: | :------: | ---- |
| `\tr()` | $\tr(M)$ |      |

### 秩运算 `\rank`

|   简拼    |    效果    | 注释 |
| :-------: | :--------: | ---- |
| `\rank()` | $\rank(M)$ |      |

### 误差函数 `\erf`

|   简拼   |   效果    | 注释 |
| :------: | :-------: | ---- |
| `\erf()` | $\erf(x)$ |      |

### 留数 `\Res`

|   简拼   |   效果    | 注释 |
| :------: | :-------: | ---- |
| `\Res()` | $\Res(x)$ |      |

### 积分主值 `\principalvalue`

| 简拼  |        效果        | 注释       |
| :---: | :----------------: | ---------- |
| `\pv` | $\pv\int(x)\dd{x}$ |            |
| `\PV` | $\PV\int(x)\dd{x}$ | 另一种写法 |

### 实部/虚部 `\Re` `\Im`

|  简拼   |   效果   | 注释 |
| :-----: | :------: | ---- |
| `\Re()` | $\Re(z)$ |      |
| `\Im()` | $\Im(z)$ |      |

---

## 4. 快速文本

### 快速quad空格+文字 `\qqtext`

|        简拼         |         效果          | 注释                         |
| :-----------------: | :-------------------: | ---------------------------- |
|     `\qq{text}`     |     $\qq{text}$       | 输出 text，前后加 quad 空格  |
|   `aa \qq{text} bb` |  $aa\qq{text}bb$      | 前后都会加上 quad 空格       |
|      `aa \qc bb`    |     $aa \qc bb $     | 快速逗号，后加 quad 空格     |
|     `aa \qcc bb`    |    $aa \qcc bb$       | 共轭复数，前后加 quad 空格   |
|     `aa \qif bb`    |    $aa \qif bb$       | 快速 if，前后加 quad 空格    |

其他的还有 `\qthen`, `\qelse`, `\qotherwise`, `\qunless`, `\qgiven`, `\qusing`, `\qassume`, `\qsince`, `\qlet`, `\qfor`, `\qall`, `\qeven`, `\qodd`, `\qinteger`, `\qand`, `\qor`, `\qas`, `\qin`，不再赘述。

---

## 5. 导数

### 微分 `\differential`

|       简拼        |                           效果                           | 注释               |
| :---------------: | :------------------------------------------------------: | ------------------ |
|       `\dd`       |                          $\dd$                           |                    |
|      `\dd x`      |                         $\dd x$                          | 没有空格（不推荐） |
|     `\dd{x}`      | $\text{\textvisiblespace}\dd{x}\text{\textvisiblespace}$ | 前后加1/4空格      |
|    `\dd[3]{x}`    |                        $\dd[3]x$                         | 方括号内表示阶次   |
| `\dd(\cos\theta)` |                    $\dd(\cos\theta)$                     | 包括自动括号       |

### 导数 `\derivative`

|         简拼         |               效果                | 注释             |
| :------------------: | :-------------------------------: | ---------------- |
|       `\dv{x}`       |      $\displaystyle \dv{x}$       | 一个参数         |
|     `\dv{y}{x}`      |     $\displaystyle \dv{y}{x}$     | 两个参数         |
|    `\dv[n]{y}{x}`    |   $\displaystyle \dv[n]{y}{x}$    | 方括号内表示阶次 |
| `\dv{x}(\cos\theta)` | $\displaystyle\dv{x}(\cos\theta)$ | 包括自动括号     |
|     `\dv*{y}{x}`     |           $\dv*{y}{x}$            | 加星号为单行形式 |

### 偏导数 `\partialderivative`

|         简拼          |                效果                | 注释             |
| :-------------------: | :--------------------------------: | ---------------- |
|       `\pdv{x}`       |      $\displaystyle \pdv{x}$       | 一个参数         |
|     `\pdv{y}{x}`      |     $\displaystyle \pdv{y}{x}$     | 两个参数         |
|    `\pdv[n]{y}{x}`    |   $\displaystyle \pdv[n]{y}{x}$    | 方括号内表示阶次 |
| `\pdv{x}(\cos\theta)` | $\displaystyle\pdv{x}(\cos\theta)$ | 包括自动括号     |
|     `\pdv*{y}{x}`     |           $\pdv*{y}{x}$            | 加星号为单行形式 |

### 变分 `\variation`

|      简拼       |      效果       |     注释      |
| :-------------: | :-------------: | :-----------: |
|     `\var`      |     $\var$      |               |
| `\var{F[g(x)]}` | $\var{F[g(x)]}$ | 前后加1/4空格 |
|  `\var(E-TS)`   |  $\var(E-TS)$   | 包括自动括号  |

### 泛函导数 `\functionalderivative`

|         简拼          |             效果              | 注释             |
| :-------------------: | :---------------------------: | ---------------- |
|       `\fdv{g}`       |    $\displaystyle \fdv{g}$    | 一个参数         |
|     `\fdv{F}{g}`      |  $\displaystyle \fdv{F}{g}$   | 两个参数         |
|    `\fdv[n]{F}{g}`    | $\displaystyle \fdv[n]{F}{g}$ | 方括号内表示阶次 |
| `\fdv{V}(\cos\theta)` | $\displaystyle\fdv{V}(E-TS)$  | 包括自动括号     |
|     `\fdv*{F}{g}`     |         $\fdv*{F}{g}$         | 加星号为单行形式 |

---

## 6. Dirac bra-ket记号

### 左矢/右矢 `\bra` `\ket`

|          简拼          |          效果          | 注释         |
| :--------------------: | :--------------------: | ------------ |
|       `\ket{u}`        |       $\ket{u}$        | 自动匹配括号 |
|       `\bra{u}`        |       $\bra{u}$        | 自动匹配括号 |
| `\bra{\phi}\ket{\psi}` | $\bra{\phi}\ket{\psi}$ | 自动收缩     |

### 内积 `\innerproduct`

|      简拼       |      效果       | 注释                   |
| :-------------: | :-------------: | ---------------------- |
| `\braket{a}{b}` | $\braket{a}{b}$ | 两个参数，自动匹配括号 |
|  `\braket{a}`   |  $\braket{a}$   | 一个参数，自动匹配括号 |
|   `\ip{a}{b}`   |   $\ip{a}{b}$   | 简写形式               |

### 外积 `\outerproduct`

|      简拼       |      效果       | 注释                   |
| :-------------: | :-------------: | ---------------------- |
|  `\dyad{a}{b}`  |  $\dyad{a}{b}$  | 两个参数，自动匹配括号 |
|   `\dyad{a}`    |   $\dyad{a}$    | 一个参数，自动匹配括号 |
| `\ketbra{a}{b}` | $\ketbra{a}{b}$ | 可替代的形式           |
|   `\op{a}{b}`   |   $\op{a}{b}$   | 简写形式               |

### 期望值 `\expectationvalue`

|        简拼        |        效果        | 注释         |
| :----------------: | :----------------: | ------------ |
|    `\expval{A}`    |    $\expval{A}$    | 隐式；单参数 |
| `\expval{A}{\psi}` | $\expval{A}{\psi}$ | 显式；双参数 |
|   `\ev{A}{\psi}`   |   $\ev{A}{\psi}$   | 简写形式     |

### 矩阵元素 `\matrixelement`

|         简拼         |         效果         | 注释         |
| :------------------: | :------------------: | ------------ |
| `\matrixel{n}{A}{m}` | $\matrixel{n}{A}{m}$ | 需要三个参数 |
|   `\mel{n}{A}{m}`    |   $\mel{n}{A}{m}$    | 简写形式     |

---

## 7. 矩阵宏

> 以下矩阵宏会生成未格式化的矩阵元素行和列，这些元素既可用作独立矩阵，也可用作更大矩阵中的子块。例如，命令 `\identitymatrix{2}`（其简写形式为 `\imat{2}`）会生成一个 2×2 单位矩阵的元素 $\smqty{1&0\\0&1}$，且不带大括号或分组。这使得该命令也可以直接用于另一个矩阵内部，例如：
>
> | 代码                                                     |                      效果                      |
> | :------------------------------------------------------- | :--------------------------------------------: |
> | \begin{pmatrix}<br/>\imat{2} \\\ a & b<br/>\end{pmatrix} | $\begin{pmatrix}\imat{2}\\ a & b\end{pmatrix}$ |
>
> 如果要在 `\imat{2}` 子矩阵的右侧或左侧指定元素，我们可以使用分组命令 `\matrixquantity` 或 `\mqty`，从而将 `\imat{2}` 有效地转换为更大矩阵中的一个单一矩阵元素：
>
> | 代码                                                         |                             效果                             |
> | :----------------------------------------------------------- | :----------------------------------------------------------: |
> | \begin{pmatrix}<br/>\mqty{\imat{2}} & \mqty{a\\b} \\\ \mqty{c&d}&e<br/>\end{pmatrix} | $\begin{pmatrix}\mqty{\imat{2}}&\mqty{a\\b}\\\mqty{c&d}&e\end{pmatrix}$ |
>
> 在这个例子中，需要额外的 `\mqty` 分组，以便让 `a` 和 `b` 元素作为一个整体元素来表现，因为 `\mqty{\imat{2}}` 本身也像一个单一矩阵元素那样起作用（同理，被分组的 `c` 和 `d` 元素也是如此）。最后，最外层的 `pmatrix` 环境也可以替换为 physics 宏包中的 `\mqty()`，从而使上面的例子可以写成一行：
>
> | 代码                                               |                        效果                        |
> | :------------------------------------------------- | :------------------------------------------------: |
> | `\mqty(\mqty{\imat{2}}&\mqty{a\\b}\\\mqty{c&d}&e)` | $\mqty(\mqty{\imat{2}}&\mqty{a\\b}\\\mqty{c&d}&e)$ |

### 矩阵 `\matrixquantity`

|    简拼    |           效果           | 注释                                     |
| :--------: | :----------------------: | :--------------------------------------- |
| `\mqty()`  | $\mqty(a & b \\ c & d)$  | 圆括号矩阵，等效于 `\pmqty`              |
| `\mqty*()` | $\mqty*(a & b \\ c & d)$ | 替代圆括号矩阵，等效于 `\Pmqty`          |
| `\mqty[]`  | $\mqty[a & b \\ c & d]$  | 方括号矩阵，等效于 `\bmqty`              |
| `\mqty||`  | $\mqty|a & b \\ c & d|$  | 竖线矩阵，等效于 `\vmqty`                |
| `\pmqty{}` | $\pmqty{a & b \\ c & d}$ | 圆括号矩阵，同 `\mqty()`；更鲁棒，下同。 |
| `\Pmqty{}` | $\Pmqty{a & b \\ c & d}$ | 替代圆括号矩阵，同 `\mqty*()`            |
| `\bmqty{}` | $\bmqty{a & b \\ c & d}$ | 方括号矩阵，同 `\mqty[]`                 |
| `\vmqty{}` | $\vmqty{a & b \\ c & d}$ | 竖线矩阵，同 `\mqty||`                   |

### 小型矩阵 `\smallmatrixquantity`

|           简拼           |           效果            | 注释                   |
| :----------------------: | :-----------------------: | :--------------------- |
| `\smqty{a & b \\ c & d}` | $\smqty{a & b \\ c & d}$  | 无括号小型矩阵（行内） |
|        `\smqty()`        | $\smqty(a & b \\ c & d)$  | 圆括号小型矩阵         |
|       `\smqty*()`        | $\smqty*(a & b \\ c & d)$ | 替代圆括号小型矩阵     |
|        `\smqty[]`        | $\smqty[a & b \\ c & d]$  | 方括号小型矩阵         |
|        `\smqty||`        | $\smqty|a & b \\ c & d|$  | 竖线小型矩阵           |

### 行列式 `matrixdeterminant`

|           简拼           |           效果           | 注释       |
| :----------------------: | :----------------------: | :--------- |
| `\mdet{a & b \\ c & d}`  | $\mdet{a & b \\ c & d}$  | 行列式     |
| `\smdet{a & b \\ c & d}` | $\smdet{a & b \\ c & d}$ | 小型行列式 |

### 单位矩阵 `\identitymatrix`

|        简拼        |        效果        | 注释         |
| :----------------: | :----------------: | :----------- |
| `\mqty(\imat{3})`  | $\mqty(\imat{3})$  | 单位矩阵     |
| `\smqty(\imat{3})` | $\smqty(\imat{3})$ | 小型单位矩阵 |

### 元素填充矩阵 `\xmatrix`

|           简拼           |           效果            | 注释                                               |
| :----------------------: | :-----------------------: | :------------------------------------------------- |
| `\mqty(\xmat{x}{2}{3})`  |  $\mqty(\xmat{x}{2}{3})$  | 第一个参数为填充元素；第二和第三个参数为行数和列数 |
| `\mqty(\xmat*{x}{2}{3})` | $\mqty(\xmat*{x}{2}{3}) $ | 加星号会自动填充下标                               |
| `\mqty(\xmat*{x}{3}{1})` | $\mqty(\xmat*{x}{3}{1})$  | 列矩阵会变成单下标                                 |
| `\mqty(\xmat*{x}{1}{3})` | $\mqty(\xmat*{x}{1}{3})$  | 行矩阵会变成单下标                                 |

### 零矩阵 `\zeromartrix`

|         简拼          |         效果          | 注释       |
| :-------------------: | :-------------------: | :--------- |
| `\mqty(\zmat{3}{2})`  | $\mqty(\zmat{3}{2})$  | 零矩阵     |
| `\smqty(\zmat{3}{2})` | $\smqty(\zmat{3}{2})$ | 小型零矩阵 |

### Pauli 矩阵 `\paulimatrix`

|       简拼        |       效果        | 注释        |
| :---------------: | :---------------: | :---------- |
| `\mqty(\pmat{0})` | $\mqty(\pmat{0})$ | 0号泡利矩阵 |
| `\mqty(\pmat{1})` | $\mqty(\pmat{1})$ | 1号泡利矩阵 |
| `\mqty(\pmat{2})` | $\mqty(\pmat{2})$ | 2号泡利矩阵 |
| `\mqty(\pmat{3})` | $\mqty(\pmat{3})$ | 3号泡利矩阵 |

### 对角矩阵 `\diagonalmartrix`

|             简拼             |             效果             | 注释                                 |
| :--------------------------: | :--------------------------: | :----------------------------------- |
| `\mqty(\dmat{a,b,c,\ddots})` | $\mqty(\dmat{a,b,c,\ddots})$ |                                      |
| `\mqty(\dmat{1,2&3\\4&5,6})` | $\mqty(\dmat{1,2&3\\4&5,6})$ | 可以将一个对角元变成一个单独的矩阵块 |

### 反对角矩阵 `\antidiagonalmartrix`

|             简拼              |          效果          | 注释 |
| :---------------------------: | :--------------------: | :--- |
| `\mqty(\admat{a,b,c,\ddots})` | $\mqty(\admat{a,b,c})$ |      |
