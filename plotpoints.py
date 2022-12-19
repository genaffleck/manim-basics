from manim import *

class InverseGraph(Scene):
  def construct(self):
    plane=NumberPlane()
    axes = Axes(
            x_range=[0.1, 26, 2],
            y_range=[0, 26, 2],
            x_length=10,
            y_length=7,
            axis_config={"color": GREEN},
            tips=True,
        ).add_coordinates()
    
    
    axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
    graph = axes.plot(lambda x: 24/x, color=WHITE)
    graph_label = axes.get_graph_label(graph, label='y=\\frac{24}{x}')
    dot1=Dot(axes.coords_to_point(1,24), color=RED)
    dot2=Dot(axes.coords_to_point(2,12), color=RED)
    dot3=Dot(axes.coords_to_point(3,8), color=RED)
    dot4=Dot(axes.coords_to_point(4,6), color=RED)
    dot5=Dot(axes.coords_to_point(6,4), color=RED)
    dot6=Dot(axes.coords_to_point(12,2), color=RED)
    dot7=Dot(axes.coords_to_point(24,1), color=RED)

    #animation
    self.wait(2)
    self.play(Create(axes), run_time=5)
    self.wait()
    self.play(Write(axis_labels))
    self.wait()
    self.play(FadeIn(dot1))
    self.wait()
    self.play(FadeIn(dot2))
    self.wait()
    self.play(FadeIn(dot3))
    self.wait()
    self.play(FadeIn(dot4))
    self.wait()
    self.play(FadeIn(dot5))
    self.wait()
    self.play(FadeIn(dot6))
    self.wait()
    self.play(FadeIn(dot7))
    self.wait()
    self.play(Create(graph), run_time=5)
    #self.play(Write(graph_label))
    self.wait(3)