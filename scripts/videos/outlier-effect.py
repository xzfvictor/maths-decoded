import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class OutlierEffectScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "How an outlier distorts mean and stddev",
            "One extreme value can wreck both summaries.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — The clean dataset: tight cluster (~26 s)
        # ──────────────────────────────────────────────────────────────────
        clean = [5, 5, 6, 6, 6, 7]
        mean_clean = sum(clean) / len(clean)  # 5.833
        # Variance = mean of squared deviations
        var_clean = sum((x - mean_clean) ** 2 for x in clean) / len(clean)
        sd_clean = var_clean ** 0.5

        # Render the data row.
        data_row = VGroup(*[MathTex(str(d), color=BLUE_TERM).scale(1.0) for d in clean])
        data_row.arrange(RIGHT, buff=0.45)
        data_row.move_to(BAND_CHART_CENTER + UP * 0.9)
        self.play(*[FadeIn(m, run_time=0.4) for m in data_row], run_time=1.6)
        self.wait(2.0)

        # Mean + sd read-out.
        read = MathTex(
            r"\bar{x} \approx 5.83,\;\; s \approx 0.69",
            color=GREEN_OK,
        ).scale(1.0)
        read.next_to(data_row, DOWN, buff=0.7)
        read_bg = BackgroundRectangle(read, color=BLACK, fill_opacity=0.95, buff=0.18)
        read_bg.move_to(read.get_center())
        self.play(FadeIn(read_bg, run_time=0.4), FadeIn(read, run_time=1.4))
        self.wait(2.0)

        tight_note = Text(
            "Tight cluster — small mean, small spread.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(read, DOWN, buff=0.5)
        tight_note_bg = BackgroundRectangle(tight_note, color=BLACK, fill_opacity=0.95, buff=0.15)
        tight_note_bg.move_to(tight_note.get_center())
        self.play(FadeIn(tight_note_bg, run_time=0.4), FadeIn(tight_note, run_time=1.2))
        self.wait(9.0)

        beat1 = beat_group(data_row, read, read_bg, tight_note, tight_note_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Add a 30: mean moves, stddev explodes (~30 s)
        # ──────────────────────────────────────────────────────────────────
        polluted = clean + [30]
        mean_poll = sum(polluted) / len(polluted)  # ≈ 9.286
        var_poll = sum((x - mean_poll) ** 2 for x in polluted) / len(polluted)
        sd_poll = var_poll ** 0.5

        data_row2 = VGroup(*[MathTex(str(d), color=BLUE_TERM).scale(1.0) for d in clean])
        data_row2.arrange(RIGHT, buff=0.45)
        data_row2.move_to(BAND_CHART_CENTER + UP * 0.8 + LEFT * 0.8)

        # The outlier appended on the right with a gap and red color.
        outlier = MathTex("30", color=RED_REJECT).scale(1.0)
        outlier.next_to(data_row2, RIGHT, buff=0.9)
        outlier_bg = BackgroundRectangle(outlier, color=BLACK, fill_opacity=0.95, buff=0.15)
        outlier_bg.move_to(outlier.get_center())
        outlier_lbl = Text("outlier", font_size=20, color=RED_REJECT)
        outlier_lbl.next_to(outlier, UP, buff=0.15)
        outlier_lbl_bg = BackgroundRectangle(outlier_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        outlier_lbl_bg.move_to(outlier_lbl.get_center())

        self.play(*[FadeIn(m, run_time=0.4) for m in data_row2], run_time=1.6)
        self.wait(1.5)
        self.play(FadeIn(outlier_bg, run_time=0.4), FadeIn(outlier, run_time=1.0))
        self.play(FadeIn(outlier_lbl_bg, run_time=0.3), FadeIn(outlier_lbl, run_time=0.8))
        self.wait(2.0)

        # New read-out: mean pulled way up, sd inflated.
        read2 = MathTex(
            r"\bar{x} \approx 9.29,\;\; s \approx 8.26",
            color=RED_REJECT,
        ).scale(1.0)
        read2.next_to(VGroup(data_row2, outlier), DOWN, buff=0.6)
        read2_bg = BackgroundRectangle(read2, color=BLACK, fill_opacity=0.95, buff=0.18)
        read2_bg.move_to(read2.get_center())
        self.play(FadeIn(read2_bg, run_time=0.4), FadeIn(read2, run_time=1.4))
        self.wait(2.0)

        why = Text(
            "Squared distances magnify the extreme value.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(read2, DOWN, buff=0.4)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.2))
        self.wait(10.0)

        beat2 = beat_group(data_row2, outlier, outlier_bg, outlier_lbl, outlier_lbl_bg, read2, read2_bg, why, why_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — The fix: median + IQR ignore extremes (~22 s)
        # ──────────────────────────────────────────────────────────────────
        fix = make_equation_card(
            r"\text{Median},\;\; \text{IQR} \;\text{ are robust to outliers}",
            color=GREEN_OK,
            scale=0.95,
        )
        fix.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(fix, run_time=1.4))
        self.wait(2.0)

        # The rule of thumb: 1.5 x IQR beyond the quartiles.
        rule = MathTex(
            r"\text{Outlier} :\; |x - Q_1| > 1.5 \cdot \text{IQR} \;\text{or}\; |x - Q_3| > 1.5 \cdot \text{IQR}",
            color=BLUE_TERM,
        ).scale(0.7)
        rule.next_to(fix, DOWN, buff=0.6)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=0.95, buff=0.15)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.4), FadeIn(rule, run_time=1.4))
        self.wait(8.0)

        beat3 = beat_group(fix, rule, rule_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~41 s, total ≈ 92 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{One outlier} \;\Rightarrow\; \bar{x} \text{ shifts, } s \text{ explodes}",
            "Recalculate without the outlier to see how much it mattered.",
            final_wait=41.0,
        )
