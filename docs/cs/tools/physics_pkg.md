# `physics` 宏包常用命令

> 目前中文网络上关于 `physics` 包的资料比较少，尽管这个包现在已经停止维护了，但是确实大大方便了公式的输入，方便课堂笔记书写。于是我将一些常用的命令整理在这里。
>
> 本文档部分翻译自：[The Physics Package](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf)。

## 1. 自动括号

|       全名       |      简拼      |          效果           | 注释                                       |
| :--------------: | :------------: | :---------------------: | :----------------------------------------- |
|   `\quantity`    |    `\qty()`    |  $\qty(\frac{aa}{bb})$  | 自动匹配大小，效果相当于`\left( \right)`   |
|                  |    `\qty[]`    |  $\qty[\frac{aa}{bb}]$  | `\qty`后面是什么括号就显示什么括号         |
|                  |    `\qty{}`    |  $\qty{\frac{aa}{bb}}$  |                                            |
|                  |  `\qty\big{}`  |      $\qty\big{}$       | 也可以手动调节大小                         |
|                  |  `\qty\Big{}`  |      $\qty\Big{}$       |                                            |
|                  | `\qty\bigg{}`  |      $\qty\bigg{}$      |                                            |
|                  | `\qty\Bigg{}`  |      $\qty\Bigg{}$      |                                            |
|                  |   `\pqty{}`    | $\pqty{\frac{aa}{bb}}$  | 效果同`\qty()`；这种写法更$\LaTeX ic$ 一点 |
|                  |   `\bqty{}`    | $\bqty{\frac{aa}{bb}}$  | 效果同`\qty[]`                             |
|                  |   `\Bqty{}`    | $\Bqty{\frac{aa}{bb}}$  | 效果同`\qty{}`                             |
| `\absolutevalue` |    `\abs{}`    |  $\abs{\frac{aa}{bb}}$  | 绝对值；自动匹配大小                       |
|                  |  `\abs\Big{}`  |      $\abs\Big{}$       | 也可以手动调节大小                         |
|                  |   `\abs*{}`    | $\abs*{\frac{aa}{bb}}$  | 加星号不自动匹配大小                       |
|     `\norm`      |   `\norm{a}`   | $\norm{\frac{aa}{bb}}$  | 范数；自动匹配大小                         |
|                  | `\norm\Big{}`  |      $\norm\Big{}$      | 也可以手动调节大小                         |
|                  |   `\norm*{}`   | $\norm*{\frac{aa}{bb}}$ | 加星号不自动匹配大小                       |
|   `\evaluated`   | `\eval{x}_a^b` |     $\eval{x}_a^b$      | 竖线求值；自动匹配大小                     |
|                  | `\eval(x|_a^b` |     $\eval(x|_a^b$      | 前加括号的形式                             |
|                  | `\eval[x|_a^b` |     $\eval[x|_a^b$      | 前加括号的形式                             |
|     `\order`     | `\order{x^2}`  |      $\order{x^2}$      | 阶次；自动调节大小                         |

