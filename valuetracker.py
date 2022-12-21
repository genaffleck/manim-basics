from manim import *

class ValueTrackers(Scene):
    def construct(self):
        k = ValueTracker(3.5)
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait(2)
        self.play(k.animate.set_value(0), run_time=3.5, rate_func=linear)