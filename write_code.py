from manim import *


class code(Scene):
  def construct(self):
    code = """\\documentclass{article}
    
      \\begin{document}
      \\end{document}"""

    codes = Code(
      code =code,
      tab_width=6,
      background_stroke_width=1,
      background_stroke_color=WHITE,
      insert_line_no=True,
      style=Code.styles_list[14],
      background="window",
      language="latex"
    ).scale(2)

    self.play(Write(codes), run_time = 5)
    self.wait(1)
    self.play(FadeOut(codes), run_time=2)