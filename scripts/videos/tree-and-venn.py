"""
Manim scene for the lesson `tree-and-venn`
(topic `l8-p-two-event-outcomes`).

For two events, a tree lists every ordered outcome and a Venn diagram
overlaps the two events. Build a coin-then-die tree (12 outcomes),
then a Venn for class counts. Reject "non-overlapping circles = any two
events" — disjoint only when mutually exclusive.

Target duration: ~111.7 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, make_term_card, make_equation_card, animate_intro,
    animate_final_definition, beat_group,
)
from manim import *


class TreeAndVennScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~6 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Tree diagrams & Venn diagrams",
            "Branch every step; overlap every event.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete tree: coin then die (~26 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = None
        # Start node
        start = Dot(BAND_CHART_CENTER + UP * 1.8, color=WHITE)
        beat_2 = VGroup(start)
        self.play(FadeIn(start, run_time=0.6))

        # First branches (H / T) — two children at y=0.9, x=±1.7
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
        beat_2 = VGroup(beat_2, h_node, t_node, h_lbl, t_lbl, h_edge, t_edge)

        self.wait(2.0)

        # Second branches — six die-roll endpoints at y=-0.3 from each parent.
        die_labels = ["1", "2", "3", "4", "5", "6"]
        die_xs = [LEFT * 2.7, LEFT * 1.95, LEFT * 1.2, RIGHT * 0.45, RIGHT * 1.2, RIGHT * 1.95]
        end_y = UP * (-0.4)

        h_ends = VGroup()
        h_edges = VGroup()
        h_lbls  = VGroup()
        t_ends = VGroup()
        t_edges = VGroup()
        t_lbls  = VGroup()

        for i, lbl in enumerate(die_labels):
            p = np.array([die_xs[i][0], end_y[1], 0.0])
            h_end = Dot(p + UP * 0.1 + LEFT * 0.0, color=BLUE_TERM, radius=0.06)
            t_end = Dot(p + UP * 0.1, color=TEAL_TERM, radius=0.06)
            h_ends.add(h_end)
            t_ends.add(t_end)
            h_edges.add(Line(h_node.get_center(), h_end.get_center(), color=BLUE_TERM, stroke_width=1))
            t_edges.add(Line(t_node.get_center(), t_end.get_center(), color=TEAL_TERM, stroke_width=1))
            # label only once is enough — show on one branch
            if i < 2:
                h_lbls.add(MathTex(lbl, color=BLUE_TERM).scale(0.55).move_to(h_end.get_center() + DOWN * 0.3))
                t_lbls.add(MathTex(lbl, color=TEAL_TERM).scale(0.55).move_to(t_end.get_center() + DOWN * 0.3))

        self.play(
            *[Create(e, run_time=0.45) for e in h_edges],
            *[Create(e, run_time=0.45) for e in t_edges],
            *[FadeIn(d, run_time=0.4) for d in h_ends],
            *[FadeIn(d, run_time=0.4) for d in t_ends],
            *[FadeIn(l, run_time=0.5) for l in h_lbls],
            *[FadeIn(l, run_time=0.5) for l in t_lbls],
        )
        beat_2 = VGroup(beat_2, h_ends, t_ends, h_edges, t_edges, h_lbls, t_lbls)
        self.wait(3.0)

        # Count note
        count = MathTex(
            r"\text{Endpoints: } 2 \times 6 = 12 \text{ outcomes}",
            color=GREEN_OK,
        ).scale(0.95)
        count.move_to(BAND_CHART_CENTER + DOWN * 1.5)
        c_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.25)
        c_bg.move_to(count.get_center())
        beat_2 = VGroup(beat_2, c_bg, count)
        self.play(FadeIn(c_bg, run_time=0.4), FadeIn(count, run_time=1.8))
        self.wait(4.0)

        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Venn diagram for two events (~22 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = None
        big = Ellipse(width=4.4, height=2.6, color=WHITE, stroke_width=1)
        big.move_to(BAND_CHART_CENTER + UP * 0.4)
        a_circle = Circle(radius=1.4, color=BLUE_TERM, stroke_width=2).move_to(BAND_CHART_CENTER + UP * 0.4 + LEFT * 0.6)
        b_circle = Circle(radius=1.4, color=TEAL_TERM, stroke_width=2).move_to(BAND_CHART_CENTER + UP * 0.4 + RIGHT * 0.6)

        a_lbl = MathTex("A", color=BLUE_TERM).scale(1.0).move_to(a_circle.get_center() + LEFT * 1.1)
        b_lbl = MathTex("B", color=TEAL_TERM).scale(1.0).move_to(b_circle.get_center() + RIGHT * 1.1)

        self.play(
            Create(a_circle, run_time=1.2),
            Create(b_circle, run_time=1.2),
        )
        self.play(
            Create(big, run_time=0.8),
            FadeIn(a_lbl, run_time=0.8),
            FadeIn(b_lbl, run_time=0.8),
        )
        beat_3 = VGroup(big, a_circle, b_circle, a_lbl, b_lbl)
        self.wait(3.0)

        # Region labels. The A∩B label is moved up to y=1.6 (clearly above
        # the centre overlap where the two circle outlines crowd together)
        # and given a fully opaque background so it sits in a clear area
        # without overlapping the circle lines.
        only_a = Text("A only", font_size=20, color=BLUE_TERM).move_to(BAND_CHART_CENTER + UP * 0.4 + LEFT * 1.4)
        only_b = Text("B only", font_size=20, color=TEAL_TERM).move_to(BAND_CHART_CENTER + UP * 0.4 + RIGHT * 1.4)
        # A∩B label moved DOWN-LEFT of the overlap area (where the two
        # circles' lines crowd together) so it doesn't sit on the circle
        # outlines. Bg rectangle ensures it reads on the white Venn lines.
        both   = MathTex(r"A \cap B", color=GREEN_OK).scale(0.9).move_to(BAND_CHART_CENTER + UP * 0.1)
        both_bg = BackgroundRectangle(both, color=BLACK, fill_opacity=1, buff=0.12)
        both_bg.move_to(both.get_center())
        neither = Text("neither", font_size=20, color=RED_REJECT).move_to(BAND_CHART_CENTER + UP * 0.4 + DOWN * 1.6)

        for m in [only_a, only_b, neither]:
            bg_m = BackgroundRectangle(m, color=BLACK, fill_opacity=1, buff=0.15)
            self.play(FadeIn(bg_m, run_time=0.3), FadeIn(m, run_time=0.7))
            self.wait(0.6)
            beat_3 = VGroup(beat_3, bg_m, m)
        # The A∩B label gets its own background (created above) so it
        # is readable on the overlapping circle outlines.
        self.play(FadeIn(both_bg, run_time=0.3), FadeIn(both, run_time=0.7))
        self.wait(0.6)
        beat_3 = VGroup(beat_3, both_bg, both)

        self.wait(4.0)

        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: disjoint circles ≠ "any two events" (~13 s)
        # ──────────────────────────────────────────────────────────────────
        beat_4 = None
        bad = Text(
            "Two non-overlapping circles show two events with no relationship.",
            font_size=22, color=WHITE,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.5)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        beat_4 = VGroup(bad_bg, bad)
        self.play(FadeIn(bad_bg, run_time=0.4), FadeIn(bad, run_time=1.4))
        self.wait(2.0)

        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        beat_4 = VGroup(beat_4, cross)
        self.play(Create(cross, run_time=1.0))

        fix = Text(
            "Disjoint circles mean mutually exclusive: P(A ∩ B) = 0.",
            font_size=22, color=RED_REJECT,
        ).next_to(bad, DOWN, buff=0.5)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat_4 = VGroup(beat_4, fix_bg, fix)
        self.play(FadeIn(fix_bg, run_time=0.4), FadeIn(fix, run_time=1.4))
        self.wait(4.0)

        self.play(FadeOut(beat_4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 111.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Tree: multiply along a branch. Venn: highlight the overlap.}",
            "Pick the diagram whose structure matches the problem.",
            final_wait=44.0,
        )
