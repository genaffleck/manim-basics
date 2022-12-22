from manim import*

class graphing3(Scene):
  def construct(self):
    text1 = Text("Graph the function:", font_size=80).set_color_by_gradient(GREEN, PINK).shift(1.5*UP)
    text2 = MathTex("y=(x+7)^2+3", font_size=120)

    plane = NumberPlane(
      axis_config={
        "stroke_color": WHITE,
        "stroke_width": 2,
      },
      background_line_style={
        "stroke_color": TEAL_C,
        "stroke_width": 0.5,
        "stroke_opacity": 0.4
      },
      x_range=(-15,4,1),
      y_range=(-1,11,1),
      x_length=12,
      y_length=7.5
    ) 

    axes = Axes(
      x_range=[-15,4,1],
      y_range=[-1,11,1],
      x_length=12,
      y_length=7.5
    ).add_coordinates()

    axis_labels = axes.get_axis_labels()
    vertex = Dot(axes.coords_to_point(-7,3), color=PURE_RED)
    func = axes.plot(lambda x: (x+7)**2+3, x_range=[-9.8,-4.2]).set_color_by_gradient(GREEN, PINK)

    #animations

    self.play(Write(text1))
    self.play(Write(text2))
    self.wait(2)
    self.play(Unwrite(text1))
    self.play(text2.animate.shift(3.5*UP+5.5*LEFT).scale(0.3))
    self.wait(2)
    self.play(Create(plane), run_time=3)
    self.wait(2)
    self.play(Create(axes), run_time=6)
    self.wait(2)
    self.play(Write(axis_labels))
    self.wait(2)
    self.play(FadeIn(vertex))
    self.wait()
    self.play(Write(func), run_time=8)
    self.wait()
    self.play(text2.animate.shift(1.25*RIGHT+0.5*DOWN).set_color(YELLOW), run_time=2)
    self.wait(2)