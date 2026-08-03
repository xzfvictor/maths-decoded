import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class WhatIsAlgorithmScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "What is a spatial algorithm?",
            "Unambiguous, finite, effective steps to solve a 3D problem.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Concrete: unfold a cuboid to find the shortest path (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Shortest path on a cuboid", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35 + LEFT * 4.4)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Two squares side-by-side (2D "net" of cuboid).
        sq1 = Square(side_length=1.2, color=BLUE_TERM, stroke_width=3)
        sq1.move_to(BAND_CHART_CENTER + UP * 0.3 + LEFT * 1.5)
        sq2 = Square(side_length=1.2, color=BLUE_TERM, stroke_width=3)
        sq2.move_to(BAND_CHART_CENTER + UP * 0.3 + RIGHT * 1.5)
        dots_a = Dot(sq1.get_corner(DOWN + LEFT), color=ORANGE_TERM)
        dots_b = Dot(sq2.get_corner(UP + RIGHT), color=GREEN_OK)
        a_lbl = MathTex("A", color=ORANGE_TERM).scale(0.8).next_to(dots_a, DL, buff=0.1)
        b_lbl = MathTex("B", color=GREEN_OK).scale(0.8).next_to(dots_b, UR, buff=0.1)
        diagonal = Line(dots_a.get_center(), dots_b.get_center(),
                        color=GREEN_OK, stroke_width=4)

        self.play(Create(sq1), Create(sq2), run_time=1.4)
        self.play(FadeIn(dots_a), FadeIn(dots_b),
                  FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.8)
        self.play(Create(diagonal, run_time=1.4))
        self.wait(2.0)

        note = Text("unfold first — then draw a straight line",
                    font_size=20, color=GREEN_OK)
        note.move_to(BAND_CHART_CENTER + DOWN * 1.15)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, sq1, sq2, dots_a, dots_b,
                           a_lbl, b_lbl, diagonal, note, note_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Three properties of an algorithm (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Three required properties", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        rows = [
            (r"\text{Unambiguous}", r"\text{each step has one meaning}", BLUE_TERM),
            (r"\text{Finite}", r"\text{ends after a bounded number of steps}", TEAL_TERM),
            (r"\text{Effective}", r"\text{each step can actually be carried out}", ORANGE_TERM),
        ]
        props = VGroup()
        for i, (name, desc, color) in enumerate(rows):
            name_card = make_equation_card(name, color=color, scale=0.85)
            desc_lbl = Text(desc, font_size=20, color=WHITE)
            row = VGroup(name_card, desc_lbl).arrange(RIGHT, buff=0.4)
            row.move_to(BAND_CHART_CENTER + UP * 0.6 + DOWN * i * 0.85)
            props.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.2, run_time=0.8) for r in props],
                        lag_ratio=0.3),
        )
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, props)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject: vague instruction is NOT an algorithm (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Not an algorithm", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        bad = make_equation_card(
            r"\text{``go that way and you'll find it''}",
            color=RED_REJECT, scale=1.0,
        )
        bad.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(bad, shift=UP * 0.2, run_time=1.4))
        self.wait(1.5)

        why = Text("vague — no exact steps, no clear finish",
                   font_size=20, color=RED_REJECT)
        why.next_to(bad, DOWN, buff=0.4)
        why_bg = BackgroundRectangle(why, color=BLACK,
                                     fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.0))
        self.wait(2.0)

        cross = Cross(VGroup(bad, why_bg, why), color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))
        self.wait(1.5)

        beat4 = beat_group(head4, head4_bg, bad, why_bg, why, cross)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 107.6 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Algorithm} \;=\; \text{unambiguous + finite + effective}",
            "Every spatial algorithm must satisfy all three properties.",
            final_wait=48.0,
        )