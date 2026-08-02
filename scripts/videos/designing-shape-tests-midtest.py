"""
Manim scene for the lesson `designing-shape-tests`
(topic `l8-sp-congruency-algorithms`).

Designing a decision algorithm that tells you whether two triangles are
congruent, similar, or neither. A good algorithm is ordered, unambiguous,
finite, and testable. The scene walks through a triangle congruence
flowchart and a triangle similarity test.

Target duration: ~105 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


def flowchart_node(text, color, scale=0.85) -> VGroup:
    """A diamond/box-shaped flow node with an opaque background."""
    if "\n" in text:
        label = Text(text, font_size=20, color=color).scale(scale)
    else:
        label = Text(text, font_size=22, color=color).scale(scale)
    bg = BackgroundRectangle(label, color=BLACK, fill_opacity=0.95, buff=0.18)
    box = SurroundingRectangle(label, color=color, buff=0.18, stroke_width=2)
    return VGroup(bg, box, label)


class DesigningShapeTestsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Designing shape tests",
            "Ordered, unambiguous, finite, testable — anyone lands on the same answer.",
            hold=1.0,
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Triangle congruence algorithm as a flowchart (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()
        # 4 rows of nodes stacked, with arrows between them.
        # Row 1 (top): question — both right-angled?
        q1 = flowchart_node("Both right-angled?", BLUE_TERM, scale=0.8)
        # Keep the question inside the chart band; subtitle lives at y ≈ 2.4.
        q1.move_to(BAND_CHART_CENTER)
        # Row 2: branch RHS vs fall through.
        n_rhs  = flowchart_node("RHS test", GREEN_OK)
        n_sss  = flowchart_node("SSS test", GREEN_OK)
        n_rhs.move_to([BAND_CHART_CENTER[0] - 3.0, BAND_CHART_CENTER[1] + UP * 0.9 + UP * 0.9][1] * 0 + np.array([-3.0, 0.6, 0]))
        n_sss.move_to(np.array([3.0, 0.6, 0]))
        # Re-anchor: row 2 at y = -1.5 (below q1 now at chart centre)
        n_rhs.move_to(np.array([-3.0, -1.5, 0]))
        n_sss.move_to(np.array([3.0, -1.5, 0]))
        # Row 3: SSS vs AAS follow-up.
        n_aas  = flowchart_node("AAS test", GREEN_OK)
        n_aas.move_to(np.array([3.0, -2.8, 0]))
        # Row 4: end states — congruent (left/centre) and cannot decide (right).
        n_yes  = flowchart_node("Congruent ✓", GREEN_OK, scale=0.95)
        n_yes.move_to(np.array([-2.0, -2.8, 0]))
        n_no   = flowchart_node("Not enough data", RED_REJECT, scale=0.85)
        n_no.move_to(np.array([3.0, -2.8, 0]))

        # Arrows.
        def arr(start, end, color=WHITE):
            return Arrow(start=start, end=end, buff=0, stroke_width=4, color=color)

        a_q1_rhs = arr(q1.get_bottom() + DOWN * 0.05, n_rhs.get_top() + UP * 0.05)
        a_q1_sss = arr(q1.get_bottom() + DOWN * 0.05, n_sss.get_top() + UP * 0.05)
        a_sss_aas = arr(n_sss.get_bottom() + DOWN * 0.05, n_aas.get_top() + UP * 0.05)
        a_rhs_yes = arr(n_rhs.get_bottom() + DOWN * 0.05,
                        n_yes.get_top() + UP * 0.05 + LEFT * 1.5)
        a_aas_yes = arr(n_aas.get_bottom() + DOWN * 0.05,
                        n_yes.get_top() + UP * 0.05 + RIGHT * 1.5)
        a_aas_no  = arr(n_aas.get_right() + RIGHT * 0.1, n_no.get_top() + UP * 0.05)

        yes_lbl  = Text("YES", font_size=18, color=GREEN_OK)
        no_lbl   = Text("NO",  font_size=18, color=RED_REJECT)
        yes_lbl.next_to(a_q1_sss, RIGHT, buff=0.15)
        no_lbl.next_to(a_q1_rhs, LEFT, buff=0.15)
        yes_lbl_bg = BackgroundRectangle(yes_lbl, color=BLACK, fill_opacity=0.95, buff=0.08)
        no_lbl_bg  = BackgroundRectangle(no_lbl,  color=BLACK, fill_opacity=0.95, buff=0.08)
        yes_lbl_bg.move_to(yes_lbl.get_center())
        no_lbl_bg.move_to(no_lbl.get_center())

        # Reveal.
        self.play(FadeIn(q1, run_time=1.2))
        self.wait(1.0)
        self.play(Create(a_q1_rhs, run_time=0.8), Create(a_q1_sss, run_time=0.8),
                  FadeIn(no_lbl, run_time=0.5), FadeIn(no_lbl_bg, run_time=0.4),
                  FadeIn(yes_lbl, run_time=0.5), FadeIn(yes_lbl_bg, run_time=0.4))
        self.wait(1.5)
        self.play(FadeIn(n_rhs, run_time=1.0), FadeIn(n_sss, run_time=1.0))
        self.wait(1.5)
        self.play(Create(a_sss_aas, run_time=0.8))
        self.play(FadeIn(n_aas, run_time=1.0))
        self.wait(1.5)
        self.play(Create(a_rhs_yes, run_time=0.8), Create(a_aas_yes, run_time=0.8),
                  Create(a_aas_no, run_time=0.8))
        self.play(FadeIn(n_yes, run_time=1.0), FadeIn(n_no, run_time=1.0))
        self.wait(3.5)

        beat_2 = beat_group(beat_2, q1, n_rhs, n_sss, n_aas, n_yes, n_no,
                            a_q1_rhs, a_q1_sss, a_sss_aas, a_rhs_yes, a_aas_yes, a_aas_no,
                            yes_lbl, yes_lbl_bg, no_lbl, no_lbl_bg)
        self.wait(120)
        raise SystemExit(0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Triangle similarity test (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # Show the three-step recipe: list, sort, divide.
        beat_3 = beat_group()
        step1 = flowchart_node("1. List each\ntriangle's sides", BLUE_TERM)
        step2 = flowchart_node("2. Sort from\nshortest to longest", TEAL_TERM)
        step3 = flowchart_node("3. Divide:\nsmall / matching big", ORANGE_TERM)

        row = VGroup(step1, step2, step3).arrange(RIGHT, buff=0.6)
        row.move_to(BAND_CHART_CENTER + UP * 1.0)
        for r in row:
            r.set_z_index(2)
        self.play(FadeIn(step1, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(step2, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(step3, run_time=1.0))
        self.wait(2.5)

        # Worked data: triangle A = 3, 4, 5; triangle B = 6, 8, 10.
        data = MathTex(
            r"\triangle A: 3,\,4,\,5 \qquad \triangle B: 6,\,8,\,10",
            color=WHITE,
        ).scale(0.9)
        data.next_to(row, DOWN, buff=0.7)
        data_bg = BackgroundRectangle(data, color=BLACK, fill_opacity=1, buff=0.2)
        data_bg.move_to(data.get_center())
        self.play(FadeIn(data_bg, run_time=0.4), FadeIn(data, run_time=1.5))
        self.wait(2.5)

        ratios = MathTex(
            r"\dfrac{3}{6} = \dfrac{4}{8} = \dfrac{5}{10} = \dfrac{1}{2}",
            color=GREEN_OK,
        ).scale(0.95)
        ratios.next_to(data, DOWN, buff=0.5)
        ratios_bg = BackgroundRectangle(ratios, color=BLACK, fill_opacity=1, buff=0.2)
        ratios_bg.move_to(ratios.get_center())
        self.play(FadeIn(ratios_bg, run_time=0.4), Write(ratios, run_time=2.0))
        self.wait(3.0)

        verdict = MathTex(r"\text{Similar with } k = \tfrac{1}{2}", color=GREEN_OK).scale(1.1)
        verdict.next_to(ratios, DOWN, buff=0.4)
        verdict_bg = BackgroundRectangle(verdict, color=BLACK, fill_opacity=1, buff=0.2)
        verdict_bg.move_to(verdict.get_center())
        self.play(FadeIn(verdict_bg, run_time=0.4), FadeIn(verdict, run_time=1.4))
        self.wait(3.5)

        beat_3 = beat_group(beat_3, step1, step2, step3, data, data_bg, ratios, ratios_bg,
                            verdict, verdict_bg)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: one matching pair is NOT enough (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\text{one matching side} \;\;\not\!\!\!\Longrightarrow\;\; \text{congruent or similar}",
            color=RED_REJECT, font_size=44,
        ).scale(0.9)
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.25)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.5), Write(bad, run_time=2.0))
        self.wait(2.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))
        self.wait(3.0)

        beat_4 = beat_group(bad, bad_bg, cross)
        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~40 s, total ≈ 105 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Test} \;=\; \text{ordered, unambiguous, finite, testable}",
            "Same steps in the same order — same answer every time.",
            final_wait=40.0,
        )