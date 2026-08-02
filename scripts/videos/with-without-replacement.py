"""
Manim scene for the lesson `with-without-replacement`
(topic `l9-p-two-step-experiments`).

With replacement: the bag is restored, so probabilities stay the same at
each step. Without replacement: the bag shrinks, so the second branch's
probabilities change. The animation builds the two cases side-by-side on
a 3R/2B bag, contrasts the denominators, and rejects "with and without
look the same".

Target duration: ~107.8 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class WithWithoutReplacementScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "With vs. without replacement",
            "With replacement: probabilities stay the same. Without: they change.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete WITH replacement: coin twice (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text(
            "Case 1 — WITH replacement",
            font_size=26, color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 2.0)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=1, buff=0.18)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.5)

        # Step 1 prob.
        p1 = MathTex(
            r"\Pr(R_1) \;=\; \dfrac{3}{5}",
            color=BLUE_TERM,
        ).scale(1.0)
        p1.move_to(BAND_CHART_CENTER + UP * 0.7)
        p1_bg = BackgroundRectangle(p1, color=BLACK, fill_opacity=1, buff=0.22)
        p1_bg.move_to(p1.get_center())
        self.play(FadeIn(p1_bg, run_time=0.4), FadeIn(p1, run_time=1.4))
        self.wait(1.5)

        # Arrow showing "restore".
        arrow = MathTex(r"\longrightarrow", color=WHITE).scale(1.5)
        arrow.next_to(p1, DOWN, buff=0.5)
        self.play(FadeIn(arrow, run_time=0.6))
        self.wait(0.5)

        restore = Text(
            "ball returned — bag still has 3 red, 2 blue",
            font_size=22, color=GREEN_OK,
        ).next_to(arrow, RIGHT, buff=0.3)
        restore_bg = BackgroundRectangle(restore, color=BLACK, fill_opacity=0.95, buff=0.15)
        restore_bg.move_to(restore.get_center())
        self.play(FadeIn(restore_bg, run_time=0.4), FadeIn(restore, run_time=1.2))
        self.wait(2.5)

        # Step 2 prob.
        p2 = MathTex(
            r"\Pr(R_2) \;=\; \dfrac{3}{5}\;=\;\Pr(R_1)",
            color=GREEN_OK,
        ).scale(1.0)
        p2.next_to(arrow, DOWN, buff=0.5)
        p2_bg = BackgroundRectangle(p2, color=BLACK, fill_opacity=1, buff=0.22)
        p2_bg.move_to(p2.get_center())
        self.play(FadeIn(p2_bg, run_time=0.4), FadeIn(p2, run_time=1.4))
        self.wait(2.5)

        # Joint.
        joint = MathTex(
            r"\Pr(\text{both R}) \;=\; \dfrac{3}{5} \times \dfrac{3}{5} \;=\; \dfrac{9}{25}",
            color=GREEN_OK,
        ).scale(1.0)
        joint.next_to(p2, DOWN, buff=0.55)
        joint_bg = BackgroundRectangle(joint, color=BLACK, fill_opacity=1, buff=0.22)
        joint_bg.move_to(joint.get_center())
        self.play(FadeIn(joint_bg, run_time=0.4), FadeIn(joint, run_time=1.8))
        self.wait(3.5)

        beat2 = VGroup(head, head_bg, p1, p1_bg, arrow, restore, restore_bg,
                       p2, p2_bg, joint, joint_bg)
        self.play(FadeOut(beat2, run_time=1.5))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete WITHOUT replacement (~26 s)
        # ──────────────────────────────────────────────────────────────────
        head2 = Text(
            "Case 2 — WITHOUT replacement",
            font_size=26, color=ORANGE_TERM,
        ).move_to(BAND_CHART_CENTER + UP * 2.0)
        head2_bg = BackgroundRectangle(head2, color=BLACK, fill_opacity=1, buff=0.18)
        head2_bg.move_to(head2.get_center())
        self.play(FadeIn(head2_bg, run_time=0.4), FadeIn(head2, run_time=1.0))
        self.wait(1.5)

        # Same starting probability — bag has 3R/2B.
        p1b = MathTex(
            r"\Pr(R_1) \;=\; \dfrac{3}{5}",
            color=ORANGE_TERM,
        ).scale(1.0)
        p1b.move_to(BAND_CHART_CENTER + UP * 0.7)
        p1b_bg = BackgroundRectangle(p1b, color=BLACK, fill_opacity=1, buff=0.22)
        p1b_bg.move_to(p1b.get_center())
        self.play(FadeIn(p1b_bg, run_time=0.4), FadeIn(p1b, run_time=1.4))
        self.wait(1.5)

        # Crossed-out bag showing the shrinkage.
        bag_note = Text(
            "ball NOT returned — bag now has 2 red, 2 blue (4 total)",
            font_size=22, color=RED_REJECT,
        ).move_to(BAND_CHART_CENTER + UP * 0.0)
        bag_bg = BackgroundRectangle(bag_note, color=BLACK, fill_opacity=0.95, buff=0.16)
        bag_bg.move_to(bag_note.get_center())
        self.play(FadeIn(bag_bg, run_time=0.4), FadeIn(bag_note, run_time=1.4))
        self.wait(2.0)

        # Step 2 prob — denominator shrinks.
        p2b = MathTex(
            r"\Pr(R_2 \mid R_1) \;=\; \dfrac{2}{4} \;=\; \dfrac{1}{2}",
            color=ORANGE_TERM,
        ).scale(1.0)
        p2b.move_to(BAND_CHART_CENTER + DOWN * 0.85)
        p2b_bg = BackgroundRectangle(p2b, color=BLACK, fill_opacity=1, buff=0.22)
        p2b_bg.move_to(p2b.get_center())
        self.play(FadeIn(p2b_bg, run_time=0.4), FadeIn(p2b, run_time=1.4))
        self.wait(2.5)

        joint2 = MathTex(
            r"\Pr(\text{both R}) \;=\; \dfrac{3}{5} \times \dfrac{2}{4} \;=\; \dfrac{6}{20} \;=\; \dfrac{3}{10}",
            color=GREEN_OK,
        ).scale(1.0)
        joint2.move_to(BAND_CHART_CENTER + DOWN * 1.8)
        joint2_bg = BackgroundRectangle(joint2, color=BLACK, fill_opacity=1, buff=0.22)
        joint2_bg.move_to(joint2.get_center())
        self.play(FadeIn(joint2_bg, run_time=0.4), FadeIn(joint2, run_time=2.2))
        self.wait(4.0)

        beat3 = VGroup(head2, head2_bg, p1b, p1b_bg, bag_note, bag_bg, p2b, p2b_bg,
                       joint2, joint2_bg)
        self.play(FadeOut(beat3, run_time=1.5))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "same formula both ways" (~13 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            '"With" and "without" replacement use the same numbers.',
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
            "Without replacement: denominator shrinks from 5 to 4.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(3.5)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 107.8 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Without replacement} \;:\; \text{denominator shrinks by } 1",
            "With replacement: probabilities repeat. Without: they change.",
            final_wait=42.0,
        )
