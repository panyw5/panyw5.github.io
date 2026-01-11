from manim import *
from manim_helpers import *
import numpy as np

config.pixel_height = 2160
config.pixel_width = 3840


class Scene01(Scene):
  """展示 Legendre 多项式及其零点分布，从 l=1 到 l=8"""
  def construct(self):
    # 基础设置
    set_purple_background(self)
    set_chinese_font()
    
    # 创建坐标轴
    axis = Axes(
      x_range=[-1.2, 1.2, 0.5],
      y_range=[-1.5, 1.5, 0.5],
      x_length=10,
      y_length=6,
      axis_config={"color": GRAY_B},
      x_axis_config={
        "numbers_to_include": [-1, -0.5, 0.5, 1],
        "stroke_width": 4,
        "stroke_opacity": 0.3
      },
      y_axis_config={
        "numbers_to_include": [-1, 1],
        "stroke_width": 4,
        "stroke_opacity": 0.3
      }
    ).shift(DOWN * 0.5)
    
    axis.x_axis.numbers.set_color(GRAY_C)
    axis.y_axis.numbers.set_color(GRAY_C)
    
    # 添加标签
    labels = axis.get_axis_labels(x_label="x", y_label="P_\\ell(x)")
    labels[0].set_color(GRAY_C)  # x 标签保持灰色
    labels[1].set_color(PURPLE_B)  # P_ell(x) 标签改为紫色
    labels[1].shift(DOWN * 0.3)  # 下移避免被遮挡
    
    # 添加 x = ±1 的虚线
    line_left = DashedLine(
      axis.c2p(-1, -1.5),
      axis.c2p(-1, 1.5),
      color=GRAY_B,
      stroke_width=3,
      stroke_opacity=0.5
    ).set_z_index(-1)
    
    line_right = DashedLine(
      axis.c2p(1, -1.5),
      axis.c2p(1, 1.5),
      color=GRAY_B,
      stroke_width=3,
      stroke_opacity=0.5
    ).set_z_index(-1)
    
    # 添加坐标轴和虚线
    self.play(
      Create(axis),
      FadeIn(labels),
      Create(line_left),
      Create(line_right)
    )
    self.wait()
    
    # 标题文本
    title = MathTex(
      r"\textbf{Legendre 多项式的零点分布}",
      tex_template=TexTemplateLibrary.ctex,
      color=YELLOW_B
    ).scale(1.2).to_edge(UP, buff=0.5)
    
    self.play(FadeIn(title, shift=DOWN))
    self.wait()
    
    # 遍历 l = 1 到 8
    for ell in range(1, 9):
      # 创建 Legendre 多项式
      # 使用 numpy 的 Legendre 多项式
      legendre_poly = np.polynomial.legendre.Legendre([0] * ell + [1])
      
      # 绘制曲线
      plot = axis.plot(
        lambda x: legendre_poly(x),
        color=PURPLE_B,
        stroke_width=7,
        x_range=[-1, 1, 0.01]
      )
      
      # 找到零点
      roots = legendre_poly.roots()
      # 只保留实数零点且在 [-1, 1] 范围内
      real_roots = [r.real for r in roots if abs(r.imag) < 1e-10 and -1 <= r.real <= 1]
      
      # 创建零点标记
      dots = VGroup(
        *[Dot(
          axis.c2p(root, 0),
          color=GREEN_D,
          radius=0.12
        ) for root in real_roots]
      )
      
      # 显示当前阶数
      ell_text = MathTex(
        f"\\ell = {ell}",
        color=YELLOW_B
      ).scale(1.0).next_to(title, DOWN, buff=0.5)
      
      # 零点数量文本
      zero_count = MathTex(
        f"\\text{{零点数量: }} {len(real_roots)}",
        tex_template=TexTemplateLibrary.ctex,
        color=GREEN_B
      ).scale(0.9).next_to(ell_text, DOWN, buff=0.3)
      
      # 动画
      if ell == 1:
        self.play(
          Create(plot),
          FadeIn(ell_text),
          FadeIn(zero_count)
        )
        self.play(FadeIn(dots, scale=0.5))
      else:
        self.play(
          ReplacementTransform(prev_plot, plot),
          ReplacementTransform(prev_ell_text, ell_text),
          ReplacementTransform(prev_zero_count, zero_count),
          ReplacementTransform(prev_dots, dots)
        )
      
      self.wait(1.5)
      
      # 保存当前对象供下次使用
      prev_plot = plot
      prev_ell_text = ell_text
      prev_zero_count = zero_count
      prev_dots = dots
    
    # 最后强调
    emphasis_text = MathTex(
      r"\textbf{所有零点都在 } (-1, 1) \textbf{ 内，且无重根}",
      tex_template=TexTemplateLibrary.ctex,
      color=GREEN_B
    ).scale(0.9).next_to(zero_count, DOWN, buff=0.5)
    
    self.play(FadeIn(emphasis_text, shift=UP))
    self.wait(2)
    
    # 淡出
    self.play(
      FadeOut(VGroup(plot, dots, ell_text, zero_count, emphasis_text, title)),
      FadeOut(axis),
      FadeOut(labels),
      FadeOut(line_left),
      FadeOut(line_right)
    )
    self.wait()


class Scene02(Scene):
  """展示零点在区间内的密集分布（高阶情况）"""
  def construct(self):
    # 基础设置
    set_purple_background(self)
    set_chinese_font()
    
    # 创建坐标轴
    axis = Axes(
      x_range=[-1.2, 1.2, 0.5],
      y_range=[-1.5, 1.5, 0.5],
      x_length=10,
      y_length=6,
      axis_config={"color": GRAY_B},
      x_axis_config={
        "numbers_to_include": [-1, -0.5, 0.5, 1],
        "stroke_width": 4,
        "stroke_opacity": 0.3
      },
      y_axis_config={
        "numbers_to_include": [-1, 1],
        "stroke_width": 4,
        "stroke_opacity": 0.3
      }
    ).shift(DOWN * 0.5)
    
    axis.x_axis.numbers.set_color(GRAY_C)
    axis.y_axis.numbers.set_color(GRAY_C)
    
    labels = axis.get_axis_labels(x_label="x", y_label="P_\\ell(x)")
    labels[0].set_color(GRAY_C)  # x 标签保持灰色
    labels[1].set_color(PURPLE_B)  # P_ell(x) 标签改为紫色
    labels[1].shift(DOWN * 0.3)  # 下移避免被遮挡
    
    # 标题
    title = MathTex(
      r"\textbf{高阶 Legendre 多项式的零点分布}",
      tex_template=TexTemplateLibrary.ctex,
      color=YELLOW_B
    ).scale(1.2).to_edge(UP, buff=0.5)
    
    self.play(
      Create(axis),
      FadeIn(labels),
      FadeIn(title, shift=DOWN)
    )
    self.wait()
    
    # 展示 l = 15
    ell = 15
    legendre_poly = np.polynomial.legendre.Legendre([0] * ell + [1])
    
    plot = axis.plot(
      lambda x: legendre_poly(x),
      color=PURPLE_B,
      stroke_width=7,
      x_range=[-1, 1, 0.005]
    )
    
    roots = legendre_poly.roots()
    real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-10 and -1 <= r.real <= 1])
    
    dots = VGroup(
      *[Dot(
        axis.c2p(root, 0),
        color=GREEN_D,
        radius=0.1
      ) for root in real_roots]
    )
    
    ell_text = MathTex(
      f"\\ell = {ell}",
      color=YELLOW_B
    ).scale(1.0).next_to(title, DOWN, buff=0.5)
    
    zero_count = MathTex(
      f"\\text{{零点数量: }} {len(real_roots)}",
      tex_template=TexTemplateLibrary.ctex,
      color=GREEN_B
    ).scale(0.9).next_to(ell_text, DOWN, buff=0.3)
    
    self.play(
      Create(plot),
      FadeIn(ell_text),
      FadeIn(zero_count)
    )
    self.wait()
    
    self.play(FadeIn(dots, lag_ratio=0.05))
    self.wait()
    
    # 强调零点分布的均匀性
    emphasis = MathTex(
      r"\textbf{零点在区间内近似均匀分布}",
      tex_template=TexTemplateLibrary.ctex,
      color=GREEN_B
    ).scale(0.9).next_to(zero_count, DOWN, buff=0.5)
    
    self.play(FadeIn(emphasis, shift=UP))
    self.wait(2)
