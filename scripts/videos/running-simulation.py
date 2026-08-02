"""
Manim scene for the lesson `running-simulation`
(topic `l9-p-simulations`).

Once the simulation is designed, run N trials, count k where the event
of interest occurred, and estimate Pr ≈ k/N. The Law of Large Numbers
says the error shrinks like 1/sqrt(N). Reject the "5 trials is enough"
mistake.

Target duration: ~85.3 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class RunningSimulationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Running a simulation",
            "Many trials, count outcomes, then estimate the probability.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The four-step recipe (~20 s)
        # ──────────────────────────────────────────────────────────────────
        recipe = VGroup(
            make_term_card("1.\,\text{Run}",  r"N\ \text{trials}",        BLUE_TERM),
            make_term_card("2.\,\text{Count}", r"k\ \text{event hits}",   TEAL_TERM),
            make_term_card("3.\,\text{Estimate}", r"k / N",                ORANGE_TERM),
            make_term_card("4.\,\text{Repeat}", r"\text{with bigger } N",  GREEN_OK),
        ).arrange(DOWN, buff=0.32)
        recipe.move_to(BAND_CHART_CENTER + UP * 0.4)
        for s in recipe:
            s.set_z_index(2)

        for s in recipe:
            self.play(FadeIn(s, shift=RIGHT * 0.15, run_time=0.6))
            self.wait(0.5)

        self.wait(4.0)

        self.play(FadeOut(recipe, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete worked example (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Setup: birthday problem with N=5000.
        setup = MathTex(
            r"\text{Birthday problem: } 23 \text{ people, } N = 5000 \text{ trials.}",
        ).scale(0.9)
        setup.move_to(BAND_CHART_CENTER + UP * 1.4)
        setup_bg = BackgroundRectangle(setup, color=BLACK, fill_opacity=1, buff=0.25)
        setup_bg.move_to(setup.get_center())
        self.play(FadeIn(setup_bg, run_time=0.4), FadeIn(setup, run_time=1.6))
        self.wait(2.5)

        # Count.
        count = MathTex(
            r"k = 2550 \;\text{ shared-birthday runs}",
            color=ORANGE_TERM,
        ).scale(1.0)
        count.next_to(setup, DOWN, buff=0.55)
        count_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.25)
        count_bg.move_to(count.get_center())
        self.play(FadeIn(count_bg, run_time=0.4), Write(count, run_time=1.4))
        self.wait(2.0)

        # Estimate.
        est = MathTex(
            r"\Pr \;\approx\; \dfrac{2550}{5000} \;=\; 0.51",
            color=GREEN_OK,
        ).scale(1.1)
        est.next_to(count, DOWN, buff=0.55)
        est_bg = BackgroundRectangle(est, color=BLACK, fill_opacity=1, buff=0.28)
        est_bg.move_to(est.get_center())
        self.play(FadeIn(est_bg, run_time=0.4), Write(est, run_time=1.6))
        self.wait(3.5)

        self.play(
            FadeOut(VGroup(setup, setup_bg, count, count_bg, est, est_bg),
                    run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Law of Large Numbers + reject "5 trials" (~16 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Law of Large Numbers", font_size=24, color=GREEN_OK)
        head.move_to(BAND_CHART_CENTER + UP * 1.6)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())

        law = MathTex(
            r"\text{error} \;\propto\; \dfrac{1}{\sqrt{N}}",
            color=GREEN_OK,
        ).scale(1.1)
        law.move_to(BAND_CHART_CENTER + UP * 0.4)
        law_bg = BackgroundRectangle(law, color=BLACK, fill_opacity=1, buff=0.28)
        law_bg.move_to(law.get_center())

        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=0.9))
        self.wait(0.5)
        self.play(FadeIn(law_bg, run_time=0.4), Write(law, run_time=1.6))
        self.wait(2.5)

        # Concrete: 10× more trials → ~3× more accuracy.
        note = Text(
            "10× more trials → roughly 3× more accurate.",
            font_size=22, color=ORANGE_TERM,
        ).next_to(law, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.18)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(3.0)

        self.play(
            FadeOut(VGroup(head, head_bg, law, law_bg, note, note_bg),
                    run_time=1.0),
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 85.3 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Pr \;\approx\; \dfrac{k}{N} \quad \text{(relative frequency)}",
            "Bigger N → smaller error. Never trust 5-trial estimates.",
            final_wait=32.0,
        )
