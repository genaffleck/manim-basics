from manim import*

class Intro(Scene):
    def construct(self):
        part1 = MathTex("5 + 5 + 1 + 1 + 1", "=", "13", font_size=100)
        part2 = MathTex("10 + 2 + 1", "=", "13", font_size=100)
        part2_rev = MathTex("13", "=", "10 + 2 + 1", font_size=100)
        
        self.wait()
        self.play(Write(part1, run_time=4))
        self.wait()
        self.play(part1.animate.scale(0.5).move_to(2*UP))
        self.wait()
        self.play(Write(part2, run_time=3))
        self.wait()
        self.play(part2.animate.scale(0.5).next_to(part1, DOWN, buff=1))
        part2_rev.scale(0.5).shift(part2[1].get_center() - part2_rev[1].get_center())
        self.wait()
        self.play(TransformMatchingTex(part2, part2_rev, path_arc=PI/2))
        self.wait()
        identity = MathTex("5 + 5 + 1 + 1 + 1", "=", "10 + 2 + 1", font_size=100).next_to(part2, DOWN, buff=1.5)
        self.play(
            FadeTransform(part1[0].copy(), identity[0]),
            Write(identity[1]),
            FadeTransform(part2_rev[2].copy(), identity[2]),
            run_time=2
        )
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(part1, shift=UP),
                FadeOut(part2_rev, shift=UP),
                identity.animate.move_to(ORIGIN),
                lag_ratio=0.5
            )
        )
        self.play(Unwrite(identity), run_time=3)
        self.wait()
