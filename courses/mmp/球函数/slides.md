---
marp: true
theme: rose-pine-dawn-modern
paginate: true
_paginate: skip
size: 16:9

math: katex

---

<center>

# 球函数

![width:800px](images/anya-intro.png)
</center>

$$
\gdef\red#1{{\color{cb8680}{#1}}} 
\gdef\green#1{{\color{4f8d63}{#1}}} 
\gdef\gray#1{{\color{gray}{#1}}} 
\gdef\purple#1{{\color{B189C6}{#1}}} 
\gdef\orange#1{{\color{dfa04b}{#1}}}
\gdef\white#1{{\color{white}{#1}}}
$$

---
<!-- footer: 球函数 -->

# 纲要

- 轴对称球函数
- Legendre 多项式的性质
- Legendre 多项式的物理应用
- 一般球函数与连带勒让德函数
- 球谐函数

---

# 分离变量

---

### 三维球坐标下 $\nabla^2 u = 0$ 的分离变量

- 球坐标下的拉普拉斯方程变量分离得到
  $$
  u(\mathbf{r}) = R(r) Y(\theta, \varphi) = R(r) H(\theta) \Phi(\varphi)
  $$
- $u$ 的**单值性** $\Rightarrow$ $\Phi(\varphi)$ 的**周期性**
  $$
  \Phi(\varphi + 2\pi) = \Phi(\varphi)
  \quad
  \Rightarrow\quad
  \Phi(\varphi) = e^{im \varphi}, m \in \mathbb{Z}
  $$
* 径向方程
  $$
  r^2 R'' + 2r R' - \lambda R = 0
  $$

---
### 三维球坐标下 $\nabla^2 u = 0$ 的分离变量

<center>

<iframe src='images/spherical_coordinates.html' frameborder='0' style='width:1024px;height:640px'></iframe>

</center>

---
### 三维球坐标下 $\nabla^2 u = 0$ 的分离变量
- $H(\theta)$ 重命名为 $P(x = \cos \theta)$，满足
  $$
  \frac{d}{dx}\bigg[(1 - x^2)\frac{dP}{dx}\bigg] + \bigg(\lambda - \frac{m^2}{1 - x^2}\bigg)P = 0
  $$
  <div class='proof comment'>

  $m$ 值来自 $\Phi(\varphi)$ 的指数
  
  $x = \pm 1$ 对应 $\theta = 0, \pi$，即南北极位置

  </div>

---
### 三维球坐标下 $\nabla^2 u = 0$ 的分离变量

- $Y(\theta, \varphi) = H(\theta) \Phi(\varphi)$ 应当形成**球面上的单值函数**
  <div class='proof comment'>

  - 当 $m \ne 0$，$H(\theta = 0, \pi) = 0$ 才能保证在南北极的函数值不随 $\varphi$ 变化
  - 当 $m = 0$，$H(\theta = 0, \pi)$ 只要**有限**即可

  </div>
- 迫使 $P$ 满足如下自然边界条件
  $$
  \left\{\begin{array}{cc}
    P(\pm 1) = 0 & m \ne 0\\
    P(\pm 1) < \infty & m = 0
  \end{array}\right.
  $$

---
<!-- header: 轴对称问题的一般解 -->

# 轴对称问题的一般解

---
### 轴对称问题的一般解

- **轴对称**问题：有一些特殊问题具有**轴对称**性，解与 $\varphi$ **<red>无关**
- 要求 $m = 0$，勒让德方程 + 自然边界条件
  $$
  \frac{d}{dx}\bigg[(1 - x^2) \frac{dP}{dx}\bigg] + \lambda P = 0, \qquad |P(\pm 1)| < \infty 
  $$
  <div class='proof comment'>

  拆解导数，除以 $1 - x^2$ 得到二阶常微分方程标准形式
  $$
    \frac{d^2P}{dx^2} - \frac{2x}{(1-x^2)} \frac{dP}{dx} + \frac{\lambda}{(1-x^2)} P = 0
  $$

  </div>


---
### 轴对称问题的一般解
- $x = 0$ 是 **<green>常点**，$x = \pm 1$ 是**正则奇点**
- **<red>为什么 $x = \pm 1$ 是正则奇点？**

---
### 轴对称问题的一般解

- 以 **<green>原点** (常点) 为中心求**级数解**
- 两个线性独立解 $y_0(x), y_1(x)$：当 $\lambda$ 取 **generic 值**，两个解 **<red>不满足**自然边界条件
  <div class='proof comment'>

  **对数发散**

  两个级数解的渐近形式为
  $$
  y(x) \sim y_0 \sum_{m}^{+\infty} \frac{1}{2m}x^{2m}
  + y_1 \sum_{m}^{+\infty} \frac{1}{2m+1}x^{2m+1}
  $$
  两个级数在 $x = \pm1$ 处**都**呈现 $\ln(1\mp x)$ 的**对数发散**
  

  </div>

---
### 轴对称问题的一般解


- **<red>对数发散和 Fuch's 定理的对数解有什么关系？**
  <answer>Fuch's 定理预言在正则奇点处会有对数解，在奇点处就有发散</answer>
- **<red>Fuch's 定理预言几个对数解？** <answer>最多一个</answer>
* **<red>这里获得几个对数发散解？**
  <answer>可以线性组合出 $\ln(1 + x)$ 和 $\ln(1-x)$</answer>
* **<red>是否有矛盾？**
  <answer>没有矛盾；两个对数发散只在一侧显现</answer>

<div style="position:absolute; top:300px; right:100px">

![width:400px](images/anya_logarithmic_divergence.png)
</div>

---
### 轴对称问题的一般解
- **自然边界条件** 要求本征值
  $$
  \lambda = 2m (2m + 1), \qquad (2m + 1)(2m + 2)
  $$
  <div class='proof comment'>
  
  即 $\lambda = \ell(\ell + 1)$，$\ell = 0, 1, 2, 3, \cdots$
  </div>
- 本征函数为 $\ell$-阶 Legendre 函数 $P_\ell(x) = P_\ell(\cos \theta)$
  <div class='proof comment'>

  $Q_\ell(x)$ 仍是无穷级数，在 $x = \mp 1$ 处有 **对数发散** 被排除

  </div>

---
### 轴对称问题的一般解
- **径向方向**的方程
  $$
  \begin{align*}
    & \ r^2 R''(r) + 2r R'(r) - \ell (\ell + 1) R(r) = 0 \\
  \Rightarrow & \ R(r) = r^\ell, \quad \text{or}, \quad  \frac{1}{r^{\ell + 1}}
  \end{align*}
  $$
  <div class='proof comment'>
  
  称为**欧拉方程**
  </div>


---
### 轴对称问题的一般解

- 一般解
  $$
  u(r, \theta, \varphi) = \sum_{\ell = 0}^{+\infty} \bigg(
    A_\ell r^\ell + \frac{B_\ell}{r^{\ell + 1}} 
    \bigg) P_\ell(\cos\theta)
  $$
- 与 $\varphi$ 无关：反映轴对称
* $A_\ell, B_\ell$ 需要**边界条件**确定：$u(r, \theta, \varphi)$ 应在求解区域内**连续有限**

---
### 轴对称问题的一般解

- 如果求解区域**包含原点 $r = 0$**：$r^{-(\ell + 1)}$ 项发散，需要 **<red>排除** (所有 $B_\ell = 0$)
* 如果求解区域**延伸到无穷远点 $r = \infty$**：$r^{\ell > 0}$ 项发散，需要 **<red>排除** (所有 $A_{\ell > 0} = 0$)
* 只有 $A_0$ 项在**全空间有限**
  <div class='proof comment'>

  Liouville 定理：有界调和函数只能是常数

  </div>

---
<!-- header: Legendre 多项式的性质  -->
# Legendre 多项式的性质

---
### Legendre 多项式

- Legendre 多项式 $P_\ell(x)$，$\ell \in \mathbb{N}$ 是一个 **$\ell$-次多项式**

  <div style="position:absolute; top:250px; right:0px">

  ![height:300px](images/image-2.png)
  </div>

  $$
  P_\ell(x) = \sum_{k = 0}^{\lfloor \ell/2 \rfloor} (-1)^k \frac{(2\ell - 2k)!}{2^\ell k!(\ell - k)! (\ell - 2k)!}x^{\ell - 2k}
  $$
  <div class='proof comment'>
  
  **最高最低幂次**

  $k = 0$ 对应最高幂次 $x^\ell$，$k = \lfloor \ell/2 \rfloor$ 对应最低幂次 $x^{0~ \text{or} ~ 1}$
  </div>

---
### Legendre 多项式的性质
- **奇偶性**
  $$
  P_\ell(-x) = (-1)^\ell P_\ell(x) 
  $$
  <div class='proof'>
  
  因为 $x^\ell$ 因子，$(-x)^{\ell - 2k} = (-1)^{\ell - 2k} x^{\ell - 2k} = (-1)^\ell x^{\ell - 2k}$
  </div>



---
### Legendre 多项式的性质


- **<red>$\ell$-次复多项式有多少个复根/零点 (重根按重数计算)**
- **<red>$P_\ell(x)$ 原则上有多少个复根？**
- **<red>这个根应该分布在哪里？** **<orange><reveal>原则上不知道</reveal>**

---
### Legendre 多项式的性质

<div style="position:absolute; top:400px; right:100px">

![width:300px](images/anya_legendre_zeros.png)

</div>

- $P_\ell(x)$ 在 $(-1, 1)$ 有 $\ell$ 个一阶零点
  <div class='proof comment'>

  作为一个 $n$ 次多项式，有 $n$ 个零点是显然的。
  
  此定理的关键是它们 **<red>没有** **重根**
  
  且**全部分布**在 $(-1, 1)$ 之间

  </div>

---

### Legendre 多项式的性质

<center>

<video width='800' src='media/media/videos/scene_legendre_zeros/2160p30/Scene01.mp4' controls></video>

</center>


---
### 微分表达式

<div style="right:100px;top:300px" class="float">

![height:290](images/image.png)

Olinde Rodrigues
</div>

- **Rodrigues 定理**：Legendre 多项式可以用如下**微分表达式**定义
  $$
  P_\ell(x) = \frac{1}{2^\ell \ell!} \frac{d^\ell}{dx^\ell}(\orange{x^2 - 1})^\ell
  $$

  $~$

  $~$



---
### 微分表达式

<div class="proof">

**证明微分表达式**

- 利用二项式定理
  $$
  (\orange{x^2 - 1})^\ell =\sum_{k = 0}^{\ell}  (-1)^k C_\ell^k x^{2\ell - 2k}
  $$
- 对上式求 $\ell$ 次导数，
  $$
  \purple{\frac{d^\ell}{dx^\ell}}(x^2 - 1)^\ell = \sum_{k = 0}^{\ell} (-1)^k C_\ell^k \purple{\frac{d^\ell}{dx^\ell}}x^{2\ell - 2k}
  $$
</div>


---
### 微分表达式

<div class='proof'>


**证明微分表达式**
- 利用求导公式
  $$
    \frac{d^\ell}{dx^\ell} x^\red{n} = \left\{
      \begin{array}{cc}
        n(n-1) ... (n - \ell + 1)x^{n-\ell} = \frac{\green{n}!}{(\purple{n - \ell})!} x^{\purple{n - \ell}}, &  \ell \le n\\
        0, &  \ell > n
      \end{array}
    \right.
  $$
- 得到
  $$
  \frac{d^\ell}{dx^\ell} x^{2\ell - 2k}
  = \left\{
    \begin{array}{cc}
      \frac{(\green{2\ell - 2k})!}{(\purple{2\ell - 2k - \ell})!} x^{2\ell - 2k - \ell}, & \ell \le 2\ell - 2k\\
      0, & \ell > 2\ell - 2k
    \end{array}\right.
  $$

</div>


---
### 微分表达式

<div class='proof'>

**证明微分表达式**

- 得到
  $$
  \frac{d^\ell}{dx^\ell}(x^2 - 1)
  = \sum_{k = 0}^{\ell} (-1)^k C_\ell^k \frac{d^\ell}{dx^\ell}x^{\green{2\ell - 2k}}
  = \sum_{k = 0}^{\red{\boldsymbol{\lfloor \ell/2 \rfloor}}}
  (-1)^k C_\ell^k \frac{(\green{2\ell - 2k})!}{(\purple{2\ell - 2k - \ell})!}
  x^{\purple{2\ell - 2k - \ell}}
  $$
- 其中非零项来自
  $$
  \ell \le 2\ell - 2k \quad \Rightarrow \quad k \le \frac{\ell}{2} \quad \Rightarrow \quad k = 0, 1, \dots, \red{\boldsymbol{\lfloor \ell/2 \rfloor}}
  $$

</div>

---
### 微分表达式

<div class='proof'>

**证明微分表达式**

- 代入组合数 $\orange{C_\ell^k}$ 定义，
  $$
  \frac{d^\ell}{dx^\ell}(x^2 - 1)^\ell
  = \sum_{k = 0}^{\lfloor \ell/2 \rfloor} 
  (-1)^k \orange{\frac{\ell!}{k! (\ell - k)!}}
  \frac{(2\ell - 2k)!}{(\green{2\ell - 2k - \ell})!}x^{2\ell - 2k - \ell}
  $$
* **重新归一化**，
  $$
  \red{\frac{1}{2^\ell \ell!}} \frac{d^\ell}{dx^\ell}(x^2 - 1)^\ell
  = \sum_{k = 0}^{\lfloor \ell/2 \rfloor} 
  (-1)^k \frac{(2\ell - 2k)!}{\red{2^\ell} k! (\ell - k)! (\green{\ell - 2k})!}x^{\ell - 2k}
  = P_\ell(x)
  $$
</div>




---
### Legendre 多项式的性质
- 原点值 (结合奇偶性)
  $$
  P_{\ell ~ \text{odd}}(0) = 0, \qquad
  P_{\ell ~ \text{even}}(0) = (-1)^{\ell/2} \frac{\ell!}{2^\ell [(\ell/2)!]^2}
  $$
  <div class='proof'>

  * 当 $\ell$ 是奇数，$P_\ell(x)$ 是**奇函数**：原点值只能为零
  
  * 当 $\ell$ 是偶数，$P_\ell(0)$ 等于**最低**幂次项，即级数表达式中 $k = \ell/2$ 项系数，
    $$
      \frac{(-1)^k (2\ell - 2k)!}{2^\ell \purple{k!} \orange{(\ell - k)!} \red{(\ell - 2k)!}}=
      \frac{(-1)^{\ell/2}(2\ell - \ell)!}{2^\ell \purple{(\ell/2)!}\orange{(\ell - \ell/2)!}\red{0!}}
      = (-1)^{\ell/2} \frac{\ell!}{2^\ell [ \ (\ell/2)! \ ]^2}
    $$
  </div>


---
### Legendre 多项式的性质

- 原点值 (结合奇偶性)
  $$
  P_{\ell ~ \text{even}}(0) = (-1)^{\ell/2} \frac{\ell!}{2^\ell [(\ell/2)!]^2}
  $$
  $$
  \Rightarrow P_{\ell = 2n}(0) = (-1)^n \frac{(2n)!}{2^{2n} (n!)^2}
  $$



---
### 微分表达式

- **定理**：$P_\ell(1) = 1$，$P_{\ell}(-1) = (-1)^\ell$

  <div class="proof">

  **求解 $P_\ell(1)$**

  根据微分表达式，
  $$
  P_\ell(1) = \frac{1}{2^\ell \ell!} \frac{d^\ell}{dx^\ell} \bigg|_{x = 1}(\orange{x^2 - 1})^\ell
  $$

  </div class="proof">

---
### 微分表达式

<div class='proof'>

**求解 $P_\ell(1)$**
- 利用平方差公式 $x^2 - 1 = \purple{(x - 1)}\orange{(x + 1)}$，以及**莱布尼兹公式**
    $$
    \frac{d^\ell}{dx^\ell}[x^2 - 1]^\ell
    = \sum_{k = 0}^{\ell} C_{\ell}^k \left[{\frac{d^k}{dx^k}\purple{(x - 1)}^\ell}\right]
    \left[{\frac{d^{\ell - k}}{dx^{\ell - k}}\orange{(x + 1)}^\ell}\right]
    $$
  * 当 $k < \ell$，对 $(x - 1)^\ell$ 求 $k$-阶导数会 **<red>残留** $\purple{(x - 1)}$，最后令 $x = 1$ 时就等于 **<red>零**
</div>

---
### 微分表达式

<div class='proof'>

**求解 $P_\ell(1)$**
- 非零项只有 $k = \ell$ 项
  $$
  P_\ell(1) = \frac{1}{\red{2^\ell}
  \orange{\ell!}}
  C_\ell^\ell
  \times \orange{\left[{\frac{d^\ell}{dx^\ell}(x - 1)^\ell}\right]}
  \times \red{(x + 1)^\ell} \bigg|_{x = 1}
  $$
- 利用 $\orange{\frac{d^\ell}{dx^\ell}(x - 1)^\ell} = \frac{d^\ell}{dx^\ell}(x^\ell + \cdots) = \ell!$
  $$
  P_\ell(1)
  = \frac{1}{\red{2^\ell}  \orange{\ell!}} 
  \times \orange{\ell!}
  \times\red{(1 + 1)^\ell} = 1
  $$
* $P(-1)$ 的值根据**奇偶性**是显然的
</div>


---
### Legendre 多项式的正交性

- Legendre 方程是 **Sturm-Liouville 问题**的特例：本征函数带权**正交**
  <div class='proof comment'>

  对于 Legendre 方程，权函数 $\rho(x) = 1$

  </div>
- **<green>内积 $(f,g)$** 定义为
  $$
  \green{(f, g) \coloneqq \int_{-1}^{+1}f(x)g(x) dx}
  $$


---
### Legendre 多项式的正交性
- **定理**：Legendre 多项式关于上述内积是**正交**的，
  $$
  (P_\ell, P_{\ell'}) = 0, \qquad \ell \ne \ell'
  $$
<div class="proof">

**证明正交性**

- 利用**分部积分**，**<red>设 $k < \ell$**
  $$
  \begin{align*}
  & \ \int x^k \orange{\frac{d^\ell}{dx^\ell}\Big[{(x^2 - 1)^\ell}\Big]} dx \qquad \orange{(\text{橙色部分是} P_\ell ~ \text{的主要成分})}\\
  = & \ \bcancel{x^k \frac{d^{\ell - 1}}{dx^{\ell - 1}}(x^2 - 1)^\ell\bigg|_{-1}^1 } 
  \red{- k} \int x^{k - 1}\frac{d^{\ell - 1}}{dx^{\ell - 1}}(x^2 - 1)^\ell dx
  \end{align*}
  $$
</div>



---

### Legendre 多项式的正交性


<div class="proof">



  * 分部积分可以同时把 $k, \ell$ 下降 $1$
  * 乘以 $\purple{(2^\ell\ell!)^{-1}}$，反复利用 $k$-次 **分部积分** **<red>($k < \ell$)**
    $$
    \int_{-1}^{+1} x^k P_\ell(x) = \frac{(-1)^kk!}{\purple{2^\ell \ell!}}
    \int_{-1}^1 x^\red{0} \frac{d^{\ell \red{- k}}}{d^{\ell - k}}(x^2 - 1)^\ell dx = 0
    $$
    最后等号利用被积函数是个**全导数** ($\ell > k$)，积分为**零**
   * 对于 $(P_{\ell}, P_{\ell'})$，**不妨设 $\ell' < \ell$**，则由于 $P_{\ell'}$ 是一组 **单项式 $x^{k < \ell}$** 的和，因此 $(P_\ell, P_{\ell'}) = 0$
</div>

---
### Legendre 多项式的模

- **<green>定义**：Legendre 多项式的 **<green>模 (norm)** 为 $\left\Vert P_\ell \right\Vert \coloneqq (P_\ell, P_\ell)^{1/2}$
- **定理**：[:bulb:proof](./animations/NormOfLegendre.html)
  $$
  \lVert P_\ell \rVert^2 = \frac{2}{2\ell + 1}, \qquad
  \lVert P_\ell \rVert = \sqrt{\frac{2}{2\ell + 1}}
  $$
---
### Legendre 多项式的模


<div class="proof">

**证明**
  
- 利用微分表达式，利用分部积分建立递推 (假设 $\ell > 0$)
- $\ell = 0$ 可以直接算出来

* 对于 $\ell \ge 1$
  $$
  \begin{align*}
    \lVert P_\ell \rVert^2
  = & \ \frac{1}{2^\ell \ell!} \int_{-1}^{+1} P_\ell(x) \red{\frac{d^\ell}{dx^\ell}} \orange{(x^2 - 1)^\ell} dx\\
  = & \ \frac{1}{2^\ell \ell!} \int_{-1}^{+1} P_\ell(x) \red{\frac{d}{dx} \frac{d^{(\ell - 1)}}{dx^{(\ell - 1)}}} \orange{(x^2 - 1)^\ell} dx
  \end{align*}
  $$


---
### Legendre 多项式的模


<div class="proof">

**证明**
- 分部积分，得到
  $$
  \lVert P_\ell \rVert^2 = \green{\text{边界}} + \frac{1}{2^\ell \ell!} \int_{-1}^{+1} P_\ell^{(1)}(x) \frac{d^{(\ell - 1)}}{dx^{(\ell - 1)}} (x^2 - 1)^\ell dx 
  $$
- 其中 **<green>边界项**
  $$
  \green{边界 = } ~ P_\ell(x)\left[{\frac{d^{(\ell - 1)}}{dx^{(\ell - 1)}}(x^2 - 1)^\ell}\right] \Bigg|_{-1}^{+1} \red{= 0}
  $$


</div>    

---
### Legendre 多项式的模


<div class='proof'>

**证明**
- 得到
  $$
  \lVert P_\ell \rVert^2 = \frac{1}{2^\ell \ell!} \int_{-1}^{+1} P_\ell^{(1)}(x) \frac{d^{(\ell - 1)}}{dx^{(\ell - 1)}} (x^2 - 1)^\ell dx 
  $$
  把 $\ell$-阶导数 **<red>降阶** 一次，转移到了 $P_\ell(x)$ 身上

- 不断重复上述分部积分操作，把 $\ell$-阶求导**全部**转移到 $P_\ell$ 身上
  $$
    \lVert P_\ell \rVert^2 = \frac{1}{2^\ell \ell!} \int_{-1}^{+1} \purple{P_\ell^{(\ell)}(x)} (1 - x^2)^\ell dx
  $$
</div>

---
### Legendre 多项式的模



<div class="proof">

**证明**

- 其中 $\purple{P_\ell^{(\ell)}(x)}$ 是**常数**
  $$
  \purple{P_\ell^{(\ell)}(x)} = \frac{d^\ell}{dx^\ell}P_\ell(x) = \frac{1}{2^\ell \ell!} \frac{d^\ell}{dx^\ell} \frac{d^\ell}{dx^\ell}(x^2 - 1)^\ell
  = \frac{1}{\purple{2^\ell \ell!}} \orange{\frac{d^{2\ell}}{dx^{2\ell}}x^{2\ell}}
  = \frac{\orange{(2\ell)!}}{\purple{2^\ell \ell!}}
  $$
- 另外
  $$
  \int_{-1}^{+1} (1 - x^2)^\ell dx = \frac{2^{2\ell + 1}(\ell!)^2}{(2\ell + 1)!}
  $$
  这个结果可以通过数学归纳法得到

</div>

---
### Legendre 多项式的模

<div class='proof'>

**证明**

- 收集所有因子，
  $$
  \lVert P_\ell \rVert^2
  = \underbrace{\frac{1}{\orange{2^\ell} \red{\ell!}}}_\text{原生} \times \underbrace{\frac{(2\ell)!}{\orange{2^\ell} \red{\ell!}}}_{P_\ell^{(\ell)}(x)} \times \frac{2^{\orange{2\ell} + 1}\red{(\ell!)^2}}{(2\ell + 1)!}= \frac{2}{2\ell + 1}
  $$


</div>

</div class="proof">    

---

### Legendre 多项式的内积

统一内积表达式
$$
(P_\ell, P_{\ell'}) = \frac{2}{2\ell + 1}\delta_{\ell, \ell'}
$$

---
### 广义傅里叶级数

- Legendre 多项式及其所满足的方程式 **Sturm-Liouville 本征问题**的特例
- $P_\ell$ 在 $[-1, 1]$ 上形成**完备基底**
* 任意 $[-1, 1]$ 上的「性质良好」函数可以用 $P_\ell$ 展开
  $$
  f(x) = \sum_{\ell = 0}^{+\infty} f_\ell P_\ell(x) 
  $$
  其中展开系数为
  $$
  f_\ell = \frac{2\ell + 1}{2} \int_{-1}^{+1}f(x)P_\ell(x)dx
  $$
---
### 广义傅里叶级数

<div class='proof'>

**展开系数**

- 由展开
  $$
  f(x) = \sum_{{\ell'} = 0}^{+\infty} f_{\ell'} P_{\ell'}(x)
  $$
- 两边同乘 $P_\ell(x)$, 并在 $[-1, 1]$ 上积分
  $$
  \int_{-1}^{+1} f(x)P_\ell(x)dx = \int_{-1}^{+1} \sum_{{\ell'} = 0}^{+\infty} f_{\ell'} P_{\ell'}(x)P_\ell(x)dx
  $$
</div>

---
### 广义傅里叶级数

<div class='proof'>

**展开系数**
- 交换积分与求和顺序
  $$
  \begin{align*}
    \int_{-1}^{+1} f(x)P_\ell(x)dx = & \ \sum_{{\ell'} = 0}^{+\infty} f_{\ell'} \orange{\int_{-1}^{+1} P_{\ell'}(x)P_\ell(x)dx} \\
    = & \ \sum_{{\ell'} = 0}^{+\infty} f_{\ell'} \orange{\frac{2}{2\ell' + 1}\delta_{\ell, \ell'}} = \frac{2}{2\ell + 1} f_\ell
  \end{align*}
  $$
  

</div>

---

### 广义傅里叶级数

- 例子：$x^n$ 用 $P_\ell$ 展开
  $$
  x^0 = P_0(x), \qquad x^1 = P_1(x)
  $$
  $$
  x^2 = \frac{2}{3}P_2(x) + \frac{1}{3}P_0(x)
  $$
  $$
  x^3 = \frac{2}{5}P_3(x) + \frac{3}{5}P_1(x)
  $$
  $$
  x^4 = \frac{8}{35}P_3(x) + \frac{4}{7} P_2(x) + \frac{1}{5}P_0(x)
  $$

---

### 母函数/生成函数

<div style='position:absolute;right:50px;top:50px'>

![width:320px](images/anya_generating_function.png)
</div>

- 无穷多个 $P_\ell$，**打包**成一个方便携带、书写的对象
  $$
  U(r, x) \coloneqq \sum_{\ell = 0}^{+\infty}  r^\ell P_\ell(x), \quad r < 1
  $$
- **<green>约定**：上述形态的函数成为 $P_\ell(x)$ 的 **<green>生成函数 (generating function)**、**<green>母函数**
  <div class='proof comment'>

  $U(r, x)$ 是 $r$ 的 **幂级数**

  </div>

---
### 母函数/生成函数
- 从生成函数出发，可以获得 $P_\ell(x)$
  $$
  \frac{1}{\ell!}\frac{d^\ell U(r, x)}{dr^\ell} \bigg|_{r = 0} = P_\ell(x), \qquad
  \oint_0 \frac{dz}{2\pi i \red{z}} z^{-\ell} U(z, x) = P_\ell(x)
  $$

---
### 母函数/生成函数

<div class='proof comment'>

- 对于任意的数学对象组成的序列 $a_n$，可以定义其 **<green>生成函数** 为**形式上**的双边幂级数
  $$
   f(z) \coloneqq \sum_{n}a_n z^n 
  $$
- 显然
  $$
   a_n = \oint \frac{dz}{2\pi i z} z^{-n} f(z)
  $$
* 在一些特殊的领域中，生成函数有时也称为 **<green>配分函数 (partition function)**、**<green>指标 (index)**、**<green>椭圆亏格 (elliptic genus)**

</div>



---
### 母函数/生成函数
- **<red>生成函数 $U(r, x)$ 到底等于什么？**
  <div class='proof comment'>
  
  如果不能知道 $U(r,x)$ 的“简化表达式”，那么它就没什么用处了
  </div>
- 策略
  <center>
  
  $U(r,x)$ 是 Laplace 方程的解 $\to$ $U(r, x)$ 是某种静电势分布

  $\to$ 找到对应的静电系统 $\to$ 得到简化的静电势表达式
  </center>


---
### 母函数/生成函数



- 对比**球体内部 ($r < 1$)** Laplace 方程的 **<green>轴对称一般解**
  $$
    U(r, x) \coloneqq \sum_{\ell = 0}^{+\infty}  r^\ell P_\ell(x)
    \leftrightarrow
    \green{u(r, x = \cos \theta)} = \sum_{\ell = 0}^{+\infty} A_\ell r^\ell  P_\ell(x)
  $$
  <div class='proof comment'>

  球体内部解要求球心处解满足自然边界条件，因此 $B_\ell = 0$

  </div>

- $U(r, x)$ 对应 $A_\ell = 1$
* $U(r, x)$ 其实是 Laplace 方程的自然边界条件下某个**轴对称**解





---
### 母函数/生成函数
- Laplace 方程的物理意义：静电场的 **<red>无源** 区域解
- **<red>$U(r,x)$ 对应什么静电系统?**


---
### 母函数/生成函数

- 考虑 $(0,0,1)$ 处**单位点电荷**在单位球体 $(x, y, z)$ 处形成的静电势 (轴对称)
  $$
  u_0(r, x = \cos\theta) = \frac{1}{\sqrt{1 - 2r \cos \theta + r^2}}
  $$
  <div class='proof comment'>

  - $u_0(r = 0, \theta)$ 有限，且在无穷远处为**势能零点**，$u_0(r \to +\infty, \theta) = 0$
  
  * 根号中的表达式是 $(0,0,1)$ 与 $(x, y, z)$ 的距离
    $$
    \sqrt{x^2 + y^2 + (z - 1)^2} = \sqrt{r^2 \sin^2 \theta + (r \cos \theta - 1)^2} = \sqrt{r^2 - 2r \cos \theta + 1}
    $$

  </div>



---
### 母函数/生成函数


<center>

![width:720](media/images/figures/PointChargeAtNorthPole_ManimCE_v0.18.1.png)

单位点电荷在北极

</center>



---
### 母函数/生成函数

- 作为 Laplace 方程解，该电势分布必然可以写成广义傅里叶级数，
  $$
  u_0(r, x) = \sum_{\ell = 0}^{+\infty} \red{A_\ell} r^\ell P_\ell(x)
  $$
- **<red>系数 $A_\ell =?$**
  <div class='proof comment'>
  
  可以硬算，也可以投机取巧：检查特殊值
  </div>

---
### 母函数/生成函数
- $u_0(r, \purple{x = \cos\theta = 1})$：分母**完全平方** $1 - 2rx + r^2 = 1 - 2r + r^2 = \orange{(1 - r)^2}$
  $$
  u_0(r, \purple{x = 1})
  = \frac{1}{\orange{\sqrt{1 - 2rx + r^2}}} = \frac{1}{\orange{1 - r}} = \sum_{\ell = 0}^{+\infty} r^\ell \purple{\times 1}
  = \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(\purple{x = 1})
  $$

---
### 母函数/生成函数
- 与轴对称 Laplace 方程在球坐标系下**球体内**的**一般解**比较
  $$
  \begin{align*}
    u_0(r, x = 1) = & \ u(r, x = 1)\\
  \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x = 1) = & \ \sum_{\ell = 0}^{+\infty} \red{A_\ell} r^\ell P_\ell(x = 1)
  \end{align*}
  $$
  $$
  \Rightarrow \quad \red{A_\ell} = 1
  $$
  <div class='proof comment'>
  
  * **<red>为什么一定要 $A_\ell = 1$？**
    <answer>左右两边同为 $r$ 的幂级数，对应系数应该相等</answer>
  </div>


---
### 母函数/生成函数


- 于是对任意 $x\in [-1,1]$
  $$
  u_0(r, x) = \frac{1}{\sqrt{1 - 2rx + r^2}} = \underbrace{\sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x)}_{u(r,x)|_{A_\ell = 1}}
  = U(r, x)
  $$



---
### 母函数/生成函数
- 当 $r > 1$，生成泛函也可以展开
  $$
  \frac{1}{\sqrt{1 - 2r x + r^2}} = \sum_{\ell = 0}^{+\infty} \frac{1}{r^{\ell + 1}} P_\ell(x)
  $$
  <div class='proof comment'>
  
  做个变量替换即可，$\tilde r = 1/r$
  </div>

---
### 母函数/生成函数
<div class='proof'>

**证明**

- 定义 $\tilde r = \frac{1}{r}$，则 $\tilde r < 1$，
  $$
  \frac{1}{\sqrt{1 - 2r x + r^2}} = \frac{\tilde r}{\sqrt{1 - 2\tilde r x + \tilde r^2}}
  $$
* 展开为 $\tilde r$ 的幂级数,
  $$
  \frac{\red{\tilde r}}{\sqrt{1 - 2\tilde r x + \tilde r^2}} = \red{\tilde r}\sum_{\ell = 0}^{+\infty} \tilde r^{\ell} P_\ell(x)
  = \sum_{\ell = 0}^{+\infty} \frac{1}{r^{\ell + 1}} P_\ell(x)
  $$
</div>


---
### 母函数/生成函数的推论

- 利用母函数可以获得 Legendre 函数的许多性质
  不同的 $P_\ell$ 及导数 $P'_\ell$ 之间满足许多有趣的关系


---
### $P_\ell$ 的和
- 取 $\orange{r = \pm1}$，$1 - 2r x + r^2 = 2 \mp 2x = 2(1 \mp x)$
  $$
  \frac{1}{\sqrt{2(1 - x)}} = \sum_{\ell = 0}^{+\infty} P_\ell(x) , \quad
  \frac{1}{\sqrt{2(1 + x)}} = \sum_{\ell = 0}^{+\infty} (-1)^\ell P_\ell(x) 
  $$
  <div class='proof comment'>
  
  这是**所有** $P_\ell$ 共同满足的关系
  </div>

---

### 递推关系

- 利用母函数，可以导出 Legendre 多项式的**递推关系 (recurrence relation)**
  <div class='proof comment'>
  
  若干 (不是全部) $P_\ell$ 及其导数之间的关系
  </div>
- 第一递推关系：来自对 $r$ 求导
- 第二递推关系：来自对 $x$ 求导
- 第三递推关系：来自对 $r, x$ 混合求导



---
### 递推关系 ($r$ 导数)
- 母函数关系两边对 $r$ 求导
  $$
  \frac{d}{dr}U(r,x) = \frac{x - r}{(1 - 2rx + r^2)^{\frac{3}{2}}}
  =  \frac{(x - r)}{(1 - 2rx + r^2)}U(r,x)
  $$
- 两边同乘 $(1 - 2rx + r^2)$，
  $$
  (1 - 2rx + r^2) \orange{\frac{d}{dr}U(r,x)} = (x - r) \purple{U(r,x)}
  $$
- 两边的 $U(r, x)$ 用 $P_\ell(x)$ 展开，
  $$
  (1 - 2rx + r^2) \orange{\sum_{\ell = 0}^{+\infty}\ell r^{\ell - 1} P_{\ell}(x)}  
  = (x - r) \purple{\sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x)}
  $$

---

### 递推关系 ($r$ 导数)

- 左边
  $$
  \begin{align*}
    & \ (1 - 2rx + r^2)\sum_{\ell = 0}^{+\infty}\ell r^{\ell - 1} P_\ell(x)\\
    = & \ \sum_{\ell = 0}^{+\infty} \ell r^{\ell - 1} P_\ell(x)
    - 2x \sum_{\ell = 0}^{+\infty} \ell r^{\ell} P_\ell(x) + \sum_{\ell = 0}^{+\infty} \ell r^{\ell + 1} P_\ell(x)  \\
    = & \ \sum_{\ell = -1}^{+\infty} (\ell + 1) r^\ell P_{\ell + 1}(x)
    - 2x \sum_{\ell = 0}^{+\infty} \ell r^{\ell} P_{\ell}(x) + \sum_{\ell = 1}^{+\infty} (\ell - 1) r^{\ell} P_{\ell - 1}(x)
  \end{align*}
  $$
---
### 递推关系 ($r$ 导数)
- 右边
  $$
  \begin{align*}
    & \ (x - r) \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x)\\
    = & \ x \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x) - \sum_{\ell = 0}^{+\infty} r^{\ell + 1} P_\ell(x)
    = \sum_{\ell = 0}^{+\infty} r^\ell \purple{x P_\ell(x)} - \sum_{\red{\boldsymbol{\ell = 1}}}^{+\infty} r^{\ell} \orange{P_{\ell - 1}(x)}
  \end{align*}
  $$

---
### 递推关系 ($r$ 导数)
- 对比 $r^\ell$ 的系数，得到 **<green>第一递推关系**
  $$
  \begin{align*}
    (\ell + 1)P_{\ell + 1}(x) - 2x \ell P_\ell(x) + (\ell - 1) P_{\ell - 1}(x) = & \ \purple{x  P_\ell(x)} - \orange{P_{\ell - 1}(x)} \\
    \Rightarrow \qquad\qquad (2\ell + 1) \ x P_\ell(x) = & \ (\ell + 1)P_{\ell + 1}(x) + \ell P_{\ell - 1}(x)
  \end{align*}
  $$
  <div class='proof comment'>

  可以约定 $P_{-1}(x) = 0$

  </div>

---
### 递推关系 ($x$ 导数)
- 母函数关系两边对 $x$ 求导
  $$
  (1 - 2rx + r^2) \frac{d}{dx}U(r,x) = r U(r,x)
  $$
- 两边代入 $U(r, x)$ 展开，
  $$
  (1 - 2rx + r^2)\sum_{\ell = 0}^{+\infty} r^\ell P'_\ell(x) = r \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x)
  $$


---
### 递推关系 ($x$ 导数)
- 化简
  $$
  \begin{align*}
    (1 - 2rx + r^2)\sum_{\ell = 0}^{+\infty} r^\ell P'_\ell(x)
  = & \ r \sum_{\ell = 0}^{+\infty} r^\ell P_\ell(x)\\
  \sum_{\ell = 0}^{+\infty}\purple{r^{\ell + 1}}[ P'_{\ell + 1}(x) - 2xP'_\ell(x) + P'_{\ell - 1}(x)] = & \ 
  \sum_{\ell = 0}^{+\infty} \purple{r^{\ell + 1}} P_\ell(x)
  \end{align*}
  $$
- 对比 $r^{\ell+1}$ 的系数，得到 **<green>第二递推关系**
  $$
  P'_{\ell + 1}(x) - 2x P'_\ell(x) + P'_{\ell - 1}(x) = P_\ell(x)
  $$


---
### 递推关系

- 对第一递推关系**求 $x$ 导数**，
  $$
  \begin{align*}
    & \ (2\ell + 1) \ x P_\ell(x) = (\ell + 1)P_{\ell + 1}(x) + \ell P_{\ell - 1}(x)\\
    \\
    \gray{(\frac{d}{dx})}\Rightarrow & \ (2\ell + 1) P_\ell(x) + (2\ell + 1) x P'_\ell(x) = (\ell + 1)P'_{\ell + 1}(x) + \ell P'_{\ell - 1}(x)\\

    \\
    \gray{(\times 2)}\Rightarrow & \ 2(2\ell + 1) P_\ell(x) =
    2(\ell + 1)P'_{\ell + 1}(x) + 2\ell P'_{\ell - 1}(x) - \red{2(2\ell + 1) x P'_\ell(x)}
  \end{align*}
  $$
- 第二递推关系乘以 $(2\ell + 1)$
  $$
  (2\ell + 1)P_\ell(x) = (2\ell + 1)P'_{\ell + 1}(x) - \red{2(2\ell + 1)x P'_\ell(x) }+ (2\ell + 1)P'_{\ell - 1}(x)
  $$


---
### 递推关系

- 两式作差，抵消 $P'_\ell(x)$ 项，
  $$
  (2\ell + 1) P_\ell(x) = [2(\ell + 1) - (2\ell + 1)]P'_{\ell + 1}(x)
  + [2\ell - (2\ell + 1)]P'_{\ell - 1}(x)
  $$
- 化简，得到第三递推关系
  $$
  (2\ell + 1)P_\ell(x) = P'_{\ell + 1}(x) - P'_{\ell - 1}(x)
  $$


---

### 递推关系

- 第一递推关系：对 $r$ 求导
  
- 第二递推关系：对 $x$ 求导
- 第三递推关系：对 $r, x$ 混合求导，结合第一递推


---
### 递推关系

<center>

<iframe src='RecursionRelation_interactive.html' frameborder='0' style='width:1024px;height:480px'></iframe>

</center>




---
<!-- header: Legendre 多项式的物理应用 -->
# Legendre 多项式的物理应用

---

### 电势、电场与偏微分方程

- 空间电势分布为 $u(\mathbf{r}) = u(x, y, z)$
- 电场与电势的关系
  $$
  \mathbf{E} = - \nabla u
  $$

---
### 电势、电场与偏微分方程
- 电场与电荷密度的关系
  $$
  \begin{align*}
    \oint_{\partial V} \mathbf{E} \cdot d\mathbf{S} = & \ \frac{\orange{Q}}{\epsilon_0}\\
   \gray{(高斯定理)}\Rightarrow \int_V \nabla \cdot \mathbf{E} dV = & \ \orange{\int_V} \frac{\orange{\rho}}{\epsilon_0} \orange{dV}
  \end{align*}
  $$
  上式对**任意小**体积成立，因此必然有
  $$
  \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
  $$

---
### 电势、电场与偏微分方程

- 电势与电荷关系：**<green>泊松方程**
  $$
  \purple{\nabla^2 u} = \nabla \cdot \nabla u = - \nabla \cdot \mathbf{E} = \purple{- \frac{\rho}{\epsilon_0}}
  $$
- 在没有电荷密度的位置：$u$ 满足 **<green>Laplace 方程**,
  $$
  \nabla^2 u = 0 
  $$

---
### 电势边界问题

<center>

![width:840](media/images/figures/ChargedSphere_ManimCE_v0.18.1.png)
</center>



---
### 电势边界问题

- 问题：考虑半径 $a$ 的薄球壳，球体内外均没有电荷分布，**球体表面 $r = a$ 上的电势已知 (与 $\varphi$ 无关)**
  $$
  u(a, \theta, \varphi) = f(\theta), \qquad u(r\to +\infty, \theta, \varphi) = 0
  $$
  **<red>求「体内与球外」电势分布**
  <div class='proof comment'>

  即原点与无穷远点均属于求解区域

  </div>

---
### 电势边界问题
- 球内，球外没有电荷分布：球内球外 Laplace 方程
  $$
  \nabla^2 u = 0 
  $$
  <div class='proof comment'>

  **<red>能否直接说明 $u$ 是常数？** <answer> 球面 $r = a$ 有电荷分布，破坏 Laplace 方程</answer>

  </div>

---
### 电势边界问题

<center>

![width:840](media/images/figures/ChargedSphere_ManimCE_v0.18.1.png)
</center>



---
### 电势边界问题

- 由于表面电势与 $\varphi$ **<red>无关**：轴对称问题
- 球坐标系下轴对称拉普拉斯方程解的一般形式为
  $$
  u(r, \theta, \varphi) = \sum_{\ell = 0}^{+\infty} (A_\ell r^\ell + \frac{B_\ell}{r^{\ell + 1}}) P_\ell(\cos \theta)
  $$

---
### 电势边界问题
- 调整 $A_\ell, B_\ell$，**重新归一化**，
  $$
  u(r, \theta, \varphi) = \sum_{\ell = 0}^{+\infty} \left({A_\ell \left({\frac{r}{a}}\right)^\ell + B_\ell \left({\frac{a}{r}}\right)^{\ell + 1}}\right) P_\ell(\cos \theta)
  $$
  <div class='proof comment'>

  球内、球外上式都适用
  
  球内外的 $A, B$ 系数**独立求解**，但应在 $r = a$ 处使得**解连续**，都等于 $f(\theta)$

  </div>

---
### 电势边界问题：球内电势分布

- 考虑**球内电势**。球心无电荷，球心电势**有限**，$B_\ell = 0$
- 在**球面上**的电势已知，$u(a, \theta) = f(\theta)$
  $$
  u(a, \theta) = \sum_{\ell = 0}^{+\infty} A_\ell \frac{a^\ell}{a^\ell} P_\ell(\cos\theta)  = \sum_{\ell = 0}^{+\infty} A_\ell P_\ell(\cos \theta) = \green{f(\theta) \coloneqq g(x = \cos \theta)}
  $$



---
### 电势边界问题：球内电势分布

- 得到
  $$
  A_\ell = \frac{2\ell + 1}{2} \int_{-1}^{+1} g(x) P_\ell(x) dx
  = \frac{2\ell + 1}{2} \int_{0}^{\pi} f(\theta) P_\ell(\cos \theta) \sin \theta d\theta
  $$
  <div class='proof comment'>

  注意 **<red>积分上下限**，$\theta = 0, \pi \rightarrow \cos \theta = 1, -1$, $d\cos \theta = \red{\boldsymbol{-}}\sin \theta d\theta$，
  $$
  \begin{align*}
  & \ \int_{-1}^{+1} g(x) P_\ell(x) dx = \int_{\pi}^{0} f(\theta) P_\ell(\cos \theta) d\cos\theta \\
  = & \ \int_{\pi}^{0} f(\theta) P_\ell(\cos \theta) (-\sin\theta) d\theta
  = \int_{0}^{\pi} f(\theta) P_\ell(\cos \theta) \sin \theta d\theta
  \end{align*}
  $$

  </div>

---
### 电势边界问题：球外电势分布

- 考虑**球外电势**。无穷远处电势为**零**，$A_{\ell > 0} = 0$，$A_0 = 0$
- 在**球面上**的电势已知，
  $$
  u(r = a, \theta) = \sum_{\ell = 0}^{+\infty} B_\ell P_\ell(\cos \theta) = f(\theta) = g(x = \cos \theta)
  $$
* 同样有
  $$
  B_\ell = \frac{2\ell + 1}{2} \int_{-1}^{+1} g(x) P_\ell(x)
  = \frac{2\ell + 1}{2} \int_{0}^{\pi} f(\theta) P_\ell(\cos \theta) \sin \theta d\theta
  $$


---
### 均匀电场中的带点导体球

- 问题：均匀电场 $\mathbf{E}_0 = E_0 \mathbf{e}_z$ 中放入半径为 $a$、带电量为 $Q$ 的金属导体球，求**球体外**的电势分布与电场分布。
  $$
  \begin{align*}
    & \ \nabla^2 u = 0, \qquad r > a \\
    & \ u(r = a, \theta) = \text{const}\\
    & \ - \oint_{r = a+} \frac{\partial u}{\partial r} dS = \frac{Q}{\epsilon_0}, \\
    & \ u(r \to +\infty, \theta, \varphi) = - E_0 r \cos \theta
  \end{align*}
  $$ 
  <div class='proof comment'>

  方程、边界条件均与 $\varphi$ 无关：**轴对称**问题

  </div>

---
### 均匀电场中的带点导体球

<div class='proof comment'>

- 球**外**没有电荷分布: $\nabla^2u=0$，$r > a$
* 静电平衡：金属导体球内部没有电场，球体等势、球表面**等势**
  $$
   u(r = a, \theta) = \green{\text{const} \coloneqq u_0}
  $$

* 高斯定理：球体外闭合曲面积分得到**总电荷**
  $$
   - \int_{r = a+} \frac{\partial u}{d r} dS = \frac{Q}{\epsilon_0}
  $$


</div>



---
### 均匀电场中的带点导体球

<div class='proof comment'>


- 无穷远的均匀电场产生电势
  $$
   u(r \to +\infty, \theta, \varphi) = - E_0 r \cos \theta, \qquad r \gg a
  $$

</div>

- **<red>为什么无穷远处的电势选为 $-E_0 r \cos\theta$?**
- 加球之前道理很简单

---
### 均匀电场中的带点导体球

<center>

![width:840](media/images/figures/ConstantElectricField_ManimCE_v0.18.1.png)

加球前的电势分布，电势零点 **<red>选** 为 $xy$ 面的无穷远处
</center>

---
### 均匀电场中的带点导体球

- **<red>为什么加了导体球之后，无穷远处的电势依然选为 $-E_0 r \cos\theta$?**
  <div class='proof comment'>

  * 添加了导体球后，电势分布重塑
  * 两个思路：**电场**角度，**电势**角度
  * 首先是**电场角度**
  * 导体球在远处产生的电场很**弱**：无穷远处电场 **$\mathbf{E}(r \to +\infty) \simeq \mathbf{E}_0$**
  * 不管有没有导体球：$\mathbf{E} = - \nabla u$


  </div>

---
### 均匀电场中的带点导体球

<div class='proof comment'>

- 无穷远处 $- \nabla u(r \to +\infty) = \mathbf{E}_0$，解为
   $$
  u(\mathbf{r}) = - E_0 r \cos \theta + \text{const}, \qquad r \to +\infty
  $$
- **<red>选择** $xy$ 平面的无穷远处保持为电势**零点**：$\text{const} = 0$
  $$
    u(\mathbf{r}) = - E_0 r \cos \theta, \qquad r \to +\infty
  $$
</div>

---
### 均匀电场中的带点导体球

<div class='proof comment'>

- 电势角度
- 电势可以**叠加**：均匀电场 $u(r, \theta) = \mathbf{E}_0$ 产生的电势 $+$ 导体球产生的电势
* 当 $r \to +\infty$：导体球的形状大小 **<red>不再重要**，粗略看成**点电荷**：
  $$
  u(r, \theta) \simeq - E_0 r \cos \theta + \frac{Q}{4\pi \epsilon_0 r} \simeq - E_0 r \cos\theta , \qquad r \to +\infty
  $$
  **公共势能零点**：$xy$ 平面的无穷远处；**<red>不能**简单地选“无穷远处做势能零点”

</div>

---
### 均匀电场中的带点导体球

- **球外**轴对称拉普拉斯问题一般解
  $$
  u(r, \theta) = \sum_{\ell = 0}^{+\infty} (A_\ell r^\ell + \frac{B_\ell}{r^{\ell + 1}}) P_\ell(\cos \theta)
  $$
  <div class='proof comment'>

  求解区域包含**无穷远**，该区域内**无电荷分布**
  
  **<red>能否通过「自然边界条件」、「有限性」直接说明所有 $A_\ell = 0$？**<answer>不能：均匀电场本身就在无穷远处产生了无穷大的电势</answer>

  </div>

---

### 均匀电场中的带点导体球

- **无穷远处**边界条件, 
  $$
  u(r \to +\infty, \theta) = \sum_{\ell = 0}^{+\infty} A_\ell r^\ell P_\ell(\cos \theta)
  = \purple{- E_0 r \cos \theta}
  $$
  <div class='proof comment'>

  $B$ 项不贡献，因为 $B_\ell r^{-\ell - 1} \to 0$

  </div>

---
### 均匀电场中的带点导体球
- 比较得到，**<purple>利用 $P_1(\cos \theta) = \cos \theta$**
  $$
  A_1 = -E_0, \qquad A_{\ell \ne 1} = 0
  $$
* 电势为
  $$
  u(r, \theta) = - E_0 r \cos \theta + \sum_{\ell = 0}^{+\infty} \frac{B_\ell}{r^{\ell + 1}}P_\ell(\cos \theta)
  $$
  <div class='proof comment'>
  
  $B_\ell$ 依然未定
  </div>



---
### 均匀电场中的带点导体球

- **球面**电势边界条件
  $$
    u(r = a, \theta) = - E_0 a \cos \theta + \sum_{\ell = 0}^{+\infty} \frac{B_\ell}{a^{\ell + 1}}P_\ell(\cos \theta) = \green{\text{const} \coloneqq u_0} (\gray{\text{待定}})
  $$
- 比较得到
  $$
    B_0 = \green{u_0a}, \qquad \red{B_1 = E_0 a^2}, \qquad B_{\ell > 1} = 0
  $$
  <div class='proof comment'>

  等式右边 $u_0$ **<red>与 $\theta$ 无关**，左边的 $-E_0 r \cos \theta$ 必须找 $B_1$ 项寻求 **<red>抵消**

  </div>

---
### 均匀电场中的带点导体球

- 得到
  $$
  \begin{align*}
    u(r, \theta) = & \ A_1 r P_1(\cos\theta) + \frac{B_0}{r}P_0(\cos\theta) + \frac{B_1}{r^2}P_1(\cos\theta)\\
    = & \ -E_0 r \cos \theta + \red{u_0} \frac{a}{r} + E_0 a \frac{a^2}{r^2}\cos \theta
  \end{align*}
  $$
* **<red>$u_0=$ ?**

---
### 均匀电场中的带点导体球

- 总电荷条件
  $$
  \begin{align*}
    \frac{Q}{\epsilon_0} = 
    & \ - \oint_{r = a+} \frac{\partial u}{\partial r} \purple{dS}\\
    = & \ - \int_0^\pi d\theta \int_0^{2\pi}d\varphi \frac{\partial}{\partial r}\bigg|_{r=a} \left({-E_0 r \cos \theta + u_0 \frac{a}{r} + E_0 a \frac{a^2}{r^2}\cos \theta}\right) \purple{a^2\sin \theta d\theta d \varphi}\\
  \end{align*}
  $$
  <div class='proof'>
  
  求导后，第一项 $- E_0 \cos \theta$，第二项 $- u_0\frac{a}{a^2} = - \frac{u_0}{a}$，第三项 $- 2E_0 \frac{a^3}{a^3}\cos \theta$，组合起来
  $$
  - 3 E_0 \cos \theta - \frac{u_0}{a}
  $$
</div>




---

### 均匀电场中的带点导体球

- 总电荷条件
  <div class='proof'>
    
  但是，在积分后，只有 $u_0$ 项存活，
  $$
  \int_0^\pi d\theta \sin \theta \cos \theta = 0 \quad \Rightarrow \quad
  \frac{Q}{\epsilon_0} = \frac{u_0}{a} 4\pi a^2
  $$
  求解得到
  $$
    u_0 = \frac{Q}{4\pi \epsilon_0 a}
  $$

  </div>

  <div class='proof comment'>

  就是没有均匀电场时，带电金属导体球面的电势、结合势

  </div>


---
### 均匀电场中的带点导体球

- 最终电势为
  $$
  u(r, \theta) = - E_0 r \cos \theta + \frac{Q}{4\pi \epsilon_0 r} + E_0 a \frac{a^2}{r^2}\cos \theta
  $$
  <div class='proof comment'>

  多极展开：外电场势，电势的单极矩，电势的偶极矩

  </div>
- 电场
  $$
  \begin{align*}
    \mathbf{E} = - \nabla u
  = \left({E_0 \cos\theta + \frac{2E_0a^3}{r^3}\cos\theta + \frac{Q}{4\pi \epsilon_0 r^2}}\right)\mathbf{e}_r\\
  + \left({-E_0 \sin\theta + \frac{E_0a^3}{r^3}\sin\theta}\right)\mathbf{e}_\theta
  \end{align*}
  $$



---

<div style='position:absolute;right:100px;top:190px'>

![width:400px](images/anya_potential_collapse.png)
</div>


### 均匀电场中的带点导体球

- 两个问题
- 放入导体球前：整个 $xy$ 平面都是势能零点

* **<red>放入导体球后势能零点分布在哪里？**
* **<red>与导体球等势的点有哪些？**




---
### 均匀电场中的带点导体球

- 最简单的情况：$Q = 0$
* **<red>不作复杂计算，能否通过物理分析找到势能零点分布？**
* 通过对称性猜测电场垂直于 $xy$ 面



---
### 均匀电场中的带点导体球

- 直接计算
* 电势零点方程
  $$
  \begin{align*}
    u(r, \theta) = - E_0 r \cos \theta + E_0 a \frac{a^2}{r^2}\cos \theta = & \ 0 \\
      E_0(- r  + \frac{a^3}{r^2})\cos \theta = & \ 0
  \end{align*}
  $$
  $$
  \Rightarrow \qquad \purple{r = a}, \quad \text{or}, \quad \purple{\cos \theta = 0}, \purple{~ \text{and} ~ r \ge a}
  $$
  <div class='proof comment'>

  不是一个简单的等势面，而是 **<red>球面** 与 **$xy$ 平面球外部分** 的 **并**，有**交点**

  </div>



---
### 均匀电场中的带点导体球

<center>

![width:840](media/images/figures/ZeroPotentialZeroCharge_ManimCE_v0.18.1.png)

$Q = 0$ 的时候势能零点分布
</center>

---
### 均匀电场中的带点导体球

- 电场**垂直于**势能面
* **<red>势能面自交点处，电场应该朝哪个方向？** <answer>哪都不朝，电场为零</answer>
* 直接验证: $Q = 0$，$r = a$，$\theta = \pi/2$，$\cos \theta = 0$，$\sin \theta = 1$
  $$
  \begin{align*}
    \mathbf{E} = - \nabla u
  = & \ \left({E_0 \cos\theta + \frac{2E_0a^3}{r^3}\cos\theta + \frac{Q}{4\pi \epsilon_0 r^2}}\right)\mathbf{e}_r \\
  & \ + \left({-E_0 \sin\theta + \frac{E_0a^3}{r^3}\sin\theta}\right)\mathbf{e}_\theta\\
  = & \ (0 + 0 + 0)\mathbf{e}_r + (- E_0 + E_0) \mathbf{e}_\theta \ \red{= \mathbf{0}}
  \end{align*}
  $$



---
### 均匀电场中的带点导体球

- $Q \ne 0$ 时候电势零点方程
  $$
  \begin{align*}
    u(r, \theta) = - E_0 r \cos \theta + \frac{Q}{4\pi \epsilon_0 r} + E_0 a \frac{a^2}{r^2}\cos \theta = & \ 0 \\
      E_0 r^2 (- 1  + \frac{a^3}{r^3})\cos \theta + \frac{Q}{4\pi \epsilon_0} = & \ 0
  \end{align*}
  $$
- 解相当复杂
* 当 $r \gg a$
  $$
  r(\theta) = \sqrt{\frac{Q}{4\pi E_0\epsilon_0 \cos \theta }}
  $$
  
---
### 均匀电场中的带点导体球

<center>


<video width='720' src='media/videos/figures/1080p60/ZeroPotential.mp4' controls></video>

势能零点，$Q$ 从 $0$ 变成**正值**，然后变成**负值**；面上方势能为负数，面下方势能为正数；注意等势面 **<purple>拓扑变化**
</center>

---
### 均匀电场中的带点导体球

- 当 $Q \ne 0$ 时候：球面势能非零
* **<red>空间哪些点与球面等势？**
  $$
  \begin{align*}
    u(r, \theta) = - E_0 r \cos \theta + \frac{Q}{4\pi \epsilon_0 r} + E_0 \frac{a^3}{r^2}\cos \theta = & \ \frac{Q}{4\pi \epsilon_0 a}\\
     E_0 r( \frac{a^3}{r^3} - 1)\cos \theta = & \ \frac{Q}{4\pi \epsilon_0 }(\frac{1}{a} - \frac{1}{r})
  \end{align*}
  $$


---
### 均匀电场中的带点导体球

<center>

<video width='720' src='media/videos/figures/1080p60/EquipotentialLine.mp4' controls></video>

与球面等势的点，$Q$ 从 $0$ 变到正值，再变到负值
</center>



---
### 均匀电场中的带点导体球

- 表面电荷密度分布
  $$
  \rho(\theta, \varphi) = \epsilon_0 \mathbf{E} \cdot \mathbf{n} = - \epsilon_0 \frac{\partial u}{\partial r}\bigg|_{r = a}
  = 3 \epsilon_0E_0 \cos \theta + \frac{Q}{4\pi a^2}
  $$
- $\theta = 0$ 时，电荷密度最正 (positive)
  <div class='proof comment'>

  但不一定有正电荷分布，得看 $Q$ 的符号及大小

  </div>
* $\theta = \pi$ 时，电荷密度最负 (negative)
  <div class='proof comment'>

  但不一定有负电荷分布，得看 $Q$ 的符号及大小

  </div>
* 当 $Q = 0$，正负表面电荷以赤道为界，各占半壁江山


---
# 一般球函数与连带勒让德函数




---
<!-- header: 一般球函数与连带勒让德函数 -->
### 连带 Legendre 函数
- 球坐标下拉普拉斯方程的 $\theta$-方向方程
  $$
  \frac{d}{dx}\bigg[(1 - x^2)\frac{d\mathscr{P}}{dx}\bigg] + \bigg(\lambda - \frac{m^2}{1 - x^2}\bigg)\mathscr{P} = 0
  $$
  <div class='proof comment'>

  为了与勒让德多项式 $P_\ell(x)$ 区分，**<green>用 $\mathscr{P}$ 表示**

  </div>

---
### 连带 Legendre 函数
- 自然边界条件：
  $$
  \left\{\begin{array}{ll}
    \mathscr{P}(\pm 1) = 0 \ , & m \ne 0\\
    \vert\mathscr{P}(\pm 1)\vert < \infty \ , & m = 0 ~ (\text{Legendre})
  \end{array}
  \right.
  $$
* 一般情况 **<red>无轴对称性**：$m = 0$ 与 $m \ne 0$ 均要考虑
  
---
### 连带 Legendre 函数
- **<green>连带 (伴随, associated) 勒让德方程** 标准形式
  $$
  \frac{d^2\mathscr{P}}{dx^2} - \frac{2x}{1-x^2} \frac{d\mathscr{P}}{dx} + \frac{1}{1-x^2}\left({\lambda - \frac{m^2}{1 - x^2}}\right)\mathscr{P} = 0, \qquad m > 0
  $$
  <div class='proof comment'>

  $m < 0$ 与 $m > 0$ 没有本质区别

  </div>

  <div class='proof comment'>
  
  作为 Sturm-Liouville 型方程，本征值是 $\lambda$，**<red>不是 $m$**；$m$ 的值由 $\varphi$ 方向方程确定；**<red>暂时还不知道 $\lambda =$ 什么** 才能满足自然边界条件
  </div>

---
### 连带 Legendre 函数
- **定理**：**连带**勒让德方程 **<green>的解 $\mathscr{P}$** 勒让德方程的解 $P$ 有**简单关系**：前者差不多是后者的 $m$ 阶导数
  $$
  \mathscr{P}(x) \sim  \green{(1 - x^2)^{\frac{m}{2}}} P^{(m)}(x)
  $$
  <div class='proof comment'>
  
  证明有点复杂
  </div>

---
### 连带 Legendre 函数

<div class="proof">

**证明连带勒让德方程的解与勒让德多项式的关系**


- 设 $\mathscr{P}(x)$ 满足**连带**勒让德方程
- **<green>定义** **<green>新符号 $p(x)$**
  $$
  \green{p(x) \coloneqq (1 - x^2)^{ - m/2}\mathscr{P}(x)}, \qquad\mathscr{P}(x) = \purple{(1 - x^2)^{\frac{m}{2}}p(x)}
  $$
  下面建立 $p$ 与 $P^{(m)}$ 的关系，由此得到 $\mathscr{P}$ 与 $P(x)$ 的关系

</div>


---
### 连带 Legendre 函数

<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**
- 利用 $\mathscr{P}$ 所满足的连带勒让德方程，研究 $p$ 所满足的微分方程。
* 一阶导数
  $$
  \begin{align*}
    \frac{d\mathscr{\mathscr{P}}(x)}{dx} 
    = & \ \frac{d}{dx}\left({\purple{(1 - x^2)^{\frac{m}{2}}p(x)}}\right)\\
    \gray{\text{(Leibniz rule)}} =  & \ (1 - x^2)^{\frac{m}{2}}p'(x) + \frac{m}{2}(-2x) (1 - x^2)^{\frac{m}{2} - 1}p(x)
    \\
    \gray{\text{(simplify)}}= & \ (1 - x^2)^{\frac{m}{2}} p'(x) - mx(1 - x^2)^{\frac{m}{2} - 1}p(x)
  \end{align*}
  $$
</div>

---

<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**

- 给 $\mathscr{P}'$ 乘以 $\red{1 - x^2}$
- 二阶导数
  $$
  \begin{align*}
    & \ \frac{d}{dx}\left({\red{(1 - x^2)}\frac{d\mathscr{P}}{dx}}\right)
  = \frac{d}{dx} \left[{(1 - x^2)^{\frac{m}{2} \red{\boldsymbol{+ 1}}}
  p'(x) - mx(1 - x^2)^{\red{\frac{m}{2}}}p(x)}\right]\\
  = & \ (1 - x^2)^{\frac{m}{2} + 1} p''(x)
  + (\frac{m}{2}+1)(-2x) (1 - x^2)^{\frac{m}{2}}p'(x)\\
  & \ - mx(1 - x^2)^{\frac{m}{2}}p'(x)
  - m(1 - x^2)^{\frac{m}{2}}p(x)\\
  & \  - m x \frac{m}{2}(-2x) (1 - x^2)^{\frac{m}{2} - 1}p(x)
  \end{align*}
  $$

  
</div>

---
### 连带 Legendre 函数


<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**
- 化简，**<purple>提取公因式 $(1 - x^2)^{\frac{m}{2}}$**
  $$
  \begin{align*}
    & \ \frac{d}{dx}\left({\red{(1 - x^2)}\frac{d\mathscr{P}}{dx}}\right)\\
    \gray{\text{(merge $p'$)}} = & \ \purple{(1 - x^2)^{\frac{m}{2}}} (1 - x^2) p''
  - \orange{2(m + 1) x} \purple{(1 - x^2)^{\frac{m}{2}}}p'(x)\\
  & \ - m\purple{(1 - x^2)^{\frac{m}{2}}}p(x) + m^2x^2 \purple{(1 - x^2)^{\frac{m}{2}}}\frac{p(x)}{1 - x^2}
  \end{align*}
  $$

</div>


---
### 连带 Legendre 函数

<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**
- 结合上述结果，利用 $\mathscr{P}$ 满足的连带勒让德方程
  $$
  \begin{align*}
    0 = & \ \frac{d}{dx} \left[{(1 - x^2)\frac{d\mathscr{P}}{dx}}\right] + \left({\lambda - \frac{m^2}{1 - x^2}}\right)\mathscr{P} \\
    = & \ (1 - x^2)^{m/2} \Big[(1 - x^2) p'' - \orange{2(m + 1)x}p' + (\purple{\lambda - m (m+1)})p \Big] 
  \end{align*}
  $$
  其中用到
  $$
     - m + \frac{m^2 x^2}{1 - x^2}  + \lambda - \frac{m^2}{1 - x^2}= \purple{\lambda - m(m + 1)}
  $$


</div>

---
### 连带 Legendre 函数

<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**
- 从而 $p(x)$ 满足
  $$
  (1 - x^2)\frac{d^2p}{dx^2} - 2(m + 1)x\frac{dp}{dx} + \left({\lambda - m(m + 1)}\right)p = 0
  $$
</div>

---
### 连带 Legendre 函数

<div class="proof">

**证明连带勒让德方程的解与勒让德多项式的关系**
- 另一方面，考虑 $m = 0$ 的 **勒让德方程**
  $$
  \purple{\frac{d}{dx}\bigg[(1 - x^2) \frac{dP}{dx}\bigg]} + \lambda P = 0, \qquad |P(\pm 1)| < \infty 
  $$
- 两边求 $m$ 次导，
  $$
  \begin{align*}
  0 = & \ \frac{d^m}{dx^m}\purple{\frac{d}{dx}\bigg[(1 - x^2)\frac{dP}{dx}\bigg]} + \lambda P^{(m)}\\
  = & \ \frac{d^m}{dx^m} \purple{\left[{(1 - x^2) \frac{d^2P}{dx^2} -2x \frac{dP}{dx}}\right]} + \lambda P^{(m)}\\
  \end{align*}
  $$

</div>

---
### 连带 Legendre 函数

<div class='proof'>

**证明连带勒让德方程的解与勒让德多项式的关系**
- 高阶导数公式，$(fg)^{(m)} = \sum_{k = 0}^m C_m^k f^{(k)} g^{(m - k)}$
  $$
  \begin{align*}
    & \ \frac{d^m}{dx^m} \purple{\left[{(1 - x^2) \frac{d^2P}{dx^2} -2x \frac{dP}{dx}}\right]}\\
  = & \ \sum_{k = 0}^{m} C_m^k \frac{d^k}{dx^k}(1 - x^2) \cdot \frac{d^{m - k}}{dx^{m - k}}\frac{d^2P}{dx^2}
   - \sum_{k = 0}^{m} C_m^k \frac{d^k}{dx^k}(2x) \cdot \frac{d^{m - k}}{dx^{m - k}}\frac{dP}{dx} 
  \end{align*}
  $$
  $(1 - x^2)$ 最多承载 $2$ 阶导数，$2x$ 最多承载 1 阶导数

</div>

---
### 连带 Legendre 函数

<div class='proof'>


**证明连带勒让德方程的解与勒让德多项式的关系**
- 把 $m$ 阶导数吸收到 $P$ 上写成 $P^{(m)}$
  $$
  \begin{align*}
    & \ \frac{d^m}{dx^m}\bigg[(1 - x^2)\frac{d^2P}{dx^2} - 2x \frac{dP}{dx}\bigg]\\
    = & \ (1 - x^2) \frac{d^2 P^{(m)}}{dx^2} - \purple{(2x) C_m^1} \frac{dP^{(m)}}{dx} + \red{C_m^2 (-2)} P^{(m)}
    - \purple{2x \frac{dP^{(m)}}{dx}} - \red{2 C_m^1 } P^{(m)}
    \\
    = & \ (1 - x^2)\frac{d^2P^{(m)}}{dx^2}
      - \purple{2(m + 1)x} \frac{dP^{(m)}}{dx} - \red{m(m + 1)} P^{(m)}
  \end{align*}
  $$

</div>

---

### 连带 Legendre 函数



<div class='proof'>


**证明连带勒让德方程的解与勒让德多项式的关系**

$~$
- 因此 $P^{(m)}$ 满足方程
  $$
  (1 - x^2)\frac{d^2 P^{(m)}}{dx^2} - 2(m + 1)x \frac{dP^{(m)}}{dx} + (\lambda - m(m + 1))P^{(m)} = 0
  $$
- 可见 $p(x) = \green{(1-x^2)^{- \frac{m}{2}}\mathscr{P}(x)}$ 与高阶导数 $\green{P^{(m)}}$ 满足**相同的微分方程**，
  $$
  \green{(1 - x^2)^{-\frac{m}{2}}\mathscr{P}(x) \sim  P^{(m)}(x)}, \quad
  \mathscr{P}(x) \sim  \green{(1 - x^2)^{\frac{m}{2}}} P^{(m)}(x)
  $$

</div>

<div style='position:absolute;right:50px;top:70px'>

![width:300px](images/anya_boundary_exhausted.png)
</div>



---
### 连带 Legendre 函数

<div class='proof'>

**连带勒让德函数的自然边界条件**


- 根据球坐标分离变量：$\mathscr{P}(x)$ 应当满足自然边界条件
  $$
  \left\{\begin{array}{lc}
    \mathscr{P}(\pm 1) = 0 \ , & m \ne 0\\
    \mathscr{P}(\pm 1) ~ \text{有限} \ , & m = 0
  \end{array}\right.
  $$
* **<red>$P(x)$ 应当满足什么边界条件，使得 $\mathscr{P}(x) \sim (1 - x^2)^{\frac{m}{2}} P^{(m)}(x)$ 满足自然边界条件？**

* **<red>$P(x)$ 能有什么边界行为？**
</div>



---
### 连带 Legendre 函数

<div class='proof'>

**连带勒让德函数的自然边界条件**

- **generic 的 $\lambda$**: $P(x)$ 在 **<red>$\mp 1$ 处**有 **<red>对数型发散**，$P(x) \sim \ln(1 \pm x)$
  $$
  \purple{P^{(m)}(x)} \sim \red{(1 \pm x)^{-m}}
  \quad\Rightarrow \quad
  \mathscr{P}(x)\sim (1 - x^2)^{\frac{m}{2}}\purple{P^{(m)}(x)} \sim  (1 \pm x)^{-\frac{m}{2}}
  $$
  对所有 $m > 0$，**<red>不满足** 自然边界条件
* **特殊的 $\lambda = \ell(\ell + 1)$**: 勒让德多项式 **<green>$P(x) = P_\ell(x)$**，**<orange>$P(\pm 1) = (\pm 1)^\ell$**，
  $$
  \mathscr{P}(x)\sim (1 - x^2)^{\frac{m}{2}}P_\ell^{(m)}(x) \sim (1 \pm x)^{m/2}
  $$
  当 $m \ge 0$，**<green>都满足自然边界条件**


</div>

---
### 连带 Legendre 函数
- **<green>定义**：**<green>连带 (associated) Legendre「函数」** $P_\ell^m(x)$，
  $$
  P_\ell^m(x) \coloneqq (1 - x^2)^{m/2} \frac{d^m P_\ell(x)}{dx^m}, \qquad \ell = 0, 1,2, \dots, \quad 0 \le m \le \ell
  $$
  <div class='proof comment'>

  - 一般而言，连带 Legendre **函数** **<red>不是** $x$ 的多项式，因为有分数 $m/2$ 幂次，因此 **<red>不称为连带 Legendre **多项式****
  
  - 与 $P_\ell^m$ 线性独立的另一个方程的解为 $Q_\ell^m$，**<red>不满足自然边界条件**，一般不讨论

  </div>
  
---
### 连带 Legendre 函数的性质

<div class='proof comment'>

**括号与没有括号**

小心区分两个符号
- $P_\ell^m(x)$：$m$ 阶连带 Legendre 函数
- $P_\ell^{(m)}(x)$：勒让德多项式的 $m$ 阶导数
$$
P^m_\ell(x) = (1 - x^2)^{\frac{m}{2}}P^{(m)}_\ell(x)
$$
</div>


---
### 连带 Legendre 函数的微分表达式

- 利用 Legendre 多项式的微分表达式 (Rodrigues 公式)，得到连带 Legendre 函数的**微分表达式**，
  $$
  P_\ell^m(x) = \frac{1}{2^\ell \ell!}(1 - x^2)^{m/2}\frac{d^{\ell + m}}{dx^{\ell + m}}(x^2 - 1)^\ell
  $$

  <div class='proof comment'>

  微分表达式中 $m$ 原则上可以是**负数**，只要保证 $\ell + m \ge 0$ 即可

  </div>
---

### 负 $m$

- 连带 Legendre 方程的一般形式
  $$
  \frac{d}{dx}\bigg[(1 - x^2)\frac{dp}{dx}\bigg] + \bigg(\lambda - \frac{m^2}{1 - x^2} \bigg)p = 0 
  $$
- 方程中 $m$ 其实**可正可负**：$m$ 的符号不重要
* 利用微分表达式，获得 $P_\ell^{-|m|}(x)$
* **自然边界** Sturm-Liouville 本征值问题的一般性质：相同本征值的解 **<red>只有**一个
  $$
  P_\ell^{-|m|}(x) = (-1)^{|m|} \frac{(\ell - |m|)!}{(\ell + |m|)!}P_\ell^{|m|}(x), \quad m \in \mathbb{Z}
  $$


---
### 正交归一关系


- **<green>相同 $m$**，**<red>不同 $\ell$** 的连带 Legendre 函数之间**正交**
  $$
  (P^\green{m}_\ell, P^\green{m}_{\ell'}) = \frac{(\ell + m)!}{(\ell - m)!} \frac{2}{2\ell + 1} \ \delta_{\ell, \ell'}, \qquad
  |m| \le \ell
  $$
  <div class='proof comment'>

  **正交性**来自 Sturm-Liouville 本征问题的一般性质：$\lambda$ 是**本征值**，**<red>$m$ 是 $q(x)$ 的一部分**
  $~$
  权函数 $\rho(x) = 1$,
  $$
    (f, g) = \int_{-1}^{+1} \overline{f(x)} g(x) dx
  $$

  </div>


---

### 正交归一关系

- **<green>相同 $m$**，**<red>不同 $\ell$** 的连带 Legendre 函数之间**正交**
  $$
  (P^\green{m}_\ell, P^\green{m}_{\ell'}) = \frac{(\ell + m)!}{(\ell - m)!} \frac{2}{2\ell + 1} \ \delta_{\ell, \ell'}, \qquad
  |m| \le \ell
  $$

  <div class='proof'>
  
  证明类似 $P_\ell$ 的定理，反复使用分部积分。
  </div>
- 从上述结果导出 **<green>模方 (norm-squared)**
  $$
  \lVert P_\ell^m \rVert^2 = \frac{(\ell + m)!}{(\ell - m)!} \frac{2}{2\ell + 1}
  $$

---
### 完备性
- Sturm-Liouville 本征问题的一般性质：**完备性**
- $[-1,1]$ 上的性质良好函数可以做**广义傅里叶展开**，
  $$
  f(x) = \sum_{\ell = m}^{+\infty} f_\ell P^m_\ell(x), \qquad x \in [-1,1] 
  $$
  $$
  f_\ell = \frac{1}{\lVert P_\ell^m \rVert^2} \int_{-1}^{+1}f(x)P_\ell^m(x)dx , \qquad 0 \le m \le \ell
  $$



---

### 球谐函数

- Laplace 或者 Helmholtz 方程的球坐标**角 $(\theta, \varphi)$ 向**行为: $Y(\theta, \varphi)$ 负责
- 球谐函数方程
  $$
  \frac{1}{\sin \theta} \frac{\partial}{\partial \theta}\bigg(
  \sin\theta  \frac{\partial Y}{\partial \theta} \bigg)
  + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial\varphi^2} + \lambda Y = 0
  $$

---
### 球谐函数
* 自然边界条件 ($u$ 单值性要求)：  
  * **良定性**：$Y(\theta = 0, \varphi), Y(\theta = \pi, \varphi)$ 与 $\varphi$ **<red>无关**，具有明确的值，且**有限**
  * **周期性**：$Y(\theta, \varphi) = Y(\theta, \varphi + 2\pi)$ 对所有 $\theta \in [0, \pi]$ 成立 (其实也是一种良定性)
  <div class='proof comment'>

  满足这些条件的 $\theta, \varphi$ 的函数形成 **<green>球面上的函数 (function on $S^2$)**：球面上一个点对应明确的一个有限函数值

  </div>

---
### 球谐函数

<center>

![width:720](media/images/figures/SphereNorthAndSouthPole_ManimCE_v0.18.1.png)

</center>

---

### 球谐函数

- $Y$ 的进一步分离变量获得 $Y(\theta, \varphi) = H(\theta)\Phi(\varphi)$
  $$
    H(\theta) = P_\ell^m(x = \cos \theta), \qquad \Phi(\varphi) = e^{i m \varphi}, \quad m \in \mathbb{Z}_{|m|\le \ell}
  $$
  <div class='proof comment'>
  
  **回顾**
  - $\Phi$ 满足的微分方程 $\Rightarrow$ 指数解 $e^{i\mu \varphi}$；周期性 $\Rightarrow$ $\mu = m$ 为整数
  - $H$ 满足连带勒让德方程；良定性 $\Rightarrow$ 自然边界条件 $\Rightarrow$ $\lambda = \ell(\ell + 1)$ $\Rightarrow$ $m$ 满足 $|m| \le \ell$，选 $P_\ell^m(x)$ 作为解
  </div>

---
### 球谐函数

- **<green>定义**：**<green>球谐函数 (Spherical harmonics)** ($\ell \in \mathbb{N}$, $m \in \mathbb{Z}_{|m| \le \ell}$)
  $$
  Y_{\ell m}(\theta, \varphi) = (-1)^m \frac{1}{\lVert P_\ell^m \rVert} P_\ell^m(\cos \theta) \frac{e^{i m \varphi}}{\sqrt{2\pi}} , \qquad
  - \ell \le m \le \ell
  $$
  <div class='proof comment'>

  $P^{m}_\ell$ 与 $P^{-m}_\ell$ 成**正比**，$Y_{\ell m}(\theta, \varphi)$ 与 $Y_{\ell, -m}(\theta, \varphi)$ **<red>核心差别** 在于指数因子 $e^{\pm i m \varphi}$

  </div>



---
### 球谐函数
<div class='proof comment'>

例子
$$
\begin{align*}
  Y_{00}(\theta, \varphi) = \frac{1}{2\sqrt{\pi}}
\end{align*}
$$
$$
Y_{1,0}(\theta, \varphi) = \sqrt{\frac{3}{4\pi}}\cos \theta, \quad
Y_{1,\pm 1}(\theta, \varphi) = \mp \sqrt{\frac{3}{8\pi}}\sin \theta e^{\pm i \varphi}
$$

</div>


---
### 球谐函数
<center>

![width:920](images/image-1.png)

</center>

---
### 球谐函数
- **正交归一定理**，对于 $-\ell \le m \le \ell$, $-\ell' \le m' \le \ell'$，$\ell, \ell' \in \mathbb{N}$
  $$
  \int_0^{2\pi}\int_0^\pi 
  Y_{\ell m}(\theta, \varphi) \overline{Y_{\ell'm'}(\theta, \varphi)} \sin \theta d\theta d \varphi = \delta_{\ell \ell'}\delta_{m m'}
  $$
  <div class='proof comment'>

  积分微元 $\sin \theta d\theta d\varphi$ 为单位球面 $S^2$ 的体积元 (volume form)/面积元
  $$
    \int_0^{2\pi}\int_0^\pi \sin\theta d\theta d\varphi = 4\pi
  $$

  </div>

---
### 球谐函数
- **完备性定理**：对于任何球面上的函数 $f(\theta, \varphi)$ 可以展开
  $$
  f(\theta, \varphi) = \sum_{\ell \in \mathbb{N}}\sum_{m = -\ell}^{+\ell}  f_{\ell m}Y_{\ell m}(\theta, \varphi),
  $$
  $$
  f_{\ell m} = \int_0^{2\pi} d\varphi \int_0^\pi f(\theta, \varphi)Y_{\ell m}(\theta, \varphi)\sin \theta d\theta 
  $$

---
### 球谐函数

<div class='proof comment'>

给定 $\ell \in \mathbb{N}$，球谐函数 $\{Y_{\ell m} | m = -\ell, \dots +\ell\}$ 形成 $SO(3)$ 群的 $2\ell + 1$ 维**线性表示**，$\ell$ 为表示的 **<green>自旋 (spin)**
$$

Y_{\ell m}(\theta, \varphi) \xrightarrow{R}
Y_{\ell m}(\theta'(\theta, \varphi), \varphi'(\theta, \varphi)) = \sum_{m' = -\ell}^{+\ell} D_{mm'}^\ell(R)Y_{\ell m'}(\theta, \varphi)

$$

</div>


---
### 球谐函数

- Laplace 方程的**一般解** (非轴对称)
  $$
  u(r, \theta, \varphi) = \sum_{\ell = 0}^{+\infty}\sum_{m = -\ell}^{+\ell}  \bigg(A_{\ell m}r^\ell + \frac{B_{\ell m}}{r^{\ell + 1}}\bigg)Y_{\ell m}(\theta, \varphi)
  $$
  <div class='proof comment'>

  其中用到径向方程的解 $r^\ell$ 与 $1/r^{\ell + 1}$，系数 $A_{\ell,m}, B_{\ell, m}$ 由边界条件确定

  </div>
- 如果问题确实具有**轴对称**，则上述 $A_{\ell, m \ne 0} = B_{\ell, m \ne 0} = 0$
  $$
  u(r, \theta, \varphi) = \sum_{\ell = 0}^{+\infty}\bigg(A_{\ell,0}r^\ell + \frac{B_{\ell, 0}}{r^{\ell + 1}}\bigg)P_\ell(\cos \theta),
  \quad Y_{\ell, m = 0}(\theta, \varphi) = P_\ell(\cos \theta)
  $$
