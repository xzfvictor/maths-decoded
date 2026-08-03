import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


def _build_boxplot(
    data: list[float],
    x_centre: float,
    y_bottom: float,
    y_top: float,
    color,
    *,
    ref_lo: float,
    ref_hi: float,
    x_width: float = 1.2,
) -> VGroup:
    """Build a vertical boxplot whose geometry maps a shared data
    range `[ref_lo, ref_hi]` onto the screen vertical band
    `[y_bottom, y_top]`. Two boxplots built with the same `ref_lo` /
    `ref_hi` get the same y-scale, so a tight cluster and a wide cluster
    line up correctly in the same frame.
    """
    arr = sorted(data)
    n = len(arr)

    def median(a):
        m = len(a)
        if m % 2 == 1:
            return float(a[m // 2])
        return 0.5 * (a[m // 2 - 1] + a[m // 2])

    half = arr[: n // 2]
    upper = arr[(n + 1) // 2 :]
    q1 = median(half)
    q3 = median(upper)
    med = median(arr)
    lo = arr[0]
    hi = arr[-1]

    span = ref_hi - ref_lo
    if span == 0:
        span = 1.0
    y_scale = (y_top - y_bottom) / span

    def to_y(v):
        return y_bottom + (v - ref_lo) * y_scale

    # Whiskers (single vertical line spanning the data range).
    whisker = Line(
        [x_centre, to_y(lo), 0],
        [x_centre, to_y(hi), 0],
        color=color, stroke_width=2,
    )
    # Cap lines at the extremes.
    cap_lo = Line(
        [x_centre - x_width / 2, to_y(lo), 0],
        [x_centre + x_width / 2, to_y(lo), 0],
        color=color, stroke_width=2,
    )
    cap_hi = Line(
        [x_centre - x_width / 2, to_y(hi), 0],
        [x_centre + x_width / 2, to_y(hi), 0],
        color=color, stroke_width=2,
    )

    # Box (Q1 to Q3).
    box = Rectangle(
        width=x_width,
        height=(q3 - q1) * y_scale,
        stroke_color=color, stroke_width=2,
        fill_color=color, fill_opacity=0.25,
    )
    box.move_to([x_centre, 0.5 * (to_y(q1) + to_y(q3)), 0])

    # Median bar across the box.
    median_bar = Line(
        [x_centre - x_width / 2, to_y(med), 0],
        [x_centre + x_width / 2, to_y(med), 0],
        color=WHITE, stroke_width=4,
    )
    return VGroup(whisker, cap_lo, cap_hi, box, median_bar)


class ComparingSpreadScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Same mean, different spread",
            "Centre alone never tells the whole story.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Two datasets with the same mean (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Two classes — same mean, different spread",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.6)

        # Same mean (50 / 7 ≈ 7.14), very different spreads.
        tight = [5, 6, 7, 7, 8, 8, 9]   # range 4, IQR 2
        loose = [2, 4, 6, 8, 8, 10, 12]  # range 10, IQR 6
        tight_mean = sum(tight) / len(tight)  # 50/7 ≈ 7.14
        loose_mean = sum(loose) / len(loose)  # 50/7 ≈ 7.14
        assert abs(tight_mean - loose_mean) < 1e-9

        tight_row = VGroup(*[MathTex(str(d), color=BLUE_TERM).scale(0.85)
                             for d in tight])
        tight_row.arrange(RIGHT, buff=0.22)
        tight_row.move_to(BAND_CHART_CENTER + UP * 0.6 + LEFT * 3.2)
        loose_row = VGroup(*[MathTex(str(d), color=TEAL_TERM).scale(0.85)
                             for d in loose])
        loose_row.arrange(RIGHT, buff=0.22)
        loose_row.move_to(BAND_CHART_CENTER + UP * 0.6 + RIGHT * 3.2)

        self.play(*[FadeIn(m, run_time=0.4) for m in tight_row], run_time=1.4)
        self.wait(0.4)
        self.play(*[FadeIn(m, run_time=0.4) for m in loose_row], run_time=1.4)
        self.wait(1.5)

        # Mean callouts — explicit "same mean" message.
        tight_mean_card = make_equation_card(
            rf"\bar{{x}} = {tight_mean:.2f}", color=BLUE_TERM, scale=0.75,
        )
        tight_mean_card.next_to(tight_row, DOWN, buff=0.4)
        loose_mean_card = make_equation_card(
            rf"\bar{{x}} = {loose_mean:.2f}", color=TEAL_TERM, scale=0.75,
        )
        loose_mean_card.next_to(loose_row, DOWN, buff=0.4)
        self.play(FadeIn(tight_mean_card, run_time=1.0))
        self.wait(0.4)
        self.play(FadeIn(loose_mean_card, run_time=1.0))
        self.wait(1.2)

        same_lbl = Text("Same mean — but look at the spread.",
                        font_size=22, color=ORANGE_TERM)
        same_lbl.move_to(BAND_CHART_CENTER + DOWN * 1.3)
        same_lbl_bg = BackgroundRectangle(same_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        same_lbl_bg.move_to(same_lbl.get_center())
        self.play(FadeIn(same_lbl_bg, run_time=0.4), FadeIn(same_lbl, run_time=1.2))
        self.wait(7.0)

        beat2 = beat_group(
            head, head_bg, tight_row, loose_row,
            tight_mean_card, loose_mean_card,
            same_lbl, same_lbl_bg,
        )
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Boxplots side by side (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Boxplots make the spread visible",
                     font_size=24, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.6)

        # Vertical band for the boxplots, safely inside y ∈ [-1.5, 1.8].
        y_top = 1.35
        y_bottom = -0.95
        ref_lo, ref_hi = 0, 14   # shared data scale (0 .. 14)

        left_x = -3.2
        right_x = 3.2
        span_x = 6.4  # distance between box centres

        def to_y(v):
            return y_bottom + (v - ref_lo) / (ref_hi - ref_lo) * (y_top - y_bottom)

        # Faint horizontal grid lines + numeric labels on the left margin.
        grid = VGroup()
        tick_labels = VGroup()
        for v in [1, 5, 7, 9, 13]:
            grid.add(Line(
                [left_x - 1.0, to_y(v), 0],
                [right_x + 1.0, to_y(v), 0],
                color="#444444", stroke_width=1, stroke_opacity=0.7,
            ))
            t_lbl = MathTex(str(v), color="#888888").scale(0.55)
            t_lbl.move_to([left_x - 1.35, to_y(v), 0])
            tick_labels.add(t_lbl)

        bp_tight = _build_boxplot(
            tight, x_centre=left_x,
            y_bottom=y_bottom, y_top=y_top,
            color=BLUE_TERM, ref_lo=ref_lo, ref_hi=ref_hi,
        )
        bp_loose = _build_boxplot(
            loose, x_centre=right_x,
            y_bottom=y_bottom, y_top=y_top,
            color=TEAL_TERM, ref_lo=ref_lo, ref_hi=ref_hi,
        )

        # Labels under the boxes.
        lbl_tight = Text("Class A", font_size=22, color=BLUE_TERM)
        lbl_tight.move_to([left_x, y_bottom - 0.25, 0])
        lbl_tight_bg = BackgroundRectangle(lbl_tight, color=BLACK,
                                           fill_opacity=0.95, buff=0.12)
        lbl_tight_bg.move_to(lbl_tight.get_center())

        lbl_loose = Text("Class B", font_size=22, color=TEAL_TERM)
        lbl_loose.move_to([right_x, y_bottom - 0.25, 0])
        lbl_loose_bg = BackgroundRectangle(lbl_loose, color=BLACK,
                                           fill_opacity=0.95, buff=0.12)
        lbl_loose_bg.move_to(lbl_loose.get_center())

        # Mean axis: horizontal line at y = mean_value across both boxplots.
        mean_value = tight_mean  # == loose_mean
        mean_line = Line(
            [left_x - 1.0, to_y(mean_value), 0],
            [right_x + 1.0, to_y(mean_value), 0],
            color=ORANGE_TERM, stroke_width=3,
        )
        mean_lbl = MathTex(rf"\bar{{x}} = {mean_value:.2f}",
                           color=ORANGE_TERM).scale(0.8)
        mean_lbl.next_to(mean_line, RIGHT, buff=0.25)
        mean_lbl_bg = BackgroundRectangle(mean_lbl, color=BLACK,
                                          fill_opacity=0.95, buff=0.12)
        mean_lbl_bg.move_to(mean_lbl.get_center())

        self.play(
            FadeIn(grid, run_time=1.0),
            FadeIn(tick_labels, run_time=1.0),
            Create(bp_tight, run_time=1.6),
        )
        self.wait(0.6)
        self.play(Create(bp_loose, run_time=1.6))
        self.wait(0.4)
        self.play(Create(mean_line, run_time=1.0))
        self.play(FadeIn(mean_lbl_bg, run_time=0.4),
                  FadeIn(mean_lbl, run_time=0.8))
        self.wait(0.4)
        self.play(
            FadeIn(lbl_tight_bg, run_time=0.3), FadeIn(lbl_tight, run_time=0.8),
            FadeIn(lbl_loose_bg, run_time=0.3), FadeIn(lbl_loose, run_time=0.8),
        )
        self.wait(4.0)

        # Hold the visual so the audience can read the contrast.
        self.wait(4.0)

        beat3 = beat_group(
            head3, head3_bg,
            bp_tight, bp_loose, grid, tick_labels,
            lbl_tight, lbl_tight_bg, lbl_loose, lbl_loose_bg,
            mean_line, mean_lbl, mean_lbl_bg,
        )
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Numbers: range and IQR (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Range and IQR tell the story numerically",
                     font_size=24, color=BLUE_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        a_range = max(tight) - min(tight)  # 4
        b_range = max(loose) - min(loose)  # 10
        a_iqr = 8 - 6                     # simple inclusive quartile method (2)
        b_iqr = 10 - 4                    # (6)

        row_a = make_equation_card(
            rf"\text{{Class A: range}} = {a_range},\;\; "
            rf"\text{{IQR}} = {a_iqr}",
            color=BLUE_TERM, scale=0.85,
        )
        row_a.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(row_a, shift=UP * 0.2, run_time=1.4))
        self.wait(1.0)

        row_b = make_equation_card(
            rf"\text{{Class B: range}} = {b_range},\;\; "
            rf"\text{{IQR}} = {b_iqr}",
            color=TEAL_TERM, scale=0.85,
        )
        row_b.move_to(BAND_CHART_CENTER + DOWN * 0.35)
        self.play(FadeIn(row_b, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        gap = make_equation_card(
            r"\text{Class B: IQR } = 3 \times \text{ Class A's}",
            color=ORANGE_TERM, scale=0.85,
        )
        gap.move_to(BAND_CHART_CENTER + DOWN * 1.1)
        self.play(FadeIn(gap, shift=UP * 0.2, run_time=1.4))
        self.wait(5.5)

        beat4 = beat_group(head4, head4_bg, row_a, row_b, gap)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 88.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Same mean} \;\not\!\!\!\Rightarrow\; \text{same spread}",
            "Always report the spread (range or IQR) alongside the mean.",
            final_wait=40.0,
        )
