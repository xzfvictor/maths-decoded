"""
Manim scene for the lesson `profit-loss`
(topic `l8-n-modelling-rationals-percentages`).

Profit and loss are always measured against the cost price. The formulas
turn the difference into a percentage of what was paid.

Target duration: ~98 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class ProfitLossScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Profit and loss as percentages",
            "Always measured against the cost price",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Profit example: hat $24 → $30, profit 25% (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat2 = VGroup()
        head = Text("1. Profit:  $24  →  $30",
                    font_size=24, color=BLUE_TERM)
        # Anchor the heading at the chart center (y = 0) so its
        # BackgroundRectangle never reaches up into the subtitle's band.
        head.move_to(BAND_CHART_CENTER)
        head_bg = BackgroundRectangle(head, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat2.add(head, head_bg)

        # Step 1: profit = sell - cost
        s1 = MathTex(
            r"\text{profit} = 30 - 24 = 6",
            color=BLUE_TERM,
        ).scale(1.1)
        s1.next_to(head, DOWN, buff=0.4)
        s1_bg = BackgroundRectangle(s1, color=BLACK, fill_opacity=1, buff=0.25)
        s1_bg.move_to(s1.get_center())
        beat2.add(s1, s1_bg)

        self.play(
            FadeIn(head_bg, run_time=0.4),
            FadeIn(head, run_time=0.9),
            FadeIn(s1_bg, run_time=0.4),
            Write(s1, run_time=1.6),
        )
        self.wait(2.5)

        # Step 2: divide by cost
        s2 = MathTex(
            r"\dfrac{6}{24} = 0.25 = 25\%",
            color=GREEN_OK,
        ).scale(1.15)
        s2.next_to(s1, DOWN, buff=0.5)
        s2_bg = BackgroundRectangle(s2, color=BLACK, fill_opacity=1, buff=0.25)
        s2_bg.move_to(s2.get_center())
        beat2.add(s2, s2_bg)

        self.play(
            FadeIn(s2_bg, run_time=0.4),
            Write(s2, run_time=1.6),
        )
        self.wait(5.0)

        self.play(FadeOut(beat2, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Loss example: bike $400 → $340, loss 15% (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat3 = VGroup()
        head2 = Text("2. Loss:  $400  →  $340",
                     font_size=24, color=ORANGE_TERM)
        # Same anchor as beat 2's head: chart center, stack below.
        head2.move_to(BAND_CHART_CENTER)
        head2_bg = BackgroundRectangle(head2, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head2_bg.move_to(head2.get_center())
        beat3.add(head2, head2_bg)

        t1 = MathTex(
            r"\text{loss} = 400 - 340 = 60",
            color=ORANGE_TERM,
        ).scale(1.1)
        t1.next_to(head2, DOWN, buff=0.4)
        t1_bg = BackgroundRectangle(t1, color=BLACK, fill_opacity=1, buff=0.25)
        t1_bg.move_to(t1.get_center())
        beat3.add(t1, t1_bg)

        self.play(
            FadeIn(head2_bg, run_time=0.4),
            FadeIn(head2, run_time=0.9),
            FadeIn(t1_bg, run_time=0.4),
            Write(t1, run_time=1.4),
        )
        self.wait(2.0)

        t2 = MathTex(
            r"\dfrac{60}{400} = 0.15 = 15\%",
            color=GREEN_OK,
        ).scale(1.15)
        t2.next_to(t1, DOWN, buff=0.5)
        t2_bg = BackgroundRectangle(t2, color=BLACK, fill_opacity=1, buff=0.25)
        t2_bg.move_to(t2.get_center())
        beat3.add(t2, t2_bg)

        self.play(
            FadeIn(t2_bg, run_time=0.4),
            Write(t2, run_time=1.4),
        )
        self.wait(2.5)

        # Why percent? Compare $50 on $50 vs $50 on $5000
        why = Text(
            "$50 profit on $50  =  100%   vs   $50 profit on $5000  =  1%",
            font_size=20,
            color=GREEN_OK,
        ).next_to(t2, DOWN, buff=0.6)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        beat3.add(why, why_bg)

        self.play(
            FadeIn(why_bg, run_time=0.4),
            FadeIn(why, run_time=1.2),
        )
        self.wait(4.0)

        self.play(FadeOut(beat3, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Warning: divide by cost, not selling price (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat4 = VGroup()
        head3 = Text("Watch out", font_size=24, color=RED_REJECT)
        # Same chart-center anchor as the previous beat headings.
        head3.move_to(BAND_CHART_CENTER)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        beat4.add(head3, head3_bg)

        warn = MathTex(
            r"\text{Always divide by the } \textbf{cost price}",
            color=RED_REJECT,
        ).scale(1.0)
        warn.next_to(head3, DOWN, buff=0.4)
        warn_bg = BackgroundRectangle(warn, color=BLACK, fill_opacity=1, buff=0.25)
        warn_bg.move_to(warn.get_center())
        beat4.add(warn, warn_bg)

        self.play(
            FadeIn(head3_bg, run_time=0.4),
            FadeIn(head3, run_time=0.9),
            FadeIn(warn_bg, run_time=0.4),
            Write(warn, run_time=1.6),
        )
        self.wait(2.5)

        # Cross a wrong calculation
        bad = MathTex(
            r"\dfrac{6}{30} = 20\% \quad (\text{wrong!})",
            color=RED_REJECT,
        ).scale(0.95)
        bad.next_to(warn, DOWN, buff=0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.22)
        bad_bg.move_to(bad.get_center())
        beat4.add(bad, bad_bg)

        cross_bad = None
        self.play(
            FadeIn(bad_bg, run_time=0.4),
            Write(bad, run_time=1.2),
        )
        self.wait(0.6)
        cross_bad = Cross(bad, color=RED_REJECT, stroke_width=4)
        beat4.add(cross_bad)
        self.play(Create(cross_bad, run_time=0.8))
        self.wait(3.0)

        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~38 s, total ≈ 98 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Profit \%} \;=\; \dfrac{\text{sell} - \text{cost}}{\text{cost}} \times 100",
            "Always divide by the cost price — that's your investment.",
            final_wait=38.0,
        )
