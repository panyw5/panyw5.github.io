---
marp: true
theme: rose-pine-dawn-modern
paginate: true
_paginate: skip
size: 16:9

math: katex
---

$$
\gdef\red#1{{\color{cb8680}{#1}}} 
\gdef\green#1{{\color{4f8d63}{#1}}} 
\gdef\gray#1{{\color{gray}{#1}}} 
\gdef\purple#1{{\color{B189C6}{#1}}} 
\gdef\orange#1{{\color{dfa04b}{#1}}}
\gdef\white#1{{\color{white}{#1}}}
$$

<center>


# 柱函数
</center>

---
<!-- header: 柱函数的基本性质 -->

<div class="twocols">

# 
# 柱函数基本性质

<p class="break"></p>

- 分离变量回顾
- 函数的整体图景
- 递推关系与渐近形式
- 生成函数

</div>

---

### 分离变量
- 处理含圆柱形边界面的物理问题
* 柱坐标 $(\rho, \varphi, z)$：径向坐标 $(\rho, z)$，角向坐标 $\varphi$
* Laplace 方程分离**径向 ($\rho, z$)**与**角向 ($\varphi$)**：第一分离常数 $\mu$
  $$
  \begin{align*}
    \frac{1}{R\rho} \frac{d}{d\rho} \bigg(\rho \frac{dR}{d\rho}\bigg) - \frac{\green{\mu}}{\rho^2} =    - \frac{1}{Z}\frac{d^2 Z}{dz^2} \qquad
    
    \frac{d^2\Phi}{d\varphi^2} + \mu \Phi =   0
  \end{align*}
  $$
  <div class='proof comment'>

  
  - $\varphi$ 方向使用**周期性边界条件**：$\mu = m^2$，$m = 0, 1, 2, \cdots$，$\Phi(\varphi) = e^{\pm im\varphi}$
  - 在单独研究 Bessel 方程时，升级 $m \to \nu$ 可以取遍**任意复数**
  </div>
  


---
### 分离变量

- 分离两个径向 $R$ 与 $z$ (第二分离常数 $\lambda$)
  $$
  \begin{align*}
    \frac{1}{\rho} \frac{d}{d\rho} \left({\rho \frac{dR}{d\rho}}\right) - \frac{m^2}{\rho^2} R = & \ - \green{\lambda} R \\
    \frac{d^2 Z}{dz^2} = & \ + \green{\lambda} Z
  \end{align*}
  $$
  <div class='proof comment'>
  
  $\lambda$ **一定程度**上刻画 $z$ 方向的平移不变性：$Z(z) = Az + B$，其中 $Z(z) = B$ 的部分刻画了平移不变的成分。
  </div>

---
### 分离变量
- 倘若 **$\lambda \ne 0$**：$\rho$ 方向可以重写为 **<green>$m$-阶Bessel 方程**
* 记 **<green>$x = \sqrt{\lambda}\rho$，$y(x) = R(\rho)$**
  $$
  y'' + \frac{1}{x}y' + \bigg(1 - \frac{m^2}{x^2}\bigg) y = 0
  $$
  <div class="proof comment">

  - 作为“径向坐标”，**<green>$x > 0$**

  - 柱坐标分离变量 **<red>不是** Bessel 方程的唯一来源，也可以来自一维线性势能的薛定谔方程等其他问题：此时 $x$ 不再具有“径向坐标”的物理意义，原则上 **<red>$x$ 可正可负**

  </div>

---
### 分离变量

<div class='proof comment'>

**分离变量**

- 柱坐标分离变量的分离常数是 $\lambda, \mu$
  
- 但是在 Bessel 方程中，**非零的 $\lambda$** 被吸收到了自变量 $x$ 的定义中，并没有显式出现

  但 $\lambda$ 会受到 $x \ne 0$ 处的**物理边界条件**约束
</div>

---
### 分离变量

- **<red>如果 $\red{\lambda=0}$ 怎么办？</red>**
* 当 $\lambda = 0$，
  $$
  \rho\frac{d}{d\rho}\bigg(\rho \frac{dR}{d\rho}\bigg) = m^2 R \qquad \xRightarrow[\tilde R(t) = R(\rho)]{\rho = e^t} \qquad
  \frac{d}{dt}\frac{d}{dt}\tilde R(t) = m^2 \tilde R(t)
  $$
  <div class='proof comment'>
  
  线性独立解可以分情况讨论：
  $$
  \begin{cases}
    \tilde R(t) = e^{\pm m t}  & m > 0\\
    \tilde R(t) = \text{const}, t & m = 0
  \end{cases}
  \quad\Rightarrow\quad
  \begin{cases}
    R(\rho) = \rho^{\pm m}  & m > 0\\
    R(\rho) = \text{const}, \ln\rho & m = 0
  \end{cases}
  $$
  </div>

---
### Bessel 方程的解

- 考虑升级 $m \to \nu\in \mathbb{C}$，$\operatorname{Re}\nu \ge 0$
  $$
  y'' + \frac{1}{x}y' + \bigg(1 - \frac{\nu^2}{x^2}\bigg) y = 0
  $$

---
### Bessel 方程的解
- 上述 $\nu$-阶 Bessel 方程属于 Sturm-Liouville 型方程，求解区间是 $(0, \infty)$
  $$
  k(x) = x, \qquad
  q(x) = \frac{\nu^2}{x}, \qquad
  \rho(x) = x
  $$
- 作为 Sturm-Liouville 问题，**<red>本征值被选定为 $= 1$**
- $\nu$ **<red>不是**本征值：$\nu$ 由角向 ($\varphi$) 边界条件决定，不管 $\nu$ 是多少，都可以获得两个线性独立解 (Fuchs 定理)
  <div class='proof comment'>
  
  额外考虑自然边界条件 $|y(0)| < \infty$ 可以排除一个解；**<red>哪一个？**
  </div>


---
### Bessel 方程的解

- **定理 (Fuchs)**：$x = 0$ 是 Bessel 函数的正则奇点，在该邻域有两个 **<green>正则解**
  $$
  \small{第一解}：\purple{\boldsymbol{y_{(1)}(x)}} = \sum_{n = 0}^{+\infty} y_n x^{n + s_1} 
  $$
  $$
  \small{第二解}：y_{(2)}(x) = \sum_{n = 0}^{+\infty} \red{y'_n} x^{n + s_2} + \underbrace{\beta \purple{\boldsymbol{y_{(1)}(x)}} \ln(x)}_{对数项}
  $$
  其中 $s_1, s_2 \in \mathbb{C}$ 称为 **<green>正则解的指标** 或者 **<green>indicial roots**，满足 $\operatorname{Re}s_1 \ge \operatorname{Re}s_2$。


---
### Bessel 方程的解

- 指标 $s_1, s_2$ 是下述指标方程 (indicial equation) 的根
  $$
  s^2 = \nu^2 \qquad \Rightarrow \qquad s_1 = +\nu, \quad s_2 = -\nu, \qquad \operatorname{Re}\nu \ge 0
  $$
- $s_1 - s_2 = 2\nu$
- 根据 $2\nu$ 的取值，有三种情况：
  - **generic**：$2\nu \not\in \mathbb{Z}$，$\beta = 0$，第二解不含对数项 $\ln(x)$
  - **ok**：$2\nu = 1, 3, 5, \cdots$，第二解不含对数 $\ln x$
  - **bad**：$2\nu = 0, 2, 4, 6, \cdots$，$\beta = 0$，第二解 **<red>一定含对数项**

---
### Bessel 方程的解

- 当 $\operatorname{Re}\nu > 0$，有 **<green>$\operatorname{Re}s_1 > 0$**，从而
  $$
  y_{(1)}(x) = \sum_{n = 0}^{+\infty} y_n x^{n + s_1} \xrightarrow{~x \to 0~} 0
  $$
- 当 $\operatorname{Re}\nu > 0$，有 **<red>$\operatorname{Re}s_2 < 0$**
  $$
  y_{(2)}(x) = \sum_{n = 0}^{+\infty} \red{y'_n} x^{n + s_2} + \underbrace{\beta \purple{\boldsymbol{y_{(1)}(x)}} \ln(x)}_{对数项} \xrightarrow{x \to 0} \infty
  $$
  <div class='proof comment'>
  
  第一项发散，第二项 (如果存在) 也发散：总是被自然边界条件排除
  </div>

---
### Bessel 方程的解

- 如果 $\nu = 0$，则 $J_0(x \to 0) = 1$，$N_\nu(x\to 0) = \infty$

---
### Bessel 方程的解

- 研究具体解的行为
- 两个线性独立的解：$\{J_\nu, N_\nu\}$
  $$
  y_{(1)}(x) = J_\nu(x) = \sum_{k = 0}^{+\infty} \frac{(-1)^k }{k! \Gamma(k + \nu + 1)}  \bigg(\frac{x}{2}\bigg)^{2k + \nu}
  $$
  $$
  y_{(2)}(x) = N_\nu (x) = \frac{\cos (\pi \nu) J_\nu(x) - J_{- \nu}(x)}{\sin (\pi \nu)}
  $$

---
### Bessel 方程的解
- Bessel 方程的解的几种叫法
* **<green>第一类**柱函数：$J_\nu(x)$
* **<green>第二类**柱函数：$N_\nu(x)$
* **<green>第三类**柱函数：$J$ 与 $N$ 的复线性组合
  $$
  \small{\text{第一种 Hankel 函数：}} \green{H^{(1)}_\nu(x) \coloneqq J_\nu(x) + i N_\nu(x)}, 
  $$
  $$
  \small{\text{第二种 Hankel 函数：}} \green{H^{(2)}_\nu(x) \coloneqq J_\nu(x) - i N_\nu(x)}
  $$

---
### Bessel 方程的解
- 四种函数**线性相关**：只有 **<red>两个</red>** 是 **线性独立**
  <div class="proof comment">

  **说明**

  类似 $\cos x, \sin x, e^{+ix}, e^{-i x}$ 的相对关系

  </div>





---
### 整体函数图像


<center>

![width:720px](media/images/figures/BesselJPlot_ManimCE_v0.18.1.png)
</center>

- 考虑最简单的情况：$\nu, x \in \mathbb{R}$


---
### 整体函数图像


<center>


<video width='1000' src='media/videos/animations/1080p60/BesselJ.mp4' controls></video>
</center>



---
### 原点渐近行为
- 下面研究 $J_\nu(x)$ 和 $N_\nu(x)$ 的原点渐近行为
- 先看 $\nu \in \mathbb{R}$ 时 $J_\nu$ 在**原点 $x = 0$ 处**的行为
  
  |   $\nu > 0$    |  $\nu = 0$   |  $\nu < 0$                       |
  |:------------:|:----------:|:--------------------------------------------------:|
  |$J_\nu(0) = 0$|$J_0(0) = 1$|  $J_{-m}(0) = 0$      |
  |              |            |$J_{- m + \epsilon}(0) = (- 1)^{m - 1} \cdot \infty$|
  |              |            |  $J_{- m - \epsilon}(0) = (- 1)^{m} \cdot \infty$  |
  
  其中 $\epsilon \in (0,1)$


---
### 原点渐近行为

- $\nu > 0$ 时，$J_\nu(x)$ 随着 $\nu$ **连续变化**，全程保持 $J_\nu(x\to 0) = \green{0}$
- $\nu = 0$ 是一个**临界点**：$J_0(x \to 0) = \orange{1}$
- $\nu < 0$ 时 $J_\nu(x \to 0)$ 随着 $\nu$ **分段连续变化**
  * 无穷多个**临界点**：$\nu = -m = -1, -2, -3, \cdots$
  * 跨过临界点时 $J_\nu(x \to 0)$ 发生 **<red>跃变**：正无穷 $\leftrightarrow$ 负无穷





---
### 原点渐近行为
- **定理**：对于一般的 $\nu \in \mathbb{C}$ 值，$J_\nu(x)$ 有如下几种原点渐近行为
  $$
  \begin{align*}
    \nu = 0:& \ \lim_{x \to 0}J_0(x) = 1\\

  \operatorname{Re}\nu > 0:& \ \lim_{x \to 0} J_{\nu}(x) = \lim_{x \to 0}J_{-1,-2,\cdots}(x) = 0\\

  \operatorname{Re}\nu ~ \red{\boldsymbol{<}} ~ 0~ \text{and}~ \red{\nu \ne 0, -1, -2, \cdots}:& \ \lim_{x \to 0} J_{\nu}(x) = \infty
  \end{align*}
  $$
  <div class="proof comment">

  **注意**

  * 除了 $\nu = 0$，**<red>不讨论 $\operatorname{Re}\nu = 0$ 时渐近行为**，因为涉及 $0^{i \operatorname{Im}\nu}$ 的非良定性
  * $\lim_{x \to 0}$ 与 $\lim_{\nu \to 0}$ **<red>不交换**，
    $$
    \lim_{\nu \to 0}\lim_{x \to 0}J_\nu(x) = 0, \qquad
    \lim_{x \to 0}\lim_{\nu \to 0} J_\nu (x) = 1
    $$

  </div>

---
### 原点渐近行为

<center>

![width:820px](media/images/figures/BesselJOrigin_ManimCE_v0.18.1.png)

不同 $\nu$ 的原点行为: **<green>绿色**代表极限为 $0$，**<red>红色**代表极限为 $\infty$，黄色代表极限为 $1$
</center>

---
### 原点渐近行为

<div class="proof">

**说明**
- 按照定义推导。考虑 $\operatorname{Re}\nu \ge 0$。
- $J_\nu(x \to 0)$ 只有**领头阶** $\orange{k = 0}$ 项的贡献，
  $$
  J_\nu(x \to 0) \sim \frac{1}{\Gamma(1 + \nu)} \bigg(\frac{x}{2}\bigg)^\nu
  $$
  根据 $\orange{\nu = 0}$ 还是 $\orange{\operatorname{Re}\nu > 0}$，**<red>分别**趋近 $\red{1}$ 和 $\red{0}$，
  $$
  \bigg(\frac{x}{2}\bigg)^0 = 1, \qquad
  \bigg(\frac{x}{2}\bigg)^{\operatorname{Re}\nu + i \operatorname{Im}\nu}
  = |x|^{\operatorname{Re}\nu}  e^{-(\operatorname{arg}x) \operatorname{Im}\nu} e^{i(...)}
  \to 0
  $$


</div>

---
### 原点渐近行为

<div class='proof'>

**说明**
- $J_{\nu < 0}(x)$ 的领头贡献还是 $k = 0$，分两种情况
- 当 $\nu = -m =  1,2,3, \cdots$，此时**分母 $\Gamma(1 + \nu) = \infty$**，使得
  $$
  J_{-m}(x\to 0) = 0
  $$
- 当 $\nu < 0$ 但不是整数，
  $$
  J_{\nu}(x \to 0) \sim \frac{1}{\Gamma(1 + \nu)}\bigg(\frac{x}{2}\bigg)^{\nu} \to \infty
  $$
  其中 $\nu = - m \pm \epsilon$ 时 $\Gamma(1 + \nu) \xrightarrow{\epsilon \to +0} \pm (-1)^{m - 1}\infty$
</div>

---
### 原点渐近行为与自然边界条件

- 综上，对于 generic $\nu$：$J_\nu(x)$ 和 $J_{-\nu}(x)$ 在原点处具有 **<red>截然不同** 的行为
  $$
  J_\nu(x \to 0) \to 0, \qquad J_{-\nu}(x \to 0) \to \infty, \qquad \operatorname{Re}\nu > 0, \ \ 2\nu \not\in \mathbb{Z}
  $$
- generic $\nu$：$J_\nu$ 和 $J_{-\nu}$ 的**线性独立性**
- $J_{\nu}$ 满足自然边界条件，$J_{-\nu}$ **<red>破坏**自然边界条件
  <div class='proof comment'>
  
  柱坐标系分离变量 $m \ne 0$ 的时候必须 $R(\rho \to 0) = 0$
  </div>
- 当 $\nu = 0$，$J_0(x \to 0) = 1$：同样满足自然边界条件 
  <div class='proof comment'>
  
  柱坐标系分离变量 $m = 0$ 的时候要求 $R(\rho \to 0)$ **有限**
  </div>


---
### 原点渐近行为
- **定理**：$N_\nu$ 有如下原点渐近行为
  $$
  N_\nu(x \to 0) \to \infty, \qquad \operatorname{Re} \nu \ge 0
  $$
  <div class="proof">


  **说明**
  - 对于 generic $\operatorname{Re}\nu > 0$
    $$
    N_\nu(x) = \frac{\cos (\pi \nu)J_\nu(x) - J_{-\nu}(x)}{\sin (\pi \nu)}
    $$
    包含 $J_{-\nu}(x)$，因此 $x \to 0$ 总是趋于**无穷大**。
  - $N_{m = 0, 1, 2, \cdots}(x)$ 由于有对数项 $\frac{2}{\pi}J_m(x)\red{\ln x}$，$x \to 0$ 时趋于**无穷大**

  </div>


---
### 原点渐近行为


<center>

![width:800px](images/LinearIndependentBesselFunctions_ManimCE_v0.18.1.png)

$N_\nu$ 与 $J_\nu$ 总是线性独立，$J_{-\nu}$ 则是两边倒
</center>


---
### 原点渐近行为


<center>

![](images/Bessel-functions.jpg)
$N_\nu$ 与 $J_\nu$ 总是线性独立，$J_{-\nu}$ 则是两边倒
</center>


---
### 原点渐近行为

- 对任意 $\nu$，Bessel 方程的两个解，只有一个满足 $x = 0$ 处的自然边界条件，另一个在 $x = 0$ 处总是 **<red>无穷大**
  <div class='proof comment'>
  
  这两个解可以取 $\{J_\nu, J_{-\nu}\}$，或者 $\{J_\nu, N_\nu\}$，结论都一样
  </div>

  <div class='proof comment'>
  
  $x = 0$ 端的自然边界条件对 $\nu$ 没有约束力
  </div>


---
### 无穷远附近行为


- **定理** (不作证明)：对于 $-\pi < \operatorname{arc}x < \pi$ (即 $\red{x \not \in \mathbb{R}_{<0}}$)
  $$
  J_\nu(x \to \infty) \sim \purple{\sqrt{\frac{2}{\pi x}}} \cos(\orange{x - \frac{\pi \nu}{2} - \frac{\pi}{4}})
  $$
  $$
  N_\nu(x \to \infty) \sim \purple{\sqrt{\frac{2}{\pi x}}} \sin(\orange{x - \frac{\pi \nu}{2} - \frac{\pi}{4}})
  $$
  $$
  H^{(1)}_\nu(x \to \infty) \sim \purple{\sqrt{\frac{2}{\pi x}}} e^{+i(\orange{x - \frac{\pi \nu}{2} - \frac{\pi}{4}})}
  $$
  $$
  H^{(2)}_\nu(x \to \infty) \sim \purple{\sqrt{\frac{2}{\pi x}}} e^{ - i(\orange{x - \frac{\pi \nu}{2} - \frac{\pi}{4}})}
  $$


---
### 无穷远附近行为

<div class="proof comment">

**说明**

- 渐近行为中 $\cos, \sin$ 和指数函数的宗量相同，
  $$
  \orange{x - \frac{\pi\nu}{2} - \frac{\pi}{4}}
  $$
  四个函数的关系类似 $\cos x, \sin x, e^{+ix}, e^{-i x}$ 的相对关系
- 都有共同衰减因子
  $$
  \purple{\sqrt{\frac{2}{\pi x}}}
  $$

</div>

---
### 零点

- **定理**：$J_\nu(x)$ 的零点均为**单零点**
* **定理**：$J_\nu(x)$ 和 $J'_\nu(x)$ 在**正实轴**上有**无穷多**零点
  <div class='proof'>
  
  * $J_\nu(x)$ 的零点数量可以从 $J_\nu(x \to \infty)$ 的 **$\cos$ 型**渐近行为看出
  * 由于连续函数 $J_\nu(x)$ 在正实轴有无穷多零点，根据**罗尔中值定理**，相邻零点之间必然有**斜率为零**的点

  </div>

  <div class='proof comment'>
  
  **罗尔中值定理**：若 $f$ 是在 $[a, b]$ 上连续，$(a,b)$ 可导的函数，且 $f(a) = f(b)$，则在 $(a, b)$ 上至少有一个点 $c$，使得 $f'(c) = 0$
  </div>


---
### 零点


- $J_\nu(x_0) = 0$ 的两种观点
  - 给定 $\nu$ **<red>求 $x_0$**：齐次第一类边界条件对 $x_0 = \sqrt{\lambda}\rho_0$ 的约束
    $\Rightarrow$ 总是有**无穷多个** $x_0$-解
  - 给定 $x_0$ **<red>求 $\nu$**：齐次第一类边界条件对 $\nu$ 的约束
    $\Rightarrow$ 总是有**无穷多个** $\nu$-解


---
### 零点
- 类似地，$J'_\nu(x_0) = 0$ 也有两种观点
  * 给定 $\nu$ **求 $x_0$**：齐次第二类边界条件对 $x_0 = \sqrt{\lambda}\rho_0$ 的约束
    $\Rightarrow$ 也有**无穷多个** $x_0$-解
  * 给定 $x_0$ **求 $\nu$**：齐次第二类边界条件对 $\nu$ 的约束
    $\Rightarrow$ 也有**无穷多个** $\nu$-解

---
### 零点

- **定理**：$J_\nu(x)$ 在 **<red>负实轴** 上的零点由**正**实轴上的零点确定，形成对称分布
  <div class='proof'>
  
  这是因为 $J_\nu(e^{\pi i }x) = e^{\pi i \nu} J_\nu(x)$，$\forall x > 0$，从而若 $x_0$ 是 $J_\nu(x_0) = 0$ 的解，则
  $$
  J(-x_0) = e^{\pi i \nu}J(x_0) = 0
  $$
  反之依然
  </div>


---
### 实性 (过于复杂不用考)

- 当 $\nu \in \mathbb{R}$，$x > 0$：$J_\nu(x)$ 保证是实数，但是 $J_{\nu}(-x) = e^{ i \pi \nu}J_\nu(x)$，从而
  $$
  \operatorname{Im}J_{\nu}(-x) = \sin(\pi \nu) J_\nu(x)
  $$
  - 当 $\nu \in \mathbb{Z}$，$J_{\nu}(-x) = (-1)^\nu J_\nu(x)$ 也是实数
  - 当 $\nu \notin \mathbb{Z}$，只有 $J_{\nu}(x) = 0 = J_{-\nu}(x)$ 才是实数




---
### 实性 (过于复杂不用考)

<center>

![width:900px](images/bessel_imag_contour_final.png)
</center>


---
### $\nu$-间递推关系

- **定理**：在四个柱函数 $J_\nu, N_\nu, H^{(1)}_\nu, H^{(2)}_\nu$ 中任取一个 **<green>记作 $Z_\nu$**，均满足 **<green>柱函数递推公式**
  $$
  \frac{d}{dx}[\purple{x^\nu Z_\nu(x)}] = \red{x^\nu Z_{\nu - 1}}
  , \qquad
  \frac{d}{dx}[\red{x^{-\nu} Z_\nu(x)}] = \purple{\stackrel{\downarrow}{-} x^{-\nu} Z_{\nu + 1}}
  $$
  <div class='proof'>
  
  **证明**
  利用 $J_\nu(x)$ 级数表达式暴力证明，由此也可以证明 $N_\nu(x)$ 也满足相同递推
  </div>
  <div class="proof comment">


  - 等号两边的 $x$ 幂次相同
  - $\nu$ 较低/较高的 $J$ 都可以是 $\nu$ 较高/较低的 $J$ 的导数

  </div>


---
### $\nu$-间递推关系
- **推论**: 递推关系的积分表述
  $$
  x^\nu Z_\nu(x) = \int^x x'^\nu Z_{\nu - 1}(x) dx', \qquad
  x^{-\nu} Z_\nu(x) = - \int^x x'^{-\nu} Z_{\nu + 1}(x) dx'
  $$
- **推论**: 分别选 $\nu = 1$，$\nu = 0$
  $$
  \frac{d}{dx}\Big(xJ_1(x)\Big) = xJ_0(x), \qquad\frac{d}{dx}J_0(x) = - J_1(x)
  $$

---

### $\nu$-间递推关系

- **推论**：$J_\nu$ 与 $J_{\nu + 1}$ 的**正**零点**相间**分布
  <div class="proof">

  **证明**

  - **第一递推**说明 $\red{x^{\nu + 1}J_\nu(x)}$ 是 $\purple{x^{\nu + 1} J_{\nu + 1}(x)}$ 的导数，
    $$
      \frac{d}{dx}[\purple{x^{\nu + 1} J_{\nu + 1}(x)}] = \red{x^{\nu + 1}J_\nu(x)}
    $$
    于是 $\purple{x^{\nu + 1} J_{\nu + 1}(x)}$ 的两个正零点之间必然有 $\red{x^{\nu + 1} J_{\nu}(x)}$ 的一个正零点，也就是 $J_\nu(x)$ 的一个正零点。
  </div>

---
### $\nu$-间递推关系

<div class='proof'>

**说明**

- 反过来，**第二递推**说明 $\purple{-x^{-\nu} J_{\nu + 1}(x)}$ 是 $\red{x^{-\nu} J_{\nu}(x)}$ 的导数，
  $$
    \frac{d}{dx}[\red{x^{-\nu} J_\nu(x)}] = \purple{- x^{-\nu} J_{\nu + 1}(x)}
  $$
  于是 $\red{x^{\nu} J_{\nu}(x)}$ 的两个正零点之间必然有 $\purple{- x^{\nu} J_{\nu + 1}(x)}$ 的一个正零点，也就是 $J_{\nu + 1}(x)$ 的一个正零点。
</div>

---
### $\nu$-间递推关系


<center>

<video width='900' src='media/videos/animations/2160p60/BesselJZeros.mp4' controls></video>
</center>

---
### $\nu$-间递推关系

- **推论**：考虑 $\nu > -1$，$J_\nu(x)$ 的 **<red>最小** 正零点比 $J_{\nu + 1}$ 的 **<red>最小**正零点更靠**左**
  <div class="proof">

  **证明**
  - 核心原因：原点是 $\purple{x^{\nu + 1}J_{\nu + 1}(x)}$ 的零点
  - 设 $x_1$ 为 $J_{\nu + 1}(x)$ 的 **<green>最小正零点**
  * 对于 $\nu > -1$，有 $\purple{x^{\nu + 1}J_{\nu + 1}(x)} \xrightarrow{x \to 0} 0$，即**原点是其零点**
  * $\red{x^{\nu + 1}J_\nu(x)}$ 作为 $\purple{x^{\nu + 1}J_{\nu + 1}(x)}$ 的导数，在原点和 $x_1$ 之间至少有一个**正零点**，从而 $J_\nu(x)$ 的最小正零点小于 $x_1$，更加靠左
  </div>

---
### $\nu$-间递推关系

<div class='proof comment'>

**$\nu \le -1$**

- 当 $\nu = -1$，$x^{\nu + 1} = \orange{x^0}$，$J_{\nu + 1}(x) = J_0(x)$，从而
  $$
  \purple{x^{\nu + 1}J_{\nu + 1}(x)} = \orange{x^0} J_0(x \to 0) = 1 \ne 0
  $$
* **缺乏原点作为零点**：$J_0(x)$ 的最小正零点左侧 **<red>不保证** 有 $J_{-1}(x)$ 的正零点
* 事实上 $J_{-1}(x) = - J_1(x)$，其最小正零点比 $J_0(x)$ 的**更靠右**
* 随着 $\nu \to -1$，$J_\nu(x)$ 的最小正零点向左移动，在 $\nu = -1$ 时**变成原点**，最小正零点由**第二正零点接管**

</div>


---
### $\nu$-间递推关系


<center>

<video width='900' src='media/videos/animations/2160p60/BesselJZerosToMinusOne.mp4' controls></video>
</center>

---
### $\nu$-间递推关系

- **推论**：**<green>柱函数等价递推公式**
  $$
  Z_{\nu - 1} + Z_{\nu + 1} = \frac{2\nu}{x} Z_\nu, 
  \qquad
  Z_{\nu - 1} - Z_{\nu + 1} = 2Z_\nu'
  $$

---
### $\nu$-间递推关系
<div class="proof">

- 递推关系
  $$
  \frac{d}{dx}[{x^\nu Z_\nu(x)}] = {x^\nu Z_{\nu - 1}}
  , \qquad
  \frac{d}{dx}[{x^{-\nu} Z_\nu(x)}] = {- x^{-\nu} Z_{\nu + 1}}
  $$
* 两个递推关系分别展开，除掉公因式 $x^\nu$、$x^{-\nu}$
  $$
  \purple{\nu x^{ - 1}Z_\nu} + \red{Z_{\nu}'} = Z_{\nu - 1}, 
  \qquad
  \stackrel{\downarrow}{-} \purple{\nu x^{ - 1}Z_\nu} + \red{Z_{\nu}'} = - Z_{\nu + 1}
  $$
* 作 **<red>差** 消去 $Z_\nu'$，或者作 **<green>和**，分别得到
  $$
  \red{\frac{2\nu}{x} Z_\nu = Z_{\nu - 1} + Z_{\nu + 1}} , \qquad
  \green{2Z_\nu' = Z_{\nu - 1} - Z_{\nu + 1}}
  $$
</div>


---
### $\nu$-间递推关系

- **<green>定义**：满足**柱函数递推公式**的函数称为 **<green>柱函数**
* 柱函数是 Bessel 方程的全体解的**子集**

  <div style='position:absolute;right:50px;top:-180px'>
  
  ![width:400px](media/images/figures/venn_bessel_cylinder.svg)
  </div>
  <div class="proof comment">

  **注意**

  Bessel 方程的解**不一定**是柱函数：$\tilde Z_\nu \coloneqq \nu J_\nu(x)$ 是 Bessel 方程的解，但 **<red>不是** 柱函数

  </div>

---

### $\nu$-间递推关系

- **定理**：柱函数递推关系可以导出 **Bessel 方程**

  <div class="proof">

  * 递推关系展开得到
    $$
    \nu x^{ - 1}Z_\nu + Z_{\nu}' = Z_{\nu - 1}, \quad
    - \nu x^{ - 1}Z_\nu + Z_{\nu}' = - \red{Z_{\nu + 1}}
    \tag{A}
    $$
  * 第一式令 $\nu \to \nu + 1$，
    $$
    \frac{\nu + 1}{x} \red{Z_{\nu + 1}} + \red{Z'_{\nu + 1}} = \purple{Z_\nu}
    \tag{B}
    $$
  * 第二式求导
    $$
    \frac{\nu}{x^2}\purple{Z_\nu} - \frac{\nu}{x}\purple{Z'_\nu}
    + \purple{Z''_\nu} =- \red{Z'_{\nu + 1}}
    \tag{C}
    $$
    
  </div>



---

### $\nu$-间递推关系


<div class="proof">

* 用 A, C 式将 **<red>$Z_{\nu + 1}$，$Z'_{\nu + 1}$** 表达成 $\purple{Z_\nu, Z'_\nu, Z''_\nu}$，代入 B 式，
  $$
  \frac{\nu + 1}{x} (\frac{\nu}{x} \purple{Z_\nu} -  \purple{Z'_\nu}) - (\frac{\nu}{x^2}  \purple{Z_\nu} - \frac{\nu}{x} \purple{Z'_\nu} + \purple{Z''_\nu}) =  \purple{Z_\nu}
  $$
* 化简得到 Bessel 方程，
  $$
  \purple{Z''_\nu} + \frac{1}{x} \purple{Z'_\nu} + (1 - \frac{\nu^2}{x^2}) \purple{Z_\nu} = 0
  $$

</div >



---
<!-- header: 整数阶柱函数 -->

<div class="twocols">

# 
# 整数阶柱函数

<p class="break"></p>

- 基本性质
- 本征值问题
- 广义傅里叶级数

</div>

---
### 基本性质
- 常见于柱坐标系的分离变量问题
* **整数阶** Bessel 函数的级数表达式：$\nu = m \in \mathbb{N}$
  $$
  J_m(x) = \sum_{k = 0 }^{+\infty} \frac{(-1)^k}{k!(k + m)!} \biggl(\frac{x}{2}\biggr)^{2k + m}
  $$
  <div class="proof">

  **说明**

  - $\Gamma(k + \nu + 1) = (k + m)!$

  </div>


---
### 基本性质

- 关于 $m$ 的**对称性** $J_{-m}(x) = (-1)^m J_m(x)$
  <div class='proof comment'>
  
  对于一般的 $\nu$，此性质不能推广
  
  </div>
* 关于 $x$ 的**对称性** $J_m(-x) = (-1)^m J_m(x)$
  <div class="proof comment">

  **说明**

  - $J_m(z)$ 是**单值**的，因此 $-x$ 不需要用 $e^{\pi i}x$ 来**强调** (<gray>~~要强调也不是不行~~)
  - 对于一般的 $\nu$ 有自然推广 $(-1)^m \to e^{\pi i \nu}$

  </div>



---


### 生成函数
- **<green>生成函数 (generating function)**/母函数
  $$
  \exp \left[{\frac{z}{2}(t - \frac{1}{t})}\right] 
  = \sum_{m = -\infty}^{+\infty}J_m(z)t^m 
  , \qquad t \in \mathbb{C}-\{0\} 
  $$
  <div class="proof comment">

  **说明**

  - 不做证明。注意求和取遍**所有整数 $m$**。
  
  - 给出母函数在 $t$ 的环状邻域 $0 < |t| < \infty$ 中的 **Laurent 展开**
  - **<red>坐标级数有无穷多个 $t^{-m}$ 项说明什么？**

  </div>

---
### 生成函数

- 母函数可以用来研究 $J_m(z)$ 的特殊求和恒等式：研究一些**特殊值**
* **<red>当 $z = 0$，$t = 1$，$t = i$ 时，可以得到什么样有趣的恒等式？**

---
### 生成函数

- 当 $z = 0$ 时，
  $$
  \sum_{m = -\infty}^{+\infty} J_m(0)t^m = J_0(0)t^0 = e^0 = 1 
  $$
- 当 $t = 1$ 时，
  $$
  \sum_{m = - \infty}^{+\infty} J_m(z) = J_0(z) + 2 \sum_{k = 1}^{+\infty} J_{2k}(z) = e^{0} = 1
  $$

---

### 生成函数
- 对生成函数的操作可以转化为对 $J_m$ 的操作：$z$ 导，$t$ 导，积分，乘积
* 指数的**导数**还是指数：**对 $z$ 求导**
  $$
  \begin{align*}
    \frac{d}{dz} e^{\frac{z}{2}(t - \frac{1}{t})}
    = \frac{1}{2} \biggl(t - \frac{1}{t}\biggr) \orange{e^{\frac{z}{2}(t - \frac{1}{t})}}
    = & \ \sum_{m \in \mathbb{Z}} J'_m(z)t^m \\
    \frac{1}{2} \biggl(t - \frac{1}{t}\biggr) \orange{\sum_{m \in \mathbb{Z}}J_m(z)t^m }
    = & \ \sum_{m \in \mathbb{Z}} J'_m(z)t^m \\
    \Rightarrow \frac{1}{2}(J_{m - 1}(z) - J_{m + 1}(z)) = & \ J'_m(z)
  \end{align*}
  $$
  <div class='proof comment'>
  
  柱函数递推公式之一
  </div>

---

### 生成函数
- 指数**积分**还是指数：对 **$z$ 求积分**，得 $J_m(z)$ 的 **<green>原函数 $\mathcal{J}_m(z)$**
  $$
  \begin{align*}
    C(t) + \purple{\frac{2}{t - 1/t}}\orange{e^{\frac{z}{2}(t - \frac{1}{t})}} = & \ \sum_{m \in \mathbb{Z}} \green{\int J_m(z) dz} \ t^m\\
    C(t) - \purple{2 t} \ \orange{\sum_{m \in \mathbb{Z}}J_m(z)t^m} \purple{\sum_{n = 0}^{+\infty}t^{2n}}  = & \
    \sum_{m \in \mathbb{Z}} \green{\mathcal{J}_m(z)} t^m \\
    \gray{M = 2n + m + 1:} \ C(t)  \orange{- 2\sum_{M \in \mathbb{Z}} \sum_{n \ge 0} J_{M - 2n - 1}(z)}t^M   = & \
    \sum_{M \in \mathbb{Z}} \orange{\mathcal{J}_M(z)} t^M 
  \end{align*}
  $$
  <div class='proof comment'>
  
  * **<red>为什么 $C$ 依赖 $t$？**
  </div>

---
### 生成函数

- **推论**：整数阶 Bessel 函数 $J_m(x)$ 的**原函数**
  $$
  \orange{\mathcal{J}_M(z)} = \int^z J_m(x)dx = \orange{-2 \sum_{n \ge 0}J_{M - 2n - 1}(z)} + \text{const}
  $$
  
---
### 生成函数

- 指数**乘法**还是指数
  $$
  \begin{align*}
  & e^{\frac{x}{2}(t - \frac{1}{t})}e^{\frac{y}{2}(t - \frac{1}{t})} 
  = \sum_{m \in \mathbb{Z}}\sum_{n \in \mathbb{Z}}J_m(x)J_n(y) t^{m + n}
   \\
  = & \ e^{\frac{x + y}{2}(t - \frac{1}{t})}
  = \sum_{M \in \mathbb{Z}} J_M(x + y) t^M
  \end{align*}
  $$
* **加法公式**：比较两侧 $t$ 的同幂次项得到 Bessel 函数的**加法公式**
  $$
  J_M(x + y) = \sum_{k \in \mathbb{Z}} J_k(x) J_{M - k}(y)
  $$


---
### 生成函数

- 围道积分从生成函数提取单个 $J_m(z)$：
  $$
  J_m(z) = \oint_0 \frac{dt}{2\pi i}\frac{1}{t} \frac{1}{t^m} e^{\frac{z}{2}(t - \frac{1}{t})}
  
  $$
* 圆围道积分重新参数化：$t = e^{i\varphi}$，$dt = de^{i \varphi} = i e^{i \varphi} d\varphi$
  $$
  J_m(z) = \int_{0}^{2\pi} \frac{d\varphi}{2\pi} e^{ i z \sin \varphi} e^{- i m \varphi}
  \stackrel{2\pi \text{周期}}{=} \int_{-\pi}^{\pi} \frac{d\varphi}{2\pi} e^{ i z \sin \varphi} e^{- i m \varphi}
  $$
  <div class='proof comment'>
  
  之前在介绍二维无界空间 $\nabla^2$-格林函数时用到
  $$
  J_0(x) = \int_0^{2\pi} \frac{d\varphi}{2\pi} e^{ix \cos \varphi}
  $$
  </div>


---
### 生成函数
- **推论**：对于 $\red{\boldsymbol{z \in \mathbb{R}}}$，利用三角不等式
  $$
  |J_m(z)| \le \int_{0}^{2\pi}\frac{d\varphi}{2\pi}
  |e^{iz \sin \varphi}| |e^{-i m \varphi}|
  = \int_{0}^{2\pi}\frac{d\varphi}{2\pi} = 1
  = 1
  $$

---
### 生成函数

- $J_m(x)$ 乘以函数 $f(x)$ 积分
  $$
  \int f(x) \purple{J_m(x)}dx = \int dx \purple{\int_{-\pi}^\pi\frac{d\varphi}{2\pi}
  e^{ix \sin \varphi} e^{-im\varphi}} f(x)
  $$
* 尝试交换积分顺序，先做 $x$ 再做 $\varphi$
  $$
  \int f(x) J_m(x) dx = \int_{-\pi}^{+\pi}\frac{d\varphi}{2\pi} e^{-i m \varphi} \green{\tilde f(\varphi)}
  , \qquad
  \green{\tilde f(\varphi) \coloneqq \int dx f(x)e^{i x \sin \varphi}}
  $$
  <div class='proof comment'>
  
  万一 $\tilde f(\varphi)$ 比较简单，则剩下的 $\varphi$ 积分就可以用各种方法计算
  </div>


---
### 生成函数

- 例子：考虑 $a, b > 0$，$f(x) = e^{-a x}$
  $$
  \int_0^{+\infty} e^{-a x}J_0(\purple{b x}) dx
  = \int_0^{+\infty} e^{-a x} \int_{-\pi}^{\pi} \frac{d\varphi}{2\pi} e^{i \purple{b x} \sin \varphi} d x
  $$
- 交换积分顺序：先做 $x$ 再做 $\varphi$
  $$
   \begin{align*}
     \int_{-\pi}^{\pi} \frac{d\varphi}{2\pi} 
     \orange{\int_0^{+\infty} e^{-a x} e^{i b x \sin \varphi} d x}
  &= \int_{-\pi}^{\pi} \orange{\frac{1}{a - ib \sin \varphi}}\frac{d \varphi}{2\pi}
   \end{align*}
  $$
- 这个积分可以通过留数方法计算，结果为：
  $$
  \int_{-\pi}^{\pi} \frac{1}{a - ib \sin \theta}\frac{d \theta}{2\pi} = \frac{1}{\sqrt{a^2 + b^2}}
  $$


---
### Sturm-Liouville 本征值问题

- 柱状区域**内部**拉普拉斯方程定解问题
  $$
  \nabla^2 u = 0, \qquad
  \alpha \frac{\partial u}{\partial \rho} + \beta u\bigg|_{\rho = a} = 0
  $$
  <div class='proof comment'>

  外边界采取**齐次第一二三类边界条件**: 没有边界没有非平凡的 $\varphi$ 依赖
  
  $0 \le \rho \le a$，$\alpha, \beta \ge 0$，不同时为零
  </div>
---

### Sturm-Liouville 本征值问题

- Laplace 方程 (稳定场) 分离变量得到**径向方程**与边界条件
  $$
  R''(\rho) + \frac{1}{\rho} R' + \biggl(\lambda - \frac{m^2}{\rho^2}\biggr) R = 0, \qquad m = 0, 1, 2, \cdots\\
  R(\rho = 0) = \begin{cases}
    \small{\text{有限}}, & m = 0 \\
    0, & m \ge 1
  \end{cases}, \qquad
  \alpha R' + \beta R \bigg|_{\rho = a} = 0
  $$
  <div class='proof comment'>
  
  * 这个 **<red>不是** Bessel 方程，因为有 $\lambda$ 项
  * 给定 $m$：$(0, a]$ 上的 **Sturm-Liouville 本征问题**，**<green>本征值 $\lambda$**，预期 $\lambda \ge 0$
    $$
    k(\rho) = \rho, \quad q(\rho) = \frac{m^2}{\rho}, \quad \green{\small{\text{权函数}} ~ w(\rho) = \rho} 
    $$
  </div>

---
### Sturm-Liouville 本征值问题
- 对于 $\lambda > 0$，改用 $\green{x = \sqrt{\lambda}\rho}$，得到**整数阶 Bessel 方程**
  $$
  y'' + \frac{1}{x} y' + \biggl(1 - \frac{m^2}{x^2}\biggr) y = 0
  $$
  解为 $R(\rho) = J_m(\sqrt{\lambda}\rho)$，$R(\rho) = N_m(\sqrt{\lambda}\rho)$
  <div class='proof comment'>
  
  $N_m(\sqrt{\lambda}\rho)$ 不满足自然边界条件，**<red>舍弃**
  </div>
- 对于 $\lambda = 0$，解**欧拉方程**：$R(\rho) = \green{\rho^m}, \rho^{-m}, \green{\rho^0}, \ln \rho$
  <div class='proof comment'>
  
  柱体内部：$\rho^{-m}$ 和 $\ln \rho$ 都不满足自然边界条件，**<red>舍弃**
  </div>

---
### Sturm-Liouville 本征值问题


- **外边界**的**齐次第一二三类边界条件**决定本征值的可能值以及存活的本征函数
  $$
  \alpha R' + \beta R \bigg|_{\rho = a} = 0
  $$
- 对于 $\lambda > 0$
  $$
  \alpha \sqrt{\lambda} J'_m(\sqrt{\lambda}a) + \beta J_m(\sqrt{\lambda}a) = 0
  $$
  <div class="proof comment">

  **说明**

  有**无穷多个解 $\lambda_{m1} < \lambda_{m2} < \cdots$**，因为 $J_m$ 与 $J'_m$ 的震荡衰减形态

  </div>

---
### Sturm-Liouville 本征值问题

- 对于 $\lambda = 0$，边界条件写成
  $$
  0 = \alpha R' + \beta R\bigg|_{\rho = a} = 
  \begin{cases}
    \alpha m a^{m-1} + \beta a^m, & R(\rho) = \rho^m & , m \ge 1 \\
    \beta, & R(\rho) = 1, & m = 0
  \end{cases}
  $$
  只可能是 $\beta = 0$ (第二类齐次边界) 同时 $m = 0$ 有解


---
### Sturm-Liouville 本征值问题

- $R(\rho)$ 函数作为 Sturm-Liouville 本征问题的本征函数，满足**正交性**
  $$
  \int_0^a R_{mi}(\rho) R_{mj}(\rho) \green{\underbrace{\rho}_{w(\rho)}} d\rho
  = \int_0^a J_m(\sqrt{\lambda_{mi}}\rho) J_m(\sqrt{\lambda_{mj}}\rho) \rho d\rho
  = 0, \quad i \ne j
  $$
- **完备性**：任意满足边界条件的函数 $f(\rho)$ 都可以展开成本征函数的线性组合
  $$
  f(\rho) = \sum_{i = 1}^{+\infty} f_{mi} J_m(\sqrt{\lambda_{mi}}\rho)
  $$
  <div class='proof comment'>
  
  $m$ 是固定的
  </div>




---
### 应用：柱状热传导问题求解

<center>

![width:700px](images/conducting-cylinder.png)

假设 $z$ 方向平移不变，求随时间变化的温度分布情况 $u(\rho, \varphi, t)$

</center>

---
### 应用：柱状热传导问题求解

- $z$-平移不变性：$u(\rho, \varphi, t)$
  <div class='proof comment'>
  
  本质是二维空间 + 1 维时间问题；但 $t$ **等效地**可以看成是第三个空间维度
  </div>
* 定解问题 (齐次第一类边界条件，初始条件有非平凡的 $\rho, \varphi$ 依赖)
  $$
  \begin{align*}
    & \ \frac{\partial u}{\partial t} - a^2 \nabla^2 u = 0
    \quad  u(\rho = \rho_0, \varphi, t) = 0, \quad
    u(\rho, \varphi, t = 0) = f(\rho, \varphi)
  \end{align*}
  $$

---
### 应用：柱状热传导问题求解

- 分离变量 $u(\rho, \varphi, t) = R(\rho)\Phi(\varphi)T(t)$, 
  $$
  \begin{align*}
    T'(t) + \lambda a^2 T(t) = & \ 0, \qquad
    \Phi''(\varphi) + m^2 \Phi(\varphi)  = 0 \\
    R'' + \frac{1}{\rho}R' + \biggl(\lambda - \frac{m^2}{\rho^2}\biggr)R = & \ 0
  \end{align*}
  $$
  <div class='proof comment'>
  
  - **两次**分离变量，**两个**分离常数：$\lambda, m^2$：时空分离产生 **Helmholtz 方程**
    $$
    \nabla^2 v(\rho, \varphi) + \lambda v(\rho, \varphi) = 0
    $$
  - $\lambda$ 刻画的 **<red>不是 $z$** 方向的平移不变性 (的偏离) ，而是时间方向
  - 第 7 章讨论过二维 $\nabla^2 u = 0$ 的极坐标系分离变量，对应这里 $\lambda = 0$
  </div>

---
### 应用：柱状热传导问题求解

- 单值性：$\Phi(\varphi) = e^{\pm im \varphi}$, $m = 0, 1, 2, \cdots$
* $R$ 方程是欧拉方程 ($\lambda = 0$) 或者 Bessel 方程 $(\lambda > 0)$，解为
  $$
  R_{mi}(\rho) = J_m(\sqrt{\lambda_{mi}}\rho)
  $$
  <div class='proof comment'>
  
  - $\rho = 0$ 处的自然边界条件选出 $J_m$ 而不是 $N_m$
  - $\rho = \rho_0$ 处的**齐次第一类边界条件**排除 $\lambda = 0$ 的解 $\rho^{\pm m}, 1, \ln \rho$
    
  其中 $\lambda_{mi}$ 通过 $\rho = \rho_0$ 的齐次第一类边界条件确定
  </div>
* $T_{mi}(t) = e^{- \lambda_{mi} a^2 t}$


---
### 应用：柱状热传导问题求解

- 一般解
  $$
  u(\rho, \varphi, t) = \sum_{m \in \mathbb{N}}\sum_i (A_{mi} \cos m\varphi+ B_{mi} \sin m\varphi) e^{- \lambda_{mi}a^2 t}
  $$
  <div class="proof comment">

  **说明**

  - $m = 0$ 时只有 $B_{0i}$ 一个有效的待定系数，$A_{0i}$ 没用，因为 $\sin 0 \varphi = 0$

  </div>
* $A, B$ 待定系数：用初始条件 $u(\rho, \varphi, t = 0) = f(\rho, \varphi)$ 确定
  

---
<!-- header: 虚宗量柱函数 -->

<div class="twocols">

# 
# 虚宗量柱函数

<p class="break"></p>

- 虚宗量 Bessel 函数
- 虚宗量 Hankel 函数
- 应用

</div>

---
### 虚宗量 Bessel 函数
- Bessel 方程
  $$
  y'' + \frac{1}{x} y' + \biggl(1 - \frac{\nu^2}{x^2}\biggr)y = 0
  $$
* 方程的宗量 $x$ 和 $\nu$ 可以均为**复数**
* 比较常用：$x \in \mathbb{R}$，**$x \in i \mathbb{R}$**


---

### 虚宗量 Bessel 函数

- 做 Wick rotation $\tau \coloneqq ix$，
  
  <center> 
  
  ![width:400px](images/Iv(x).png)

  $I_\nu(x) \coloneqq e^{- i \nu \pi/2}J_\nu(e^{\pi i/2}x), \qquad e^{\pi i/2} x \in i \mathbb{R}$
  </center>


---
### 虚宗量 Bessel 方程

- $I_\nu(x)$ 满足
  $$
  y'' + \frac{1}{x} y + \left({i^2 - \frac{\nu^2}{x^2}}\right)y = 0
  $$
  $$
  y'' + \frac{1}{x} y + \left({- 1 - \frac{\nu^2}{x^2}}\right)y = 0
  $$
  <div class="proof comment">

  **说明**

  被求导的不是 $J_\nu$ 的完整宗量：$I_\nu(x) \sim J_\nu(ix)$

  </div>



---

### 虚宗量 Bessel 函数

- $I_\nu(x)$ 的级数表达式
  $$
  I_\nu(x) = \sum_{k = 0}^{+\infty} \frac{1}{k!\Gamma(k + \nu + 1)} \biggl(\frac{x}{2}\biggr)^{2k + \nu}
  $$
  <div class="proof comment">

  **说明**

  $I_\nu(x)$ 的别称：变型 Bessel 函数，第一类虚宗量 Bessel 函数，第一类变型 Bessel 函数

  </div>

---

### 虚宗量 Bessel 函数
- **定理**：对于实数 $\nu$，$x$，$I_\nu(x)$ **单调增**函数
* **定理**：$I_0(x \to 0) = 1$，$I_m(x \to 0) = 0$，$m = 1, 2,3, \dots$
* **定理**：$I_{-m}(x) = I_m(x)$，$m = 0, 1,2, \dots$
* **定理**：$I_m(- x) = (-1)^m I(x)$，$m = 0,1,2, \dots$
* **定理**：递推公式
  $$
  \frac{d}{dx}[x^\nu I_\nu(x)] = x^\nu I_{\nu - 1}(x), \quad
  \frac{d}{dx}[x^{-\nu} I_\nu(x)] = x^{-\nu}I_{\nu + 1}(x)
  $$




---

### 虚宗量 Hankel 函数

- **<green>定义**：$\nu$ 阶虚宗量 **<green>Hankel 函数**
  $$
  K_\nu(x) = \frac{\pi}{2 \sin \pi \nu} (I_{-\nu}(x) - I_\nu(x))
  $$
  <div class="proof comment">

  **说明**

  别称：第二类虚宗量 Bessel 函数，第二类变型 Bessel 函数

  </div>
* **对称性**：$K_{-\nu}(x) = K_\nu(x)$
  <div class="proof comment">

  **说明**

  以后假设 $\operatorname{Re}\nu \ge 0$

  </div>




---

### 极限


- **0 极限**：
  $$
  \begin{align*}
    \lim_{x \to 0} I_\nu(x) = 0, \quad
  \lim_{x \to 0} K_\nu(x) = \infty, \quad \nu \not\in & \ \mathbb{N}\\
  \lim_{x \to 0}I_0(x) = 1, \quad \lim_{x \to 0} I_\nu(x) = 0, \quad \nu \in & \ \mathbb{N}_{> 0}\\
  \lim_{x \to 0}K_\nu(x) = \infty, \quad \nu \in & \ \mathbb{N}
  \end{align*}
  $$
  <div class="proof comment">

  **说明**

  柱内解抛弃 $K_\nu$，保留 $I_\nu$

  </div>



---

### 渐近行为


- **$\infty$ 渐近**：
  $$
  \begin{align*}
    I_\nu(x) \xrightarrow{x \to \infty} & \ \frac{e^x}{\sqrt{2\pi x}}, & \ - \frac{\pi}{2} <\operatorname{arg}x < \frac{\pi}{2} \\
    K_\nu(x) \xrightarrow{{x \to \infty}} & \ \sqrt{\frac{\pi}{2x}} e^{ - x}, & \
    - \pi < \operatorname{arg}x < \pi
  \end{align*}
  $$
  <div class="proof comment">

  **说明**

  柱内解抛弃 $I_\nu$，保留 $K_\nu$

  </div>



---

### 虚宗量 Hankel 函数


- **$\infty$ 渐近**：
  $$
  \begin{align*}
    I_\nu(x) \xrightarrow{x \to \infty} & \ \frac{e^x}{\sqrt{2\pi x}}, & \ - \frac{\pi}{2} <\operatorname{arg}x < \frac{\pi}{2} \\
    K_\nu(x) \xrightarrow{{x \to \infty}} & \ \sqrt{\frac{\pi}{2x}} e^{ - x}, & \
    - \pi < \operatorname{arg}x < \pi
  \end{align*}
  $$
  <div class="proof comment">

  **说明**

  柱内解抛弃 $I_\nu$，保留 $K_\nu$

  </div>


---
<!-- header: 柱函数应用 -->

### 导热圆柱体


- 边界条件与 $\varphi$ 无关：$u(\mathbf{r}) = u(\rho, z)$
  $$
  \begin{align*}
    & \ \nabla^2 u = \frac{1}{\rho} \frac{\partial}{\partial \rho} \bigg(\rho \frac{\partial u}{\partial \rho}\bigg) + \frac{\partial^2 u}{\partial z^2} = 0\\
    & \ \frac{\partial u}{\partial \rho}\bigg|_{\rho = a} = \frac{1}{k}q(z)\\
    & \ u(\rho, z = 0) = u(\rho, z = h) = u_0
  \end{align*}
  $$

---

### 导热圆柱体


- 边界条件齐次化：$u(\rho, z) = u_0 + v(\rho, z)$
  $$
  \begin{align*}
    & \ \nabla^2 v = \frac{1}{\rho} \frac{\partial}{\partial \rho} \bigg(\rho \frac{\partial v}{\partial \rho}\bigg) + \frac{\partial^2 v}{\partial z^2} = 0\\
    & \ \frac{\partial v}{\partial \rho}\bigg|_{\rho = a} = \frac{1}{k}q(z)\\
    & \ v(\rho, z = 0) = v(\rho, z = h) = 0
  \end{align*}
  $$
* 分离变量：$u(\rho, z) = R(\rho)Z(z)$
  $$
  \begin{align*}
    R'' + \frac{1}{\rho}R' - \lambda R = 0, \quad Z'' + \lambda Z = 0\\
    Z(0) = Z(h) = 0
  \end{align*}
  $$


---
### 导热圆柱体

- $Z$ 方向本征值与本征函数
  $$
  \lambda = \left({\frac{n\pi}{h}}\right)^2,
  \qquad
  Z_n(z) = \sin \left({\frac{n \pi}{h}z}\right), \qquad
  n \in \mathbb{N}_{> 0}
  $$



---
### 导热圆柱体

- $R$ 方向方程: $x \coloneqq \sqrt{\lambda}\rho$, $R(\rho) = \tilde R(x)$
  $$
  \tilde R''(x) + \frac{1}{x}\tilde R'(x) + i^2 \tilde R(x) = 0
  $$
  <div class="proof comment">

  **说明**

  相当于虚宗量 Bessel 方程，$\nu = 0$

  </div>
* $R$ 方向解
  $$
  R(\rho) = \{I_0 \left({\frac{n \pi}{\rho}}\right), K_0 \left({\frac{n\pi}{\rho}}\right)\}
  $$
  <div class="proof comment">

  **说明**

  其中 $K_0$ 被自然边界条件 $R(\rho = 0) < \infty$ 排除

  </div>

---
### 导热圆柱体

- $v$ 一般解
  $$
  v(\rho, z) = \sum_{n = 1}^{+\infty} A_n I_0(n\pi\rho/h) \sin \frac{n\pi}{h}z
  $$
* 边界条件约束
  $$
  A_n = \frac{1}{k} \frac{2I_1(n\pi a/h)}{n \pi} \int_0^hq(z) \sin \frac{n\pi}{h}z dz
  $$
* 最终解：$u = u_0 + v$


---
<!-- header: 半奇数阶柱函数 -->


---
<!-- header: 球贝塞尔函数 -->

bbb

---
