---
marp: true
theme: rose-pine-dawn-modern
paginate: true
_paginate: skip
size: 16:9

math: katex

---
# 留数定理
$$
\gdef\red#1{{\color{cb8680}{#1}}} 
\gdef\green#1{{\color{4f8d63}{#1}}} 
\gdef\gray#1{{\color{gray}{#1}}} 
\gdef\purple#1{{\color{B189C6}{#1}}} 
\gdef\orange#1{{\color{dfa04b}{#1}}}
\gdef\white#1{{\color{white}{#1}}}
$$


---
<!-- header: 留数 -->

### 留数定义

- **<green>定义**：考虑 $a$ 为 $f(z)$ 的 **孤立奇点**，因此存在 $R > 0$ 使得 $f$ 在 $N(a, R) - \{a\}$ 中解析。定义 $f$ 在 $a$ 处的 **<green>留数 (residue)** 为
  $$
  \green{\mathop{\operatorname{Res}}_{z = a} f(z)} \coloneqq \frac{1}{2\pi i} \oint_{|z - a| = \rho < R} f(z) dz
  $$

  <center>
  
  ![width:550px](image/residue-def-tikz.svg)
  </center>

---

### 留数定义

- **<green>定义**：考虑 $a$ 为 $f(z)$ 的 **孤立奇点**，因此存在 $R > 0$ 使得 $f$ 在 $N(a, R) - \{a\}$ 中解析。定义 $f$ 在 $a$ 处的 **<green>留数 (residue)** 为
  $$
  \green{\mathop{\operatorname{Res}}_{z = a} f(z)} \coloneqq \orange{\frac{1}{2\pi i}} \oint_{|z - a| = \rho < R} f(z) dz
  $$

  <div class='proof comment'>

  **留数的记号**

  留数的记号因人而异，可以写
  $$
  \operatorname{Res}f(a), \quad \operatorname{Res}(f, a), \quad \operatorname{Res}\Big|_{z = a}f(z), \quad
  \mathop{\operatorname{Res}}_{z \to a}f(z), \quad \cdots
  $$
  </div>



---

### 留数定义

<div class='proof comment'>

**只有一个奇点**

根据设定，$f$ 在去心邻域内解析，因此积分围道 **<red>只** 包围一个奇点 $a$。
</div>

<div class='proof comment'>

**奇点类型**

$a$ 可以是 $f$ 的任意孤立奇点，**三种都行**。
</div>

---

### 留数定义

<div class='proof comment'>

**$\rho$ 无关性**

显然积分与 $\rho$ 无关，只要 $0 < \rho < R$
</div>

<div class='proof comment'>

**围道**

积分围道 **不一定** 是圆圈，只要是在 $N(a, R) - \{a\}$ 中的简单围道即可。
</div>

---

### 留数定义

<div class='proof comment'>

**Laurent 展开系数**

$f$ 在 $0 < |z - a| < R$ 中解析，因此可 Laurent 展开，
$$
f(z) = \sum_{n = - \infty}^{+\infty} \lambda_n (z - a)^n
$$

其中，
$$
\lambda_{-1} = \frac{1}{2\pi i} \oint_{|z - a| = \rho} f(\zeta) d\zeta = \mathop{\operatorname{Res}}_{z = a} f(z)
$$
</div>

---

### 留数例子

- 考虑 $f(z) = \frac{\lambda}{z}$

  奇点是 $0$，是 **单极点**；$f(z) = \cdots + 0 + \lambda z^{-1} + 0 + \cdots$

  留数 $\mathop{\operatorname{Res}}_{z = 0}f(z) = \lambda$

* 考虑 $f(z) = \frac{\lambda}{z - 1}$

  奇点是 $1$，是 **单极点**；$f(z) = \cdots + 0 + \lambda (z - 1)^{-1} + 0 + \cdots$

  留数 $\mathop{\operatorname{Res}}_{z = 1}f(z) = \lambda$

---
### 留数例子

- 考虑 $f(z) = \frac{\lambda}{z^2}$

  奇点是 $0$，是 **二阶极点**；$f(z) = \cdots + 0 + \lambda z^{-2} + 0 + \cdots$

  留数 $\mathop{\operatorname{Res}}_{z = 0}f(z) = 0$
* 考虑 $f(z) = \frac{\lambda}{z^3}$

  奇点是 $0$，是 **三阶极点**；$f(z) = \cdots + 0 + \lambda z^{-3} + 0 + \cdots$

  留数 $\mathop{\operatorname{Res}}_{z = 0}f(z) = 0$

---

### 留数例子

- **<red>高阶极点的留数为零？**
* 考虑 $f(z) = \frac{1}{z^2} \frac{\lambda}{z - 1}$，$\lambda \ne 0$。

* 则 **原点** 是孤立奇点，且是 **二阶极点**。

* 以原点为中心，在去心邻域 $0 < |z| < 1$ 内，
  $$
  \begin{align*}
  f(z) &= - \frac{\lambda}{z^2} \orange{\frac{1}{1 - z}}
  = - \frac{\lambda}{z^2} \orange{\sum_{k = 0}z^k}= - \frac{\lambda}{z^2} \ \green{- \frac{\lambda}{z}} - \lambda - \ldots
  \end{align*}
  $$
  因此
  $$
  \mathop{\operatorname{Res}}_{z = 0} f(z) = - \lambda \ne 0
  $$

---

### 留数例子

* 考虑在 $a$ 某邻域中解析的函数 $\varphi(z)$，以及
  $$
  f(z) = \frac{1}{(z - a)^m} \varphi(z), \qquad m \ge 1
  $$
* 对 $\varphi$ 做泰勒展开，
  $$
  \begin{align*}
  f(z) &= \frac{1}{(z - a)^m} \orange{\sum_{k \ge 0} \frac{\varphi^{(k)}(a)}{k!} (z - a)^k} \\
  &= \ldots + \frac{1}{\red{(z - a)^m}} \green{\frac{\varphi^{(m - 1)}(a)}{(m - 1)!}} \red{(z - a)^{m - 1}} + \ldots
  \end{align*}
  $$

---
### 留数例子

* 因此
  $$
  \mathop{\operatorname{Res}_{z = a}} f(z) = \green{\frac{\varphi^{(m - 1)}(a)}{(m - 1)!}}
  $$
  
  <div class='proof comment'>

  **高阶导数公式**

  - 也可以用**高阶导数公式**：若 $\varphi(z)$ 在 $a$ 某邻域内解析，
    $$
    \operatorname{Res}_{z = a}f(z)
    = \frac{1}{2\pi i}\oint \frac{\varphi(z)}{(z - a)^m}dz
    = \frac{1}{(m - 1)!} \varphi^{(m - 1)}(a)
    $$
  </div>


---

### 留数的常用公式

* **公式 1**：Laurent 展开求 $-1$ 次幂系数
* **公式 2**：若 $a$ 是 **$m$-阶极点**，则
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z)
  = \frac{1}{(m - 1)!} \frac{d^{m - 1}}{dz^{m - 1}}\bigg|_{z = a}\Big[
  (z - a)^m f(z)
  \Big]
  $$

  <div class='proof comment'>

  **$m$**

  注意 $m$ 与 $m - 1$ 的位置。当 $m = 1$ 的时候，定义 $0$ 阶导数
  $$
  \frac{d^0}{dz^0}\bigg|_{z = a} \Big[(z - a) f(z)\Big] = \lim_{z \to a}\Big[(z - a)f(z)\Big]
  $$
  </div>

---

### 留数的常用公式

* **公式 2**：若 $a$ 是 $m$-阶极点，则
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z)
  = \frac{1}{(m - 1)!} \frac{d^{m - 1}}{dz^{m - 1}}\bigg|_{z = a}\Big[
  (z - a)^m f(z)
  \Big]
  $$

  <div class="proof">

  **说明**

  由于 $f(z)$ 在 $a$ 是 $m$-阶极点，因此**在 $a$ 去心邻域** $f(z) = \varphi(z)/(z - a)^m$。用刚介绍的讨论，
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z) = \frac{\green{\varphi}^{\purple{(m - 1)}}\green{(a)}}{\orange{(m - 1)!}} = \frac{1}{\orange{(m-1)!}} \purple{\frac{d^{m - 1}}{dz^{m - 1}}}\bigg|_{z = a}\Big[\green{(z - a)^m f(z)}\Big]
  $$
  </div>

---

### 留数的常用公式

* **公式 3**：若 $f(z) = \frac{\varphi(z)}{\psi(z)}$，其中 $\varphi, \psi$ 在 $a$ 某邻域内解析，且 $\varphi(a)\ne 0$，而 $a$ 是 $\psi$ 的 **单零点**。则
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z) = \frac{\varphi(a)}{\psi'(a)}
  $$

  <div class='proof comment'>

  **导数**

  导数只对分母做。
  </div>

---

### 留数的常用公式

* **公式 3**：若 $f(z) = \frac{\varphi(z)}{\psi(z)}$，其中 $\varphi, \psi$ 在 $a$ 某邻域内解析，且 $\varphi(a)\ne 0$，而 $a$ 是 $\psi$ 的 **单零点**。则
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z) = \frac{\varphi(a)}{\psi'(a)}
  $$

  <div class="proof">

  **说明**

  显然 $a$ 是**单极点**。利用公式 2，
  $$
  \begin{align*}
  \mathop{\operatorname{Res}}_{z = a} f(z) &= \lim_{z \to a} (z - a)f(z)\\
  &= \lim_{z \to a} (z - a)\frac{\varphi(z)}{\psi'(a)(z - a) + O(z - a)^2}
  = \frac{\varphi(a)}{\psi'(a)}
  \end{align*}
  $$
  </div>

---

### 留数的常用公式

* **公式 4**：若 $f(z) = \frac{\varphi(z)}{z - a}$，其中 $\varphi$ 在 $a$ 某邻域内解析，且 $\varphi(a)\ne 0$。则
  $$
  \mathop{\operatorname{Res}}_{z = a} f(z) = \varphi(a)
  $$
  
  <div class='proof'>
  
  **说明**

  用上一个公式证明。
  </div>

---

### 留数的常用公式

* **公式 5**：考虑若
  $$
  f(z) = \frac{\varphi(z)}{(z - z_1)(z - z_2) \cdots (z - z_n)}, \qquad
  z_i \ne z_j, \forall i \ne j
  $$
  且 $\varphi(z)$ 在所有 $z_i$ 附近解析，则
  $$
  \mathop{\operatorname{Res}}_{z = z_i} f(z) = \frac{\varphi(z_i)}{\prod_{\substack{j = 1, j \ne i}}^n(z_i - z_j)}
  $$

---

<div class="proof">

**说明**

利用公式 3，以及暴力求导结果
$$
[(z - z_1)(z - z_2) \cdots (z - z_n)]'_{z = z_i} = \prod_{\substack{j = 1 \\ j \ne i}}^n(z_i - z_j)
$$
</div>

---

### 留数的常用公式

* 例：考虑函数 $f(z) = \frac{1}{z^n}$，$n = 1, 2, 3, \ldots$。求 $f$ 在原点处的留数。

  <div class="proof">

  **解**

  - 由定义，留数是原点附近的一个围道积分，或者 Laurent 展开负一次幂项系数。可以考虑直接计算：当 $n = 1$ 时结果为 $1$，否则为 $0$。

  </div>

---
### 留数的常用公式

<div class='proof'>


- 或者用公式 2：原点是 $n$-阶极点，因此
  $$
  \mathop{\operatorname{Res}}_{z = 0}f(z) = \frac{1}{(n - 1)!}\frac{d^{n - 1}}{dz^{n - 1}} \bigg|_{z = 0}\Big[z^n\frac{1}{z^n}\Big]
  $$

  (1) 当 $n > 1$ 时，$\frac{d^{n - 1}}{dz^{n - 1}} [1] = 0$

  (2) 当 $n = 1$ 时，
  $$
  \frac{d^0}{dz^0} [1] = \purple{\lim_{z \to 0} 1} = 1
  $$
</div>

---

### 留数的常用公式

* 例：证明
  $$
  \operatorname{Res}_{z = z_k} \frac{1}{z^{2n} + 1} = - \frac{z_k}{2n}
  $$
  其中 **<green>$z_k$** 是 $-1$ 的第 $k$ 个 $2n$ 次根，**<green>$z_k \coloneqq e^{\frac{\pi i}{2n} + \frac{2\pi i k}{2n}}$**

  <div class="proof">

  **说明**

  利用公式 3，以及 $(z^{2n} + 1)' = \purple{2n z^{2n - 1}}$，
  $$
  \operatorname{Res}_{z = z_k} \frac{1}{z^{2n} + 1} = \frac{1}{\purple{2n z_k^{2n - 1}}} = \frac{z_k}{2n z_k^{2n}} = - \frac{z_k}{2n}
  $$
  其中最后一个等号用了 $z_k^{2n} + 1 = 0$。
  </div>


---
### 留数的常用公式

<div class="proof">

**说明**

- 也可以先把 $z^{2n} + 1$ 因式分解，$z^{2n} + 1 = \prod_{k = 0}^{2n - 1}(z - z_k)$，利用公式 5 得到
  $$
  \operatorname{Res}_{z = z_k} \frac{1}{z^{2n} + 1} = \frac{1}{\prod_{\substack{j = 0 \\ j \ne k}}^{2n - 1}(z_k - z_j)}
  $$
* 比较两个方法，得到恒等式
  $$
  - \frac{z_k}{2n} = \frac{1}{\prod_{\substack{j = 0 \\ j \ne k}}^{2n - 1}(z_k - z_j)}
  $$
</div>

---

# 留数定理

---
<!-- header: 留数定理 -->

### 留数定理

* **留数定理**：设 $f$ 在单连通或复连通区域 $D$ 中有 **有限个** **孤立** 奇点 $a_{i = 1, \ldots, n}$，且 $f$ 在 $\overline D - \{a_i\}$ 上解析。则
  $$
  \frac{1}{2\pi i}\oint_{\partial D} f(z) dz = \sum_{i = 1}^n \mathop{\operatorname{Res}}_{z = a_i}f(z)
  $$

  <center>
  
  ![width:500px](image/Residue-Theorem-1.svg)
  </center>


---

### 留数定理

<center>

![width:700px](image/Residue-Theorem-2.svg)

</center>


---

### 留数定理


<center>

![width:700px](image/Residue-Theorem-3.svg)

</center>

---

### 留数定理


<center>

![width:700px](image/Residue-Theorem-4.svg)

</center>

---

### 留数定理

* **留数定理**：设 $f$ 在单连通或复连通区域 $D$ 中有 **有限个** **孤立** 奇点 $a_{i = 1, \ldots, n}$，且 $f$ 在 $\overline D - \{a_i\}$ 上解析。则
  $$
  \frac{1}{2\pi i}\oint_{\partial D} f(z) dz = \sum_{i = 1}^n \mathop{\operatorname{Res}}_{z = a_i}f(z)
  $$

  <div class='proof comment'>

  **证明思路**

  对复通区域 $D - \{a_i\}$ 使用柯西积分定理即可。
  </div>

---

# 留数定理的应用

---
<!-- header: 留数定理的应用 -->

### 常见围道积分的计算

* 计算积分
  $$
  \mathcal{I} \coloneqq \oint_{|z| = \rho \ne 0, 1} \frac{1}{z(z - 1)^2} dz
  $$

  <div class="proof">

  **求解**

  - 首先判断奇点：
    <center>
    
    一阶极点 $z = 0$ $\qquad\qquad$ 二阶极点 $z = 1$
    </center>

  * $0 < \rho < 1$：围道包围原点，
    $$
    \mathcal{I} = (2\pi i) \mathop{\operatorname{Res}}_{z = 0} f(z)
    = 2\pi i\lim_{z \to 0} [zf(z)] = 2\pi i
    $$

  </div>

---

### 常见围道积分的计算



<div class="proof">

**求解**
- 当 $\rho > 1$：围道包围 $z = 0$，$z = 1$，于是
  $$
  \mathcal{I} = 2\pi i \left(
  \mathop{\operatorname{Res}}_{z = 0}f(z)
  + \mathop{\operatorname{Res}}_{z = 1}f(z)
  \right)
  $$
  第一个留数已经知道了。
</div>

---

### 常见围道积分的计算



<div class="proof">

**求解**

- 利用留数公式计算第二个留数，
  $$
  \begin{align*}
  = & \ 2\pi i\left[
  1 + \frac{1}{(2 - 1)!} \frac{d}{dz}\Big|_{z = 1} \Big((z - 1)^2 f(z)\Big)
  \right] \\
  = & \ 2\pi i\left[
  1 - \frac{1}{z^2}\Big|_{z = 1}
  \right] = 0
  \end{align*}
  $$
</div>


---

### 常见围道积分的计算

- 计算积分
  $$
  \mathcal{I} = \oint_{|z| = \rho > 0} \frac{\sin z}{z} dz
  $$

  <div class="proof">

  **求解**

  - 围道包围奇点为原点，因此 $\mathcal{I} = 2\pi i \operatorname{Res}_{z = 0}\frac{\sin z}{z}$。有许多方法计算。

  - 原点是 **可去奇点**，因此 **主要部分** 为 **<red>零**，从而 $-1$-次幂项系数为零，因此留数为零。

  - 也可以用 Cauchy 积分公式，$\mathcal{I} = 2\pi i (\sin z)\Big|_{z = 0} = 0$。
  </div>

---

### 常见围道积分的计算

- 计算积分
  $$
  \mathcal{I} = \oint_{|z| = \rho > 0} \frac{z}{\sin z} dz, \qquad
  \rho > 0, \rho \ne n \pi
  $$

  <div class="proof">

  **求解**

  * 先判断奇点：
    $$
    \sin z = 0 \qquad \Rightarrow \qquad z = k\pi, \quad k\in \mathbb{Z}
    $$

  * 无穷多个奇点：**对称** 分布在 $0$ 两侧。
  </div>


---

### 常见围道积分的计算



<div class="proof">

**求解**

- 假设 $-n \pi, - (n - 1)\pi, \ldots, 0, \ldots, (n - 1)\pi, n \pi$ 被围道所包围。

- 这些都是积分函数的 **单极点**，除了原点是 **可去极点**。
* 计算留数
    $$
    \mathop{\operatorname{Res}}_{z = k \pi} \frac{z}{\sin z}
    = \frac{z}{(\sin z)'} \Big|_{z = k \pi} = \frac{k\pi}{\cos k\pi} = (-1)^k k\pi \xrightarrow{k = 0} 0
    $$

</div>


---

### 常见围道积分的计算


<div class="proof">

**求解**

于是积分等于
$$
\begin{align*}
  \mathcal{I}
= & \ 2\pi i \sum_{k = - n}^{+n} (k \pi) (-1)^k\\
= & \ 2\pi i \sum_{k = 1}^{+n} \red{(k \pi)} \blue{(-1)^k}
+ 2\pi i \sum_{k = 1}^{n} \red{(- k \pi)} \blue{(-1)^{- k}} = 0
\end{align*}
$$
</div>

---

### 常见围道积分的计算

* 计算积分
  $$
  \mathcal{I} = \oint_{|z| = 1} e^{\frac{1}{z}}
  $$

  <div class="proof">

  **求解**

  - 注意到 $z = 0$ 是 **本性奇点**，只须 Laurant 展开然后取 $-1$-次幂项。

  * 在原点去心邻域 $0 < |z| < \infty$ 中定义 **<green>$\tilde z = 1/z$</green>**，于是
    $$
    e^{\tilde z} = \sum_{k \ge 0} \frac{1}{k!} (\tilde z)^k = \sum_{k \ge 0} \frac{1}{k!} \frac{1}{z^k}
    \qquad \Rightarrow\lambda_{-1} = 1 \qquad \Rightarrow \mathcal{I} = 2\pi i \times 1
    $$
  </div>

---

### 其他复积分计算

* 假设 $f(z)$ 在 $a$ 处有一个 **单极点**，$\operatorname{Arc}(r, \theta_1 \to \theta_2)$ 是以 $a$ 为中心半径为 $r$ 的一小段弧，从辐角 $\theta_1$ 延伸到 $\theta_2$。论证
  $$
  \frac{1}{i(\theta_1 - \theta_2)}\lim_{r \to 0}\int_{\operatorname{Arc}(r, \theta_1 \to \theta_2)} f(z) dz
  = \operatorname{Res}_{z = a}f(z)
  $$

  <center>
  
  ![width:400px](image/ex-1.svg)
  </center>

---

### 其他复积分计算

* 假设 $f(z)$ 在 $a$ 处有一个 **单极点**，$\operatorname{Arc}(r, \theta_1 \to \theta_2)$ 是以 $a$ 为中心半径为 $r$ 的一小段弧，从辐角 $\theta_1$ 延伸到 $\theta_2$。论证
  $$
  \frac{1}{i(\theta_1 - \theta_2)}\lim_{r \to 0}\int_{\operatorname{Arc}(r, \theta_1 \to \theta_2)} f(z) dz
  = \operatorname{Res}_{z = a}f(z)
  $$

---
### 其他复积分计算

<div class="proof">

**求解**

- 由于 $a$ 是单极点，在 $a$ 的去心邻域，$f(z) = \frac{R}{z - a} + g(z)$，其中 **<green>$R$ 是 $f$ 在 $a$ 的留数**，$g(z)$ 是一个在 $a$ 邻域内解析的函数。
- 因此，
  $$
  \int_{\operatorname{Arc}(r, \theta_1 \to \theta_2)} f(z) dz
  = \int_{\theta_1}^{\theta_2} \frac{R}{r e^{i\theta}} r ie^{i\theta} d\theta
  + \int_{\operatorname{Arc}(r, \theta_1 \to \theta_2)} g(z) dz
  $$
</div>

---

### 其他复积分计算

<div class="proof">

**求解**

* 第一项 **<red>非零** (分子分母 $r$ 抵消了)
  $$
  \int_{\theta_1}^{\theta_2} \frac{R}{r e^{i\theta}} r ie^{i\theta} d\theta
  = i \green{R} (\theta_2 - \theta_1)
  $$
* 第二项 ($\propto r$) **<red>趋于零**，因为 $g(z)$ 解析，因此在 $a$ 的小邻域内 **有界**，而积分曲线长度 **趋于零**。
* 因此，
  $$
  \lim_{r \to 0}\int_{\operatorname{Arc}(r, \theta_1 \to \theta_2)} f(z) dz = i (\theta_2 - \theta_1) \green{\mathop{\operatorname{Res}}_{z = a}f(z)}
  $$
</div>

---

### 其他复积分计算

* **推论**：若 $f(z)$ 在 $a$ 处有单极点，则小半圆积分给出 **半留数**
  $$
  \frac{1}{2\pi i}\int f(z)dz = \orange{\frac{1}{2}} \mathop{\operatorname{Res}}_{z = a} f(z)
  $$

  <center>
  
  ![width:250px](image/half-circle.svg)
  </center>

---

### 三角有理函数积分

* 考虑 **有理函数** $R(x, y)$，以及 $[0, 2\pi]$ 积分
  $$
  \mathcal{I} = \int_0^{2\pi} R(\cos \theta, \sin \theta) d\theta
  $$

* 利用
  $$
  \cos \theta = \frac{1}{2} (e^{i \theta} + e^{- i \theta}), \qquad
  \sin \theta = \frac{1}{2i} (e^{i \theta} - e^{- i \theta})
  $$

* 重写
  $$
  \mathcal{I} = \oint_{|z| = 1} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right) \frac{dz}{iz}, \qquad z = e^{i \theta}
  $$

<div class='proof comment'>

**$d\theta$**

注意 $dz = d(e^{i\theta}) = e^{i \theta} i d\theta = z i d\theta$，因此 $d\theta = dz/(iz)$.
</div>

---

### 三角有理函数积分

<div class='proof'>

**说明**

积分微元
$$
dz = de^{i \theta} = i e^{i \theta} d\theta = iz d\theta
\qquad\Rightarrow \qquad
d\theta = \frac{dz}{iz}
$$
</div>

---

### 三角有理函数积分

* 考虑 **$0 < a < 1$**。计算
  $$
  \mathcal{I} = \int_0^{2\pi} \frac{d\theta}{1 + a \cos\theta}
  $$

  <div class="proof">

  **求解**

  按公式，
  $$
  \mathcal{I} = \oint_{|z|= 1 } \frac{1}{1 + a \frac{z + z^{-1}}{2}} \frac{dz}{iz} = (-2i) \oint_{|z| = 1}\frac{dz}{az^2 + 2z + a}
  $$
  </div>

---

### 三角有理函数积分


<div class="proof">

**求解**

- 分母有两个根 (积分函数的两个 **单极点**)
  $$
  z_\pm = \frac{-2 \pm \sqrt{4 - 4a^2}}{2a} = - \frac{1}{a} \pm \sqrt{\frac{1}{a^2} - 1}
  $$
* 显然，$|z_-| > |z_+|$，因为 $0 < a < 1$
</div>

---

### 三角有理函数积分


<div class="proof">

**求解**

- 接下来判断两个单极点与 **单位圆** 的 **相对位置**。

* 韦达定理：
  $$
  z_+ z_- = 1 \Rightarrow |z_+| |z_-| = 1 \Rightarrow |z_+| < 1 < |z_-|
  $$
* 因此，$z_-$ 位于单位 **圆外**，$z_+$ 位于单位 **圆内**。
</div>

---

### 三角有理函数积分


<div class="proof">

**求解**

- 积分提取单位圆 **内** $z_+$ 处的留数，
  $$
  \begin{align*}
  \mathcal{I} & 
  = 2\pi i(-2i) \mathop{\operatorname{Res}}_{z = z_+}\frac{1}{a(z - z+) (z - z_-)} = \frac{2\pi i(-2i)}{a(z_+ - z_-)}
  =  \frac{2\pi}{\sqrt{1 - a^2}}
  \end{align*}
  $$
  因为 $z_+ - z_- = 2 \sqrt{a^{-2} - 1}$
</div>

---

### 无穷积分与瑕积分

- 考虑 **<red>$m \ge 0$**，计算
  $$
  \mathcal{I} = \int_{-\infty}^{+\infty} f(x) e^{i m x}dx
  $$
  其中 $f(x)$ 满足如下性质
  * 在 **上半平面** 几乎处处解析，除了 **有限个** 孤立奇点 $\{a_i\}$
  * 有如下 **<green>大 $z$ 一致趋零行为**: 当 $|z| \to +\infty$ 且 $\operatorname{Im}z \ge 0$
    $$
    \left\{\begin{array}{c c}
    z f(z) \Rightarrow 0, & \text{若} \ m = 0 \\
    f(z) \Rightarrow 0, & \text{若} \ m > 0
    \end{array}\right .
    $$

---

### 无穷积分与瑕积分

- 则有
  $$
  \lim_{R \to +\infty} \int_{-R}^{+R}f(x)e^{im x}dx
  = 2\pi i \sum_{i} \mathop{\operatorname{Res}}_{z = a_i} \Big[f(z)e^{im z} \Big]
  $$

  <div class='proof comment'>

  **一致趋零**

  函数 **<green>$f(z) \Rightarrow 0$** 指的是函数 $f$ **<green>一致趋零**，即当 $z \to \infty$ (沿上半平面的所有方向) $f(z)$ 都趋于零，而且趋零的速度 **大致相同**：
  
  <center>
  
  对 $\forall \epsilon > 0$，$\exists R > 0$，s.t. 当 $|z| > R$ 就有 $|f(z)| < \epsilon$
  </center>
  </div>



---

### 无穷积分与瑕积分

<div class='proof comment'>

**一致趋零例子**

下面是常见的 $z \to \infty$ 时一致趋零的函数
$$
\begin{align*}
	\frac{1}{z^{m > 0}} \Rightarrow 0, \qquad
	\frac{P_m(z)}{P_{m + 1}(z)} \Rightarrow 0 \ , \qquad
	\frac{1}{z^{m > 0} + a} \Rightarrow 0, \ a \in \mathbb{C} \ .
\end{align*}
$$
</div>

---

### 无穷积分与瑕积分

<div class="proof">

**证明概要**

$[-R, R]$ 的积分可以通过添加大半圆变成围道积分，

<center>

![width:700px](image/improper-integral-1.svg)
</center>
</div>

---

### 无穷积分与瑕积分

<div class="proof">

**证明概要**

(1) **Jordan 引理 (证明见教材)**：大 $z$ **一致趋零**行为导致
$$
\begin{align*}
	\lim_{R \to +\infty}\red{\int_{\Gamma_R}} f(z) e^{i m z} dz = 0 \ .
\end{align*}
$$

(2) 利用留数定理
$$
\begin{align*}
	\left(\int_{-R}^{+R} + \red{\int_{\Gamma_R}}\right)f(z) e^{i m z}dz
			= & \ \purple{2\pi i \sum_{i} \mathop{\operatorname{Res}}_{z = a_i} \left[f(z) e^{i m z}\right]}\\
	\orange{\lim_{R \to + \infty}} \int_{-R}^{+R} f(z)e^{imz}dz = & \ \purple{2\pi i \sum_{i} \mathop{\operatorname{Res}}_{z = a_i} \left[f(z) e^{i m z}\right]} \ .
\end{align*}
$$
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**主值与一般值**

- 无界积分 $\int_{-\infty}^{+\infty}$ 本身 **<red>没有明确定义**
* 上面的极限
  $$
  \begin{align*}
    \lim_{R \to +\infty}\int_{-R}^{+R}f(x) e^{i m x} dx 
  \end{align*}
  $$
  **<green>定义** 了无界积分的 **<green>主值 (principal value)**。在许多场合中，$\int_{-\infty}^{+\infty}$ 指代的就是主值。
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**主值与一般值**

- 除了主值，还可以考虑 **<green>一般值**，
  $$
    \coloneqq \lim_{R_1 \to \infty,R_2 \to \infty}\int_{- R_1}^{R_2} f(x) e^{i m x}dx \ .
  $$

* 主值是一般值的 **特殊情况** $R_1 = R_2$，比一般值更容易 **存在**。
  $$
  
    \int_{- R_1}^{R_2} \frac{x}{x^2 + 1} dx = \frac{1}{2}\ln \frac{1 + R_2^2}{1 + R_1^2} \xrightarrow{R_2 = \lambda R_1, R_1 \to +\infty} \frac{1}{2}\ln(\lambda^2) \ .
  
  $$
  若一般值确实 **存在**，则主值 $=$ 一般值。
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**$m$ 的符号**

- 上述定理只适用于 **<purple>$m = 0$ 或者 $m > 0$**。
- 为了 $\Gamma_R$ 积分最后 **<red>为零**，在 **上半平面** 中 $z \to \infty$ 时候我们希望指数因子快速 **衰减**：利用 $z = |z|e^{i\theta} = \purple{|z|\cos\theta + i |z| \sin \theta}$
  $$
    e^{im z} = e^{im (\purple{|z| \cos \theta + i |z| \sin \theta})} = e^{ i m |z| \cos \theta} \red{e^{- m |z| \sin \theta}}, \qquad \theta \in [0, \pi]
  $$
  因 $\red{\sin \theta} \ge 0$，需要 $m \ge 0$ 保证快速衰减 (或不增长 <gray>~~不干活可以但别捣乱~~</gray>)。

* 如果 $m < 0$，则应当取 **下半平面** 的 $\Gamma_R$ 以及 **下半平面** 的孤立奇点留数。
</div>

---

### 无穷积分与瑕积分

- 计算积分
  $$
  \begin{align*}
    \int_{-\infty}^{+\infty} \frac{1}{x^{2n} + 1}dx, \qquad n = 1, 2,3,\ldots \ .
  \end{align*}
  $$

  <div class="proof">

  **求解**

  * 由于 **<purple>$n \ge 1$</purple>**，因此积分函数可以看成 **<purple>$f(z) e^{i m z}$ with $m = 0$**，**<purple>$zf(z) \Rightarrow 0$</purple>**。

  * 积分函数的 **单极点** (不含 $\pm 1$)
    $$
      z^{2n} + 1 = 0 \quad \Rightarrow \quad a_k = e^{\frac{\pi i}{2n}} e^{\frac{2\pi i}{2n} k}, \quad k = 0, 1, 2, \ldots, \orange{2n - 1} \ .
    $$
  </div>

---

### 无穷积分与瑕积分

<div class='proof'>

<center>

![width:500px](image/x2n+1.jpg)
</center>
</div>

---

### 无穷积分与瑕积分


<div class="proof">

**求解**

- 其中位于 **上半平面** 的是 $k = 0, 1, 2, \ldots, \orange{n - 1}$，共 $n$ 个。
- 求留数
  $$
    \mathop{\operatorname{Res}}_{z = a_k}f(z) 
    \stackrel{\text{公式 3}}{=} \frac{1}{2n a_k^{2n - 1}}
    = \frac{a_k}{2n \green{a_k ^{2n}}} = \frac{a_k}{2n \green{(-1)}} = \purple{- \frac{a_k}{2n}}
  $$
* 根据积分公式
  $$
    \mathcal{I}
    =  2\pi i\sum_{k = 0}^{n - 1} \mathop{\operatorname{Res}}_{z = a_k} f(z)
    = \purple{-} \frac{2\pi i}{\purple{2n}} \sum_{k = 0}^{n -1} \purple{a_k}
    = - \frac{2\pi i}{2n} \sum_{k = 0}^{n -1} \orange{e^{\frac{\pi i}{2n}}} e^{\frac{k \pi i}{n}}
  $$
</div>

---

### 无穷积分与瑕积分



<div class="proof">

**求解**

利用等比数列求和公式
$$
\begin{align*}
  = & \ - \frac{2\pi i}{2n} \orange{e^{\frac{\pi i}{2n}}} \frac{(1 - \red{e^{ \frac{\pi i}{n}n}} )}{1 - e^{\frac{\pi i}{n}}}
  \stackrel{\red{e^{\frac{\pi i }{n}n} = -1}}{=}\
  - \frac{2\pi i}{n}  \frac{1}{\purple{e^{- \frac{\pi i}{2n}} - e^{\frac{\pi i}{2n}}}}\\
  = & \ - \frac{2\pi i}{n}  \frac{1}{\purple{2i \sin(- \frac{\pi}{2n})}}
  = \frac{\pi}{n} \frac{1}{\sin \frac{\pi}{2n}} \ .
\end{align*}
$$
</div>

---

### 无穷积分与瑕积分

- 计算积分
  $$
  \begin{align*}
    \mathcal{I} = \int_0^{+\infty} \frac{\cos mx}{x^{2} + 1} dx, \qquad m > 0
  \end{align*}
  $$
  <div class='proof comment'>
  
  **积分下限**

  注意下限是 $0$，不是 $-\infty$
  </div>


---
### 无穷积分与瑕积分
<div class="proof">

**求解**

- 首先要把积分化为全实轴积分。
  $$
  \mathcal{I} = \orange{\frac{1}{2}} \int_{-\infty}^{+\infty} \frac{\cos mx}{x^2 + 1}dx
  $$
- 利用 **偶** 函数性，和 **奇** 函数性，
  $$
  \mathcal{I}
    = \frac{1}{2} \int_{-\infty}^{+\infty} \frac{\cos mx + \red{i \sin mx}}{x^2 + 1}dx
    = \int_{-\infty}^{+\infty} \frac{1}{2}\frac{e^{i m x}}{x^2 + 1}dx
  $$
  积分函数现在是 $f(x) e^{i m x}$ 的形式，其中 $m > 0$
</div>

---

### 无穷积分与瑕积分


<div class="proof">

**求解**

- $f(z)$ 在上半平面有单极点 $z = + i$，
  $$
    \mathop{\operatorname{Res}}_{z = + i} f(z)e^{i m z} = \mathop{\operatorname{Res}}_{z = + i} \frac{1}{2}\frac{e^{i m z}}{z^2 + 1}
    = \left[\frac{1}{2}\frac{e^{i m z}}{(z^2 + 1)'}\right]_{z = i} = \purple{\frac{1}{2} \frac{e^{-m}}{2i}} \ .
  $$
* 因此
  $$
    \mathcal{I} = (2\pi i) \times \purple{\frac{1}{2} \frac{e^{-m}}{2i}} = \frac{\pi}{2} e^{-m} \ .
  $$
</div>


---
### 无穷积分与瑕积分

<div class='proof comment'>

另一种思路是取**实部**：
$$
\int_{-\infty}^{+\infty} \frac{\cos m x}{x^2 + 1}dx = \operatorname{Re}\int_{-\infty}^{+\infty} \frac{e^{i m x}}{x^2 + 1} dx \ .
$$
</div>

---

### 无穷积分与瑕积分

- 考虑 $m > 0$，计算积分
  $$
  \begin{align*}
    \mathcal{I} = \int_{-\infty}^{+\infty} \frac{\sin mx}{x - i} dx, \qquad m > 0
  \end{align*}
  $$

  <div class="proof">

  **解**

  - 拆解 $\sin mx$，
    $$
      \mathcal{I} = \frac{1}{2i} \int_{-\infty}^{+\infty} \frac{e^{i m x} - e^{- i m x}}{x - i} dx \ .
    $$
  - 两个积分分别计算
  </div>

---

### 无穷积分与瑕积分



<div class="proof">

**解**

- 第一个积分 $\frac{1}{z-i}$ 在上半平面有单极点 $i$，利用 $\operatorname{Res}_{z = i} \frac{e^{i m z}}{z - i} = \orange{e^{- m}}$，
  $$
    \frac{1}{2i}\int_{-\infty}^{+\infty} \frac{e^{i m z}}{z - i}dz = \frac{1}{2i} (2\pi i) \orange{e^{-m}} = \pi e^{-m} \ .
  $$

* 第二个积分可以利用变量替换 $z' = -z$，
  $$

    \int_{-\infty}^{+\infty} \frac{e^{-i m z}}{z - i}dz = - \int_{+\infty}^{-\infty} \frac{e^{i m z'}}{ - z' - i}dz' = 0

  $$

  因为 $(z' + 1)^{-1}e^{i m z'}$ 在 $z'$ 上半平面 **<red>没有** 奇点。
</div>

---

### 无穷积分与瑕积分

<div class="proof">

**解**

总结
$$

	\mathcal{I} = \pi e^{-m} \ .

$$
</div>

<div class='proof comment'>

**虚部**

小心，不能直接用**取虚部**的方法计算：
$$

	\operatorname{Im} \bigg(\frac{e^{i m z}}{z - i}\bigg) \ \red{\ne} \ \frac{\sin mz}{z - i} \ .

$$
</div>



---

### 无穷积分与瑕积分

- **定理**：函数 $f(z)$ 在 **上半平面** 和 **实轴** 上几乎处处解析，除了有限个上半平面孤立奇点 $\{a_i\}$ 和实轴上 **<red>单极点 $\{b_j\}$**。此外，
  $$
  \begin{align*}
    z \xrightarrow{\text{上半平面}} \infty: \quad \left\{\begin{array}{c c}
      z f(z) \Rightarrow 0, & m = 0 \\
      f(z) \Rightarrow 0, & m > 0
    \end{array}\right . \ .
  \end{align*}
  $$
  则有 
  $$
  \begin{align*}
    \int_{-\infty}^{+\infty} f(x) e^{i m x} dx = 2\pi i \left[
    \sum_{i} \mathop{\operatorname{Res}}_{z = a_i} f(z) e^{i m z}
    + \orange{\frac{1}{2}} \sum_{j} \mathop{\operatorname{Res}}_{z = b_j} f(z) e^{i m z} 
    \right] \nonumber
  \end{align*}
  $$

---

### 无穷积分与瑕积分

<div class='proof comment'>

**主值**

此处的符号 $\int_{-\infty}^{+\infty}$ 同样指代积分 **<green>主值**，定义为
$$

	\green{\int_{-\infty}^{+\infty} = \lim_{\substack{ R\to \infty \\ \epsilon \to 0}} \int_{[- R , R] - \cup_j (b_j - \epsilon, b_j + \epsilon)}}

$$

<center>

![width:550px](image/improper-integral-2.svg)
</center>
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**证明大意**

<center>

![width:480px](image/improper-integral-2-enclosed.svg)
</center>

要点：绕 $b_j$ 的 **<green>下小半圆 $C_j$** 积分为 **半留数**
$$

	\int_{C_j} f(z) e^{i m z} = 2\pi i \orange{\frac{1}{2}} \mathop{\operatorname{Res}}_{z = b_j} \Big[f(z) e^{i m z}\Big] \ .

$$
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**证明大意**

留数定理
$$
\begin{align*}
	& \ 2\pi i \left[\sum_{i} \mathop{\operatorname{Res}}_{z = a_i} f(z)e^{im z}
	+ \sum_{j}\mathop{\operatorname{Res}}_{z = b_j} f(z)e^{im z}\right] \\
	= & \ 2\pi i \int f(x)e^{i m x}dx + 2\pi i \sum_{j} \orange{\frac{1}{2}}\mathop{\operatorname{Res}}_{z = b_j} f(z)e^{im z}
\end{align*}
$$
其中，左边的完整留数项被右边的半留数项抵消了 **<red>一半**。
</div>

---

### 无穷积分与瑕积分

- 考虑 $m > 0$，计算积分
  $$

    \mathcal{I} = \int_0^{+\infty} \frac{\sin mx}{x} dx \ .

  $$
  <div class='proof comment'>
  
  注意积分下限
  </div>

---
### 无穷积分与瑕积分

<div class="proof">

**解**

- 利用偶函数性，
  $$

    \mathcal{I} = \purple{\frac{1}{2}} \int_{-\infty}^{+\infty} \frac{\sin mx}{x} dx
    = \purple{\frac{1}{2}} \orange{\operatorname{Im}} \int_{-\infty}^{+\infty} \frac{e^{i m x}}{x} dx \ .

  $$
* 于是利用积分公式以及单极点 $z = 0$，可得
  $$

    \mathcal{I}
    = \purple{\frac{1}{2}}\operatorname{Im} \left[{2\pi i \times \orange{\frac{1}{2}} \mathop{\operatorname{Res}}_{z = 0} \frac{1}{z}e^{i m z}}\right]
    = \frac{\pi}{2} \ .

  $$
</div>

---

### 无穷积分与瑕积分

<div class='proof comment'>

**$m$ 无关**

上述积分结果与 **<red>$m$ 无关**；后面介绍 $\delta$ 函数还会碰到



<center>

<video width='800' src='media/videos/animations/1080p60/DeltaFunctionTrigonometric.mp4' controls></video>
</center>
</div>

---

### 无穷积分与瑕积分

- 考虑 $m > 0, a > 0$，计算积分
  $$

    \mathcal{I} = \int_{-\infty}^{+\infty} \frac{\sin mx}{x - a}dx

  $$

---
### 无穷积分与瑕积分

<div class="proof">

**解**

- 利用 **$a \in \mathbb{R}$**，重写
$$

  \mathcal{I} = \purple{\operatorname{Im}} \int_{-\infty}^{+\infty} \frac{e^{i m x}}{x - a} dx
  = \purple{\operatorname{Im}} \Bigg[2\pi i \orange{\frac{1}{2}} \mathop{\operatorname{Res}}_{z = a} \Big(\frac{1}{z} e^{i m z}\Big)\Bigg]

$$

* 利用 $\operatorname{Res}_{z = a}z^{-1}e^{i m z} = e^{im a}$，
  $$

    \mathcal{I} = \operatorname{Im}\Big[\pi i e^{i m a}\Big] = \pi \cos (ma)

  $$
</div>

---

### 大圆弧引理

- **大圆弧引理**：若 $f(z)$ 在大圆弧 $C_R = \{R e^{i \theta} \ | \ \theta_1 \le \theta \le \theta_2\}$ 上 **连续**，且当圆弧上的点 $z$ 的大小 $|z| \to \infty$，$z f(z) \Rightarrow \lambda$，则
  $$

    \lim_{R \to +\infty}\int_{C_R} f(z) dz = i \lambda (\theta_2 - \theta_1) \ .

  $$
  <div class='proof comment'>
  
  与之前的 Jordan 引理类似
  </div>

---

### 小圆弧引理

- 考虑一小段圆弧 $S_\epsilon = \{a + \epsilon e^{i\theta} \ | \ \theta_1 \le \theta\le \theta_2 \}$

* **小圆弧引理**：设 $f(z)$ 在 $a$ 附近小圆弧上 **连续**，当 $z \to a$，$(z - a)f(z) \Rightarrow \lambda$，则
  $$

    \lim_{\epsilon \to 0}\int_{C_\epsilon}f(z) dz = i \lambda (\theta_2 - \theta_1) \ .

  $$

  <center>
  
  ![width:300px](image/small-arc.svg)
  </center>

---
### 小圆弧引理

<div class='proof comment'>

**解析性**

小圆弧引理 **<red>没有假设** 复解析性，只需要连续性和一致极限存在
</div>

<div class='proof comment'>

若 $a$ 是 $f(z)$ 的单极点，则 $\lambda = \operatorname{Res}_{z = a}f(z)$
</div>

- **推论**：若 $(z - a)f(z) \Rightarrow 0$，那么不管 $\theta_1, \theta_2$ 为何值，
  $$
  \lim_{\epsilon \to 0} \int_{C_\epsilon} f(z) dz = 0
  $$



---

### 根式积分例子

- 考虑根式函数的积分
  $$

    \mathcal{I} = \int_0^{+\infty} f(x) dx, \qquad f(x)= \frac{x^{1/3}}{x^2 + 1} \ .

  $$
* 若替换 $x \to z$：$f(z)$ 多值函数，**<red>三阶支点 $0, \infty$**，$\pm i$ 是**单极点**

---
### 根式积分例子

<center>

![width:600px](image/three-points.svg)

分子 $z^{1/3}$ 的的割线与单值分支设定：$(-1)^{1/3} = e^{\frac{\pi i}{3}}$
</center>

---

### 根式积分例子

<div class='proof comment'>

**无穷近似**

- 当 $x \ge 0$ 时，$x^{1/3}$ 有非常 **确定** 的实数值，因此 $x^{1/3}/(x^2 + 1)$ 也有非常确定的值。

* 升级 $x \to z$ 后，**<green>$[0, +\infty)$ 上方直线 $C_1$** 上 $z^{1/3}/(z^2 + 1)$ 的函数值无限接近 $x^{1/3}/(x^2 + 1)$ 在正实轴的值。

  <center>

  ![width:500px](image/complex-plane-cut.svg)
  </center>

* 通过研究 $C_1$ 积分，可以无穷近似 **<green>原本的积分 $\mathcal{I}$**。
</div>

---

### 根式积分例子

- 补全积分围道

  <center>
  
  ![width:500px](image/multi-value-contour.svg)
  </center>

---

### 根式积分例子

- 函数在割线上方 $C_1$ 与下方 $C_2$ 的取值，
  $$

    \lim_{\epsilon \to +0}f(x + i \epsilon) = \frac{x^{1/3}}{x^2 + 1}, \quad
    \lim_{\epsilon \to +0}f(x - i \epsilon) = \orange{ e^{\frac{2\pi i}{3}}} \frac{x^{1/3}}{x^2 + 1} \ .

  $$

  <center>
  
  ![width:600px](image/phase-difference.svg)
  </center>  

---

### 根式积分例子

- 因此 ($C_1$ 向右，$C_2$ 向左)
  $$

    \int_{C_2} f(z) dz = \red{-} \orange{ e^{\frac{2\pi i}{3}}} \green{\int_{C_1}f(z) dz} = - e^{\frac{2\pi i}{3}} \green{\mathcal{I}} \ .

  $$
  <div class='proof comment'>
  
  $C_1$ 积分几乎就是原本 $[0, +\infty)$ 积分
  </div>
* 因此
  $$
  \left({\int_{C_1} + \int_{C_2}}\right)f(z)dz 
  = (1 - e^{\frac{2\pi i}{3}}) \green{\mathcal{I}} \ .
  $$

---
### 根式积分例子


- 因此，
  $$
  \begin{align*}
    \oint_C f(z) dz = \int_{C_1 + C_2 + C_r + C_R} f(z) dz = & \ 2\pi i \sum_\pm \mathop{\operatorname{Res}}_{z \to \pm i}f(z) \\
    (1 - e^{\frac{2\pi i}{3}})\mathcal{I} + \cancel{\red{\int_{C_r + C_R} f(z) dz}} 
    = & \ 2\pi i \sum_\pm \mathop{\operatorname{Res}}_{z \to \pm i}f(z)
  \end{align*}
  $$
- 大圆弧小圆弧引理：$C_r + C_R$ 积分 **<red>不贡献**
  $$
  (z - 0) \frac{z^{1/3}}{z^2 + 1} \stackrel{z \to 0}{\Rightarrow} 0, \qquad
  z \frac{z^{1/3}}{z^2 + 1} \stackrel{z \to \infty}{\Rightarrow} 0
  $$

---

### 根式积分例子

- 计算留数，利用公式 3，
  $$

    \mathop{\operatorname{Res}}_{z = \pm i} \frac{z^{1/3}}{z^2 + 1}
    = \frac{z^{1/3}}{(z^2 + 1)'}\bigg|_{z = \pm i}
    = \frac{z^{1/3}}{2z} \bigg|_{z = \pm i}

  $$
* 分子 $z^{1/3}$ 是 **多值函数**，我们已经选择了割线，并要求
  $$

    z^{1/3}\bigg|_{z = + i} = \purple{e^{\frac{1}{3} \frac{\pi i}{2}}}, \quad
    z^{1/3}\bigg|_{z = - i} = \green{e^{\frac{1}{3} \frac{3\pi i}{2}}} \\
    ~\\
    \Rightarrow\mathop{\operatorname{Res}}_{z = +i}f(z) = \frac{1}{2i}\purple{e^{\frac{1}{3} \frac{\pi i}{2}}}, \quad
    \mathop{\operatorname{Res}}_{z = -i}f(z) = \frac{\green{e^{\frac{1}{3}\frac{3\pi i}{2}}}}{2(-i)} = - \frac{1}{2}

  $$

---

### 根式积分例子

- 因此
  $$
  \begin{align*}
    (1 - e^{\frac{2\pi i}{3}}) \mathcal{I}
    = & \ 2\pi i\left( \frac{1}{2i}e^{\frac{\pi i}{6}} + (- \frac{1}{2})\right) \\
    \Rightarrow \qquad \mathcal{I} = & \  \frac{\pi}{\sqrt{3}} \ .
  \end{align*}
  $$




---

### 计算积分的另一种方法

* 使用电脑软件，如 Mathematica

---

# 回顾

---

### 回顾

* 有两种常见的解析区形状：开圆盘、环状
* 问题：设 $f$ 在图中开圆盘中解析, 下面三个表达式分别等于多少？

  <center>
  
  ![width:900px](image/question-3.svg)
  </center>

---

### 回顾

* 若函数 $f(z)$ 在图中开圆盘中解析，以 $a$ 为中心作泰勒展开
  $~$
  $
  \displaystyle f(z) =\sum _{n=0}^{+\infty }\left[\oint _{\Gamma }\frac{d\zeta }{2\pi i}\frac{f( \zeta )}{( \zeta -a)^{n+1}}\right]( z-a)^{n}
  $

  <div style="position:absolute;top:30%;left:65%">

  ![width:400px](image/question-1.svg)
  </div>

* 问题：$\Gamma$ 应该取 **<red>大** 圆圈、**<red>小** 圆圈还是 **<red>两个都可以**？

---

### 回顾

* 若函数 $f(z)$ 在图中开圆盘中几乎处处解析，红点为 **<red>奇点**。

  <div style="position:absolute;top:30%;left:65%">

  ![width:400px](image/question-2.svg)
  </div>

* 问题：是否有 $f(z) = \sum_{n = 0}^{+\infty}\frac{1}{n!} f^{(n)}(a)(z - a)^n$？
* 问题：是否有 $f(z') = \sum_{n = 0}^{+\infty}\frac{1}{n!} f^{(n)}(a)(z' - a)^n$？
