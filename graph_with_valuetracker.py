from manim import *

class graph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5,10,2],
            y_range=[-2,20, 2],
            x_length=5,
            y_length=7,
            # axis_config={"include_numbers": True},
            color = YELLOW
        )

        func = axes.plot(lambda x: (x-3)**2+1, x_range=[-1,7]).set_color_by_gradient(RED)

        #animations

        self.play(Write(axes), run_time=3)
        self.play(Write(func), run_time=3)
        self.wait()

        x = ValueTracker(-1)
        d1 = always_redraw(lambda : Dot().move_to(axes.c2p(x.get_value(), 0)))
        d2 = always_redraw(lambda :Dot().move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value()))))
        d3 = always_redraw(lambda: Dot().move_to(axes.c2p(0, func.underlying_function(x.get_value()))))

        l1 = always_redraw(lambda : DashedLine(start = d1, end = d2))
        l2 = always_redraw(lambda: DashedLine(start = d3, end = d2))
        func_value = always_redraw(lambda : Text(f"{func.underlying_function(x.get_value()):.1f}", font_size=15, color=YELLOW).next_to(d3, RIGHT))
        x_value = always_redraw(lambda : Text(f"{x.get_value():.1f}", font_size=15, color=YELLOW).next_to(d1, UP))
        
        self.play(FadeIn(d1))
        self.play(FadeIn(d2))
        self.play(FadeIn(d3))

        self.play(Write(l1))
        self.play(Write(l2))

        self.add(func_value)
        self.add(x_value)
        self.play(x.animate.set_value(7), run_time = 10)
        self.wait()