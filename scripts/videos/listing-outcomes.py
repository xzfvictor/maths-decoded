"""
Manim scene for the lesson `listing-outcomes`
(topic `l9-p-two-step-experiments`).

For a two-step experiment, every outcome is an ordered pair. A tree
diagram branches every step and the leaves are every possible outcome.
The animation builds a coin-then-die tree (12 leaves), generalises to
the multiplication principle, and rejects the "list fewer branches"
shortcut.

Target duration: ~86.7 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition,
)
from manim import *


class ListingOutcomesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Listing outcomes: lists, tables, trees",
            "Branch every step; leaves list every ordered pair.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete tree: coin then die (~24 s)
        # ──────────────────────────────────────────────────────────────────
        start = Dot(BAND_CHART_CENTER + UP * 1.9, color=WHITE)
        self.play(FadeIn(start, run_time=0.6))

        # First branches — H / T at y=0.9, x=±1.6.
        h_node = Dot(BAND_CHART_CENTER + UP * 0.9 + LEFT * 1.7, color=BLUE_TERM)
        t_node = Dot(BAND_CHART_CENTER + UP * 0.9 + RIGHT * 1.7, color=TEAL_TERM)
        h_lbl = MathTex("H", color=BLUE_TERM).scale(0.9).next_to(h_node, UP, buff=0.25)
        t_lbl = MathTex("T", color=TEAL_TERM).scale(0.9).next_to(t_node, UP, buff=0.25)
        h_edge = Line(start.get_center(), h_node.get_center(), color=BLUE_TERM)
        t_edge = Line(start.get_center(), t_node.get_center(), color=TEAL_TERM)

        self.play(
            Create(h_edge, run_time=0.6),
            Create(t_edge, run_time=0.6),
            FadeIn(h_node, run_time=0.4),
            FadeIn(t_node, run_time=0.4),
            FadeIn(h_lbl, run_time=0.6),
            FadeIn(t_lbl, run_time=0.6),
        )
        self.wait(2.0)

        # Six die-roll endpoints at y=-0.4 from each parent — listed once.
        die_labels = ["1", "2", "3", "4", "5", "6"]
        die_xs = [LEFT * 2.85, LEFT * 2.10, LEFT * 1.35, RIGHT * 0.60, RIGHT * 1.35, RIGHT * 2.10]
        end_y = UP * (-0.4)

        h_ends = VGroup()
        h_edges = VGroup()
        h_lbls = VGroup()
        t_ends = VGroup()
        t_edges = VGroup()
        t_lbls = VGroup()

        for i, lbl in enumerate(die_labels):
            p = np.array([die_xs[i][0], end_y[1], 0.0])
            h_end = Dot(p, color=BLUE_TERM, radius=0.06)
            t_end = Dot(p + UP * 0.001, color=TEAL_TERM, radius=0.06)
            h_ends.add(h_end)
            t_ends.add(t_end)
            h_edges.add(Line(h_node.get_center(), h_end.get_center(), color=BLUE_TERM, stroke_width=1))
            t_edges.add(Line(t_node.get_center(), t_end.get_center(), color=TEAL_TERM, stroke_width=1))
            if i < 3:
                h_lbls.add(MathTex(lbl, color=BLUE_TERM).scale(0.55).move_to(h_end.get_center() + DOWN * 0.3))
                t_lbls.add(MathTex(lbl, color=TEAL_TERM).scale(0.55).move_to(t_end.get_center() + DOWN * 0.3))

        self.play(
            *[Create(e, run_time=0.4) for e in h_edges],
            *[Create(e, run_time=0.4) for e in t_edges],
            *[FadeIn(d, run_time=0.3) for d in h_ends],
            *[FadeIn(d, run_time=0.3) for d in t_ends],
            *[FadeIn(l, run_time=0.4) for l in h_lbls],
            *[FadeIn(l, run_time=0.4) for l in t_lbls],
        )
        self.wait(2.0)

        # Count note.
        count = MathTex(
            r"\text{Leaves: } 2 \times 6 = 12 \text{ ordered outcomes}",
            color=GREEN_OK,
        ).scale(0.95)
        count.move_to(BAND_CHART_CENTER + DOWN * 1.5)
        c_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.25)
        c_bg.move_to(count.get_center())
        self.play(FadeIn(c_bg, run_time=0.4), FadeIn(count, run_time=1.8))
        self.wait(3.0)

        # Wipe the tree.
        tree = VGroup(
            start, h_node, t_node, h_lbl, t_lbl, h_edge, t_edge,
            h_ends, t_ends, h_edges, t_edges, h_lbls, t_lbls,
            count, c_bg,
        )
        self.play(FadeOut(tree, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — The multiplication principle (~22 s)
        # ──────────────────────────────────────────────────────────────────
        # General rule: m outcomes at step 1, n at step 2 → m*n outcomes.
        step1 = make_term_card(r"\text{Step 1}", r"\text{m outcomes}", BLUE_TERM)
        step2 = make_term_card(r"\text{Step 2}", r"\text{n outcomes}", TEAL_TERM)
        row = VGroup(
            MathTex(r"\times", color=WHITE).scale(1.4),
            step1,
        ).arrange(RIGHT, buff=0.4)
        # Re-arrange nicely: step1, "x", step2.
        row = VGroup(step1, MathTex(r"\times", color=WHITE).scale(1.4), step2).arrange(RIGHT, buff=0.4)
        row.move_to(BAND_CHART_CENTER + UP * 0.8)
        for m in row:
            m.set_z_index(2)

        self.play(FadeIn(step1, shift=UP * 0.2, run_time=1.0))
        self.wait(0.6)
        self.play(
            FadeIn(row[1], run_time=0.6),
            FadeIn(step2, shift=UP * 0.2, run_time=1.0),
        )
        self.wait(2.0)

        rule = MathTex(
            r"\text{Total outcomes} \;=\; m \times n",
            color=GREEN_OK,
        ).scale(1.1)
        rule.next_to(row, DOWN, buff=0.6)
        rule_bg = BackgroundRectangle(rule, color=BLACK, fill_opacity=1, buff=0.28)
        rule_bg.move_to(rule.get_center())
        self.play(FadeIn(rule_bg, run_time=0.5), Write(rule, run_time=2.0))
        self.wait(2.5)

        # Concrete instance.
        eg = MathTex(
            r"\text{Coin}\,\times\,\text{Die} \;=\; 2 \times 6 \;=\; 12",
            color=GREEN_OK,
        ).scale(1.0)
        eg.next_to(rule, DOWN, buff=0.5)
        eg_bg = BackgroundRectangle(eg, color=BLACK, fill_opacity=0.95, buff=0.2)
        eg_bg.move_to(eg.get_center())
        self.play(FadeIn(eg_bg, run_time=0.4), FadeIn(eg, run_time=1.5))
        self.wait(3.0)

        eg2 = MathTex(
            r"\text{Die}\,\times\,\text{Die} \;=\; 6 \times 6 \;=\; 36",
            color=TEAL_TERM,
        ).scale(1.0)
        eg2.next_to(eg, DOWN, buff=0.4)
        eg2_bg = BackgroundRectangle(eg2, color=BLACK, fill_opacity=0.95, buff=0.2)
        eg2_bg.move_to(eg2.get_center())
        self.play(FadeIn(eg2_bg, run_time=0.4), FadeIn(eg2, run_time=1.5))
        self.wait(3.0)

        beat3 = VGroup(row, rule, rule_bg, eg, eg_bg, eg2, eg2_bg)
        self.play(FadeOut(beat3, run_time=1.4))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: short-cut the second branch (~10 s)
        # ──────────────────────────────────────────────────────────────────
        bad = Text(
            "Two coins tossed — so I only need 4 outcomes total.",
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.7)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        # Show the corrected count: 2 × 2 = 4 (which is what they had —
        # replace with a more interesting mistake).
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            "List EVERY ordered pair — order matters.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(2.5)

        beat4 = VGroup(bad, bad_bg, cross, fix, fix_bg)
        self.play(FadeOut(beat4, run_time=1.2))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 86.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Total outcomes} \;=\; m \times n",
            "Branch every step; the leaves list every ordered pair.",
            final_wait=32.0,
        )
