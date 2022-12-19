from manim import*

class Updater(Scene):
  def construct(self):
    rectangle = RoundedRectangle(
      stroke_width=4,
      stroke_color=WHITE,
      fill_color=YELLOW, #why rendered rectangle is not yellow? hmmm...
      fill_opacity=0.9,
      width=4.5,
      height=2
    ).shift(UP*2.5+LEFT*4)

    mathtext = MathTex("\\frac{3}{4}=0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
    mathtext.move_to(rectangle.get_center())
    mathtext.add_updater(lambda x: x.move_to(rectangle.get_center()))


    self.play(FadeIn(rectangle))
    self.play(Write(mathtext))
    self.play(rectangle.animate.shift(RIGHT*5+DOWN*3), run_time=5)
    self.wait()
    mathtext.clear_updaters()
    self.play(rectangle.animate.shift(LEFT*2+UP*1), run_time=3)
    