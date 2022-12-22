from manim import *

class Graph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 10, 1],
            x_length=3,
            y_length=6,
            axis_config={"color": GREEN},
            tips=False,
        ).add_coordinates()
        dot = Dot()
        axis_labels = axes.get_axis_labels()
        func = axes.plot(lambda x: (x-3)**2+1, color=YELLOW)
        graph_label = axes.get_graph_label(func, label=r"f(x)=(x-3)^2+1", x_val=6, direction=DOWN*0.2+(RIGHT*0.1), color=BLUE).scale(0.5)
        arrow = Arrow([1.5, 2.25, 0], [2.25, 2.5, 0], buff=0)
        #dot1 = Dot(func.get_bottom())

        self.wait(2)
        self.play(Create(axes), run_time=4, rate_func=linear)
        self.play(Write(axis_labels))
        self.play(Create(dot), Create(func), MoveAlongPath(dot, func), run_time=2)

        self.play(Create(arrow))
        self.play(Write(graph_label))
        self.wait(2)