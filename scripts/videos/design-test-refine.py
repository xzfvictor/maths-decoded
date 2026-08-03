import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class DesignTestRefineScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Design, test, refine",
            "Spatial problems need iteration, not a one-shot answer.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Design: sketch a plan for a 3D path (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Step 1: Design", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.35)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(0.8)

        # Three small dots as a "path".
        p1 = Dot(BAND_CHART_CENTER + LEFT * 2.5 + UP * 0.6, color=BLUE_TERM)
        p2 = Dot(BAND_CHART_CENTER + UP * 0.2, color=BLUE_TERM)
        p3 = Dot(BAND_CHART_CENTER + RIGHT * 2.5 + DOWN * 0.4, color=BLUE_TERM)
        path = VGroup(
            Line(p1.get_center(), p2.get_center(), color=BLUE_TERM, stroke_width=4),
            Line(p2.get_center(), p3.get_center(), color=BLUE_TERM, stroke_width=4),
        )
        # Arrow to "design" card.
        design_card = make_equation_card(
            r"\text{Plan a path A} \rightarrow \text{B} \rightarrow \text{C}",
            color=BLUE_TERM, scale=0.9,
        )
        design_card.move_to(BAND_CHART_CENTER + DOWN * 0.9)
        design_card.set_z_index(2)

        self.play(FadeIn(p1, run_time=0.4), FadeIn(p2, run_time=0.4),
                  FadeIn(p3, run_time=0.4))
        self.play(Create(path, run_time=1.0))
        self.play(FadeIn(design_card, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        beat2 = beat_group(head, head_bg, p1, p2, p3, path, design_card)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Test: does the design work? (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Step 2: Test", font_size=26, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(0.8)

        check_ok = make_equation_card(
            r"\text{Check: stays in safe zone?}",
            color=ORANGE_TERM, scale=0.9,
        )
        check_ok.move_to(BAND_CHART_CENTER + UP * 0.4)
        self.play(FadeIn(check_ok, shift=UP * 0.2, run_time=1.2))
        self.wait(1.5)

        result = make_equation_card(
            r"\text{Result: hits an obstacle at step 2!}",
            color=RED_REJECT, scale=0.9,
        )
        result.move_to(BAND_CHART_CENTER + DOWN * 0.7)
        self.play(FadeIn(result, shift=UP * 0.2, run_time=1.2))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, check_ok, result)
        self.play(FadeOut(beat3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Refine: redirect path; loop until success (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Step 3: Refine", font_size=26, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(0.8)

        # New midpoint that avoids obstacle.
        new_p2 = Dot(BAND_CHART_CENTER + UP * 0.6, color=GREEN_OK)
        new_path = VGroup(
            Line(p1.get_center(), new_p2.get_center(), color=GREEN_OK, stroke_width=4),
            Line(new_p2.get_center(), p3.get_center(), color=GREEN_OK, stroke_width=4),
        )
        new_path.move_to(BAND_CHART_CENTER)

        self.play(FadeIn(new_p2, run_time=0.4))
        self.play(Create(new_path, run_time=1.2))
        self.wait(1.5)

        # Show the loop as a cycle diagram.
        loop_label = Text("repeat until it works",
                          font_size=22, color=GREEN_OK)
        loop_label.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        loop_label_bg = BackgroundRectangle(loop_label, color=BLACK,
                                            fill_opacity=0.95, buff=0.15)
        loop_label_bg.move_to(loop_label.get_center())

        ok_label = make_equation_card(
            r"\text{Path now avoids the obstacle.}",
            color=GREEN_OK, scale=0.9,
        )
        ok_label.move_to(BAND_CHART_CENTER + DOWN * 1.05)
        self.play(FadeIn(loop_label_bg, run_time=0.4),
                  FadeIn(loop_label, run_time=1.0))
        self.play(FadeIn(ok_label, shift=UP * 0.2, run_time=1.2))
        self.wait(2.0)

        beat4 = beat_group(head4, head4_bg, new_p2, new_path,
                           loop_label, loop_label_bg, ok_label)
        self.play(FadeOut(beat4, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 94.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Design} \;\to\; \text{Test} \;\to\; \text{Refine} \;\to\; \cdots",
            "Iterate: each cycle gets you closer to a working solution.",
            final_wait=43.0,
        )