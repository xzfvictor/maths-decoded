import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class EnlargementBasicsScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Enlargement basics", "Every point travels from a centre by scale factor k")

        # Beat 2: a point, centre, ray, and a positive scale factor.
        beat = None
        centre = Dot(LEFT * 2.8 + DOWN * 0.65, color=ORANGE_TERM)
        c_label = MathTex("C", color=ORANGE_TERM).scale(0.8).next_to(centre, DOWN, buff=0.18)
        c_bg = BackgroundRectangle(c_label, color=BLACK, fill_opacity=0.95, buff=0.08); c_bg.move_to(c_label.get_center())
        point = Dot(LEFT * 0.9 + UP * 0.25, color=BLUE_TERM)
        p_label = MathTex("P", color=BLUE_TERM).scale(0.8).next_to(point, RIGHT, buff=0.18)
        p_bg = BackgroundRectangle(p_label, color=BLACK, fill_opacity=0.95, buff=0.08); p_bg.move_to(p_label.get_center())
        image = Dot(RIGHT * 2.9 + UP * 1.15, color=TEAL_TERM)
        i_label = MathTex("P'", color=TEAL_TERM).scale(0.8).move_to(image.get_center() + UP * 0.22 + RIGHT * 0.12)
        i_bg = BackgroundRectangle(i_label, color=BLACK, fill_opacity=0.95, buff=0.08); i_bg.move_to(i_label.get_center())
        ray = Line(centre.get_center(), image.get_center(), color=WHITE)
        labels = VGroup(MathTex(r"CP'=k\cdot CP", color=GREEN_OK).scale(0.95).move_to(UP * 0.95), MathTex(r"k=2", color=TEAL_TERM).scale(0.9).move_to(DOWN * 0.95))
        bg = BackgroundRectangle(labels, color=BLACK, fill_opacity=0.95, buff=0.18); bg.move_to(labels.get_center())
        beat = beat_group(beat, centre, c_bg, c_label, point, p_bg, p_label, image, i_bg, i_label, ray, labels, bg)
        self.play(FadeIn(bg), FadeIn(labels), FadeIn(centre), FadeIn(c_bg), FadeIn(c_label), FadeIn(point), FadeIn(p_bg), FadeIn(p_label), Create(ray), FadeIn(image), FadeIn(i_bg), FadeIn(i_label)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 3: the recipe plus a coordinate example.
        beat = None
        recipe = VGroup(Text("1  choose centre C", font_size=22, color=ORANGE_TERM), Text("2  choose k", font_size=22, color=TEAL_TERM), Text("3  move each point along its ray", font_size=22, color=BLUE_TERM)).arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to(LEFT * 2.0 + UP * 0.35)
        recipe_bg = BackgroundRectangle(recipe, color=BLACK, fill_opacity=1, buff=0.2); recipe_bg.move_to(recipe.get_center())
        example = VGroup(MathTex(r"P=(1,2)", color=BLUE_TERM), MathTex(r"C=(0,0),\ k=2", color=ORANGE_TERM), MathTex(r"P'=(2,4)", color=TEAL_TERM)).arrange(DOWN, buff=0.38).scale(0.9).move_to(RIGHT * 2.5 + UP * 0.2)
        ex_bg = BackgroundRectangle(example, color=BLACK, fill_opacity=1, buff=0.2); ex_bg.move_to(example.get_center())
        beat = beat_group(beat, recipe_bg, recipe, ex_bg, example)
        self.play(FadeIn(recipe_bg), LaggedStart(*[FadeIn(x) for x in recipe], lag_ratio=0.18)); self.wait(3); self.play(FadeIn(ex_bg), LaggedStart(*[Write(x) for x in example], lag_ratio=0.18)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 4: reject the idea that an enlargement changes the shape.
        beat = None
        bad = Text("\"An enlargement distorts the shape.\"", font_size=25).move_to(UP * 0.45)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.18); bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        fix = Text("No: angles and orientation are preserved when k is positive.", font_size=20, color=GREEN_OK).move_to(DOWN * 0.7)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.17); fix_bg.move_to(fix.get_center())
        beat = beat_group(beat, bad_bg, bad, cross, fix_bg, fix)
        self.play(FadeIn(bad_bg), FadeIn(bad)); self.wait(1.5)
        # Let the bad statement sit before drawing the strike-through so
        # the two animations don't fight for the same vertical band.
        self.wait(1.0)
        self.play(Create(cross)); self.wait(1.0)
        self.play(FadeIn(fix_bg), FadeIn(fix)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"CP'=k\,CP\quad\text{along the ray from }C", "An enlargement keeps the shape similar while scaling it.", final_wait=20)
