import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SineRuleScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "The sine rule",
            "a/sin A = b/sin B = c/sin C — link sides and opposite angles.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: 30°-60°-90° triangle, find missing side (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Worked example", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        given = make_equation_card(
            r"a = 5,\ A = 30^\circ,\ B = 60^\circ,\ \text{find } b",
            color=BLUE_TERM, scale=0.9,
        )
        given.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(given, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        # Rearrange sine rule to isolate b.
        solve = make_equation_card(
            r"b \;=\; \dfrac{a\,\sin B}{\sin A}",
            color=GREEN_OK, scale=1.1,
        )
        solve.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        self.play(FadeIn(solve, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        ans = make_equation_card(
            r"= \dfrac{5\sin 60^\circ}{\sin 30^\circ} \approx 8.66",
            color=GREEN_OK, scale=0.95,
        )
        ans.move_to(BAND_CHART_CENTER + DOWN * 1.05)
        self.play(FadeIn(ans, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, given, solve, ans)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The general rule (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("General rule", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        eq = make_equation_card(
            r"\dfrac{a}{\sin A} \;=\; \dfrac{b}{\sin B} \;=\; \dfrac{c}{\sin C}",
            color=GREEN_OK, scale=1.1,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(eq, shift=UP * 0.2, run_time=1.8))
        self.wait(2.5)

        note = Text("Ratio is constant for the triangle.",
                    font_size=20, color=WHITE)
        note.next_to(eq, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, eq, note, note_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Use case: given a side and an angle pair, find missing side (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Use when", font_size=26, color=TEAL_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        cases = VGroup()
        for i, txt in enumerate([
            r"\text{a side and its opposite angle}",
            r"\text{two angles and any side}",
            r"\text{two sides and a non-included angle}",
        ]):
            row = make_equation_card(txt, color=TEAL_TERM, scale=0.85)
            row.move_to(BAND_CHART_CENTER + UP * 0.65 + DOWN * i * 0.75)
            cases.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.2, run_time=0.7) for r in cases],
                        lag_ratio=0.3),
        )
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, cases)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 99.0 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\dfrac{a}{\sin A} \;=\; \dfrac{b}{\sin B} \;=\; \dfrac{c}{\sin C}",
            "Side over the sine of its opposite angle is constant.",
            final_wait=45.0,
        )