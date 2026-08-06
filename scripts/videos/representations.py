"""
Manim scene for the lesson `representations`
(topic `l9-st-sampling-methods`).

Sample variation and the choice of representation: two samples from the
same population give different numbers, and the chosen display can
change the impression.

Render target: ~70-80 s, final_wait=20 s.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RepresentationsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Sample variation & representation",
            "Same data, different stories — choose your display with care.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Two samples, different numbers
        # ──────────────────────────────────────────────────────────────────
        s1 = make_term_card("\\$52{,}000", "Sample 1 (n = 50)", BLUE_TERM)
        s2 = make_term_card("\\$55{,}000", "Sample 2 (n = 50)", TEAL_TERM)
        vs = MathTex("\\neq", color=WHITE).scale(1.5)
        pair = VGroup(s1, vs, s2).arrange(RIGHT, buff=0.5)
        pair.move_to(BAND_CHART_CENTER + UP * 0.4)
        for m in pair:
            m.set_z_index(2)

        self.play(
            FadeIn(s1, shift=UP * 0.2, run_time=1.0),
            FadeIn(vs, run_time=0.6),
            FadeIn(s2, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(1.0)

        note = Text(
            "Same population. Same method. Different numbers.",
            font_size=22,
            color=YELLOW,
        ).next_to(pair, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.5), FadeIn(note, run_time=1.0))
        self.wait(1.0)

        big = Text(
            "Bigger samples vary less.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(note, DOWN, buff=0.4)
        big_bg = BackgroundRectangle(big, color=BLACK, fill_opacity=0.95, buff=0.18)
        big_bg.move_to(big.get_center())
        self.play(FadeIn(big_bg, run_time=0.5), FadeIn(big, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(
            beat_group(pair, note, note_bg, big, big_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Truncated axis makes small changes look dramatic
        # ──────────────────────────────────────────────────────────────────
        # Two side-by-side bar charts of the same quarterly sales.
        title_a = Text("Axis from $0", font_size=20, color=BLUE_TERM)
        title_a.move_to(LEFT * 3.2 + UP * 1.5)
        title_a_bg = BackgroundRectangle(title_a, color=BLACK, fill_opacity=0.95, buff=0.12)
        title_a_bg.move_to(title_a.get_center())

        title_b = Text("Axis from smallest", font_size=20, color=RED_REJECT)
        title_b.move_to(RIGHT * 3.2 + UP * 1.5)
        title_b_bg = BackgroundRectangle(title_b, color=BLACK, fill_opacity=0.95, buff=0.12)
        title_b_bg.move_to(title_b.get_center())

        # Both charts share an axis line at y = -1.5 (bottom of safe area).
        # Bars for chart A (axis from 0): 100 vs 105 — barely visible.
        a_bar1 = Rectangle(
            width=0.6, height=1.6, color=BLUE_TERM, fill_opacity=0.85,
        ).move_to(LEFT * 3.5 + UP * (-1.5 + 0.8))
        a_bar2 = Rectangle(
            width=0.6, height=1.7, color=BLUE_TERM, fill_opacity=0.85,
        ).next_to(a_bar1, RIGHT, buff=0.4)
        a_axis = Line(LEFT * 4.2 + DOWN * 1.5, LEFT * 2.2 + DOWN * 1.5,
                      color=WHITE, stroke_width=2)

        # Bars for chart B (axis from 100): 100 vs 105 — looks huge.
        b_bar1 = Rectangle(
            width=0.6, height=0.4, color=RED_REJECT, fill_opacity=0.85,
        ).move_to(RIGHT * 3.0 + UP * (-1.5 + 0.2))
        b_bar2 = Rectangle(
            width=0.6, height=2.0, color=RED_REJECT, fill_opacity=0.85,
        ).next_to(b_bar1, RIGHT, buff=0.4)
        b_axis = Line(RIGHT * 3.7 + DOWN * 1.5, RIGHT * 1.7 + DOWN * 1.5,
                      color=WHITE, stroke_width=2)

        chart_a = VGroup(a_axis, a_bar1, a_bar2, title_a_bg, title_a)
        chart_b = VGroup(b_axis, b_bar1, b_bar2, title_b_bg, title_b)

        self.play(
            FadeIn(chart_a, run_time=1.0),
            FadeIn(chart_b, run_time=1.0),
        )
        self.wait(1.5)

        note2 = Text(
            "Same data. The right chart looks alarming — the left is honest.",
            font_size=22,
            color=YELLOW,
        ).move_to(BAND_CHART_CENTER + DOWN * 2.5)
        note2_bg = BackgroundRectangle(note2, color=BLACK, fill_opacity=0.95, buff=0.18)
        note2_bg.move_to(note2.get_center())
        self.play(FadeIn(note2_bg, run_time=0.5), FadeIn(note2, run_time=1.0))
        self.wait(2.0)
        self.play(FadeOut(
            beat_group(chart_a, chart_b, note2, note2_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Cherry-picking rejects the dishonest display
        # ──────────────────────────────────────────────────────────────────
        cherry = Text(
            "Cherry-picking: pick the time range that fits your story.",
            font_size=22,
            color=RED_REJECT,
        ).move_to(BAND_CHART_CENTER + UP * 0.4)
        cherry_bg = BackgroundRectangle(cherry, color=BLACK, fill_opacity=0.95, buff=0.18)
        cherry_bg.move_to(cherry.get_center())

        self.play(FadeIn(cherry_bg, run_time=0.5), FadeIn(cherry, run_time=1.0))
        self.wait(0.8)

        cross = Cross(cherry, color=RED_REJECT, stroke_width=5)
        reject_lbl = Text("not honest", font_size=22, color=RED_REJECT)
        reject_lbl.next_to(cherry, DOWN, buff=0.5)
        reject_bg = BackgroundRectangle(reject_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        reject_bg.move_to(reject_lbl.get_center())
        self.play(Create(cross, run_time=0.8))
        self.play(FadeIn(reject_bg, run_time=0.5), FadeIn(reject_lbl, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(
            beat_group(cherry, cherry_bg, cross, reject_lbl, reject_bg),
            run_time=0.8,
        ))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Display} \;=\; \text{part of the story}",
            "Sampling varies; choose honest axes and full data.",
            final_wait=20,
        )
