from manim import*

class QuadraticGraph(Scene):
  def construct(self):
    text1 = Text("Graph the function: ", font_size=80).set_color_by_gradient(GREEN, PINK)
    text2 = MathTex("y=(x-4)^2+1", font_size=120)

    plane = NumberPlane(
      axis_config={
        "stroke_color": WHITE,
        "stroke_width": 1, 
        },
      background_line_style={
        "stroke_color": TEAL,
        "stroke_width": 0.5,
        "stroke_opacity": 0.4,
      },
      x_range=(-4,8,1),
      y_range=(-2,10,1),
      x_length=7,
      y_length=7,
    )

    axes = Axes(
            x_range=[-4, 8, 1],
            y_range=[-2, 10, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": GREEN},
            tips=False,
        ).add_coordinates()

    dot = Dot(axes.coords_to_point(4, 1), color=BLUE_C)
    axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
    func = axes.plot(lambda x: (x-4)**2+1, x_range=[1.1,6.9]).set_color_by_gradient(GREEN, PINK)
    graph_label = axes.get_graph_label(func, label=r"f(x)=(x-4)^2+1", x_val=6.8, direction=DOWN*0.2+(RIGHT*0.1), color=YELLOW).scale(0.75)
    
    #animations
    self.play(Write(text1.shift(1.5*UP)))
    self.play(Write(text2.next_to(text1, DOWN, buff=0.5)))
    self.wait(6)
    self.play(Unwrite(text1), Unwrite(text2))
    self.play(Write(plane),run_time=6)
    self.wait(3)
    self.play(Create(axes), run_time=6)
    self.wait(3)
    self.play(Write(axis_labels))
    self.wait(3)
    self.play(FadeIn(dot))
    self.wait(3)
    self.play(Create(func), run_time=6)
    self.wait(1)
    self.play(Write(graph_label), run_time=2)
    self.wait(3)
 