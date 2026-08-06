import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SimilarityAspectsScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Similarity after enlargement", "What stays the same — and what scales")

        # Beat 2: preserved shape facts.
        beat = None
        same = VGroup(
            Text("same angles", font_size=24, color=GREEN_OK),
            Text("parallel lines stay parallel", font_size=24, color=GREEN_OK),
            Text("a circle stays a circle", font_size=24, color=GREEN_OK),
        ).arrange(DOWN, buff=0.32).move_to(LEFT * 2.3 + DOWN * 0.05)
        same_bg = BackgroundRectangle(same, color=BLACK, fill_opacity=1, buff=0.2); same_bg.move_to(same.get_center())
        circle = Circle(radius=0.65, color=BLUE_TERM).move_to(RIGHT * 2.7 + DOWN * 0.05)
        circle2 = Circle(radius=1.15, color=TEAL_TERM).move_to(RIGHT * 2.7 + DOWN * 0.05)
        similar = Text("same shape", font_size=22, color=TEAL_TERM).move_to(RIGHT * 2.7 + DOWN * 1.2)
        sim_bg = BackgroundRectangle(similar, color=BLACK, fill_opacity=0.95, buff=0.16); sim_bg.move_to(similar.get_center())
        beat = beat_group(beat, same_bg, same, circle, circle2, sim_bg, similar)
        self.play(FadeIn(same_bg), LaggedStart(*[FadeIn(x) for x in same], lag_ratio=0.16), Create(circle)); self.wait(2); self.play(Create(circle2)); self.play(FadeIn(sim_bg), FadeIn(similar)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 3: k, k squared, k cubed, with the 1 cm square and cube intuition.
        beat = None
        scales = VGroup(
            MathTex(r"\text{lengths}\ \times k", color=BLUE_TERM),
            MathTex(r"\text{areas}\ \times k^2", color=TEAL_TERM),
            MathTex(r"\text{volumes}\ \times k^3", color=ORANGE_TERM),
        ).arrange(DOWN, buff=0.35).scale(0.95).move_to(LEFT * 2.3 + DOWN * 0.05)
        scales_bg = BackgroundRectangle(scales, color=BLACK, fill_opacity=1, buff=0.2); scales_bg.move_to(scales.get_center())
        square = Square(side_length=1.0, color=BLUE_TERM).move_to(RIGHT * 2.4 + UP * 0.45)
        sq_label = Text("1 cm × 1 cm", font_size=20, color=BLUE_TERM).next_to(square, DOWN, buff=0.2)
        sq_note = MathTex(r"k\times k\text{ little squares}\Rightarrow k^2", color=TEAL_TERM).scale(0.72).move_to(RIGHT * 2.35 + DOWN * 0.95)
        sq_bg = BackgroundRectangle(VGroup(sq_label, sq_note), color=BLACK, fill_opacity=0.95, buff=0.16); sq_bg.move_to(VGroup(sq_label, sq_note).get_center())
        beat = beat_group(beat, scales_bg, scales, square, sq_label, sq_note, sq_bg)
        self.play(FadeIn(scales_bg), LaggedStart(*[Write(x) for x in scales], lag_ratio=0.18)); self.wait(2); self.play(Create(square), FadeIn(sq_label)); self.play(FadeIn(sq_bg), Write(sq_note)); self.wait(6)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 4: reject the linear-only rule; area and volume grow by powers.
        beat = None
        bad = Text("\"Area and volume scale by k too.\"", font_size=24).move_to(UP * 0.45)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.18); bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        fix = MathTex(r"\text{lengths: }k\qquad\text{areas: }k^2\qquad\text{volumes: }k^3", color=GREEN_OK).scale(0.82).move_to(DOWN * 0.7)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.19); fix_bg.move_to(fix.get_center())
        beat = beat_group(beat, bad_bg, bad, cross, fix_bg, fix)
        self.play(FadeIn(bad_bg), FadeIn(bad)); self.wait(1.5); self.play(Create(cross)); self.wait(0.6); self.play(FadeIn(fix_bg), Write(fix)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"\text{lengths}\times k,\quad \text{areas}\times k^2,\quad \text{volumes}\times k^3", "Angles and shape stay the same: the image is similar.", final_wait=20)
