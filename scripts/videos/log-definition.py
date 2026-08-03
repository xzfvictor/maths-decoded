"""
Manim scene for the lesson `log-definition`
(topic `l10a-an-logarithms-scales`).

log_a(b) = c  ⟺  a^c = b. Show log_2(8) = 3 because 2^3 = 8.
Reject the mistake of swapping base and argument.

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
import numpy as np


class LogDefinitionScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Definition of a logarithm",
            "log_a(b) = c  ⟺  a^c = b",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Define the equivalence (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        defn = MathTex(
            r"\log_{a}(b) = c \quad\iff\quad a^{c} = b",
            color=BLUE_TERM,
        ).scale(1.1)
        defn.move_to(BAND_CHART_CENTER + UP * 0.7)
        defn_bg = BackgroundRectangle(defn, color=BLACK, fill_opacity=1, buff=0.3)
        defn_bg.move_to(defn.get_center())
        beat_2 = beat_group(beat_2, defn, defn_bg)
        self.play(FadeIn(defn_bg, run_time=0.4), Write(defn, run_time=2.0))
        self.wait(1.5)

        # Annotate: base, argument, value.
        base_lbl = Text("a = base", font_size=22, color=BLUE_TERM)
        base_lbl.next_to(defn, DOWN, buff=0.4)
        base_lbl_bg = BackgroundRectangle(base_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        base_lbl_bg.move_to(base_lbl.get_center())
        beat_2 = beat_group(beat_2, base_lbl, base_lbl_bg)
        self.play(FadeIn(base_lbl_bg, run_time=0.3), FadeIn(base_lbl, run_time=0.7))
        self.wait(0.5)

        arg_lbl = Text("b = the number we are taking the log of", font_size=22, color=ORANGE_TERM)
        arg_lbl.next_to(base_lbl, DOWN, buff=0.3)
        arg_lbl_bg = BackgroundRectangle(arg_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        arg_lbl_bg.move_to(arg_lbl.get_center())
        beat_2 = beat_group(beat_2, arg_lbl, arg_lbl_bg)
        self.play(FadeIn(arg_lbl_bg, run_time=0.3), FadeIn(arg_lbl, run_time=0.9))
        self.wait(0.5)

        val_lbl = Text("c = the power we'd raise a to", font_size=22, color=GREEN_OK)
        val_lbl.next_to(arg_lbl, DOWN, buff=0.3)
        val_lbl_bg = BackgroundRectangle(val_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        val_lbl_bg.move_to(val_lbl.get_center())
        beat_2 = beat_group(beat_2, val_lbl, val_lbl_bg)
        self.play(FadeIn(val_lbl_bg, run_time=0.3), FadeIn(val_lbl, run_time=0.9))
        self.wait(2.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Worked example: log_2(8) = 3 (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        ex = MathTex(r"\log_{2}(8) = ?", color=BLUE_TERM).scale(1.1)
        ex.move_to(BAND_CHART_CENTER + UP * 0.8)
        ex_bg = BackgroundRectangle(ex, color=BLACK, fill_opacity=1, buff=0.25)
        ex_bg.move_to(ex.get_center())
        beat_3 = beat_group(beat_3, ex, ex_bg)
        self.play(FadeIn(ex_bg, run_time=0.4), Write(ex, run_time=1.4))
        self.wait(1.0)

        # Ask: what power of 2 gives 8?
        ask = Text("What power of 2 gives 8?", font_size=22, color=ORANGE_TERM)
        ask.next_to(ex, DOWN, buff=0.5)
        ask_bg = BackgroundRectangle(ask, color=BLACK, fill_opacity=1, buff=0.18)
        ask_bg.move_to(ask.get_center())
        beat_3 = beat_group(beat_3, ask, ask_bg)
        self.play(FadeIn(ask_bg, run_time=0.3), FadeIn(ask, run_time=1.0))
        self.wait(1.0)

        # Show the chain.
        chain = MathTex(
            r"2^{3} = 8 \quad\Rightarrow\quad \log_{2}(8) = 3",
            color=GREEN_OK,
        ).scale(1.0)
        chain.next_to(ask, DOWN, buff=0.5)
        chain_bg = BackgroundRectangle(chain, color=BLACK, fill_opacity=1, buff=0.2)
        chain_bg.move_to(chain.get_center())
        beat_3 = beat_group(beat_3, chain, chain_bg)
        self.play(FadeIn(chain_bg, run_time=0.4), Write(chain, run_time=1.8))
        self.wait(1.5)

        # More examples.
        more = MathTex(
            r"\log_{3}(27) = 3,\quad \log_{10}(100) = 2,\quad \log_{5}(125) = 3",
            color=BLUE_TERM,
        ).scale(0.85)
        more.next_to(chain, DOWN, buff=0.5)
        more_bg = BackgroundRectangle(more, color=BLACK, fill_opacity=1, buff=0.2)
        more_bg.move_to(more.get_center())
        beat_3 = beat_group(beat_3, more, more_bg)
        self.play(FadeIn(more_bg, run_time=0.4), Write(more, run_time=1.8))
        self.wait(2.0)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: swapping base and argument (~20 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = beat_group()

        wrong = MathTex(
            r"\log_{2}(8) = 8^{2} = 64\ \text{?}",
            color=RED_REJECT,
        ).scale(1.0)
        wrong.move_to(BAND_CHART_CENTER + UP * 0.6)
        wrong_bg = BackgroundRectangle(wrong, color=BLACK, fill_opacity=1, buff=0.25)
        wrong_bg.move_to(wrong.get_center())
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        beat_4 = beat_group(beat_4, wrong, wrong_bg, cross)
        self.play(
            FadeIn(wrong_bg, run_time=0.4),
            Write(wrong, run_time=1.4),
            Create(cross, run_time=0.7),
        )
        self.wait(1.0)

        right = Text(
            "Base 2 stays the base; the answer is a power, not a product.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(wrong, DOWN, buff=0.5)
        right_bg = BackgroundRectangle(right, color=BLACK, fill_opacity=0.95, buff=0.18)
        right_bg.move_to(right.get_center())
        beat_4 = beat_group(beat_4, right, right_bg)
        self.play(FadeIn(right_bg, run_time=0.3), FadeIn(right, run_time=1.2))
        self.wait(2.0)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~48 s, total ≈ 106 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\log_{a}(b) = c \iff a^{c} = b",
            "Logs answer: 'what power gives this?'",
            final_wait=48.0,
        )
