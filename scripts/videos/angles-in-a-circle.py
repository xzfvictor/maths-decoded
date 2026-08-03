import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *
import numpy as np


class AnglesInACircleScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Angles in a circle",
            "Centre angle = 2 × circumference angle on the same arc.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Circle with centre and circumference points (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Same arc, two angles", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        centre = np.array([0.0, 0.0, 0.0]) + BAND_CHART_CENTER + DOWN * 0.05
        radius = 1.05
        circle = Circle(radius=radius, color=WHITE).move_to(centre)
        centre_dot = Dot(centre, color=ORANGE_TERM)

        # Two points A and B on the circle.
        angle_a = np.deg2rad(30)   # angle of arc (from positive x-axis).
        angle_b = np.deg2rad(170)
        a_pt = centre + radius * np.array([np.cos(angle_a), np.sin(angle_a), 0])
        b_pt = centre + radius * np.array([np.cos(angle_b), np.sin(angle_b), 0])
        a_dot = Dot(a_pt, color=BLUE_TERM)
        b_dot = Dot(b_pt, color=BLUE_TERM)
        a_lbl = MathTex("A", color=BLUE_TERM).scale(0.9).next_to(a_dot, UR, buff=0.1)
        b_lbl = MathTex("B", color=BLUE_TERM).scale(0.9).next_to(b_dot, UL, buff=0.1)

        # Centre angle (orange).
        centre_angle = Arc(radius=0.6, start_angle=angle_a,
                           angle=(angle_b - angle_a), color=ORANGE_TERM)
        c_lbl = MathTex(r"\theta_c", color=ORANGE_TERM).scale(0.9)
        mid_a = angle_a + (angle_b - angle_a) / 2
        c_lbl.move_to(centre + 0.85 * np.array([np.cos(mid_a), np.sin(mid_a), 0]))
        c_lbl_bg = BackgroundRectangle(c_lbl, color=BLACK,
                                       fill_opacity=0.9, buff=0.15)
        c_lbl_bg.move_to(c_lbl.get_center())

        # Circumference point P (on the major arc), draw two chords.
        p_angle = np.deg2rad(-60)
        p_pt = centre + radius * np.array([np.cos(p_angle), np.sin(p_angle), 0])
        p_dot = Dot(p_pt, color=TEAL_TERM)
        p_lbl = MathTex("P", color=TEAL_TERM).scale(0.9).next_to(p_dot, DR, buff=0.1)
        line_pa = Line(p_pt, a_pt, color=TEAL_TERM, stroke_width=3)
        line_pb = Line(p_pt, b_pt, color=TEAL_TERM, stroke_width=3)

        # Circumference angle marker at P.
        ap_vec = a_pt - p_pt
        bp_vec = b_pt - p_pt
        ap_dir = angle_of_vector(ap_vec[:2])
        bp_dir = angle_of_vector(bp_vec[:2])
        # Compute small arc at P between segments PA and PB.
        diff = bp_dir - ap_dir
        if diff > np.pi:
            diff -= 2 * np.pi
        if diff < -np.pi:
            diff += 2 * np.pi
        circ_angle = Arc(radius=0.4, start_angle=ap_dir,
                         angle=diff, color=GREEN_OK).move_arc_center_to(p_pt)
        theta_p = MathTex(r"\theta_p", color=GREEN_OK).scale(0.85)
        theta_p_pos = p_pt + 0.6 * np.array(
            [np.cos(ap_dir + diff / 2), np.sin(ap_dir + diff / 2), 0]
        )
        theta_p.move_to(theta_p_pos)
        theta_p_bg = BackgroundRectangle(theta_p, color=BLACK,
                                          fill_opacity=0.9, buff=0.15)
        theta_p_bg.move_to(theta_p.get_center())

        self.play(Create(circle, run_time=1.4))
        self.play(FadeIn(centre_dot, run_time=0.5),
                  FadeIn(a_dot), FadeIn(b_dot),
                  FadeIn(a_lbl), FadeIn(b_lbl), run_time=1.0)
        self.play(Create(centre_angle, run_time=1.0),
                  FadeIn(c_lbl_bg), FadeIn(c_lbl), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(p_dot), FadeIn(p_lbl),
                  Create(line_pa), Create(line_pb), run_time=1.2)
        self.play(Create(circ_angle, run_time=1.0),
                  FadeIn(theta_p_bg), FadeIn(theta_p), run_time=0.8)
        self.wait(1.5)

        beat2 = beat_group(head, head_bg, circle, centre_dot,
                           a_dot, b_dot, a_lbl, b_lbl,
                           centre_angle, c_lbl, c_lbl_bg,
                           p_dot, p_lbl, line_pa, line_pb,
                           circ_angle, theta_p, theta_p_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Theorem: theta_centre = 2 * theta_circumference (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Centre–circumference theorem", font_size=26, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        eq = make_equation_card(
            r"\theta_c = 2\,\theta_p",
            color=GREEN_OK, scale=1.4,
        )
        eq.move_to(BAND_CHART_CENTER + UP * 0.3)
        self.play(FadeIn(eq, shift=UP * 0.2, run_time=1.6))
        self.wait(2.5)

        note = Text("Same arc AB, two viewpoints.",
                    font_size=20, color=WHITE)
        note.next_to(eq, DOWN, buff=0.4)
        note_bg = BackgroundRectangle(note, color=BLACK,
                                      fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.0))
        self.wait(2.0)

        beat3 = beat_group(head3, head3_bg, eq, note, note_bg)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Same segment: equal angles (~18 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Same segment", font_size=26, color=TEAL_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        # Two circumference points Q and R on the same major arc.
        q_angle = np.deg2rad(-30)
        r_angle = np.deg2rad(-100)
        q_pt = centre + radius * np.array([np.cos(q_angle), np.sin(q_angle), 0])
        r_pt = centre + radius * np.array([np.cos(r_angle), np.sin(r_angle), 0])
        circle2 = circle.copy()
        q_dot = Dot(q_pt, color=TEAL_TERM)
        r_dot = Dot(r_pt, color=TEAL_TERM)
        q_lbl = MathTex("Q", color=TEAL_TERM).scale(0.9).next_to(q_dot, DR, buff=0.1)
        r_lbl = MathTex("R", color=TEAL_TERM).scale(0.9).next_to(r_dot, DL, buff=0.1)

        # Chords QA, QB and RA, RB.
        qa = Line(q_pt, a_pt, color=TEAL_TERM, stroke_width=3)
        qb = Line(q_pt, b_pt, color=TEAL_TERM, stroke_width=3)
        ra = Line(r_pt, a_pt, color=TEAL_TERM, stroke_width=3)
        rb = Line(r_pt, b_pt, color=TEAL_TERM, stroke_width=3)
        circle_grp = VGroup(circle2, a_dot.copy(), b_dot.copy(), a_lbl.copy(), b_lbl.copy(),
                            q_dot, r_dot, q_lbl, r_lbl, qa, qb, ra, rb)
        circle_grp.move_to(BAND_CHART_CENTER + UP * 0.15)

        self.play(FadeIn(circle_grp, run_time=1.5))
        self.wait(2.0)

        eq4 = make_equation_card(
            r"\angle Q = \angle R",
            color=GREEN_OK, scale=1.2,
        )
        eq4.move_to(BAND_CHART_CENTER + DOWN * 1.05)
        self.play(FadeIn(eq4, shift=UP * 0.2, run_time=1.4))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, circle_grp, eq4)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 83.9 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\theta_{\text{centre}} = 2\,\theta_{\text{circumference}}",
            "Equal angles for all points on the same circumference arc.",
            final_wait=38.0,
        )