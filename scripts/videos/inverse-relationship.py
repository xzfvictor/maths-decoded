"""
Manim scene for the lesson `inverse-relationship`
(topic `l10a-aa-exp-log-inverse`).

Exponentials and logarithms are inverse functions: y = a^x and
x = log_a(y) undo each other. The animation draws both curves on the
same axes, shows the reflection across y = x line, and rejects the
mistake of thinking log takes the reciprocal of a^x.

Target duration: ~84.2 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class InverseRelationshipScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Exponentials and logarithms are inverses",
            "y = a^x and x = log_a(y) undo each other.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Plot y = 2^x and x = log_2(y) on the same axes (~26 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        ax = Axes(
            x_range=[-2.5, 4.5, 1],
            y_range=[-2, 2, 1],
            x_length=6.0,
            y_length=2.8,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2},
        ).move_to(BAND_CHART_CENTER + LEFT * 0.4 + DOWN * 0.2)
        beat_2 = beat_group(beat_2, ax)

        x_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(i, 0), DOWN, buff=0.15)
            for i in [-1, 1]
        ])
        y_lbls = VGroup(*[
            MathTex(str(i), font_size=22).next_to(ax.c2p(0, i), LEFT, buff=0.15)
            for i in [-1, 1]
        ])
        zero_origin = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DL, buff=0.1)
        beat_2 = beat_group(beat_2, x_lbls, y_lbls, zero_origin)

        # y = 2^x: only above x > some range, since for very negative x the
        # value is tiny. y > 0 always.
        exp_curve = ax.plot(
            lambda x: 2 ** x,
            x_range=[-2.0, 0.5],
            color=BLUE_TERM,
            stroke_width=4,
        )
        # x = log_2(y) means y = 2^x → swap axes. Equivalent: log curve
        # plotted as x = log_2(y) means y > 0; or equivalently plot
        # y = log_2(x) for x > 0.
        log_curve = ax.plot(
            lambda x: np.log2(x) if x > 0 else np.nan,
            x_range=[0.25, 4.0],
            color=ORANGE_TERM,
            stroke_width=4,
        )
        beat_2 = beat_group(beat_2, exp_curve, log_curve)

        self.play(Create(ax), run_time=1.2)
        self.play(
            *[Write(lbl) for lbl in x_lbls],
            *[Write(lbl) for lbl in y_lbls],
            Write(zero_origin),
            run_time=1.4,
        )
        self.play(Create(exp_curve), run_time=1.8)
        self.play(Create(log_curve), run_time=1.8)
        self.wait(1.5)

        # Curve labels.
        exp_lbl = MathTex(r"y = 2^{x}", color=BLUE_TERM).scale(0.9)
        exp_lbl.move_to(ax.c2p(-0.7, -0.6) + UP * 0.1)
        exp_lbl_bg = BackgroundRectangle(exp_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        exp_lbl_bg.move_to(exp_lbl.get_center())
        log_lbl = MathTex(r"y = \log_{2}(x)", color=ORANGE_TERM).scale(0.9)
        log_lbl.move_to(ax.c2p(3.0, -1.1))
        log_lbl_bg = BackgroundRectangle(log_lbl, color=BLACK, fill_opacity=0.95, buff=0.1)
        log_lbl_bg.move_to(log_lbl.get_center())
        beat_2 = beat_group(beat_2, exp_lbl, exp_lbl_bg, log_lbl, log_lbl_bg)
        self.play(
            FadeIn(exp_lbl_bg, run_time=0.3), FadeIn(exp_lbl, run_time=0.6),
            FadeIn(log_lbl_bg, run_time=0.3), FadeIn(log_lbl, run_time=0.6),
        )
        self.wait(2.0)

        # Reflection line y = x.
        diag = ax.plot(
            lambda x: x,
            x_range=[-2.0, 2.0],
            color=GREEN_OK,
            stroke_width=2,
        )
        beat_2 = beat_group(beat_2, diag)
        self.play(Create(diag, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Two identities (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head = Text("They undo each other", font_size=26, color=GREEN_OK)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_3 = beat_group(beat_3, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        id1 = MathTex(
            r"a^{\log_{a}(x)} = x",
            color=BLUE_TERM,
        ).scale(1.1)
        id1.move_to(BAND_CHART_CENTER + UP * 0.4)
        id1_bg = BackgroundRectangle(id1, color=BLACK, fill_opacity=1, buff=0.25)
        id1_bg.move_to(id1.get_center())
        beat_3 = beat_group(beat_3, id1, id1_bg)
        self.play(FadeIn(id1_bg, run_time=0.4), Write(id1, run_time=1.6))
        self.wait(1.0)

        id2 = MathTex(
            r"\log_{a}(a^{x}) = x",
            color=ORANGE_TERM,
        ).scale(1.1)
        id2.next_to(id1, DOWN, buff=0.5)
        id2_bg = BackgroundRectangle(id2, color=BLACK, fill_opacity=1, buff=0.25)
        id2_bg.move_to(id2.get_center())
        beat_3 = beat_group(beat_3, id2, id2_bg)
        self.play(FadeIn(id2_bg, run_time=0.4), Write(id2, run_time=1.6))
        self.wait(1.0)

        # Common point.
        common = MathTex(
            r"\text{Common point: } (1, 0),\ (0, 1)",
            color=GREEN_OK,
        ).scale(0.95)
        common.next_to(id2, DOWN, buff=0.5)
        common_bg = BackgroundRectangle(common, color=BLACK, fill_opacity=1, buff=0.2)
        common_bg.move_to(common.get_center())
        beat_3 = beat_group(beat_3, common, common_bg)
        self.play(FadeIn(common_bg, run_time=0.3), Write(common, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: log_a(x) = 1 / a^x (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\log_{2}(8) = \dfrac{1}{2^{8}} = \dfrac{1}{256}\;\text{?}",
            color=RED_REJECT,
        ).scale(0.95)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.6),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        ok = MathTex(
            r"\log_{2}(8) = 3,\quad \text{not } 1/256",
            color=GREEN_OK,
        ).scale(1.0)
        ok.next_to(wrong, DOWN, buff=0.5)
        ok_bg = BackgroundRectangle(ok, color=BLACK, fill_opacity=1, buff=0.2)
        ok_bg.move_to(ok.get_center())
        beat_4 = beat_group(beat_4, ok, ok_bg)
        self.play(FadeIn(ok_bg, run_time=0.3), Write(ok, run_time=1.4))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (final_wait=38 s, total ≈ 84.2 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"y = a^{x} \;\text{ and }\; x = \log_{a}(y) \;\text{ are inverses}",
            "Mirror across y = x; domains and ranges swap.",
            final_wait=38.0,
        )
