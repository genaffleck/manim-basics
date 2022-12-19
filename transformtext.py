from manim import*

class TextTransform(Scene):
  def construct(self):
    step1 = MathTex("-3x", "+4","=", "7", font_size=100)
    step2 = MathTex("-3x", "=","7","-4", font_size=100)
    step3 = MathTex("-3x", "=", "3", font_size=100)
    step4 = MathTex("\\frac{-3x}{-3}","=", "\\frac{3}{-3}", font_size=100)
    step5 = MathTex("x","=","-1", font_size=100)
    rectangle = Rectangle(height=1, width=4, stroke_color=YELLOW)

    self.play(Write(step1))
    self.wait()
    self.play(step1.animate.move_to(3*UP+1*LEFT))
    self.wait()
    self.play(TransformMatchingTex(step1.copy(),step2.shift(2*UP+0.75*RIGHT)), run_time=4)
    self.wait(4)
    self.play(TransformMatchingTex(step2.copy(),step3.shift(1*UP+0.1*LEFT)))
    self.wait(4)
    self.play(FadeTransform(step3, step4.shift(0.2*RIGHT)))
    self.wait(4)
    self.play(FadeIn(step5.shift(2*DOWN+0.85*RIGHT)),run_time=4)
    self.play(DrawBorderThenFill(rectangle.shift(2*DOWN+0.75*RIGHT)))
    self.play(Uncreate(rectangle.set_points(rectangle.get_points()[::-1]))) 
    self.wait()
