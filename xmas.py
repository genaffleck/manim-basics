from manim import *

class MerryChristmas(Scene):
  def construct(self):
    k = ValueTracker(3)
    radius = 1
    num = always_redraw(lambda: DecimalNumber(num_decimal_places=1).set_color(PURE_RED).scale(3).set_value(k.get_value()))
    text = Tex("Merry Christmas").scale(2.5).set_color_by_gradient(PURE_RED, RED_A).shift(0.5*UP)
    text2 = Tex("9-Rizal").scale(2.5).set_color_by_gradient(PURE_RED, RED_A).next_to(text, DOWN)
    
    #animations
    self.wait()
    self.play(FadeIn(num))
    self.play(k.animate.set_value(0), run_time=3, rate_func=linear)
    self.play(FadeOut(num))
    self.play(Write(text))
    self.play(Write(text2))
    self.play(ApplyWave(VGroup(text, text2)))
    self.play(Flash(
      text2,
      line_length=1,
      num_lines=12, color=YELLOW,
      flash_radius=radius+SMALL_BUFF,
      time_width=0.3, run_time=2,
      rate_func = rush_from))
    self.play(AnimationGroup(FadeOut(text, shift=UP*1.5), FadeOut(text2, shift=UP*1.5)))