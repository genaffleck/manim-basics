from manim import*

class Shifting(Scene):


  def construct(self):

    box = Rectangle(
      stroke_color=BLUE,
      fill_color=RED,
      stroke_opacity=0.8,
      fill_opacity=0.5,
      height=1,
      width=1
    )

    plane = NumberPlane(
      axis_config={
        "unit_size":1,
        "stroke_color": WHITE, 
        }
      ,
      background_line_style={
        "stroke_color": TEAL,
        "stroke_width": 4,
        "stroke_opacity": 0.6,
      }
    )

    #animation - shifting

    self.add(plane)
    self.add(box)
    self.play(box.animate.shift(RIGHT*2), run_time=2)
    self.play(box.animate.shift(UP*3), run_time=3)
    self.play(box.animate.shift(LEFT*5+DOWN*6), run_time=5)
    self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=1)