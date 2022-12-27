from manim import *

class transform_Equation(Scene):
  def construct(self):
    eqn = MathTex("a^2","+","b^2","=","c^2", font_size=80).shift(UP*1.5)
    eqn2 = MathTex("c^2","=","a^2","+","b^2", font_size=80).next_to(eqn, DOWN)
    eqn3 = MathTex("\sqrt{c^2}", "=", "\sqrt{a^2+b^2}", font_size=80).next_to(eqn2, DOWN)
    #animations
    self.play(Write(eqn), run_time=2)
    self.play(TransformMatchingTex(eqn.copy(), eqn2), run_time=2)
    self.play(FadeIn(eqn3, shift=DOWN*0.3), run_time=2)
    self.wait(2)
    self.play(FadeOut(VGroup(eqn, eqn2, eqn3)))

class A1(Scene):
  def construct(self):
    circ = Circle(radius=2)

    self.play(Create(circ))

class A2(Scene):
  def construct(self):
    sq = Square(side_length=3)

    # self.play(Create(sq.rotate(1.5*PI)))