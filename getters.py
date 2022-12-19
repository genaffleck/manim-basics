from manim import *

class Getters(Scene):
  def construct(self):

    rect = Rectangle(color=WHITE, fill_color=ORANGE, fill_opacity=0.8, height=3, width=2.5).to_edge(UL, buff=0.5)
    circ = Circle().to_edge(DOWN)
    arrow = always_redraw(
      lambda : Line(
        start = rect.get_bottom(), end=circ.get_top(), buff=0.5
        ).add_tip()
      )

    self.play(Create(VGroup(rect, circ, arrow)), run_time=3)
    self.wait()
    self.play(rect.animate.to_edge(UR, buff=0.5), circ.animate.to_edge(DL, buff=0.5),  run_time=3)
    self.play(rect.animate.to_edge(UL, buff=0.5), circ.animate.to_edge(DR, buff=0.5), run_time=3)