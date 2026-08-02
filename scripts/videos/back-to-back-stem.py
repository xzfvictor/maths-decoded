"""
Manim scene for the lesson `back-to-back-stem`
(topic `l9-st-comparing-data-sets`).

A back-to-back stem-and-leaf plot shares one stem column. Leaves
on the left are read right-to-left; leaves on the right are read
left-to-right. We build one for two small class score lists.

Target duration: ~67.97 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class BackToBackStemScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title + subtitle (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Back-to-back stem-and-leaf",
            "One shared stem, two sets of leaves, side by side.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Build the plot: stems 5-9 (~20 s)
        # ──────────────────────────────────────────────────────────────────
        # Class A scores:  52, 65, 70, 74, 88  (left side, reversed)
        # Class B scores:  60, 64, 71, 79, 90  (right side)
        # Stems: 5, 6, 7, 8, 9.
        stems = [5, 6, 7, 8, 9]
        # Class A leaves by stem (read right-to-left in the plot).
        class_a = {
            5: [2],
            6: [5],
            7: [0, 4],
            8: [8],
            9: [],
        }
        # Class B leaves by stem (read left-to-right).
        class_b = {
            5: [],
            6: [0, 4],
            7: [1],
            8: [],
            9: [0],
        }

        # Row y-positions.
        y_top = 2.0
        row_h = 0.7
        row_ys = [y_top - i * row_h for i in range(len(stems))]

        # Two header labels.
        head_a = Text("Class A", font_size=22, color=BLUE_TERM).move_to([-2.4, y_top + 0.6, 0])
        head_a_bg = BackgroundRectangle(head_a, color=BLACK, fill_opacity=0.95, buff=0.1)
        head_a_bg.move_to(head_a.get_center())
        head_b = Text("Class B", font_size=22, color=TEAL_TERM).move_to([2.4, y_top + 0.6, 0])
        head_b_bg = BackgroundRectangle(head_b, color=BLACK, fill_opacity=0.95, buff=0.1)
        head_b_bg.move_to(head_b.get_center())

        self.play(
            FadeIn(head_a_bg, run_time=0.3), FadeIn(head_a, run_time=0.7),
            FadeIn(head_b_bg, run_time=0.3), FadeIn(head_b, run_time=0.7),
        )
        self.wait(1.0)

        # Build the plot row-by-row so the audience sees it assemble.
        leaves_a_text = VGroup()
        leaves_b_text = VGroup()
        stem_text = VGroup()

        for i, s in enumerate(stems):
            y = row_ys[i]
            # Stem in the middle.
            st = MathTex(f"{s}", color=WHITE).scale(1.1).move_to([0, y, 0])
            st_bg = BackgroundRectangle(st, color=BLACK, fill_opacity=1, buff=0.18)
            st_bg.move_to(st.get_center())
            stem_text.add(VGroup(st_bg, st))

            # Class A leaves: read right-to-left, so reverse for display.
            a_leaves = list(reversed(class_a[s]))
            a_str = " ".join(str(x) for x in a_leaves) if a_leaves else "—"
            a_color = BLUE_TERM if a_leaves else "#888888"
            at = MathTex(a_str, color=a_color).scale(0.9).move_to([-1.6, y, 0])
            at_bg = BackgroundRectangle(at, color=BLACK, fill_opacity=0.9, buff=0.12)
            at_bg.move_to(at.get_center())
            leaves_a_text.add(VGroup(at_bg, at))

            # Class B leaves: left-to-right.
            b_leaves = class_b[s]
            b_str = " ".join(str(x) for x in b_leaves) if b_leaves else "—"
            b_color = TEAL_TERM if b_leaves else "#888888"
            bt = MathTex(b_str, color=b_color).scale(0.9).move_to([1.6, y, 0])
            bt_bg = BackgroundRectangle(bt, color=BLACK, fill_opacity=0.9, buff=0.12)
            bt_bg.move_to(bt.get_center())
            leaves_b_text.add(VGroup(bt_bg, bt))

            # Reveal one row at a time.
            self.play(
                FadeIn(stem_text[i], run_time=0.6),
                FadeIn(leaves_a_text[i], run_time=0.6),
                FadeIn(leaves_b_text[i], run_time=0.6),
            )
            self.wait(0.6)

        # Vertical bar between the two sides (the "stem column").
        sep = Line([0, y_top + 0.2, 0], [0, row_ys[-1] - 0.2, 0],
                   color=WHITE, stroke_width=3)
        self.play(Create(sep, run_time=0.8))
        self.wait(2.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Reading direction (~10 s)
        # ──────────────────────────────────────────────────────────────────
        # Highlight a Class A row and a Class B row.
        pick_a = SurroundingRectangle(leaves_a_text[2], color=GREEN_OK, buff=0.18, stroke_width=3)
        pick_b = SurroundingRectangle(leaves_b_text[1], color=GREEN_OK, buff=0.18, stroke_width=3)
        self.play(Create(pick_a, run_time=0.8))
        self.wait(0.6)
        self.play(Create(pick_b, run_time=0.8))
        self.wait(1.0)

        # Reading-rule caption.
        rule = Text(
            "Left leaves: read right-to-left (closest to stem first).",
            font_size=22, color=BLUE_TERM,
        ).move_to(BAND_CHART_CENTER + DOWN * 2.6)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=0.95, buff=0.18)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.4), FadeIn(rule, run_time=1.4))
        self.wait(2.5)

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: same stem is not the same value (~6 s)
        # ──────────────────────────────────────────────────────────────────
        bad = MathTex(
            r"\text{``same stem 7''} \;\not\!\!\!\Rightarrow\; \text{same value}",
            color=RED_REJECT,
        ).scale(0.95)
        bad.move_to(BAND_CHART_CENTER + UP * 2.6)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.22)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), Write(bad, run_time=1.4))
        self.wait(1.0)

        why = Text(
            "Stem 7 with leaf 4 = 74; with leaf 1 = 71.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.4)
        why_bg = BackgroundRectangle(why, color=BLACK, fill_opacity=0.95, buff=0.18)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.0))
        self.wait(1.5)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=0.7))
        self.wait(1.5)

        beat4_group = VGroup(
            bad, bad_bg, why, why_bg, cross,
            head_a, head_a_bg, head_b, head_b_bg,
            stem_text, leaves_a_text, leaves_b_text, sep,
            rule, rule_bg, pick_a, pick_b,
        )
        self.play(FadeOut(beat4_group, run_time=1.3))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final boxed takeaway (held; total ≈ 68 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Back-to-back: one stem, two leaves, side by side}",
            "Read left side right-to-left, right side left-to-right.",
            final_wait=25.0,
        )
