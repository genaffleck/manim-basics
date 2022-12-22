from manim import *

class graphing1(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 2],
            x_length=4,
            y_range=[0, 16, 4],
            y_length=6.5
        ).to_edge(DOWN, buff=0.5).add_coordinates()
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x: x**2, x_range=[-3.8, 3.8], color=GREEN)
        func_label = MathTex(r"f(x)=x^2").next_to(parab, UR, buff=0.1).scale(0.5).set_color(GREEN)

        # animations
        self.play(DrawBorderThenFill(plane), run_time=2)
        self.play(Write(VGroup(labels, parab)), run_time=3, rate_func=linear)
        self.play(Write(func_label))
        self.wait()