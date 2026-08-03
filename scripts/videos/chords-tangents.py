import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class ChordsTangentsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Chords and tangents",
            "Tangent–chord angle = inscribed angle in the alternate segment.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Draw circle, tangent, chord (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Tangent at A", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        centre = np.array([0.0, 0.0, 0.0]) + BAND_CHART_CENTER
        radius = 1.0
        circle = Circle(radius=radius, color=WHITE).move_to(centre)

        # Tangent point A at angle 60°.
        a_angle = np.deg2rad(60)
        a_pt = centre + radius * np.array([np.cos(a_angle), np.sin(a_angle), 0])
        a_dot = Dot(a_pt, color=BLUE_TERM)
        a_lbl = MathTex("A", color=BLUE_TERM).scale(0.9).next_to(a_dot, RIGHT, buff=0.2)

        # Tangent line at A (perpendicular to OA). Direction = rotate 90°.
        tangent_dir = np.array([-np.sin(a_angle), np.cos(a_angle), 0])
        tangent_line = Line(
            a_pt - tangent_dir * 1.3, a_pt + tangent_dir * 1.3,
            color=ORANGE_TERM, stroke_width=4,
        )
        tangent_lbl = MathTex(r"\text{tangent}", color=ORANGE_TERM).scale(0.8)
        tangent_lbl_pos = a_pt + tangent_dir * 1.35 + DOWN * 0.15
        tangent_lbl.move_to(tangent_lbl_pos)
        tangent_lbl_bg = BackgroundRectangle(tangent_lbl, color=BLACK,
                                              fill_opacity=0.9, buff=0.15)
        tangent_lbl_bg.move_to(tangent_lbl.get_center())

        # Chord AB. Choose B at angle 200°.
        b_angle = np.deg2rad(200)
        b_pt = centre + radius * np.array([np.cos(b_angle), np.sin(b_angle), 0])
        b_dot = Dot(b_pt, color=BLUE_TERM)
        b_lbl = MathTex("B", color=BLUE_TERM).scale(0.9).next_to(b_dot, DL, buff=0.1)
        chord = Line(a_pt, b_pt, color=BLUE_TERM, stroke_width=4)
        chord_lbl = MathTex(r"\text{chord}", color=BLUE_TERM).scale(0.8)
        chord_lbl.move_to((a_pt + b_pt) / 2 + RIGHT * 0.2)
        chord_lbl_bg = BackgroundRectangle(chord_lbl, color=BLACK,
                                           fill_opacity=0.9, buff=0.15)
        chord_lbl_bg.move_to(chord_lbl.get_center())

        self.play(Create(circle, run_time=1.4))
        self.play(FadeIn(a_dot), FadeIn(a_lbl), run_time=0.6)
        self.play(Create(tangent_line, run_time=1.0),
                  FadeIn(tangent_lbl_bg), FadeIn(tangent_lbl), run_time=0.6)
        self.play(FadeIn(b_dot), FadeIn(b_lbl), run_time=0.6)
        self.play(Create(chord, run_time=1.0),
                  FadeIn(chord_lbl_bg), FadeIn(chord_lbl), run_time=0.6)
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, circle, a_dot, a_lbl,
                           tangent_line, tangent_lbl, tangent_lbl_bg,
                           b_dot, b_lbl, chord, chord_lbl, chord_lbl_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Tangent–chord angle equals alternate-segment inscribed angle (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Alternate segment", font_size=26, color=TEAL_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        # Recreate compact diagram for the theorem.
        circle2 = Circle(radius=radius, color=WHITE).move_to(centre)
        a_dot2 = Dot(a_pt, color=BLUE_TERM)
        b_dot2 = Dot(b_pt, color=BLUE_TERM)
        tangent2 = Line(a_pt - tangent_dir * 1.3, a_pt + tangent_dir * 1.3,
                        color=ORANGE_TERM, stroke_width=4)
        chord2 = Line(a_pt, b_pt, color=BLUE_TERM, stroke_width=4)
        # Inscribed point C on the opposite side of chord from the tangent-chord angle.
        c_angle = np.deg2rad(150)
        c_pt = centre + radius * np.array([np.cos(c_angle), np.sin(c_angle), 0])
        c_dot = Dot(c_pt, color=TEAL_TERM)
        c_lbl = MathTex("C", color=TEAL_TERM).scale(0.9).next_to(c_dot, UP, buff=0.25)
        ca = Line(c_pt, a_pt, color=TEAL_TERM, stroke_width=3)
        cb = Line(c_pt, b_pt, color=TEAL_TERM, stroke_width=3)

        # Mark angle at A (between tangent and chord).
        ang_a = Angle(Line(a_pt, a_pt + tangent_dir * 0.8),
                      chord2, radius=0.35, color=GREEN_OK)
        # Mark angle at C (inscribed).
        ang_c = Angle(ca, cb, radius=0.35, color=GREEN_OK)

        diagram = VGroup(circle2, a_dot2, b_dot2, tangent2, chord2,
                         c_dot, c_lbl, ca, cb, ang_a, ang_c)
        diagram.scale(0.85)
        diagram.move_to(BAND_CHART_CENTER + LEFT * 2.4)

        self.play(FadeIn(diagram, run_time=2.0))
        self.wait(2.0)

        eq = make_equation_card(
            r"\angle_{\text{tan–chord}} \;=\; \angle_{\text{alternate}}",
            color=GREEN_OK, scale=1.0,
        )
        eq.move_to(BAND_CHART_CENTER + RIGHT * 2.8)
        self.play(FadeIn(eq, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, diagram, eq)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Reject the wrong segment (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Common mistake", font_size=26, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        # Wrong: C on the SAME side as the tangent-chord angle.
        wrong_c_angle = np.deg2rad(330)
        wrong_c_pt = centre + radius * np.array(
            [np.cos(wrong_c_angle), np.sin(wrong_c_angle), 0]
        )
        wrong_circle = Circle(radius=radius, color=WHITE).move_to(centre)
        wrong_a = Dot(a_pt, color=BLUE_TERM)
        wrong_b = Dot(b_pt, color=BLUE_TERM)
        wrong_tan = Line(a_pt - tangent_dir * 1.3, a_pt + tangent_dir * 1.3,
                         color=ORANGE_TERM, stroke_width=4)
        wrong_chord = Line(a_pt, b_pt, color=BLUE_TERM, stroke_width=4)
        wrong_c = Dot(wrong_c_pt, color=RED_REJECT)
        wrong_c_lbl = MathTex("C'", color=RED_REJECT).scale(0.9).next_to(
            wrong_c, DR, buff=0.1)
        wrong_ca = Line(wrong_c_pt, a_pt, color=RED_REJECT, stroke_width=3)
        wrong_cb = Line(wrong_c_pt, b_pt, color=RED_REJECT, stroke_width=3)
        wrong_diag = VGroup(wrong_circle, wrong_a, wrong_b, wrong_tan, wrong_chord,
                            wrong_c, wrong_c_lbl, wrong_ca, wrong_cb)
        wrong_diag.scale(0.85)
        wrong_diag.move_to(BAND_CHART_CENTER + LEFT * 2.4)

        self.play(FadeIn(wrong_diag, run_time=1.5))

        cross = Cross(wrong_diag, color=RED_REJECT, stroke_width=5)
        self.play(Create(cross, run_time=1.0))

        wrong_note = Text("must be the alternate segment!",
                          font_size=20, color=RED_REJECT)
        wrong_note.move_to(BAND_CHART_CENTER + RIGHT * 2.8)
        wrong_note_bg = BackgroundRectangle(wrong_note, color=BLACK,
                                           fill_opacity=0.95, buff=0.15)
        wrong_note_bg.move_to(wrong_note.get_center())
        self.play(FadeIn(wrong_note_bg, run_time=0.4),
                  FadeIn(wrong_note, run_time=1.0))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, wrong_diag, cross,
                           wrong_note, wrong_note_bg)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 95.9 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\angle_{\text{tan–chord}} = \angle_{\text{alternate segment}}",
            "The chord cuts the circle into two arcs; pick the OTHER arc.",
            final_wait=43.0,
        )