"""
Manim scene for the lesson `population-vs-sample`
(topic `l8-st-population-sample`).

A population is the entire group you want to know about; a sample is
the smaller group you actually measure. Conclusions about a population
are only as good as the sample that represents it.

Render target: ~74 s, matched to the audio narration length. The title
stays visible at the top of the frame for the entire animation so it
serves as a constant header.
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class PopulationVsSampleScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (CONSTANT header for entire animation)
        # ──────────────────────────────────────────────────────────────────
        title_group = animate_intro(
            self,
            "Populations vs. samples",
            "Population = every member. Sample = subset you measure.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete example: 1200 Year 8 students, 40 measured (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # "1200" representing the whole Year 8 cohort.
        # Original scale(2.2) overflowed and overlapped the pop_lbl below;
        # reduce to 1.3 so the number sits cleanly above its label.
        pop_num = MathTex("1200", color=BLUE_TERM).scale(1.3)
        pop_num.move_to(BAND_CHART_CENTER + UP * 0.9)
        pop_lbl = Text("Year 8 students at the school", font_size=22, color=BLUE_TERM)
        pop_lbl.next_to(pop_num, DOWN, buff=0.35)
        pop_lbl_bg = BackgroundRectangle(pop_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        pop_lbl_bg.move_to(pop_lbl.get_center())

        self.play(FadeIn(pop_num, run_time=1.2))
        self.wait(1.0)
        self.play(
            FadeIn(pop_lbl_bg, run_time=0.5),
            FadeIn(pop_lbl, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        pop_tag = Text("POPULATION", font_size=24, color=BLUE_TERM)
        pop_tag_bg = BackgroundRectangle(pop_tag, color=BLACK, fill_opacity=0.95, buff=0.18)
        pop_tag_bg.move_to(pop_tag.get_center())
        pop_tag.next_to(pop_lbl, DOWN, buff=0.35)
        self.play(
            FadeIn(pop_tag_bg, run_time=0.5),
            FadeIn(pop_tag, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(3.0)

        # ── Partial FadeOut: clear the population card before the sample
        # appears, so the 6 elements never share the screen at once.
        pop_card = beat_group(pop_num, pop_lbl, pop_lbl_bg, pop_tag, pop_tag_bg)
        self.play(FadeOut(pop_card, run_time=1.0))
        self.wait(0.5)

        # Now reveal the 40-student sample below. Reduced scale (2.2 → 1.3)
        # so the "40" sits cleanly above its label.
        samp_num = MathTex("40", color=ORANGE_TERM).scale(1.3)
        samp_num.move_to(BAND_CHART_CENTER + UP * 0.9)
        samp_lbl = Text("students you actually measure", font_size=22, color=ORANGE_TERM)
        samp_lbl.next_to(samp_num, DOWN, buff=0.35)
        samp_lbl_bg = BackgroundRectangle(samp_lbl, color=BLACK, fill_opacity=0.95, buff=0.18)
        samp_lbl_bg.move_to(samp_lbl.get_center())

        self.play(FadeIn(samp_num, run_time=1.2))
        self.wait(1.0)
        self.play(
            FadeIn(samp_lbl_bg, run_time=0.5),
            FadeIn(samp_lbl, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        samp_tag = Text("SAMPLE", font_size=24, color=ORANGE_TERM)
        samp_tag_bg = BackgroundRectangle(samp_tag, color=BLACK, fill_opacity=0.95, buff=0.18)
        samp_tag_bg.move_to(samp_tag.get_center())
        samp_tag.next_to(samp_lbl, DOWN, buff=0.35)
        self.play(
            FadeIn(samp_tag_bg, run_time=0.5),
            FadeIn(samp_tag, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Generalise: parameter (whole population) vs statistic (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat2_group = beat_group(samp_num, samp_lbl, samp_lbl_bg,
                                 samp_tag, samp_tag_bg)
        self.play(FadeOut(beat2_group, run_time=1.5))

        # Two stacked definitions: parameter on top, statistic below.
        param = MathTex(
            r"\text{Parameter} = \dfrac{\sum x}{N}",
            color=BLUE_TERM,
        ).scale(0.85)
        param.move_to(BAND_CHART_CENTER + UP * 1.1)
        param_bg = BackgroundRectangle(param, color=BLACK, fill_opacity=1, buff=0.25)
        param_bg.move_to(param.get_center())
        param_box = SurroundingRectangle(param, color=BLUE_TERM, buff=0.3, stroke_width=2)

        self.play(
            FadeIn(param_bg, run_time=0.5),
            Write(param, run_time=1.8),
        )
        self.play(Create(param_box, run_time=1.0))
        self.wait(2.0)

        # "Uses the whole population" annotation.
        param_note = Text("uses the whole population", font_size=22, color=BLUE_TERM)
        param_note_bg = BackgroundRectangle(param_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        param_note_bg.move_to(param_note.get_center())
        param_note.next_to(param_box, DOWN, buff=0.35)
        self.play(
            FadeIn(param_note_bg, run_time=0.5),
            FadeIn(param_note, run_time=1.0),
        )
        self.wait(3.0)

        stat = MathTex(
            r"\text{Statistic} = \dfrac{\sum x}{n}",
            color=ORANGE_TERM,
        ).scale(0.85)
        stat.move_to(BAND_CHART_CENTER + DOWN * 0.5)
        stat_bg = BackgroundRectangle(stat, color=BLACK, fill_opacity=1, buff=0.25)
        stat_bg.move_to(stat.get_center())
        stat_box = SurroundingRectangle(stat, color=ORANGE_TERM, buff=0.3, stroke_width=2)

        self.play(FadeOut(VGroup(param_note, param_note_bg), run_time=1.0))
        self.play(
            FadeIn(stat_bg, run_time=0.5),
            Write(stat, run_time=1.8),
        )
        self.play(Create(stat_box, run_time=1.0))
        self.wait(2.0)

        stat_note = Text("computed from the sample only", font_size=22, color=ORANGE_TERM)
        stat_note_bg = BackgroundRectangle(stat_note, color=BLACK, fill_opacity=0.95, buff=0.18)
        stat_note_bg.move_to(stat_note.get_center())
        stat_note.next_to(stat_box, DOWN, buff=0.35)
        self.play(
            FadeIn(stat_note_bg, run_time=0.5),
            FadeIn(stat_note, run_time=1.0),
        )
        self.wait(3.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: why we can't always measure the whole population
        # ──────────────────────────────────────────────────────────────────
        beat3_group = VGroup(
            param, param_bg, param_box, stat, stat_bg, stat_box,
            stat_note, stat_note_bg,
        )
        self.play(FadeOut(beat3_group, run_time=1.5))

        reject = MathTex(
            r"\text{Measure every single person?}",
            color=RED_REJECT,
        ).scale(1.05)
        reject.move_to(BAND_CHART_CENTER + UP * 0.5)
        reject_bg = BackgroundRectangle(reject, color=BLACK, fill_opacity=1, buff=0.28)
        reject_bg.move_to(reject.get_center())

        self.play(
            FadeIn(reject_bg, run_time=0.5),
            Write(reject, run_time=1.6),
        )
        self.wait(1.5)

        cross = Cross(reject, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))
        self.wait(2.5)

        reasons = Text(
            "Too big. Too costly. Sometimes impossible.",
            font_size=24,
            color=RED_REJECT,
        )
        reasons_bg = BackgroundRectangle(reasons, color=BLACK, fill_opacity=1, buff=0.2)
        reasons_bg.move_to(reasons.get_center())
        reasons.move_to(BAND_CHART_CENTER + DOWN * 0.6)
        self.play(
            FadeIn(reasons_bg, run_time=0.5),
            Write(reasons, run_time=1.4),
        )
        self.wait(2.0)

        # Solution: use a sample and accept the uncertainty.
        fix = Text(
            "Use a sample.  Acknowledge the uncertainty.",
            font_size=24,
            color=GREEN_OK,
        )
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=1, buff=0.2)
        fix_bg.move_to(fix.get_center())
        fix.move_to(BAND_CHART_CENTER + DOWN * 1.7)
        self.play(
            FadeIn(fix_bg, run_time=0.5),
            FadeIn(fix, run_time=1.2),
        )
        self.wait(4.0)

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway
        # ──────────────────────────────────────────────────────────────────
        beat4_group = VGroup(reject, reject_bg, cross, reasons, reasons_bg, fix, fix_bg)
        self.play(FadeOut(beat4_group, run_time=1.5))

        animate_final_definition(
            self,
            r"\text{Population} \;=\; \text{everyone} \quad / \quad "
            r"\text{Sample} \;=\; \text{subset}",
            "Conclusions about a population are only as good as the sample.",
            final_wait=27.0,
        )
