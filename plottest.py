from manim import *


class plotgraph(Scene):
    def construct(self):
        a=Axes(
            axis_config={"include_numbers": True}
        )

        self.add(a)
        graph=a.plot(lambda x: x, color=GREEN)
        graph2=a.plot(lambda x: x**2, x_range=[-2,2], color=RED)
        graph3=a.plot(lambda x: x**3, color=RED)
        graph4=a.plot(lambda x: x**4, color=RED)
        self.add(graph)
        self.wait()
        self.play(ReplacementTransform(graph,graph2), run_time=3)        
        self.wait()
        self.play(ReplacementTransform(graph2,graph3), run_time=3)
        self.wait()
        self.play(ReplacementTransform(graph3,graph4), run_time=3)
        self.wait()