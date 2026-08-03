"""
Manim scene for the lesson `log-definition`
(topic `l10a-an-logarithms-scales`).

A logarithm answers the question "what power do I raise the base to
in order to get this number?". For example, log_2(8) = 3 because
2^3 = 8. Notes: log of a positive number only; log can be negative.
Estimate a log by squeezing between two known powers.

Target duration: ~106 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class LogDefinitionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "What is a logarithm?",
            "What power of the base gives this number?",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The big question (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        question = Text(
            "What power of 2 gives 8?",
            font_size=28,
            color=BLUE_TERM,
        )
        question.move_to(BAND_CHART_CENTER + UP * 0.9)
        question_bg = BackgroundRectangle(question, color=BLACK, fill_opacity=1, buff=0.2)
        question_bg.move_to(question.get_center())
        beat_2 = beat_group(beat_2, question, question_bg)
        self.play(FadeIn(question_bg, run_time=0.4), FadeIn(question, run_time=1.5))
        self.wait(2.0)

        # Answer: 2^3 = 8.
        answer = MathTex(
            r"2^{3} \;=\; 8",
            color=GREEN_OK,
        ).scale(1.1)
        answer.next_to(question, DOWN, buff=0.55)
        answer_bg = BackgroundRectangle(answer, color=BLACK, fill_opacity=1, buff=0.25)
        answer_bg.move_to(answer.get_center())
        beat_2 = beat_group(beat_2, answer, answer_bg)
        self.play(FadeIn(answer_bg, run_time=0.4), Write(answer, run_time=1.4))
        self.wait(2.5)

        # Restate as a log.
        logf = MathTex(
            r"\log_{2}(8) \;=\; 3",
            color=ORANGE_TERM,
        ).scale(1.1)
        logf.next_to(answer, DOWN, buff=0.45)
        logf_bg = BackgroundRectangle(logf, color=BLACK, fill_opacity=1, buff=0.25)
        logf_bg.move_to(logf.get_center())
        beat_2 = beat_group(beat_2, logf, logf_bg)
        self.play(FadeIn(logf_bg, run_time=0.4), Write(logf, run_time=1.4))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Two notations (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        head = Text("Two notations to recognise", font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.15)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_3 = beat_group(beat_3, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.5)

        n10 = MathTex(
            r"\log \;\;=\;\; \log_{10} \quad (\text{used in science})",
            color=GREEN_OK,
        ).scale(1.0)
        n10.move_to(BAND_CHART_CENTER + UP * 0.4)
        n10_bg = BackgroundRectangle(n10, color=BLACK, fill_opacity=1, buff=0.2)
        n10_bg.move_to(n10.get_center())
        beat_3 = beat_group(beat_3, n10, n10_bg)
        self.play(FadeIn(n10_bg, run_time=0.4), Write(n10, run_time=1.6))
        self.wait(2.0)

        ln = MathTex(
            r"\ln \;=\; \log_{e}, \quad e \approx 2.7 \quad (\text{natural log})",
            color=ORANGE_TERM,
        ).scale(0.95)
        ln.next_to(n10, DOWN, buff=0.45)
        ln_bg = BackgroundRectangle(ln, color=BLACK, fill_opacity=1, buff=0.2)
        ln_bg.move_to(ln.get_center())
        beat_3 = beat_group(beat_3, ln, ln_bg)
        self.play(FadeIn(ln_bg, run_time=0.4), Write(ln, run_time=1.8))
        self.wait(6.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Rules of the log domain (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        r1 = MathTex(
            r"\text{log of a positive number only — no 0, no negatives}",
            color=BLUE_TERM,
        ).scale(0.95)
        r1.move_to(BAND_CHART_CENTER + UP * 0.95)
        r1_bg = BackgroundRectangle(r1, color=BLACK, fill_opacity=1, buff=0.2)
        r1_bg.move_to(r1.get_center())
        beat_4 = beat_group(beat_4, r1, r1_bg)
        self.play(FadeIn(r1_bg, run_time=0.4), FadeIn(r1, run_time=1.4))
        self.wait(2.0)

        r2 = MathTex(
            r"\text{log itself can be any real number, positive or negative}",
            color=BLUE_TERM,
        ).scale(0.95)
        r2.next_to(r1, DOWN, buff=0.45)
        r2_bg = BackgroundRectangle(r2, color=BLACK, fill_opacity=1, buff=0.2)
        r2_bg.move_to(r2.get_center())
        beat_4 = beat_group(beat_4, r2, r2_bg)
        self.play(FadeIn(r2_bg, run_time=0.4), FadeIn(r2, run_time=1.6))
        self.wait(1.5)

        # Worked example for negative result: log_5(0.2) = -1.
        neg = MathTex(
            r"\log_{5}(0.2) \;=\; -1 \quad \text{because} \quad 5^{-1} \;=\; 0.2",
            color=GREEN_OK,
        ).scale(0.9)
        neg.next_to(r2, DOWN, buff=0.45)
        neg_bg = BackgroundRectangle(neg, color=BLACK, fill_opacity=1, buff=0.2)
        neg_bg.move_to(neg.get_center())
        beat_4 = beat_group(beat_4, neg, neg_bg)
        self.play(FadeIn(neg_bg, run_time=0.4), Write(neg, run_time=1.8))
        self.wait(6.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Estimating a log by squeezing (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_5 = beat_group()

        est_head = Text("Estimate by squeezing",
                        font_size=24, color=BLUE_TERM)
        est_head.move_to(BAND_CHART_CENTER + UP * 0.95)
        est_head_bg = BackgroundRectangle(est_head, color=BLACK, fill_opacity=0.95, buff=0.15)
        est_head_bg.move_to(est_head.get_center())
        beat_5 = beat_group(beat_5, est_head, est_head_bg)
        self.play(FadeIn(est_head_bg, run_time=0.4), FadeIn(est_head, run_time=1.0))
        self.wait(1.5)

        bound = MathTex(
            r"10^{2} \;=\; 100 \quad < \quad 500 \quad < \quad 10^{3} \;=\; 1000",
            color=ORANGE_TERM,
        ).scale(0.95)
        bound.move_to(BAND_CHART_CENTER + UP * 0.2)
        bound_bg = BackgroundRectangle(bound, color=BLACK, fill_opacity=1, buff=0.2)
        bound_bg.move_to(bound.get_center())
        beat_5 = beat_group(beat_5, bound, bound_bg)
        self.play(FadeIn(bound_bg, run_time=0.4), Write(bound, run_time=1.8))
        self.wait(2.0)

        ans = MathTex(
            r"\log(500) \;\approx\; 2.7 \quad \text{(closer to 3)}",
            color=GREEN_OK,
        ).scale(1.0)
        ans.next_to(bound, DOWN, buff=0.45)
        ans_bg = BackgroundRectangle(ans, color=BLACK, fill_opacity=1, buff=0.2)
        ans_bg.move_to(ans.get_center())
        beat_5 = beat_group(beat_5, ans, ans_bg)
        self.play(FadeIn(ans_bg, run_time=0.4), Write(ans, run_time=1.6))
        self.wait(5.5)
        self.play(FadeOut(beat_5, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 6 — Final takeaway (~33 s, total ≈ 106 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\log_{a}(b) \;=\; c \;\;\text{whenever}\;\; a^{c} \;=\; b",
            "Logs answer: what power of the base gives this number?",
            final_wait=33.0,
        )
