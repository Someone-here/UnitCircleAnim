from numpy import cos
from manim import *


class UnitCircle(Scene):
    def construct(self):

        theta_tracker = ValueTracker(0)

        unit_circle = Circle(color=BLUE)
        self.play(Create(unit_circle))
        self.play(unit_circle.animate.scale(2), run_time=2)

        plane = NumberPlane(background_line_style={
            "stroke_color": TEAL,
        })
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

        # Opposite side with label
        opp = always_redraw(lambda: Line(radius.get_end(), [
                            radius.get_end()[0], 0, 0], color=RED))
        opp_label = always_redraw(lambda: Text("Opp").shift(
            [opp.get_center()[0] - 0.1, opp.get_center()[1], 0]).rotate(90 * DEGREES).scale(0.25))

        # Adjacent side with label
        adj = always_redraw(lambda: Line(ORIGIN, opp.get_end(), color=RED))
        adj_label = always_redraw(lambda: Text("Adj").scale(0.25).shift(
            [adj.get_center()[0], adj.get_center()[1] + 0.1, 0]))

        # Theta angle with label
        theta = always_redraw(lambda: Angle(Line(ORIGIN, RIGHT * 2), radius))
        theta_label = always_redraw(lambda: MathTex("\\theta").shift(
            theta.get_center() + RIGHT * 0.15 + UP * 0.1).scale(0.5))
        radius_label = always_redraw(lambda: MathTex("Hyp").shift(
            radius.get_center() + [-0.1, 0.1, 0]).scale(0.5).rotate(theta_tracker.get_value() * DEGREES))

        # Sin Text
        sin_text = MathTex("\\sin(\\theta) = \\frac{Opp}{Hyp}").next_to(
            area_text, RIGHT * 3)
        sin_text1 = MathTex(
            "\\sin(\\theta) = \\frac{Opp}{1} = Opp").next_to(sin_text, DOWN)

        # Cos Text
        cos_text = MathTex("\\cos(\\theta) = \\frac{Adj}{Hyp}").next_to(
            sin_text1, DOWN * 3)
        cos_text1 = MathTex(
            "\\cos(\\theta) = \\frac{Adj}{1} = Adj").next_to(cos_text, DOWN)

        # Tan Text
        tan_text = MathTex("\\tan(\\theta) = \\frac{Opp}{Adj}").next_to(
            area_text, LEFT * 3)
        tan_text1 = MathTex(
            "\\tan(\\theta) = \\frac{Opp}{Adj} = \\frac{\\sin(\\theta)}{\\cos(\\theta)}").next_to(tan_text, DOWN)

        # Tan Line and label
        tan = always_redraw(lambda: Line(
            radius.get_end(), [(1/cos(theta_tracker.get_value() * (PI/180))) * 2, 0, 0], color=RED))

        tan_label = always_redraw(lambda: MathTex("\\tan(\\theta)").shift(
            tan.get_center() + [0, 0.1, 0]).scale(0.5).rotate(theta_tracker.get_value() * DEGREES - 90 * DEGREES))

        # sin, cos and tan values
        sin_value = always_redraw(lambda: DecimalNumber(
            np.sin(theta_tracker.get_value() * (PI/180)),
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )).shift([sin_text1.get_x() + 0.1, sin_text1.get_y(), 0])
        cos_value = always_redraw(lambda: DecimalNumber(
            np.cos(theta_tracker.get_value() * (PI/180)),
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )).shift([cos_text1.get_x() + 0.1, cos_text1.get_y(), 0])
        tan_value = always_redraw(lambda: DecimalNumber(
            np.tan(theta_tracker.get_value() * (PI/180)),
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )).shift([tan_text1.get_x() + 0.2, tan_text1.get_y(), 0])

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

        self.play(Write(tan_text))
        self.play(Write(tan_text1))
        self.play(Create(tan), Write(tan_label))

        self.wait(1)

        for j in [sin_text1, cos_text1, tan_text1]:
            self.play(j.animate.become(
                MathTex(j.get_tex_string()[:15]).shift([j.get_x() - 1, j.get_y(), 0])))

        self.play(Write(sin_value), Write(cos_value), Write(tan_value))

        self.wait(1)

        # for i in [20, 60, 90, 120, 180, 240, 270, 300, 330]:
        #     self.play(theta_tracker.animate.set_value(i))
        #     self.wait(0.5)


class UnitCircle2(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True}).scale(2)

        self.add(plane)
