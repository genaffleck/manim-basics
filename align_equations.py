from manim import *

class AlignedEquations(Scene):
  def construct(self):
    eqn = MathTex(r"\textrm{Simplify}\ \frac{2}{\sqrt{3}}", font_size=80).shift(UP*3+LEFT*1.25)
    step1 = MathTex(
      r"& = \frac{2}{\sqrt{3}}\cdot\frac{\sqrt{3}}{\sqrt{3}}\\",
      r"& = \frac{2\sqrt{3}}{3}",
      font_size = 80
    ).next_to(eqn, DOWN*2).set_color(YELLOW)
        
    code = """
    Example 1 
      """

    codes = Code(
      code =code,
      tab_width=6,
      background_stroke_width=1,
      background_stroke_color=WHITE,
      insert_line_no=False,
      style=Code.styles_list[14],
      background="window",
      language="latex"
    ).scale(0.5).shift(UP*3.1+LEFT*5)
    # animations
    
    self.wait()
    self.play(Write(codes), run_time=2)
    self.wait()
    self.play(Write(eqn), run_time=3)
    self.wait(4)
    self.play(Write(step1[0]), run_time=3)
    self.wait(2)
    self.play(Write(step1[1]), run_time=3)
    self.wait(2)