"""
Manim scene for the lesson `simulating-compound-events`
(topic `l8-p-compound-experiments`).

Use random numbers to model multi-step experiments and estimate
probabilities for compound events. The recipe: assign numbers, run many
trials, count, and estimate. Reject running only a handful of trials.

Target duration: ~86.7 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class SimulatingCompoundEventsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Simulating compound events",
            "Random numbers model multi-step experiments.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: coin tossed 3×, "at least one H" (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        # Show the model setup first.
        setup = MathTex(
            r"\text{Per trial: three random } \{0, 1\}\,(\text{0 = T},\ \text{1 = H})",
        ).scale(0.9)
        setup.move_to(BAND_CHART_CENTER + UP * 1.4)
        setup_bg = BackgroundRectangle(setup, color=BLACK, fill_opacity=1, buff=0.25)
        setup_bg.move_to(setup.get_center())
        beat_2 = VGroup(setup_bg, setup)
        self.play(FadeIn(setup_bg, run_time=0.4), FadeIn(setup, run_time=2.0))
        self.wait(3.0)

        # Show a few trial strings.
        t1 = MathTex(r"\text{Trial 1: } 1,0,1", color=BLUE_TERM).scale(0.9)
        t2 = MathTex(r"\text{Trial 2: } 0,0,0", color=TEAL_TERM).scale(0.9)
        t3 = MathTex(r"\text{Trial 3: } 1,1,1", color=ORANGE_TERM).scale(0.9)
        trials = VGroup(t1, t2, t3).arrange(DOWN, buff=0.35)
        trials.next_to(setup, DOWN, buff=0.55)
        for t in trials:
            tb = BackgroundRectangle(t, color=BLACK, fill_opacity=1, buff=0.18)
            tb.move_to(t.get_center())
            beat_2 = VGroup(beat_2, tb, t)
            self.play(FadeIn(tb, run_time=0.3), FadeIn(t, run_time=0.8))
            self.wait(0.6)

        self.wait(3.0)

        # Count statement.
        count = MathTex(
            r"\text{Out of 500 trials, 'at least one H' was counted 437 times.}",
            color=GREEN_OK,
        ).scale(0.9)
        count.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        c_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.25)
        c_bg.move_to(count.get_center())
        self.play(
            FadeOut(beat_2, run_time=0.8),
            FadeIn(c_bg, run_time=0.4),
            FadeIn(count, run_time=2.0),
        )
        beat_2 = None
        beat_2 = VGroup(c_bg, count)
        self.wait(3.0)

        est = MathTex(
            r"\Pr(\text{at least one H}) \approx 437 / 500 = 0.874",
            color=GREEN_OK,
        ).scale(1.0)
        est.next_to(count, DOWN, buff=0.5)
        est_bg = BackgroundRectangle(est, color=BLACK, fill_opacity=1, buff=0.25)
        est_bg.move_to(est.get_center())
        beat_2 = VGroup(beat_2, est_bg, est)
        self.play(FadeIn(est_bg, run_time=0.4), FadeIn(est, run_time=2.0))
        self.wait(3.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The simulation recipe (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        step1 = make_term_card("1.\,\text{Model}",     "assign numbers",        BLUE_TERM)
        step2 = make_term_card("2.\,\text{Run}",       "many trials",            TEAL_TERM)
        step3 = make_term_card("3.\,\text{Count}",     "compound event",         ORANGE_TERM)
        step4 = make_term_card("4.\,\text{Estimate}",  "count / n",              GREEN_OK)
        steps_row = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.18)
        steps_row.scale(0.3)
        # Position the steps group so the first (top) card sits around y=0.7
        # and the whole stack stays below the title — no overlap.
        # Safe area is y ∈ [-1.5, 1.8]; with scale 0.3 the stack is ~1.94 tall,
        # so center at y = -0.3 keeps topmost card at y ≈ 0.67 and bottom at
        # y ≈ -1.27 — both inside the safe area.
        steps_row.move_to(BAND_CHART_CENTER + DOWN * 0.3)
        for s in steps_row:
            s.set_z_index(2)

        for s in steps_row:
            self.play(FadeIn(s, shift=RIGHT * 0.15, run_time=0.7))
            self.wait(0.7)
        beat_3 = VGroup(steps_row)

        # Always report fields — placed ABOVE the cards (between title and
        # top card) so the whole stack fits inside the safe area.
        report = Text(
            "Report: what was simulated, n, count, probability.",
            font_size=22, color=GREEN_OK,
        ).next_to(steps_row, UP, buff=0.45)
        r_bg = BackgroundRectangle(report, color=BLACK, fill_opacity=0.95, buff=0.18)
        r_bg.move_to(report.get_center())
        beat_3 = VGroup(beat_3, r_bg, report)
        self.play(FadeIn(r_bg, run_time=0.4), FadeIn(report, run_time=1.4))
        self.wait(8.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: 5 trials is not a simulation (~10 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = MathTex(
            r"\text{'I tried 5 times — so the probability is } 0.2\text{.'}",
            color=RED_REJECT,
        ).scale(0.95)
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        beat_4 = VGroup(bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=2.0))
        self.wait(2.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = VGroup(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        why = Text(
            "n = 5 is far too small — sampling variation dominates.",
            font_size=20, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        beat_4 = VGroup(beat_4, why_bg, why)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.4))
        self.wait(2.5)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 86.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr \approx \dfrac{\text{count of event}}{n \text{ trials}}",
            "Many trials, then report what was simulated and the relative frequency.",
            final_wait=32.0,
        )
