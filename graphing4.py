from manim import*

class graphing4(Scene):
  def construct(self):
    text1 = Text("Graph the quadratic function: ", font_size=60).set_color_by_gradient(PINK, GREEN).shift(UP)
    text2 = MathTex("y=-(x+6)^2-3", font_size=80).next_to(text1, DOWN, buff=0.5)
    plane = NumberPlane(
      x_length=12,
      y_length=7.5,
      x_range=(-17,7),
      y_range=(-16,2),
      background_line_style={
        "stroke_color": YELLOW,
        "stroke_width": 0.4,
        "stroke_opacity":0.4
      }
    )
    axes = Axes(
      x_range=[-17,7,2],
      y_range=[-16,2,2],
      x_length=12,
      y_length=7.5,
      color=GREEN,
      tips=False
    ).add_coordinates()

    axes_labels = axes.get_axis_labels()
    dot = Dot(axes.coords_to_point(-6,-3), color=PURE_RED)
    func = axes.plot(lambda x: -(x+6)**2-3, x_range=[-9.5,-2.5],color=PURE_GREEN)

    #animations

    self.play(Write(text1))
    self.wait()
    self.play(Write(text2))
    self.wait()
    self.play(AnimationGroup(
      FadeOut(text1, run_time=2),
      text2.animate.shift(5.2*LEFT).scale(0.5),
      lag_ratio=0.5
      )
    )
    self.wait()
    self.play(Create(plane), run_time=5)
    self.wait(2)
    self.play(Create(axes), run_time=5)
    self.wait(2)
    self.play(Write(axes_labels))
    self.wait(2)
    self.play(FadeIn(dot))
    self.wait(2)
    self.play(Write(func), run_time=6)
    self.wait(2)
    self.play(text2.animate.shift(1*UP+2*RIGHT).set_color(PURE_GREEN))
    self.wait(2)