"""
Manim scene for the lesson `interpret-justify`
(topic `l9-st-choosing-displays`).

Interpreting and justifying a display: state the axes, identify
centre / spread / shape / outliers, and tie the pattern back to
the context. We illustrate with a sample bar chart and a histogram
example.

Target duration: ~69.48 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class InterpretJustifyScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Interpreting and justifying a display",
            "Axes first, then centre, spread, shape — and the context.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Read the axes (template) (~12 s)
        # ──────────────────────────────────────────────────────────────────
        axes_card = make_term_card(
            r"\text{Axes}", r"\text{names + units}", BLUE_TERM,
        )
        axes_card.move_to(BAND_CHART_CENTER + UP * 1.4)
        self.play(FadeIn(axes_card, shift=UP * 0.3, run_time=1.4))
        self.wait(2.0)

        # A simple bar chart to make the point concrete.
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 12, 4],
            x_length=5.5, y_length=2.6,
            axis_config={"include_numbers": True, "font_size": 18},
            tips=False,
        )
        axes.move_to(BAND_CHART_CENTER + DOWN * 0.6)

        bar_heights = [3, 7, 5, 10, 4]
        bars = VGroup()
        bar_colors = [BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK, YELLOW]
        for i, h in enumerate(bar_heights):
            b = Rectangle(
                width=0.6, height=h * 0.2,
                fill_color=bar_colors[i], fill_opacity=0.85,
                stroke_color=bar_colors[i], stroke_width=2,
            )
            b.align_to(axes.c2p(i + 0.7, 0), DL)
            bars.add(b)

        self.play(Create(axes, run_time=1.2))
        self.wait(0.4)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bars], lag_ratio=0.2),
            run_time=1.5,
        )
        self.wait(2.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — CSSS: centre, spread, shape, story (~18 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = VGroup(axes_card, axes, bars)
        self.play(FadeOut(beat2_group, run_time=1.3))

        # Four-pillar list.
        pillar_specs = [
            (r"\text{Centre}",   r"\text{mean / median}",   BLUE_TERM),
            (r"\text{Spread}",   r"\text{range / IQR}",     TEAL_TERM),
            (r"\text{Shape}",    r"\text{skew / modality}", ORANGE_TERM),
            (r"\text{Story}",    r"\text{back to context}", GREEN_OK),
        ]
        rows = VGroup()
        for name, sub, color in pillar_specs:
            name_tex = MathTex(name, color=color).scale(0.9)
            sub_tex  = MathTex(sub, color=color).scale(0.7)
            sub_tex.next_to(name_tex, RIGHT, buff=0.4)
            row = VGroup(name_tex, sub_tex)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.move_to(BAND_CHART_CENTER + UP * 0.4)

        for r in rows:
            bg = BackgroundRectangle(r, color=BLACK, fill_opacity=0.95, buff=0.18)
            bg.move_to(r.get_center())
            r.bg = bg
            self.play(FadeIn(bg, run_time=0.3), FadeIn(r, run_time=0.8))
            self.wait(0.7)
        self.wait(2.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "looks symmetric" with no numbers (~8 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\text{``looks symmetric''} \;\Rightarrow\; \text{?}",
            color=RED_REJECT,
        ).scale(1.0)
        bad.move_to(BAND_CHART_CENTER + UP * 0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.4))
        self.wait(1.0)

        why = Text(
            "Always name centre, spread, shape with numbers.",
            font_size=22, color=RED_REJECT,
        )
        why.next_to(bad, DOWN, buff=0.55)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=0.8))
        self.wait(1.5)

        beat4_group = VGroup(bad, bad_bg, why, why_bg, cross, rows, *[r.bg for r in rows])
        self.play(FadeOut(beat4_group, run_time=1.3))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; total ≈ 69 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{State axes, centre, spread, shape — then the story}",
            "A claim is justified when the numbers back it up.",
            final_wait=26.0,
        )
