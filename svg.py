from manim import *

class Svg(Scene):
  def construct(self):
    self.camera.background_color = WHITE
    svg_image = SVGMobject("SIGNATURE.svg")

    self.play(Write(svg_image), run_time=5, rate_func=linear)
    self.wait()