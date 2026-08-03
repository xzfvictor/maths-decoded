"""
Manim scene for the lesson `log-scales`
(topic `l10a-an-logarithms-scales`).

Logarithmic scales compress huge ranges into a readable axis: equal
steps along the axis correspond to equal ratios, not equal differences.
Show the decibels (10×), pH (10×) and Richter (10×) scales — each one
encodes a tenfold ratio per unit.

Target duration: ~80 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class LogScalesScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Logarithmic scales",
            "Equal steps on the axis mean equal ratios, not equal differences.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Show three 10× scales side-by-side (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_2 = beat_group()

        head = Text("Three scales, each jumps by ×10",
                    font_size=24, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.15)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        beat_2 = beat_group(beat_2, head, head_bg)
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.2))
        self.wait(1.0)

        db = make_equation_card(
            r"\text{dB} \;=\; 10\,\log\!\left(\dfrac{I}{I_{0}}\right)",
            color=GREEN_OK,
            scale=0.78,
        )
        db.move_to(BAND_CHART_CENTER + UP * 0.1 + LEFT * 3.6)
        db_lbl = Text("sound intensity", font_size=20, color=GREEN_OK)
        db_lbl.next_to(db, DOWN, buff=0.25)
        db_lbl_bg = BackgroundRectangle(db_lbl, color=BLACK,
                                        fill_opacity=0.95, buff=0.12)
        db_lbl_bg.move_to(db_lbl.get_center())
        db_grp = VGroup(db, db_lbl, db_lbl_bg)
        beat_2 = beat_group(beat_2, db_grp)

        ph = make_equation_card(
            r"\text{pH} \;=\; -\log[\,\text{H}^{+}\,]",
            color=ORANGE_TERM,
            scale=0.78,
        )
        ph.move_to(BAND_CHART_CENTER + UP * 0.1 + RIGHT * 0.1)
        ph_lbl = Text("acidity", font_size=20, color=ORANGE_TERM)
        ph_lbl.next_to(ph, DOWN, buff=0.25)
        ph_lbl_bg = BackgroundRectangle(ph_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.12)
        ph_lbl_bg.move_to(ph_lbl.get_center())
        ph_grp = VGroup(ph, ph_lbl, ph_lbl_bg)
        beat_2 = beat_group(beat_2, ph_grp)

        rk = make_equation_card(
            r"\text{Richter} \;\propto\; \log(\text{amplitude})",
            color=TEAL_TERM,
            scale=0.78,
        )
        rk.move_to(BAND_CHART_CENTER + UP * 0.1 + RIGHT * 3.7)
        rk_lbl = Text("earthquakes", font_size=20, color=TEAL_TERM)
        rk_lbl.next_to(rk, DOWN, buff=0.25)
        rk_lbl_bg = BackgroundRectangle(rk_lbl, color=BLACK,
                                         fill_opacity=0.95, buff=0.12)
        rk_lbl_bg.move_to(rk_lbl.get_center())
        rk_grp = VGroup(rk, rk_lbl, rk_lbl_bg)
        beat_2 = beat_group(beat_2, rk_grp)

        self.play(FadeIn(db_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(0.6)
        self.play(FadeIn(ph_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(0.6)
        self.play(FadeIn(rk_grp, shift=UP * 0.2, run_time=1.3))
        self.wait(3.0)
        self.play(FadeOut(beat_2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Each tick = a tenfold ratio (~25 s)
        # ──────────────────────────────────────────────────────────────────
        beat_3 = beat_group()

        tick = MathTex(
            r"\Delta \text{(axis)} \;=\; 1 \;\Longleftrightarrow\; \times 10 \text{ (real value)}",
            color=BLUE_TERM,
        ).scale(1.0)
        tick.move_to(BAND_CHART_CENTER + UP * 0.4)
        tick_bg = BackgroundRectangle(tick, color=BLACK, fill_opacity=1, buff=0.22)
        tick_bg.move_to(tick.get_center())
        beat_3 = beat_group(beat_3, tick, tick_bg)
        self.play(FadeIn(tick_bg, run_time=0.4), Write(tick, run_time=2.0))
        self.wait(2.5)

        # Concrete examples under each scale.
        dbe = Text("+10 dB = sound is 10× louder",
                   font_size=20, color=GREEN_OK)
        dbe.move_to(BAND_CHART_CENTER + UP * -0.3 + LEFT * 3.6)
        dbe_bg = BackgroundRectangle(dbe, color=BLACK, fill_opacity=0.95, buff=0.12)
        dbe_bg.move_to(dbe.get_center())
        beat_3 = beat_group(beat_3, dbe, dbe_bg)

        phe = Text("pH −1 means 10× more acid",
                   font_size=20, color=ORANGE_TERM)
        phe.move_to(BAND_CHART_CENTER + UP * -0.3 + RIGHT * 0.1)
        phe_bg = BackgroundRectangle(phe, color=BLACK, fill_opacity=0.95, buff=0.12)
        phe_bg.move_to(phe.get_center())
        beat_3 = beat_group(beat_3, phe, phe_bg)

        rke = Text("+1 Richter = 10× shake",
                   font_size=20, color=TEAL_TERM)
        rke.move_to(BAND_CHART_CENTER + UP * -0.3 + RIGHT * 3.7)
        rke_bg = BackgroundRectangle(rke, color=BLACK, fill_opacity=0.95, buff=0.12)
        rke_bg.move_to(rke.get_center())
        beat_3 = beat_group(beat_3, rke, rke_bg)

        self.play(FadeIn(dbe_bg, run_time=0.3), FadeIn(dbe, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(phe_bg, run_time=0.3), FadeIn(phe, run_time=1.0))
        self.wait(0.5)
        self.play(FadeIn(rke_bg, run_time=0.3), FadeIn(rke, run_time=1.0))
        self.wait(5.5)
        self.play(FadeOut(beat_3, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Final takeaway (~30 s, total ≈ 80 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\Delta \text{(axis)} \;=\; 1 \;\Longleftrightarrow\; \times 10 \text{ real value}",
            "Each scale encodes tenfold ratios — once you've used one, all feel familiar.",
            final_wait=30.0,
        )
