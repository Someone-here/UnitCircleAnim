from numpy import cos
from manim import *


class UnitCircle(Scene):
    def construct(self):

        theta_tracker = ValueTracker(0)
        unit_circle = Circle(color=BLUE)
        self.play(Create(unit_circle))
        self.play(unit_circle.animate.scale(2), run_time=2)
        plane = NumberPlane(color=GREEN)
        self.play(Create(plane), run_time=3, lag_ratio=0.1)
        self.play(plane.animate.scale(2))
        radius = always_redraw(lambda: Line(
            ORIGIN, RIGHT * 2, 0, color=RED).rotate_about_origin(theta_tracker.get_value() * DEGREES))
        radius_brace = Brace(radius, DOWN, buff=0.1)
        r_text = radius_brace.get_text("r = 1")
        self.play(Create(radius))
        self.play(Create(radius_brace), Create(r_text))
        area_text = MathTex("A =  \pi r^2= \pi 1^2 = \pi").shift(UP * 3)
        self.play(Write(area_text))
        self.wait(1)
        self.play(FadeOut(radius_brace), FadeOut(r_text))
        self.play(theta_tracker.animate.set_value(45))

        theta = always_redraw(lambda: Angle(Line(ORIGIN, RIGHT * 2), radius))
        opp = always_redraw(lambda: Line(radius.get_end(), [
                            radius.get_end()[0], 0, 0], color=RED))
        opp_label = always_redraw(lambda: Text("Opp").shift(
            [opp.get_center()[0] - 0.1, opp.get_center()[1], 0]).rotate(90 * DEGREES).scale(0.25))
        adj = always_redraw(lambda: Line(ORIGIN, opp.get_end(), color=RED))
        adj_label = always_redraw(lambda: Text("Adj").scale(0.25).shift(
            [adj.get_center()[0], adj.get_center()[1] + 0.1, 0]))
        theta_label = always_redraw(lambda: MathTex("\\theta").shift(
            theta.get_center() + RIGHT * 0.15 + UP * 0.1).scale(0.5))
        radius_label = always_redraw(lambda: MathTex("Hyp").shift(
            radius.get_center() + [-0.1, 0.1, 0]).scale(0.5).rotate(theta_tracker.get_value() * DEGREES))
        sin_text = MathTex("\\sin(\\theta) = \\frac{Opp}{Hyp}").next_to(
            area_text, RIGHT * 3)
        sin_text1 = MathTex(
            "\\sin(\\theta) = \\frac{Opp}{1} = Opp").next_to(sin_text, DOWN)
        cos_text = MathTex("\\cos(\\theta) = \\frac{Adj}{Hyp}").next_to(
            sin_text1, DOWN * 3)
        cos_text1 = MathTex(
            "\\cos(\\theta) = \\frac{Adj}{1} = Adj").next_to(cos_text, DOWN)
        self.play(Create(theta), Write(theta_label))
        self.play(Create(opp), Create(adj))
        self.play(Write(opp_label), Write(adj_label), Write(radius_label))
        self.play(Write(sin_text))
        self.play(Write(sin_text1))
        self.play(FadeTransform(opp_label, always_redraw(lambda: MathTex("\\sin(\\theta)").shift(
            [opp.get_center()[0] - 0.1, opp.get_center()[1], 0]).rotate(90 * DEGREES).scale(0.5))))
        self.play(Write(cos_text))
        self.play(Write(cos_text1))
        self.play(FadeTransform(adj_label, always_redraw(lambda: MathTex("\\cos(\\theta)").shift(
            [adj.get_center()[0] + 0.2, adj.get_center()[1] + 0.1, 0]).scale(0.5))))

        tan = always_redraw(lambda: Line(
            radius.get_end(), [(1/cos(theta_tracker.get_value() * (PI/180))) * 2, 0, 0], color=RED))

        tan_label = always_redraw(lambda: Text("Tan").shift(
            tan.get_center() + [0, 0.1, 0]).scale(0.25).rotate(theta_tracker.get_value() * DEGREES - 90 * DEGREES))

        self.play(Create(tan), Write(tan_label))

        self.play(theta_tracker.animate.set_value(10), run_time=2)
        self.play(theta_tracker.animate.increment_value(350), run_time=10)


class UnitCircle2(Scene):
    def construct(self):
        theta = ValueTracker(45)
        circle = Circle(color=BLUE).scale(2)
        self.play(Create(circle))
        radius = always_redraw(lambda: Line(
            ORIGIN, RIGHT * 2, 0, color=RED).rotate_about_origin(theta.get_value() * DEGREES))
        self.play(Create(radius))
        tan = always_redraw(lambda: Line(
            radius.get_end(), [(1/cos(theta.get_value() * (PI/180))) * 2, 0, 0], color=RED))
        self.play(Create(tan))
        self.play(theta.animate.increment_value(360), run_time=10)
