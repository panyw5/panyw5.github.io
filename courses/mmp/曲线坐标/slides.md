---
marp: true
theme: rose-pine-dawn-modern
paginate: true
_paginate: skip
size: 16:9
math: katex

---
<center>

# 正交曲线坐标下的分离变量
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

# 纲要
- 正交曲线坐标系
- 正交曲线坐标系的微分算符
- 3d 球坐标、柱坐标下的分离变量

---

# 正交曲线坐标系

---
### 坐标系
- **<red>什么是坐标系？**
- 考虑 **二维空间 $\mathbb{R}^2$**
- 为了描述、标记 $\mathbb{R}^2$ 中 (一些开集) 的点，使用 **<green>坐标系 (coordinate system)**

  <div class='proof comment'>

  **坐标系定义**

  用**两个**实参数，实现**尽可能一一对应**地描述 $\mathbb{R}^2$ 或其开集的点

  </div>

---
### 笛卡尔坐标系
- 常用坐标系：**<green>笛卡尔坐标系 $(x,y)$**
  - 一组坐标值 $(x,y)$ $\to$ 一个点
  * 一个点 $\to$ 一组坐标值 $(x,y)$
  * 适用范围：全 $\mathbb{R}^2$
* 直线坐标线与坐标网格

---
### 极坐标系
- 常用坐标系：**<green>极坐标系 $r, \varphi$**
  $$
  \green{x = r \cos \varphi, \quad y = r \sin \varphi}
  $$
  - 一组坐标值 $(r, \varphi)$ $\to$ 一个点
  - 一个点 (**<red>绝大多数情况**) $\to$ 一组坐标值 $(r, \varphi)$
    
    <div class='proof comment'>
    
    **极坐标的坐标奇点**
    
    原点对应 $(r = 0, \forall \varphi)$，一对多/**<red>非良定 (ill-defined)**。
    原点是极坐标的 **<green>坐标奇点 (coordinate singularity)**
    
    </div>

---
### 极坐标系

- 适用范围：(几乎) 全 $\mathbb{R}^2$
  
  <div class='proof comment'>
  
  **适用范围说明**
  
  如果不想考虑原点，则适用于 $\mathbb{R}^2 - \{0\}$
  
  </div>

- 坐标线与坐标网格：由**曲线**组成

---
### 极坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/PolarCoordinateLines.mp4" controls>
</video>


极坐标的坐标线
</center>

---
### 坐标系
- 几何空间：**客观存在**

  <div class='proof comment'>

  **几何空间例子**

  如 $S^1$，$\mathbb{R}^2$, $S^2$, $\mathbb{R}^3$

  </div>

- 几何空间中的**点**：客观存在
- 对几何空间的点的**坐标描述 (description)**：**<red>非客观存在**

  <div class='proof comment'>

  **坐标描述的非客观性**

  同一个点可以用 **<red>不同** 的坐标描述，选新坐标 **<red>不改变** 几何点、几何体的本质

  </div>

---
### 坐标系

- 坐标系 $\Rightarrow$ **坐标线**、**坐标网格**
- 不同坐标可以有效覆盖几何体的 **<red>不同**区域


---
### 坐标系: 奇点
- **极坐标系 $r, \varphi$**
- 原点 $(0, 0)$ 的极坐标 $(r = 0, \varphi)$：**<red>不唯一**
- $(x,y) \to (r,\varphi)$ 的Jacobi 矩阵在原点 **<red>退化 (非满秩)，行列式为零**
  $$
  \det \frac{\partial(x, y)}{\partial(r, \varphi)}
  = \det \begin{pmatrix}
    \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \varphi}\\
    \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \varphi}
  \end{pmatrix}
  = r \to 0
  $$
  反过来，Jacobi 逆矩阵**发散**
  $$
  \det \frac{\partial (r, \varphi)}{\partial (x,y)} = \frac{1}{r} \to +\infty
  $$

---
### 坐标系: 奇点
- 坐标奇点处，**<red>几何并没有奇性，是常点**

  <div class='proof comment'>

  **几何与坐标的区别**

  错的不是几何，是坐标

  <center>


  ![height:300](images/Xnip2024-11-20_07-36-56.png)
  </center>

  </div>



---
### 坐标系
- 考虑三维空间 $\mathbb{R}^3$
- 可以用直角坐标系 $\mathbf{r} \coloneqq (x, y, z)$ 标记 $\mathbb{R}^3$ 中任何一个点
- 坐标系选择 **<red>不唯一**
  - 直角坐标
  - 球坐标系
  - 柱坐标系
  - 椭球坐标系

---
### 坐标系
<center>

![width:700px](media/images/animations/SphericalCoordinate_ManimCE_v0.18.1.png)
</center>
<center>

球坐标 $(r, \theta, \varphi)$
</center>

---
### 坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/SphericalCoordinatesLines.mp4" controls>
</video>

球坐标的坐标线
</center>

---
### 坐标系
<center>

![width:800px](media/images/animations/CylindricalCoordinate_ManimCE_v0.18.1.png)
柱坐标
</center>

---
### 坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/CylindricalCoordinate.mp4" controls>
</video>

柱坐标
</center>

---
### 坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/CylindricalCoordinateLines.mp4" controls>
</video>

柱坐标的坐标线 ($\varphi$-线、$z$-线 与 $\rho$-线)
</center>

---
### 正交曲线坐标系
- 记新的坐标系的坐标为 $q_1, q_2, q_3$

  <div class='proof comment'>

  **$q$-坐标系**

  $q_i$ 是个**抽象名字**，指代第 $i$ 个坐标，简称为 **<green>$q$-坐标系**

  </div>
- 坐标线可能是**曲线**

---
### 正交曲线坐标系

- $q$-坐标与直角坐标之间的关系
  $$
  x = \green{x(q_1, q_2, q_3)}, \ 
  y = y(q_1, q_2, q_3), \
  z = z(q_1, q_2, q_3)
  $$
  或者用 **<green>矢量记号**
  $$
  \mathbf{r} = \mathbf{r}(q_1, q_2, q_3), \quad
  \mathbf{r} = \green{x(...)} \mathbf{e}_x + y(...) \mathbf{e}_y + z(...) \mathbf{e}_z
  $$

---
### 正交曲线坐标系
- 设 $q_1, q_2, q_3$ **<red>分别**发生**无穷小变化** $dq_i$，则相应的无穷小**位移**是
  $$
  \frac{\partial \mathbf{r}}{\partial q_1}dq_1, \qquad
  \frac{\partial \mathbf{r}}{\partial q_2}dq_2, \qquad
  \frac{\partial \mathbf{r}}{\partial q_3}dq_3
  $$
  
---
### 正交曲线坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/CoordinateSystem.mp4"
controls>
</video>

</center>

---

<div class='proof comment'>
  
**坐标线的切矢量**

$\partial \mathbf{r}/\partial q_i$ 相当于 $q_i$-坐标线的 **<red>切矢量**

$~$

<center>

![height:350px](images/coordinate-basis-1.png) ![height:350px](images/coordinate-basis-2.png)
</center>


</div>

---
### 正交曲线坐标系

<div class='proof comment'>

**坐标基底与无穷小位移**

* 当 $q_i$ **同时**发生无穷小变化，
  $$
  d\mathbf{r} = \sum_{i = 1}^{3} \green{\frac{\partial \mathbf{r}}{\partial q_i}}dq_i
  $$
* 三个偏导数 **<green>$\partial \mathbf{r}/\partial q_i$** 也称为 $q$-坐标系的 **<green>坐标基底 (coordinate basis)**

* 可以把坐标基底 **<green>$\partial \mathbf{r}/\partial q_i$** 具体的 **$x, y, z$ 分量**写出来
  $$
  \green{\frac{\partial \mathbf{r}}{\partial q_i}} = \frac{\partial x}{\partial q_i}\mathbf{e}_x + \frac{\partial y}{\partial q_i} \mathbf{e}_y + \frac{\partial z}{\partial q_i} \mathbf{e}_z
  $$

</div>

---
### 正交曲线坐标系

- **<green>定义**：如果坐标系在其覆盖区域内处处满足如下条件，则称为 **<green>正交曲线坐标系**
  $$
  \frac{\partial \mathbf{r}}{\partial q_i} \cdot \frac{\partial \mathbf{r}}{\partial q_j} = 0, \qquad i \ne j
  $$
  
  <div class='proof comment'>
  
  **正交性的几何意义**
  
  几何上看，这要求过任意**一点**的三条坐标线的 **切线** **相互正交**
  
  </div>

---
### 正交曲线坐标系
<center>

<video width="800" src="media/videos/animations/2160p60/OrthogonalCoordinateBasis.mp4" controls>
</video>

</center>

---
### 正交曲线坐标系
<center>

![width:800px](media/images/animations/NonOrthogonalCoordinateSystem_ManimCE_v0.18.1.png)
**<red>非正交**曲线坐标系
</center>

---
### 正交曲线坐标系
<div class='proof comment'>

**度规与度规矩阵**

- $q$-坐标系的坐标基矢内积时常被称为 **<green>度规 (metric)**、**<green>度规矩阵**
  $$
  \green{g_{ij} \coloneqq \frac{\partial \mathbf{r}}{\partial q_i} \cdot \frac{\partial \mathbf{r}}{\partial q_j}}
  \quad \Rightarrow \quad \green{[g_{ij}]}
  $$

* 对于 **正交** 曲线坐标系，度规矩阵是 **<red>对角** 的，
  $$
  [g_{ij}] = \begin{pmatrix}
  |\partial \mathbf{r}/\partial q_1|^2 & 0 & 0 \\ 0 & |\partial \mathbf{r}/\partial q_2|^2 & 0\\ 0&0& |\partial \mathbf{r}/\partial q_3|^2
  \end{pmatrix}
  $$

* 在讲义中，**<green>定义度规系数 $h_i^2 = |\partial \mathbf{r}/\partial q_i|^2$**
</div>

---
### 柱坐标系
- 柱坐标系 $(\rho, \varphi, z)$
  $$
  x = \rho \cos \varphi, \quad
  y = \rho \sin \varphi, \quad z = z
  $$
- 柱坐标系的矢量表达式，
  $$
  \mathbf{r} = \rho \cos \varphi \mathbf{e}_x + \rho \sin \varphi \mathbf{e}_y + z \mathbf{e}_z
  $$
- 偏导数 (坐标基底)
  $$
  \begin{align*}
    \frac{\partial \mathbf{r}}{\partial \rho} = & \ \cos \varphi \mathbf{e}_x + \sin \varphi \mathbf{e}_y
    & \ 
    \frac{\partial \mathbf{r}}{\partial \varphi} = & \ - \rho\sin \varphi \mathbf{e}_x + \rho \cos \varphi \mathbf{e}_y & 
    \frac{\partial \mathbf{r}}{\partial z} = & \ \mathbf{e}_z
  \end{align*}
  $$

---
### 柱坐标系
- 验证可得**正交性**
  $$
  \frac{\partial \mathbf{r}}{\partial \rho} \cdot \frac{\partial \mathbf{r}}{\partial \varphi}
  \ = \ \frac{\partial \mathbf{r}}{\partial \rho} \cdot \frac{\partial \mathbf{r}}{\partial z}
  \ = \ \frac{\partial \mathbf{r}}{\partial \varphi} \cdot \frac{\partial \mathbf{r}}{\partial z}
  = 0
  $$
- 对上述坐标基底进行**归一化**，**<green>定义 $\mathbf{e}_{\rho, \varphi, z}$**
  $$
  \begin{align*}
    \bigg| \frac{\partial \mathbf{r}}{\partial \rho} \bigg| = & \ 1 & \Rightarrow & \ \green{\mathbf{e}_\rho = \cos \varphi \mathbf{e}_x + \sin \varphi \mathbf{e}_y} \\
    \bigg| \frac{\partial \mathbf{r}}{\partial \varphi} \bigg| = & \ \rho & \Rightarrow & \ \green{\mathbf{e}_\varphi = - \sin \varphi \mathbf{e}_x +  \cos \varphi \mathbf{e}_y}\\
    \bigg| \frac{\partial \mathbf{r}}{\partial z} \bigg| = & \ 1 & \Rightarrow & \ \green{\mathbf{e}_z = \mathbf{e}_z}
  \end{align*}
  $$

---
### 球坐标系
- 球坐标系 $(r, \theta, \varphi)$
  $$
  x = r \sin \theta \cos \varphi, \quad
  y = r \sin \theta \sin \varphi, \quad
  z = r \cos \theta 
  $$
- 用矢量标记
  $$
  \mathbf{r} = r \sin \theta \cos \varphi \mathbf{e}_x + r \sin \theta \sin \varphi \mathbf{e}_y + r \cos \theta \mathbf{e}_z
  $$

---
### 球坐标系
- 偏导数 (坐标基底)
  $$
  \begin{align*}
    \frac{\partial \mathbf{r}}{\partial r}
  = & \ \sin \theta \cos \varphi \mathbf{e}_x + \sin \theta \sin \varphi \mathbf{e}_y + \cos \theta \mathbf{e}_z\\
    \frac{\partial \mathbf{r}}{\partial \theta}
  = & \ \red{r}\cos \theta \cos \varphi \mathbf{e}_x
  + \red{r}\cos \theta \sin \varphi \mathbf{e}_y
  - \red{r}\sin \theta \mathbf{e}_z
  \\
  \frac{\partial \mathbf{r}}{\partial \varphi} = & \ - r \red{\sin \theta}\sin \varphi \mathbf{e}_x + r \red{\sin \theta}\cos \varphi \mathbf{e}_y
  \end{align*}
  $$

---
### 球坐标系
<div class='proof'>

**验证球坐标系的正交性**

$$
\frac{\partial \mathbf{r}}{\partial r} \cdot \frac{\partial \mathbf{r}}{\partial \theta}
= r \sin \theta \cos \theta \cos \varphi \cos \varphi + r \sin \theta \cos \theta \sin \varphi \sin \varphi - r \sin \theta \cos \theta = 0
$$
$$
\frac{\partial \mathbf{r}}{\partial r} \cdot \frac{\partial \mathbf{r}}{\partial \varphi}
= r \sin \theta \cos \theta \cos \varphi (- \sin \varphi) + r \sin \theta \cos \theta \sin \varphi \cos \varphi = 0
$$
$$
\frac{\partial \mathbf{r}}{\partial \theta} \cdot \frac{\partial \mathbf{r}}{\partial \varphi}
= r \cos \theta \sin \theta \cos \varphi (- \sin \varphi) + r \cos \theta \sin \theta \sin \varphi \cos \varphi = 0
$$
</div>

---
### 球坐标系
- 三个坐标基底矢量的长度
  $$
  \bigg|\frac{\partial \mathbf{r}}{\partial r}\bigg| = 1, \quad
  \bigg|\frac{\partial \mathbf{r}}{\partial \theta}\bigg| = r, \quad
  \bigg|\frac{\partial \mathbf{r}}{\partial \varphi}\bigg| = \red{r\sin\theta}
  $$
- 对坐标基底矢量进行归一化：**<green>定义 $\mathbf{e}_{r, \theta, \varphi}$**
  $$
  \begin{align*}
    \mathbf{e}_r = & \ \sin \theta \cos \varphi \mathbf{e}_x + \sin \theta \sin \varphi \mathbf{e}_y + \cos \theta \mathbf{e}_z\\
    \mathbf{e}_\theta = & \ \cos \theta \cos \varphi \mathbf{e}_x + \cos \theta \sin \varphi \mathbf{e}_y - \sin \theta \mathbf{e}_z\\
    \mathbf{e}_\varphi = & \ - \sin \varphi \mathbf{e}_x + \cos \varphi \mathbf{e}_y
  \end{align*}
  $$


---

# 正交曲线坐标系的微分算符

---
### 梯度
- 下面研究曲线坐标系下常见微分算符的具体形式
- 梯度 $\nabla$、拉普拉斯算符 $\nabla^2$：作用在**函数**上
- 散度 $\nabla \cdot$、旋度 $\nabla \times$：作用在**矢量场**上
  > $\nabla^2 = \nabla \cdot \nabla$

---
### 梯度
- 任意曲线坐标系 $(q_1, q_2, q_3)$
- **<green>定义**：**正交归一**基底 $\mathbf{e}_i$
  $$
  \mathbf{e}_i = \frac{1}{|\partial \mathbf{r}/\partial q_i|} \frac{\partial \mathbf{r}}{\partial q_i}, \qquad
  \bigg|\frac{\partial \mathbf{r}}{\partial q_i}\bigg|^2 = \frac{\partial \mathbf{r}}{\partial q_i} \cdot \frac{\partial \mathbf{r}}{\partial q_i}
  $$

  <div class='proof comment'>

  **度规系数与基底矢量**

  * 模方 $|\partial \mathbf{r}/\partial q_i|^2 = h_i^2$ 即为 **<green>度规系数**

  * 笛卡尔坐标系的坐标基底矢量是 $\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z$，不应与一般 $q$-坐标系的 $\mathbf{e}_i$ **<red>混淆**

  </div>

---
### 梯度
- 三维矢量空间的**基底**：任意矢量都可以用 **<red>正交归一基底 $\mathbf{e}_i$** 展开
  $$
  \mathbf{v} = \sum_{i=1}^{3}v_i \mathbf{e}_i 
  $$
  $$
  \gray{(利用正交归一确定系数)}\quad \Rightarrow v_i = \mathbf{e}_i \cdot \mathbf{v}
  $$
  
  <div class='proof comment'>
  
  **展开系数的唯一性**
  
  一旦选定 $\mathbf{e}_i$，矢量 $\mathbf{v}$ 的展开系数 $v_i$ 是 **<red>定死** 的
  
  </div>

---
### 梯度
- 任意函数 $u$ 的 **<green>梯度 $\nabla u$** 是一个**矢量 (场)**
  $$
  \green{\nabla u}  =
    \frac{\partial u}{\partial x}\mathbf{e}_x 
    + \frac{\partial u}{\partial y} \mathbf{e}_y
    + \frac{\partial u}{\partial z}\mathbf{e}_z 
  $$
  
  <div class='proof comment'>
  
  **梯度算符的作用**
  
  函数 $u$ 的梯度可以看成是 **<green>微分算符 $\nabla = \mathbf{e}_x \partial_x + \mathbf{e}_y \partial_y + \mathbf{e}_z \partial_z$** **从左侧** **向右** 作用在 $u$ 上
  $$
  \nabla u = \bigg(
  \mathbf{e}_x \frac{\partial}{\partial x}
  + \mathbf{e}_y\frac{\partial}{\partial y} 
  + \mathbf{e}_z \frac{\partial}{\partial z}
  \bigg)u
  $$
  
  </div>

---
### 梯度
- 在 $q$-坐标系用 $q_i$-坐标正交归一基底 **<red>重新** 做展开
  $$
  \nabla u = \sum_{i = 1}^{3} (\purple{\mathbf{e}_i \cdot \nabla u}) \mathbf{e}_i
  $$
- 计算系数 $\purple{\mathbf{e}_i \cdot \nabla u}$：代入 $\mathbf{e}_i$ 与 $\partial \mathbf{r}/\partial q_i$ 的关系
  $$
  \green{\mathbf{e}_i} \cdot \nabla u
  = \green{\frac{1}{|\partial \mathbf{r}/\partial q_i|}} \left[{\green{\frac{\partial \mathbf{r}}{\partial q_i}} \cdot \nabla u}\right]
  $$
- **<red>$\frac{\partial \mathbf{r}}{\partial q_i} \cdot \nabla u$ 具体是什么？**

---

### 梯度
- **<red>$\frac{\partial \mathbf{r}}{\partial q_i} \cdot \nabla u$ 具体是什么？** 用直角坐标系详细书写
  $$
  \frac{\partial \mathbf{r}}{\partial q_i} = \frac{\partial x}{\partial q_i}\mathbf{e}_x + \frac{\partial y}{\partial q_i} \mathbf{e}_y + \frac{\partial z}{\partial q_i} \mathbf{e}_z
  $$
  $$
  \nabla u = \frac{\partial u}{\partial \mathbf{r}} = \frac{\partial u}{\partial x}\mathbf{e}_x
    + \frac{\partial u}{\partial y} \mathbf{e}_y
    + \frac{\partial u}{\partial z} \mathbf{e}_z
  $$

---
### 梯度
- 做点乘
  $$
  \frac{\partial \mathbf{r}}{\partial q_i} \cdot \nabla u = \frac{\partial x}{\partial q_i} \frac{\partial u}{\partial x}
  + \frac{\partial y}{\partial q_i} \frac{\partial u}{\partial y}
  + \frac{\partial z}{\partial q_i} \frac{\partial u}{\partial z}
  $$
* 右边：其实是 (复合函数偏导)
  $$
  = \frac{\partial u}{\partial q_i}
  $$

<!-- ---
### 梯度
- 点乘的结果：**复合函数求导** (链式法则)
  $$
  \frac{\partial \mathbf{r}}{\partial q_i} \cdot \green{\nabla u} = \frac{\partial u}{\partial q_i}
  = \frac{\partial \mathbf{r}}{\partial q_i} \cdot \green{\frac{\partial u}{\partial \mathbf{r}}}
  $$
  
  <div class='proof comment'>
  
  **链式法则与现代微分几何**
  
  * $\partial u/\partial \mathbf{r}$ 这个符号使得链式法则更加明显
  
  * 现代微分几何：$q_i \to x^\mu$, $\partial \mathbf{r}/\partial q_i \to \partial/\partial x^\mu$
    $$
    \frac{\partial \mathbf{r}}{\partial q_i} \cdot \nabla u
    \quad\to\quad \left({\frac{\partial}{\partial x^\mu}}\right)^\nu \nabla_\nu u
    = \frac{\partial u}{\partial x^\mu}
    $$
  
  </div> -->

---
### 梯度
- $\mathbf{e}_i \cdot \nabla u$ 可以写成
  $$
  \purple{\mathbf{e}_i \cdot \nabla u}
  = \frac{1}{|\partial \mathbf{r}/\partial q_i|} \red{\frac{\partial \mathbf{r}}{\partial q_i} \cdot \nabla u}
  = \frac{1}{|\partial \mathbf{r}/\partial q_i|} \red{\frac{\partial u}{\partial q_i}}
  $$
- $\nabla u$ 可以写成
  $$
    \nabla u = \sum_{i = 1}^{3} \purple{(\mathbf{e}_i \cdot \nabla u)} \mathbf{e}_i
    = \sum_{i = 1}^{3} \left({\purple{\frac{1}{|\partial \mathbf{r}/\partial q_i|} \frac{\partial u}{\partial q_i}}}\right) \green{\mathbf{e}_i}
  $$
  
  <div class='proof comment'>
  
  **公式应用**
  
  后面将会用这个公式书写不同坐标系下的 $\nabla u$
  
  </div>

---
### 梯度
<div class='proof comment'>

**梯度的进一步改写**

- 还可以进一步改写 $\nabla$，代入 $\mathbf{e}_i$ 的定义 $\green{\mathbf{e}_i = |\frac{\partial \mathbf{r}}{\partial q_i}|^{-1} \frac{\partial \mathbf{r}}{\partial q_i}}$
$$
\nabla u = \sum_{i = 1}^{3} \left({\purple{\frac{1}{|\partial \mathbf{r}/\partial q_i|} \frac{\partial u}{\partial q_i}}}\right) \green{\mathbf{e}_i}
= \sum_{i = 1}^{3} \frac{1}{\green{|\partial \mathbf{r}/\partial q_i|}^2} \frac{\partial u}{\partial q_i} \green{\frac{\partial \mathbf{r}}{\partial q_i}}
$$
</div>

---
### 梯度
<div class='proof comment'>

**全微分与坐标变换**

- 考虑 $d \mathbf{r} = (dx, dy, dz)$，得到 **<green>全微分**
  $$
  du = \nabla u \cdot d\mathbf{r} = \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy + \frac{\partial u}{\partial z}dz
  $$

- 在曲线坐标系下，
  $$
  \nabla u = \sum_{i = 1}^{3} \frac{1}{|\partial \mathbf{r}/\partial q_i|^2} \frac{\partial u}{\partial q_i} \frac{\partial \mathbf{r}}{\partial q_i},\qquad d\mathbf{r} = \sum_{j = 1}^{3} \frac{\partial \mathbf{r}}{\partial q_j}dq_j,
  $$

</div>

---
### 梯度

<div class='proof comment'>


- 乘起来
  $$
  \nabla u \cdot d\mathbf{r} = \sum_{i, j = 1}^{3} \frac{1}{\red{|\partial \mathbf{r}/\partial q_i|^2}} \frac{\partial u}{\partial q_i}
  \red{\frac{\partial \mathbf{r}}{\partial q_i} \cdot \frac{\partial \mathbf{r}}{\partial q_j}} dq_j
  = \sum_{i = 1}^{3} \frac{\partial u}{\partial q_i}dq_i = du
  $$
</div>

---
### 梯度
<div class='proof comment'>

**全微分的普遍性**

- 即不管什么正交曲线坐标系，都必然有
$$
  du = \sum_{i = 1}^{3} \frac{\partial u}{\partial q_i}dq_i
$$
事实上，上式对任意坐标系都成立，不仅仅是正交曲线坐标系。
</div>

---
### 梯度
- 柱坐标系 $(\rho, \varphi, z)$
  $$
  \begin{align*}
    \mathbf{e}_\rho \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial \rho|} \frac{\partial u}{\partial \rho}, \qquad & \bigg|\frac{\partial \mathbf{r}}{\partial \rho} \bigg| = & \ 1\\
    \mathbf{e}_\varphi \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial \varphi|} \frac{\partial u}{\partial \varphi}, \qquad & \bigg|\frac{\partial \mathbf{r}}{\partial \varphi}\bigg| = & \ \red{\rho}\\
    \mathbf{e}_z \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial z|} \frac{\partial u}{\partial z}, \qquad & \bigg|\frac{\partial \mathbf{r}}{\partial z}\bigg| = & \ 1
  \end{align*}
  $$
- 梯度
  $$
  \nabla u
  = \sum_{i = 1}^{3} \left(\frac{1}{|\partial \mathbf{r}/\partial q_i|} \frac{\partial u}{\partial q_i}\right) \green{\mathbf{e}_i}
  = \frac{\partial u}{\partial \rho} \mathbf{e}_\rho
  + \frac{1}{\red{\rho}}\frac{\partial u}{\partial \varphi}\mathbf{e}_\varphi
  + \frac{\partial u}{\partial z} \mathbf{e}_z
  $$

---
### 梯度
- 球坐标系 $(r, \theta, \varphi)$
  $$
  \begin{align*}
    \mathbf{e}_r \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial r|} \frac{\partial u}{\partial r}, & \bigg|\frac{\partial \mathbf{r}}{\partial r}\bigg| = & \ 1\\
    \mathbf{e}_\theta \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial \theta|} \frac{\partial u}{\partial \theta}, & \bigg|\frac{\partial \mathbf{r}}{\partial \theta}\bigg| = & \ \red{r} \\
    \mathbf{e}_\varphi \cdot \nabla u = & \ \frac{1}{|\partial \mathbf{r}/\partial \varphi|} \frac{\partial u}{\partial \varphi}, & \bigg|\frac{\partial \mathbf{r}}{\partial \varphi}\bigg| = & \ \red{r\sin\theta}
  \end{align*}
  $$
- 梯度
  $$
  \nabla u
  = \sum_{i = 1}^{3} \left(\frac{1}{|\partial \mathbf{r}/\partial q_i|} \frac{\partial u}{\partial q_i}\right) \green{\mathbf{e}_i}
  = \frac{\partial u}{\partial r}\mathbf{e}_r
  + \frac{1}{\red{r}}\frac{\partial u}{\partial \theta} \mathbf{e}_\theta
  + \frac{1}{\red{r\sin\theta}}\frac{\partial u}{\partial \varphi} \mathbf{e}_\varphi
  $$

---
### 梯度
- 直角坐标系下梯度
  $$
  \nabla u = \mathbf{e}_x \frac{\partial u}{\partial x}
  + \mathbf{e}_y \frac{\partial u}{\partial y}
  + \mathbf{e}_z \frac{\partial u}{\partial z}
  $$
- 柱坐标系下的梯度
  $$
  \nabla u = \frac{\partial u}{\partial \rho} \mathbf{e}_\rho
  + \frac{1}{\rho}\frac{\partial u}{\partial \varphi}\mathbf{e}_\varphi
  + \frac{\partial u}{\partial z} \mathbf{e}_z
  $$
- 球坐标系下的梯度
  $$
  \nabla u = \frac{\partial u}{\partial r}\mathbf{e}_r
  + \frac{1}{r}\frac{\partial u}{\partial \theta} \mathbf{e}_\theta
  + \frac{1}{r\sin\theta}\frac{\partial u}{\partial \varphi} \mathbf{e}_\varphi
  $$

---
### 梯度
- 给定一个 $u$：上面三个 $\nabla u$ 处处**相等**

---
### 梯度算符
- $\nabla$ 的使命：把函数 $u$ 变成一个矢量场 $\nabla u$
- 通过**求导**的方式，把数学对象变成其它数学对象的东西，称为 **<green>微分算符 (differential operator)**
- 其它常见微分算符
  $$
  \frac{d}{dx}, \quad \frac{\partial}{\partial x}, \quad
  d, \quad \nabla \cdot, \quad \nabla \times, \quad
  \partial_x, \quad \partial_y, \quad\dots
  $$
  > $d u = \frac{du}{dx}dx$
- **梯度算符 $\nabla$** 是一个比较简单的微分算符

---
### 梯度算符
- 直角坐标系下梯度**算符**
  $$
  \nabla = \mathbf{e}_x \frac{\partial}{\partial x}
  + \mathbf{e}_y \frac{\partial}{\partial y}
  + \mathbf{e}_z \frac{\partial}{\partial z}
  $$
- 柱坐标系下的梯度**算符**
  $$
  \nabla = \mathbf{e}_\rho\frac{\partial }{\partial \rho}
  + \mathbf{e}_\varphi\frac{1}{\rho}\frac{\partial }{\partial \varphi}
  + \mathbf{e}_z\frac{\partial }{\partial z}
  $$
- 球坐标系下的梯度**算符**
  $$
  \nabla = \mathbf{e}_r\frac{\partial}{\partial r}
  + \mathbf{e}_\theta \frac{1}{r}\frac{\partial}{\partial \theta}
  + \mathbf{e}_\varphi \frac{1}{r\sin\theta}\frac{\partial}{\partial \varphi}
  $$

---
### 梯度算符
- **同一个**梯度算符 $\nabla$，用不同坐标系书写
- 这些微分算符**从左侧向右作用**到函数上
  $$
  \begin{align*}
    \nabla u = & \ \left({\mathbf{e}_x \frac{\partial}{\partial x}
  + \mathbf{e}_y \frac{\partial}{\partial y}
  + \mathbf{e}_z \frac{\partial}{\partial z}}\right)u \\
    = & \ \left({\mathbf{e}_\rho\frac{\partial }{\partial \rho} 
  + \mathbf{e}_\varphi\frac{1}{\rho}\frac{\partial }{\partial \varphi}
  + \mathbf{e}_z\frac{\partial }{\partial z} }\right)u \\
    = & \ \left(\mathbf{e}_r\frac{\partial}{\partial r}
  + \mathbf{e}_\theta \frac{1}{r}\frac{\partial}{\partial \theta}
  + \mathbf{e}_\varphi \frac{1}{r\sin\theta}\frac{\partial}{\partial \varphi}\right)u
  \end{align*}
  $$

---
### 拉普拉斯算符
- **<green>定义**：**<green>拉普拉斯算符 $\nabla^2$** 为
  $$
  \nabla^2 u \coloneqq \nabla \cdot (\nabla u)
  = \partial_x \partial_x u + \partial_y \partial_y u + \partial_z \partial_z u
  $$
  
  <div class='proof comment'>
  
  **拉普拉斯算符的作用顺序**
  
  $u$ 先被 $\nabla$ **作用**，然后再被 $\nabla \cdot$ **作用**
  
  </div>

---
### 拉普拉斯算符
- 柱坐标系
  $$
  \begin{align*}
    \nabla^2 \purple{u} = & \ \left({\mathbf{e}_\rho\frac{\partial }{\partial \rho} 
    + \mathbf{e}_\varphi \frac{1}{\rho}\frac{\partial }{\partial \varphi}
    + \mathbf{e}_z\frac{\partial }{\partial z} }\right)\cdot \left({
      \mathbf{e}_\rho\frac{\partial \purple{u}}{\partial \rho} 
    + \mathbf{e}_\varphi\frac{1}{\rho}\frac{\partial \purple{u}}{\partial \varphi}
    + \mathbf{e}_z\frac{\partial \purple{u}}{\partial z}
    }\right)
  \end{align*}
  $$
- **<red>不能**直接做矢量乘法来计算，求导算符 **<red>向右** 作用，应考虑 $\mathbf{e}_i$ 的导数
  $$
  \red{\frac{\partial}{\partial \varphi} \mathbf{e}_\varphi} = - \mathbf{e}_\rho, \qquad
  \purple{\frac{\partial}{\partial \varphi} \mathbf{e}_\rho} = \mathbf{e}_\varphi
  $$


---
### 拉普拉斯算符
<center>

<video width="720" src='media/videos/animations/1080p60/CylindricalCoordinateBasisVectors.mp4' controls></video>

$e_\varphi, e_\rho$ 随 $\varphi$ 改变
</center>


---
### 拉普拉斯算符
<center>

<video width="720" src='media/videos/animations/1080p60/DerivativeOfOrthonormalBasisPolarCoordinates.mp4' controls></video>

</center>

---
### 拉普拉斯算符
- 拉普拉斯算符
  $$
  \nabla^2 u = \frac{1}{\rho} \frac{\partial}{\partial \rho} \left({\rho \frac{\partial u}{\partial \rho}}\right) + \frac{1}{\rho^2}\frac{\partial^2 u}{\partial \varphi^2} + \frac{\partial^2 u}{\partial z^2}
  $$
  <div class='proof'>

  **柱坐标系拉普拉斯算符推导**

  直接验证。展开
  $$
  \begin{align*}
    & \ \frac{\partial^2 u}{\partial \rho^2} + \frac{1}{\rho^2} \frac{\partial^2 u}{\partial \varphi^2}
    + \frac{\partial^2 u}{\partial z^2}
    + \mathbf{e}_\varphi \cdot \frac{1}{\rho} \purple{\partial_\varphi \mathbf{e}_\rho} \frac{\partial u}{\partial \rho}
    + \mathbf{e}_\varphi \cdot \frac{1}{\rho} \red{\partial_\varphi \mathbf{e}_\varphi} \frac{1}{\rho} \frac{\partial u}{\partial \varphi}\\
    & = \frac{\partial^2 u}{\partial \rho^2} + \frac{1}{\rho^2} \frac{\partial^2 u}{\partial \varphi^2}
    + \frac{\partial^2 u}{\partial z^2}
    + \frac{1}{\rho} \frac{\partial u}{\partial \rho} + 0
    = \frac{1}{\rho}\frac{\partial }{\partial \rho} \left({\rho \frac{\partial u}{\partial \rho}}\right)
    + \frac{1}{\rho^2}\frac{\partial^2 u}{\partial \varphi^2}
    + \frac{\partial^2 u}{\partial z^2}
  \end{align*}
  $$
  </div>

---
### 拉普拉斯算符
- 球坐标系
  $$
  \begin{align*}
    \nabla^2 u = & \ \bigg(
    \mathbf{e}_r\frac{\partial}{\partial r}
    + \mathbf{e}_\theta \frac{1}{r}\frac{\partial}{\partial \theta}
    + \mathbf{e}_\varphi \frac{1}{r\sin\theta}\frac{\partial}{\partial \varphi}
    \bigg)\\
    & \ \qquad\qquad \cdot \bigg(
      \mathbf{e}_r\frac{\partial u}{\partial r}
    + \mathbf{e}_\theta \frac{1}{r}\frac{\partial u}{\partial \theta}
    + \mathbf{e}_\varphi \frac{1}{r\sin\theta}\frac{\partial u}{\partial \varphi}
    \bigg)
  \end{align*}
  $$
- 正交归一基矢与位置有关
* 拉普拉斯算符
  $$
  \begin{align*}
    \nabla^2 u =\frac{1}{r^2} \frac{\partial}{\partial r}\bigg(r^2 \frac{\partial u}{\partial r}\bigg)
    + \frac{1}{r^2 \sin\theta} \frac{\partial}{\partial \theta}\bigg(\sin \theta \frac{\partial u}{\partial \theta}\bigg)
    + \frac{1}{r^2 \sin^2 \theta}\frac{\partial^2 u}{\partial \varphi^2}
  \end{align*}
  $$


<!-- header: 分离变量 -->
<div class="twocols">
# 
# 曲线坐标系分离变量
<p class="break"></p>
- 总体思路
- 球坐标下的分离变量
- 柱坐标下的分离变量
</div>

---

# 正交曲线坐标系下的分离变量

---
### 总体思路
- 三类方程的分离变量：波动、扩散和稳定场
- 把时间分出去都会得到空间部分的 Helmholtz 方程，
  $$
  \nabla^2 v(\mathbf{r}) + k^2 v(\mathbf{r}) = 0
  $$
  > 当 $k^2 = 0$，方程也称为 **<green>Laplace** 方程

---
### 总体思路
- 三维空间二阶偏微分方程的分离变量
- **球坐标** $(r, \theta, \varphi)$
  - 分离 $r$ 与 $(\theta, \varphi)$ $\to$ 分离 $\theta$ 和 $\varphi$
  - **径向**方程：**<green>Bessel** 方程或者 **<green>Euler** 方程
  - $\theta$ 向方程：**<green>Legendre** 方程或 **<green>associated Legendre** 方程
- **柱坐标** $(z, \rho, \varphi)$
  - 分离 $\varphi$ 与 $(z, \rho)$ $\to$ 分离 $z$ 和 $\rho$
  - **径向**方程：**<green>Bessel** 方程或者 **<green>Euler** 方程

---
### 波动方程
- 齐次波动方程
  $$
  \left({\frac{\partial^2}{\partial t^2} - a^2 \nabla^2 }\right)u = 0 \ .
  $$
- 假设 $u(\mathbf{r}, t) = v(\mathbf{r})T(t)$，则分离变量得到
  $$
  \nabla^2 v + k^2 v = 0, \qquad \frac{d^2}{dt^2}T(t) + k^2 a^2 T(t) = 0
  $$
  
  <div class='proof comment'>
  
  **分离常数的物理意义**
  
  其中 $k^2$ 是 **<green>分离常数**：具有 **<green>动量** 的物理含义
  
  </div>


---
### 波动方程
- 空间部分方程 $\nabla^2v + k^2v=0$ 称为 **<green>Helmholtz** 方程
- 通常 $k^2 \ge 0$
  
  <div class='proof comment'>
  
  **负分离常数的非物理性**
  
  倘若 $k^2 < 0$，则
  $$
  T(t) = e^{\pm i |k|a t}
  $$
    
  导致 $T(t)$ 的 **<red>指数衰减或者膨胀**行为，而非**震荡行为**，一般认为不符合波动的特性，**<red>非物理**
  
  </div>

---
### 输运、扩散、热传导方程
- 热传导、输运方程
  $$
  \frac{\partial u}{\partial t} - a^2 \nabla^2 u = 0
  $$
- 假设 $u(\mathbf{r}, t) = v(\mathbf{r})T(t)$，则分离变量得到
  $$
  \nabla^2 v + k^2 v = 0, \qquad \frac{d}{dt}T(t) + k^2 a^2 T(t) = 0
  $$
- 空间部分：**<green>Helmholtz** 方程，$k^2 \ge 0$ 
  
  <div class='proof comment'>
  
  **负分离常数的非物理性**
  
  $k^2 < 0$ 会导致 $T(t)$ 的 **<red>指数膨胀**行为，一般认为 **<red>非物理**
  
  </div>

---
### 稳定场
- 稳定场方程就是 Laplace 方程，也是 Helmholtz 方程的特例

---
### 球坐标下 Helmholtz 方程分离变量
- 球坐标下方程完整形式
  $$
  \frac{1}{r^2} \frac{\partial}{\partial r} \left({r^2 \frac{\partial u}{\partial r}}\right)
  + \frac{1}{r^2 \sin \theta}\frac{\partial}{\partial \theta} \left({\sin\theta \frac{\partial u}{\partial \theta}}\right)
  + \frac{1}{r^2\sin^2 \theta}\frac{\partial^2 u}{\partial \varphi^2} + \purple{k^2 u} = 0
  $$
- 分离变量流程：
  
  (1) 先分离径向坐标 $r$ 与 角向坐标 $(\theta, \varphi)$
  
  (2) 再分离 $\theta$ 和 $\varphi$

---
### 球坐标下 Helmholtz 方程分离变量
- 方程同乘 $r^2$
- 代入 $u(\mathbf{r}) = R(r)Y(\theta, \varphi)$，把 $\purple{k^2}$ 项归入 **<red>径向** 部分
  $$
  \frac{d}{dr} \left({r^2 \frac{dR}{dr}}\right) + \purple{k^2 r^2 R} = \green{\lambda} R
  $$
  $$
  \frac{1}{\sin \theta}\frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial Y}{\partial \theta}}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial \varphi^2} = - \green{\lambda} Y
  $$
  
  <div class='proof comment'>
  
  **第一个分离常数**
  
  **<green>$\lambda$** 是**第一个**分离常数
  
  </div>

---
### 球坐标下 Helmholtz 方程分离变量
- 径向方程除以 $r^2$
  $$
  \frac{1}{r^2}\frac{d}{dr} \left({r^2 \frac{dR}{dr}}\right) + \left({k^2 - \frac{\lambda}{r^2} }\right)R = 0
  $$
- 重写为
  $$
  \frac{1}{\red{k^2}}\frac{d}{dr}\bigg(\red{k^2} r^2 \frac{dR}{dr} \bigg) + \left({k^2 r^2 - \lambda}\right)R = 0
  $$

---
### 球坐标下 Helmholtz 方程分离变量
- 吸收 $k^2$，**重归一化** **<green>$x = kr$**，**<green>$\tilde R(x) \coloneqq R(r = x/k)$**
  $$
  \frac{d}{dx} \left({x^2 \frac{d \tilde R}{dx}}\right)
  + \left({x^2 - \lambda}\right)\tilde  R = 0
  $$

  <div class='proof comment'>

  此方程称为 **<green>球 Bessel 方程**；标准形式为
  $$
    x^2 y'' + 2x y' + (x^2 - \lambda)y = 0
  $$

  </div>

---
### 球坐标下 Helmholtz 方程分离变量
- 重定义 **<green>$y(x) \coloneqq \sqrt{x}\tilde R(x)$**，变成 $y$ 的方程，
  $$
  \frac{1}{x} \frac{d}{dx} \left({x\frac{dy}{dx}}\right)
  + \left({1 - \frac{\lambda + \frac{1}{4}}{x^2}}\right)y = 0
  $$

<div class='proof comment'>

**半奇数阶 Bessel 方程**

重新记 **<green>$\lambda = \ell (\ell + 1)$**，
$$
  \lambda + \frac{1}{4} = (\purple{\ell + \frac{1}{2}})^2, \qquad
  \frac{1}{x} \frac{d}{dx} \left({x\frac{dy}{dx}}\right)
  + \left({1 - \frac{(\purple{\ell + \frac{1}{2}})^2}{x^2}}\right)y = 0
$$
也称为 **<green>半奇数 $(\purple{\ell + \frac{1}{2}})$-阶 Bessel 方程**

</div>

---
### 球坐标下 Helmholtz 方程分离变量
- 角向方程
  $$
  \frac{1}{\sin \theta}\frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial Y}{\partial \theta}}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial \varphi^2} = - \green{\lambda} Y
  $$
- 角向进一步分离：$Y(\theta, \varphi) = \green{H(\theta) \Phi(\varphi)}$，$\lambda$ 归 $H$ 管，
  $$
  \frac{1}{\sin \theta}\frac{d}{d\theta} \left({\sin\theta \frac{dH}{d\theta}}\right)
  + \left({\lambda - \frac{\mu}{\sin^2 \theta}}\right) H = 0,
  \qquad
  \frac{d^2\Phi}{d\varphi^2} + \mu \Phi = 0
  $$
  
  <div class='proof comment'>
  
  **第二个分离常数**
  
  $\mu \in \mathbb{R}$ 是**第二个**分离常数
  
  </div>

---
### 球坐标下 Helmholtz 方程分离变量
<div class='proof'>

**球坐标 Helmholtz 方程分离：角向方程推导**

- 代入 $Y = H \Phi$，两边除以 $H\Phi$
  $$
  \frac{1}{H}\frac{1}{\sin \theta}\frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial H}{\partial \theta}}\right) + \frac{1}{\Phi} \red{\frac{1}{\sin^2 \theta}} \frac{\partial^2 \Phi}{\partial \varphi^2} = - \green{\lambda}
  $$
* 乘以 $\sin^2\theta$，
  $$
  \frac{1}{H}\sin \theta\frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial H}{\partial \theta}}\right)
  + \frac{1}{\Phi} \frac{\partial^2 \Phi}{\partial \varphi^2} = - \green{\lambda} \sin^2\theta
  $$

</div>


---
### 球坐标下 Helmholtz 方程分离变量

<div class='proof'>

- 移项，定义第二个 **<green>分离常数 $\mu$**，
  $$
  \frac{1}{H} \sin \theta \frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial H}{\partial \theta}}\right) + \green{\lambda} \sin^2\theta = - \frac{1}{\Phi} \frac{\partial^2 \Phi}{\partial \varphi^2} = \green{+ \mu}
  $$
</div>


---
### 球坐标下 Helmholtz 方程分离变量

<div class='proof'>

**分离后的角向方程**

- $H$ 的方程，除以 $\sin^2\theta$
  $$
  \frac{1}{H} \frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left({\sin \theta \frac{\partial H}{\partial \theta}}\right) + \green{\lambda} = + \frac{\mu}{\sin^2\theta}
  $$
* $\Phi$ 的方程
  $$
  \frac{1}{\Phi} \frac{\partial^2 \Phi}{\partial \varphi^2} = - \mu
  $$
</div>

---
### 球坐标下 Helmholtz 方程分离变量
- 两个分离常数 $\lambda, \mu$
- 边界条件用于确定 $\lambda, \mu$ 的可能值

---
### 球坐标下 Helmholtz 方程分离变量
- $\Phi$ 满足二阶线性常系数常微分方程，
  $$
  \Phi(\varphi) = A_+ e^{i \sqrt{\mu} \varphi} + A_- e^{-i \sqrt{\mu} \varphi}
  $$
  
  <div class='proof comment'>
  
  **$\mu = 0$ 的情形**
  
  $\mu = 0$ 时 $\Phi$ 是常函数
  
  </div>

---
### 球坐标下 Helmholtz 方程分离变量

- **<red>几何性**：$(r, \theta, \varphi)$ 与 $(r, \theta, \varphi + 2\pi)$ 是**同一个点**
- **<red>单值性**：$u$ 应该有**明确 (well-defined)** 的值，$\Phi$ 也应该有明确的值
- **<green>周期性**边界条件确定 $\mu$
  $$
  \begin{align*}
    & \ \Phi(\varphi + 2\pi) = \Phi(\varphi) \\ 
    \Rightarrow & \ \Phi(\varphi) = A_+ e^{ im \varphi} + A_- e^{- i m \varphi}, \qquad \green{\mu = m^2} \in \mathbb{N}
  \end{align*}
  $$

---
### 球坐标下 Helmholtz 方程分离变量
<center>

<video width="1000" src='media/videos/animations/1080p60/SingleValuenessInSphericalCoordinates.mp4' controls></video>

</center>

---
### 球坐标下 Helmholtz 方程分离变量
- $\theta$ 方向方程：变量替换 **<green>$x = \cos \theta$**，**<green>$P(x) \coloneqq H(\theta)$**，结合 $\mu = m^2$
  $$
  \begin{align*}
    \frac{1}{\sin \theta}\frac{d}{d\theta} \left({\sin\theta \frac{dH}{d\theta}}\right) + \left({\lambda - \frac{\mu}{\sin^2 \theta}}\right) H = 0\\
    \Rightarrow \qquad \frac{d}{dx}\bigg[(1 - x^2) \frac{dP}{dx}\bigg] + \bigg(\lambda - \frac{m^2}{1 - x^2}\bigg)P = 0
  \end{align*}
  $$
- 特殊点 $\theta = \red{0}, \green{\pi} \ \leftrightarrow \ x = \red{1}, \green{-1}$

---
### 球坐标下 Helmholtz 方程分离变量
- $\theta$ 方向函数 $Y(\theta)$ 应添加一些 **<green>自然边界条件**
  <div class='proof comment'>
  
  即人类根据朴素的物理直觉认为**理所应当**的一些边界条件
  </div>
- 选定 $\theta= 0, \pi$ <gray>(以及固定的 $r$)</gray>
  - 球面 $S^2_r$ 的 **北极**和**南极**，任何 $\varphi$ 值都对应 **<red>同一个点**
    <div class='proof comment'>
    
    $\theta = 0, \pi$ 的地方，即整条 **$z$ 轴** 都是球坐标 **<red>奇点**
    </div>
  - **<red>单值性**：同一点应该有确定的 $u$ 值

---
### 球坐标下 Helmholtz 方程分离变量
<center>

<video width="1000" src='media/videos/animations/1080p60/SingleValuenessInSphericalCoordinatesTheta.mp4' controls></video>

</center>

---
### 球坐标下 Helmholtz 方程分离变量
- 然而，当 $m \ne 0$
    $$
    Y(\theta = 0 ~ \text{or} ~ \pi, \varphi) = H(\theta = 0 ~ \text{or} ~ \pi)e^{\pm i m \varphi}
    $$
    $Y$ 却会跟 **随 $\varphi$ 变化**：这 **<red>不合理**，北极和南极 **<red>没有确定** 的 $Y$ 值
* 破局之道：
  * 当 $m \ne 0$ 时，强迫 $H(\theta = 0 \text{ or }\pi) = 0$
  * 当 $m = 0$ 时，只要求 $H(\theta = 0 \text{ or }\pi)$ **有限**
    
    <div class='proof comment'>
    
    **轴对称情形**
    
    **轴对称**会迫使 $m = 0$，因为 $u$ 与 **<red>$\varphi$ 无关**。一般问题的解中可能会有轴对称的**成分**
    
    </div>

---
### 球坐标下 Helmholtz 方程分离变量
- $\theta$ 方向方程与边界条件：
  $$
  \begin{align*}
    & \ \frac{d}{dx}\bigg[(1 - x^2) \frac{dP}{dx}\bigg] + \bigg(\lambda - \frac{m^2}{1 - x^2}\bigg)P = 0\\
    & \ P(\pm 1) = \left\{ \begin{array}{ll}
      0 & m \ne 0\\
      \text{有限} & m = 0
    \end{array} \right.
  \end{align*}
  $$
  
  <div class='proof comment'>
  
  **Legendre 方程与 associated Legendre 方程**
  
  当 $m = 0$，称为 **<green>勒让德 (Legendre)** 方程 
  
  当 $m \ne 0$，称为 **<green> 连带勒让德 (associated Legendre)** 方程
  
  </div>

- 第十章、第十一章介绍勒让德和连带勒让德函数：$\lambda, P(x)$ 将同时确定

---
### 球坐标下 Helmholtz 方程分离变量
<center>

![](images/image-1.png)
勒让德 (Adrien-Marie Legendre) (左) 与 傅里叶 (右)，作者 Julien-Léopold Boilly
Adrien-Marie Legendre 的唯一肖像
</center>

---
### 球坐标下 Helmholtz 方程分离变量
<center>

![height:400px](images/image-2.png)
Louis Legendre，法国政治家
百年乌龙：有长达 **<red>200 年** 时间被当成是 Adrien-Marie Legendre 的肖像
</center>

---
### 球坐标下 Helmholtz 方程分离变量

<div class='proof comment'>

**Legendre 方程标准形式**

Legendre 方程**标准形式**
$$
(1 - x^2)\frac{d^2 P}{dx^2} - 2x \frac{dP}{dx} + \lambda P = 0
$$
连带 (伴随) Legendre 方程**标准形式**
$$
(1 - x^2)\frac{d^2 P}{dx^2} - 2x \frac{dP}{dx} + \left({\lambda - \frac{m^2}{1 - x^2}}\right) P = 0
$$

</div>

---
### 柱坐标下 Laplace 方程分离变量
- **Laplace 方程**是 Helmholtz 方程的特例：$k^2 = 0$
- Laplace 方程完整形式
  $$
  \frac{1}{\rho}\frac{\partial}{\partial \rho} \left({\rho \frac{\partial u}{\partial \rho}}\right)
  + \frac{1}{\rho^2}\frac{\partial^2 u}{\partial \varphi^2}
  + \frac{\partial^2 u}{\partial z^2} = 0
  $$
- 分离 $(z, \rho)$ 与 $\varphi$：$u = R(\rho)\Phi(\varphi)Z(z)$
  $$
  \begin{align*}
    \frac{1}{R\rho} \frac{d}{d\rho} \bigg(\rho \frac{dR}{d\rho}\bigg) - \frac{\green{\mu}}{\rho^2} = & \  - \frac{1}{Z}\frac{d^2 Z}{dz^2} \\
    \frac{d^2\Phi}{d\varphi^2} + \green{\mu} \Phi =& \  0
  \end{align*}
  $$

---
### 柱坐标下 Laplace 方程分离变量
- 考虑圆柱内部的分离变量问题
  
  <div class='proof comment'>
  
  **圆柱内部区域**
  
  $\rho \le a$，$z_\text{min} \le z \le z_\text{max}$
  
  </div>

- 分离 $z, \rho$
  $$
  \begin{align*}
    \frac{1}{\rho} \frac{d}{d\rho} \left({\rho \frac{dR}{d\rho}}\right) - \frac{\mu}{\rho^2} R = & \ - \green{\lambda} R , \qquad
    \frac{d^2 Z}{dz^2} = & \ + \green{\lambda} Z
  \end{align*}
  $$

---
### 柱坐标下 Laplace 方程分离变量

<div class='proof comment'>

**$\lambda$ 的物理意义**

$\lambda$ 控制 **$z$-dependence**。
当 $\lambda =0$ 说明 $z$-轴平移不变性，问题退化为**二维**问题
当 $\lambda \ne 0$，问题是非平凡的 **三维** 问题

</div>

---
### 柱坐标下 Laplace 方程分离变量
- 边界条件控制 $\lambda, \mu$ 的可能取值
- **周期性** 边界条件
  $$
  \begin{align*}
    & \ \Phi(\varphi + 2\pi) = \Phi(\varphi) \\
    \Rightarrow & \ \Phi(\varphi) = e^{im\varphi}, \qquad \green{\mu = m^2} \in \mathbb{N}
  \end{align*}
  $$

---
### 柱坐标下 Laplace 方程分离变量
- 柱状区域的 **<green>外边界 $\rho = a$**：**第三类** 齐次边界条件
  $$
  \alpha \frac{dR(\rho)}{d\rho} + \beta R(\rho) \Bigg|_{\rho = a}= 0, \qquad \alpha, \beta \ge 0, ~ \alpha \beta > 0
  $$
  
  <div class='proof comment'>
  
  **第三类边界条件的来源**
  
  此条件可能来自 $u$ 的第三类齐次边界条件
  $$
    \alpha \frac{\partial u}{\partial \rho} + \beta u \Bigg|_{\rho = a} = 0
  $$
  当 $\alpha = 0$，退化为 **第一类** 齐次边界条件，当 $\beta = 0$，退化为 **第二类** 齐次边界条件
  
  </div>

---
### 柱坐标下 Laplace 方程分离变量
- $\rho$ 方向函数 $R(\rho)$ 还涉及 **<green>自然边界条件**
  
  <div class='proof comment'>
  
  **自然边界条件**
  
  即人类根据朴素的物理直觉认为理所应当的一些边界条件
  
  </div>


---
### 柱坐标下 Laplace 方程分离变量
- 选定 $\rho = 0$ <gray>(以及任意固定的 $z$)</gray>
  - **<green>中轴线**：任何 $\varphi$ 值都对应 **<red>同一个点**
    
    <div class='proof comment'>
    
    **柱坐标的坐标奇性**
    
    柱坐标的 **<red>坐标奇性**
    
    </div>

  - 然而，当 $m \ne 0$
    $$
    u(\rho = 0, \varphi, z) = R(\rho = 0)\red{e^{\pm i m \varphi}}Z(z)
    $$
    却会跟 **随 $\varphi$ 变化**：这 **<red>不合理**，$\rho = 0$ **<red>没有确定** 的 $u$ 值

---
### 柱坐标下 Laplace 方程分离变量
- **<green>自然边界条件**：
  - $m \ne 0$ 时，强迫 $R(\rho = 0) = 0$；
  - $m = 0$ 时，只要求 $R(\rho = 0)$ **有限**

---
### 柱坐标下 Laplace 方程分离变量
- $\rho$ 方向方程和边界条件
  $$
  \begin{align*}
    & \ \frac{1}{\rho} \frac{d}{d\rho} \left({\rho \frac{dR}{d\rho}}\right)
    + \left({\lambda - \frac{m^2}{\rho^2}}\right) R = 0 \\
    & \ R(\rho = 0) = \left\{ \begin{array}{ll}
      0 & m \ne 0\\
      \text{有限} & m = 0 
    \end{array} \right.\\
    & \ \alpha \frac{dR(\rho)}{d\rho} + \beta R(\rho) \Bigg|_{\rho = a}= 0
  \end{align*}
  $$
- $R(\rho)$ 的**外边界条件**和**中轴线自然边界条件**共同控制 $\lambda$ 的取值

---
### 柱坐标下 Laplace 方程分离变量
- $R$ 方程属于 **<green>Sturm-Liouville 问题**

  <div class='proof comment'>

  **Sturm-Liouville 问题标准形式**

  Sturm-Liouville 问题标准形式
  $$
  \frac{d}{dx} \left({\red{k(x)} \frac{dy}{dx}}\right) - \green{q(x)} y(x) + \lambda \purple{w(x)} y(x) = 0
  $$

  </div>

  $$
    \frac{1}{\rho} \frac{d}{d\rho} \left({\rho \frac{dR}{d\rho}}\right)
    + \left({\lambda - \frac{m^2}{\rho^2}}\right) R = 0  \quad  \Rightarrow \quad \frac{d}{d\rho} \left({\red{\rho} \frac{dR}{d\rho}}\right)
    - \green{\frac{m^2}{\rho}} R + \lambda \purple{\rho} R = 0
  $$

---
### 柱坐标下 Laplace 方程分离变量
- 对比读取系数函数
  $$
  \red{\rho \ge 0}, \quad 
  \green{\frac{m^2}{\rho} \ge 0}, \quad 
  \purple{\rho \ge 0}
  $$

---
### 柱坐标下 Laplace 方程分离变量
- **Sturm-Liouville 定理**：本征值 $\lambda \ge 0$
  
  <div class='proof comment'>
  
  **$\lambda$ 的分类处理**
  
  $\lambda = 0$ 与 $\lambda > 0$ 应 **<red>分开处理**
  
  </div>

---
### 柱坐标下 Laplace 方程分离变量
- 倘若 **$\lambda > 0$**，重定义 $x \coloneqq \sqrt{\lambda}\rho$，$y(x) \coloneqq R(\rho)$，得到 **<green>Bessel 方程** **标准形式**
  $$
  \begin{align*}
    & \ \frac{1}{x} \frac{d}{dx} \left({x\frac{dy}{dx}}\right)
  + \left({1 - \frac{m^2}{x^2}}\right) y = 0 \\
  \text{or} \quad & \ x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + \left({x^2 - m^2}\right)y = 0
  \end{align*}
  $$
  此方程为 **<green>$m$-阶 Bessel 方程</green>**
  
  <div class='proof comment'>

  
  回忆：球坐标系下分离变量的径向方程也是一种 Bessel 方程
  
  </div>

- 第十二章介绍 Bessel 函数

---
### 柱坐标下 Laplace 方程分离变量
- 倘若 **$\lambda = 0$**，则方程简化，
  
  <div class='proof comment'>
  
  **$z$-平移不变的成分**
  
  对应 $z$-平移不变的成分
  
  </div>

  $$
  \frac{1}{\rho} \frac{d}{d\rho} \left({\rho \frac{dR}{d\rho}}\right)
    + \left({ - \frac{m^2}{\rho^2}}\right) R
  \quad\Rightarrow\quad \purple{\rho \frac{d}{d\rho}} \left({\purple{\rho \frac{d}{d\rho}} R}\right) = m^2 R
  $$
  此为 **<green>Euler 方程** <gray>(见第 7 章)

---
### 柱坐标下 Laplace 方程分离变量
* 变量替换 $\rho(t) = e^t$，$\green{R(t) \coloneqq R(\rho(t))}$，使得
  $$
  \purple{\rho \frac{d}{d\rho}} = \frac{d}{dt}, \qquad \frac{d^2 R(t)}{dt^2} = m^2 R(t)
  $$
- 对 $m$ 的取值**分类讨论**

---
### 柱坐标下 Laplace 方程分离变量
- 当 $m \ne 0$，$R(\rho) = \rho^m$
  
  <div class='proof comment'>
  
  **$m \ne 0$ 的情况分析**
  
  * 当 $m < 0$，$\rho^{-m}$ 在 $z$ 轴上 **<red>发散**，不符合自然边界条件 $R(0) = 0$，**<red>舍去**
  
  * 当 $m > 0$，$\rho^m$ 在 $z$ 轴上 **<red>为零**，符合自然边界条件  $R(0) = 0$。
  * 另外检查 $\rho = a$ 的第三类边界条件
    $$
    \alpha \frac{dR(\rho)}{d\rho} + \beta R(\rho) \Bigg|_{\rho = a} = m \alpha a^{m - 1} + \beta a^m \red{> 0}
    $$
    **<red>不满足**，**<red>舍去**
  
  * **<red>$m \ne 0$ 全军覆没**
  
  </div>

---
### 柱坐标下 Laplace 方程分离变量
- 当 $m = 0$，$R(\rho) = 1, \ln \rho$

<div class='proof comment'>

**$m = 0$ 的情况分析**

* $R(\rho) = \ln \rho$ 在 $\rho = 0$ 处 **<red>发散**，不符合自然边界条件 $R(0)$ 有限 ，**<red>舍去**
* $R(\rho) = 1$ 在 $\rho = 0$ 处 **<red>有限**，符合自然边界条件 $R(0)$ 有限
* 另外检查 $\rho = a$ 的**第三类**边界条件
  $$
  \alpha R'(\rho) + \beta R(\rho) \big|_{\rho = a} = \beta
  $$
  如果实际上是**第二类**边界条件 **$(\beta = 0)$**，**<green>可以保留 $R(\rho) = 1$**，否则 **<red>舍去**

* **<red>当且仅当** $\rho = a$ 处取**第二类**边界条件，$m = 0$ 是合法的解，$R(\rho) = 1$

</div>

- 当且仅当 $\rho = a$ 取**第二类**边界条件，$\lambda = 0$ 是可取的，此时 $m = 0$。否则 $\lambda = 0$ **<red>不可取**。

---
### 柱坐标下 Laplace 方程分离变量
- $\lambda, m$ 的分类总结
  $$
  \begin{matrix}
    & \lambda = 0 & \lambda > 0\\
    m = 0& 第二类外边界 & m\text{-阶 Bessel} \\
    m \ne 0& \times & m\text{-阶 Bessel}
  \end{matrix}
  $$

---
### 柱坐标下 Laplace 方程分离变量
- $z$ 方向方程很简单
  $$
  \frac{d^2 Z}{dz^2} = \lambda Z \quad \Rightarrow \quad Z = e^{\pm \sqrt{\lambda}z}
  $$
  
  <div class='proof comment'>
  
  **Sturm-Liouville 定理**
  
  Sturm-Liouville $\lambda \ge 0$
  
  </div>

- 自然边界条件：$Z$ 在 $z$ 的各边界处 (包括无穷远) 都是**有限**的
  - $z \in [z_\text{min}, z_\text{max}]$: 解是 $e^{\pm \sqrt{\lambda}x}$ 的线性组合
  - $z \in [z_\text{min}, +\infty)$：解只能取 $e^{- \sqrt{\lambda}x}$
  - $z \in (-\infty, z_\text{max}]$：解只能取 $e^{+ \sqrt{\lambda}x}$
