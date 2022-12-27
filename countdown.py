from manim import *

config.background_color = WHITE
config.frame_width = 8
config.frame_height = 8

class Countdown(Scene):
  def construct(self):
    k = ValueTracker(15)
    num = always_redraw(lambda: DecimalNumber(num_decimal_places=1).set_color(PURE_BLUE).scale(3).set_value(k.get_value()))
    text = Tex("Time's up").scale(3).set_color(PURE_BLUE)

    self.play(FadeIn(num))
    self.play(k.animate.set_value(0), run_time=15, rate_func=linear)
    self.play(FadeOut(num))
    self.play(Write(text))