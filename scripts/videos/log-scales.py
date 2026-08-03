"""
Manim scene for the lesson `log-scales`
(topic `l10a-an-logarithms-scales`).

Logarithms turn huge exponential ranges into compact readable scales.
The animation uses the Richter scale (a 10^5 fold jump from mag 1 to
mag 6) to show why log plots compress data that linear axes cannot.

Target duration: ~80.6 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class LogScalesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Logarithmic scales",
            "Compress huge ranges: a jump of 1 on the log axis is x10.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: Richter scale magnitudes vs. energy (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Earthquake energy", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        # Side-by-side: magnitude (linear-feeling small) vs. energy (10^N).
        mag_card = make_equation_card(
            r"\text{Mag. } 1 \rightarrow 6",
            color=BLUE_TERM, scale=0.9,
        )
        mag_card.move_to(BAND_CHART_CENTER + UP * 0.5 + LEFT * 2.0)
        mag_lbl = Text("linear scale", font_size=20, color=BLUE_TERM)
        mag_lbl.next_to(mag_card, DOWN, buff=0.25)
        mag_lbl_bg = BackgroundRectangle(mag_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.15)
        mag_lbl_bg.move_to(mag_lbl.get_center())
        mag_grp = VGroup(mag_card, mag_lbl, mag_lbl_bg)

        en_card = make_equation_card(
            r"\text{Energy: } 10^{1} \rightarrow 10^{6}",
            color=ORANGE_TERM, scale=0.9,
        )
        en_card.move_to(BAND_CHART_CENTER + UP * 0.5 + RIGHT * 2.0)
        en_lbl = Text("100 000× larger", font_size=20, color=ORANGE_TERM)
        en_lbl.next_to(en_card, DOWN, buff=0.25)
        en_lbl_bg = BackgroundRectangle(en_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.15)
        en_lbl_bg.move_to(en_lbl.get_center())
        en_grp = VGroup(en_card, en_lbl, en_lbl_bg)

        self.play(FadeIn(mag_grp, shift=UP * 0.2, run_time=1.2))
        self.wait(1.5)
        self.play(FadeIn(en_grp, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        beat2 = beat_group(head, head_bg, mag_grp, en_grp)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: log axis compresses exponential ranges (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Take the logarithm", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        # A compact bar visualisation: log values 1, 2, 3, 4, 5, 6.
        bars = VGroup()
        log_values = [1, 2, 3, 4, 5, 6]
        for i, lv in enumerate(log_values):
            x = -3.5 + i * 1.4
            bar = Rectangle(
                width=0.7, height=lv * 0.18,
                color=BLUE_TERM, fill_opacity=0.75, stroke_width=1,
            )
            bar.move_to(BAND_CHART_CENTER + LEFT * 0.3 + RIGHT * x + UP * (lv * 0.18 / 2 - 0.7))
            bars.add(bar)

        # X-axis labels for the bar group.
        x_lbls = VGroup()
        for i, lv in enumerate(log_values):
            x = -3.5 + i * 1.4
            lbl = MathTex(f"{lv}", color=WHITE).scale(0.6)
            lbl.move_to(BAND_CHART_CENTER + RIGHT * x + DOWN * 1.2)
            x_lbls.add(lbl)

        bars_grp = VGroup(bars, x_lbls)
        bars_grp.move_to(BAND_CHART_CENTER + UP * 0.1)

        axis_lbl = Text("log(energy)", font_size=20, color=WHITE)
        axis_lbl.next_to(bars_grp, LEFT, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3, run_time=0.6) for b in bars],
                        lag_ratio=0.15),
        )
        self.play(FadeIn(x_lbls, run_time=0.8), FadeIn(axis_lbl, run_time=0.6))
        self.wait(3.0)

        # Highlight a 1-unit step on the log axis (10x in energy).
        step_note = Text("each step of 1 = ×10 energy", font_size=22, color=GREEN_OK)
        step_note.move_to(BAND_CHART_CENTER + DOWN * 2.0)
        step_note_bg = BackgroundRectangle(step_note, color=BLACK,
                                           fill_opacity=0.95, buff=0.15)
        step_note_bg.move_to(step_note.get_center())

        self.play(FadeIn(step_note_bg, run_time=0.4), FadeIn(step_note, run_time=1.0))
        self.wait(3.0)

        beat3 = beat_group(head3, head3_bg, bars, x_lbls, axis_lbl,
                           step_note, step_note_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: linear axis would squish mag-1 off the page (~14 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Linear axes fail", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        # Visualise tiny mag-1 bar next to giant mag-6 bar.
        bars_lin = VGroup()
        energies = [1, 10, 100, 1000, 10000, 100000]
        max_e = max(energies)
        for i, e in enumerate(energies):
            x = -3.5 + i * 1.4
            # On a linear scale, height ∝ energy (so mag-1 is invisible).
            h = (e / max_e) * 2.5
            bar = Rectangle(
                width=0.7, height=max(h, 0.05),
                color=RED_REJECT, fill_opacity=0.7, stroke_width=1,
            )
            bar.move_to(BAND_CHART_CENTER + UP * (h / 2 - 1.0) + RIGHT * x)
            bars_lin.add(bar)

        x_lbls2 = VGroup()
        for i, e in enumerate(energies):
            x = -3.5 + i * 1.4
            if e >= 1000:
                lbl_txt = f"{e // 1000}k"
            else:
                lbl_txt = str(e)
            lbl = MathTex(lbl_txt, color=WHITE).scale(0.55)
            lbl.move_to(BAND_CHART_CENTER + RIGHT * x + DOWN * 1.2)
            x_lbls2.add(lbl)

        bars_lin_grp = VGroup(bars_lin, x_lbls2)
        bars_lin_grp.move_to(BAND_CHART_CENTER + UP * 0.1)

        axis_lbl2 = Text("energy (linear)", font_size=20, color=WHITE)
        axis_lbl2.next_to(bars_lin_grp, LEFT, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3, run_time=0.5) for b in bars_lin],
                        lag_ratio=0.12),
        )
        self.play(FadeIn(x_lbls2, run_time=0.8), FadeIn(axis_lbl2, run_time=0.6))

        # Mag-1 bar is invisible.
        bad_note = Text("mag-1 invisible", font_size=22, color=RED_REJECT)
        bad_note.move_to(BAND_CHART_CENTER + DOWN * 2.0)
        bad_note_bg = BackgroundRectangle(bad_note, color=BLACK,
                                          fill_opacity=0.95, buff=0.15)
        bad_note_bg.move_to(bad_note.get_center())
        self.play(FadeIn(bad_note_bg, run_time=0.4), FadeIn(bad_note, run_time=1.0))
        self.wait(2.5)

        beat4 = beat_group(head4, head4_bg, bars_lin, x_lbls2, axis_lbl2,
                           bad_note, bad_note_bg)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~15 s, held)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\log_{10}(E) = \text{magnitude}",
            "A jump of 1 on a log axis = ×10 the underlying value.",
            final_wait=35.0,
        )