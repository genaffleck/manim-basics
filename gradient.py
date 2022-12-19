from manim import*

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9

class GradientText(Scene):


  def construct(self):

    #text=Tex("Inverse Variation", font_size=150).set_color_by_gradient(PURE_RED, YELLOW_E)
    text2=Text("Negative", font_size=125, weight=SEMIBOLD).shift(UP*1.5).set_color_by_gradient(PURE_RED, YELLOW_E).set_stroke(width=4,color=BLACK)
    text3=Text("Exponent", font_size=125, weight=SEMIBOLD).set_color_by_gradient(PURE_RED, YELLOW_E).set_stroke(width=4,color=BLACK).next_to(text2, DOWN)
    self.play(Write(text2))
    self.play(Write(text3))
    self.wait(2)
