"""
Manim scene for the lesson `planning-the-investigation`
(topic `l8-st-statistical-investigations`).

A statistical investigation is a structured way to answer a question
using data. The plan matters as much as the numbers: pose the question,
plan the sample, collect, and report — and reject biased sampling.

Target duration: ~81.5 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, PURPLE_ACCENT, make_term_card, make_equation_card,
    animate_intro, animate_final_definition, beat_group,
)
from manim import *


class PlanningTheInvestigationScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Planning a statistical investigation",
            "Question → Sample → Data → Inference",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: sleep question (~16 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        # Vague starting question, then the sharpened version.
        vague = Text(
            "How much sleep do students get?",
            font_size=28, color=WHITE,
        )
        vague.next_to(BAND_CHART_CENTER + UP * 1.4, DOWN, buff=0.3)
        vague_bg = BackgroundRectangle(vague, color=BLACK, fill_opacity=1, buff=0.18)
        vague_bg.move_to(vague.get_center())
        beat_2 = beat_group(beat_2, vague_bg, vague)

        self.play(
            FadeIn(vague_bg, run_time=0.4),
            FadeIn(vague, shift=UP * 0.2, run_time=1.2),
        )
        self.wait(2.0)

        # Replace with the sharpened question.
        sharp = MathTex(
            r"\text{What is the mean nightly sleep of Year 8 students at our school?}",
        ).scale(0.85)
        sharp.move_to(BAND_CHART_CENTER + UP * 0.4)
        sharp_bg = BackgroundRectangle(sharp, color=BLACK, fill_opacity=1, buff=0.25)
        sharp_bg.move_to(sharp.get_center())
        beat_2 = beat_group(beat_2, sharp_bg, sharp)

        self.play(
            FadeOut(vague, run_time=0.6),
            FadeOut(vague_bg, run_time=0.6),
        )
        self.play(
            FadeIn(sharp_bg, run_time=0.4),
            Write(sharp, run_time=2.0),
        )

        # Annotate the two refinements.
        pop_lbl = Text("population: who", font_size=22, color=BLUE_TERM)
        pop_lbl.next_to(sharp, DOWN, buff=0.4)
        pop_bg = BackgroundRectangle(pop_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        pop_bg.move_to(pop_lbl.get_center())
        beat_2 = beat_group(beat_2, pop_bg, pop_lbl)
        self.play(FadeIn(pop_bg, run_time=0.4), FadeIn(pop_lbl, run_time=1.2))
        self.wait(3.0)

        var_lbl = Text("variable: what we measure", font_size=22, color=TEAL_TERM)
        var_lbl.next_to(pop_lbl, DOWN, buff=0.4)
        var_bg = BackgroundRectangle(var_lbl, color=BLACK, fill_opacity=0.95, buff=0.15)
        var_bg.move_to(var_lbl.get_center())
        beat_2 = beat_group(beat_2, var_bg, var_lbl)
        self.play(FadeIn(var_bg, run_time=0.4), FadeIn(var_lbl, run_time=1.2))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The four steps of any statistical investigation (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        # Use smaller scale (0.6) and tighter buff (0.2) so the 4-card row
        # fits comfortably inside the chart band x ∈ [-6, 6] without the
        # leftmost "1. extPose" card clipping off the screen.
        step1 = make_term_card("1.\,\text{Pose}",   "Question",         BLUE_TERM).scale(0.6)
        step2 = make_term_card("2.\,\text{Plan}",   "Sample + size",    TEAL_TERM).scale(0.6)
        step3 = make_term_card("3.\,\text{Collect}","Data + analyse",   ORANGE_TERM).scale(0.6)
        step4 = make_term_card("4.\,\text{Report}", "Inference + uncer.", PURPLE_ACCENT).scale(0.6)
        steps_row = VGroup(step1, step2, step3, step4).arrange(RIGHT, buff=0.2)
        # Move the row slightly RIGHT of center so the leftmost card
        # has ≥0.5 unit of breathing room from the left frame edge.
        steps_row.move_to(BAND_CHART_CENTER + UP * 0.2 + RIGHT * 0.3)
        for s in steps_row:
            s.set_z_index(2)
        beat_3 = beat_group(beat_3, step1, step2, step3, step4)

        self.play(FadeIn(step1, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(step2, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(step3, shift=UP * 0.2, run_time=1.2))
        self.wait(1.0)
        self.play(FadeIn(step4, shift=UP * 0.2, run_time=1.2))
        self.wait(3.0)

        # Highlight: the sample step decides whether the answer is trustworthy.
        hl = SurroundingRectangle(step2[0], color=GREEN_OK, buff=0.22, stroke_width=3)
        hl.set_z_index(3)
        beat_3 = beat_group(beat_3, hl)
        self.play(Create(hl, run_time=1.0))
        self.wait(3.0)

        cap = Text(
            "Random sampling keeps the estimate fair.",
            font_size=22, color=GREEN_OK,
        ).next_to(steps_row, DOWN, buff=0.6)
        cap_bg = BackgroundRectangle(cap, color=BLACK, fill_opacity=0.95, buff=0.18)
        cap_bg.move_to(cap.get_center())
        beat_3 = beat_group(beat_3, cap_bg, cap)
        self.play(FadeIn(cap_bg, run_time=0.4), FadeIn(cap, run_time=1.2))
        self.wait(6.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: "asked my three friends" is not a sample (~10 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = Text(
            '"I asked my three best friends."',
            font_size=28, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.22)
        bad_bg.move_to(bad.get_center())
        beat_4 = beat_group(beat_4, bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = beat_group(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        why = Text(
            "Convenience sample — biased by who you know.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.6)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        beat_4 = beat_group(beat_4, why_bg, why)
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(3.5)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held to match audio; total ≈ 81.5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Question} \rightarrow \text{Sample} \rightarrow \text{Conclusion}",
            "Plan first, then trust the inference. A biased sample cannot be saved by analysis.",
            final_wait=30.0,
        )
