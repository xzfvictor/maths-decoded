"""
Manim scene for the lesson `test-refine`
(topic `l9-sp-geometric-algorithms`).

An algorithm is finished only when it works on every case it's meant
to handle. The animation walks the test → check → revise loop on a
broken angle-bisector, then lists edge cases worth trying, and rejects
"rewriting from scratch on every fail".

Target duration: ~95.4 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class TestRefineScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Testing, refining, evaluating",
            "Run, check, revise — until it works for every case.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: a broken angle bisector (~24 s)
        # ──────────────────────────────────────────────────────────────────
        # An angle ABC at the centre.
        apex = Dot(BAND_CHART_CENTER + UP * 0.8, color=WHITE)
        ray_a = Line(BAND_CHART_CENTER + UP * 0.8, BAND_CHART_CENTER + DOWN * 1.5 + LEFT * 2.0,
                     color=BLUE_TERM, stroke_width=4)
        ray_c = Line(BAND_CHART_CENTER + UP * 0.8, BAND_CHART_CENTER + DOWN * 1.5 + RIGHT * 2.0,
                     color=TEAL_TERM, stroke_width=4)
        b_lbl = MathTex("B", color=WHITE).scale(0.9).next_to(apex, UP, buff=0.2)
        b_lbl_bg = BackgroundRectangle(b_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        b_lbl_bg.move_to(b_lbl.get_center())
        angle_60 = MathTex(r"60^{\circ}", color=WHITE).scale(0.9).move_to(
            BAND_CHART_CENTER + DOWN * 0.2 + RIGHT * 0.0
        )
        angle_bg = BackgroundRectangle(angle_60, color=BLACK, fill_opacity=0.95, buff=0.12)
        angle_bg.move_to(angle_60.get_center())

        self.play(
            Create(ray_a, run_time=1.0),
            Create(ray_c, run_time=1.0),
            FadeIn(apex, run_time=0.5),
            FadeIn(b_lbl_bg, run_time=0.3),
            FadeIn(b_lbl, run_time=0.5),
            FadeIn(angle_bg, run_time=0.3),
            FadeIn(angle_60, run_time=0.8),
        )
        self.wait(2.0)

        # Run the algorithm: result lands off-centre, splitting into 28° and 32°.
        bad_split = MathTex(
            r"\text{Result: } 28^{\circ}\,+\,32^{\circ} \;(\text{not equal})",
            color=RED_REJECT,
        ).scale(1.0)
        bad_split.move_to(BAND_CHART_CENTER + DOWN * 1.2)
        bad_split_bg = BackgroundRectangle(bad_split, color=BLACK, fill_opacity=1, buff=0.22)
        bad_split_bg.move_to(bad_split.get_center())
        self.play(FadeIn(bad_split_bg, run_time=0.4), FadeIn(bad_split, run_time=1.6))
        self.wait(2.5)

        diagnosis = Text(
            "Compass radius was changed between arcs — use the SAME radius both times.",
            font_size=20, color=GREEN_OK,
        ).next_to(bad_split, DOWN, buff=0.5)
        diag_bg = BackgroundRectangle(diagnosis, color=BLACK, fill_opacity=0.95, buff=0.16)
        diag_bg.move_to(diagnosis.get_center())
        self.play(FadeIn(diag_bg, run_time=0.4), FadeIn(diagnosis, run_time=1.4))
        self.wait(3.0)

        beat2 = VGroup(apex, ray_a, ray_c, b_lbl, b_lbl_bg, angle_60, angle_bg,
                       bad_split, bad_split_bg, diagnosis, diag_bg)
        self.play(FadeOut(beat2, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The testing loop (~24 s)
        # ──────────────────────────────────────────────────────────────────
        step1 = make_term_card(r"1.\,\text{Run}",     r"\text{on a sample}", BLUE_TERM)
        step2 = make_term_card(r"2.\,\text{Check}",   r"\text{against the goal}", TEAL_TERM)
        step3 = make_term_card(r"3.\,\text{Revise}",  r"\text{fix one step}", ORANGE_TERM)
        step4 = make_term_card(r"4.\,\text{Re-test}", r"\text{edge cases too}", GREEN_OK)
        loop = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.32)
        loop.move_to(BAND_CHART_CENTER + UP * 0.6)
        for s in loop:
            s.set_z_index(2)

        for s in loop:
            self.play(FadeIn(s, shift=RIGHT * 0.15, run_time=0.8))
            self.wait(0.8)

        # Edge-cases note.
        edges = Text(
            "Edge cases to try: very small angles, equal sides, a point on the line.",
            font_size=20, color=GREEN_OK,
        ).next_to(loop, DOWN, buff=0.55)
        edges_bg = BackgroundRectangle(edges, color=BLACK, fill_opacity=0.95, buff=0.16)
        edges_bg.move_to(edges.get_center())
        self.play(FadeIn(edges_bg, run_time=0.4), FadeIn(edges, run_time=1.6))
        self.wait(4.5)

        beat3 = VGroup(loop, edges, edges_bg)
        self.play(FadeOut(beat3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: start over from scratch (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            "A failed test → rewrite the algorithm from scratch.",
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            "Change ONE step, re-test — narrow down, don't restart.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(2.0)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 95.4 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Run} \;\to\; \text{Check} \;\to\; \text{Revise} \;\to\; \text{Re-test}",
            "Refine one step at a time — try edge cases before declaring it done.",
            final_wait=36.0,
        )
