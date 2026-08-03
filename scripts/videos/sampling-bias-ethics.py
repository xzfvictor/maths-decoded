"""
Manim scene for the lesson `sampling-bias-ethics`
(topic `l10a-ap-investigating-reports`).

Sampling bias (selection, voluntary-response, non-response) and
research ethics (consent, anonymity, no harm). The animation pairs a
biased-sample sketch with an ethics checklist.

Target duration: ~95.7 s (matches the audio narration length).
"""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SamplingBiasEthicsScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        animate_intro(
            self,
            "Sampling bias and ethics",
            "Bias distorts results; ethics protects participants.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Three types of bias (~24 s)
        # ──────────────────────────────────────────────────────────────────
        head = Text("Common biases", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.7)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        head_bg.move_to(head.get_center())
        self.play(FadeIn(head_bg, run_time=0.4), FadeIn(head, run_time=1.0))
        self.wait(1.0)

        rows = [
            ("Selection", "Only some groups contacted", BLUE_TERM),
            ("Voluntary response", "Self-selected volunteers", ORANGE_TERM),
            ("Non-response", "Some refuse to answer", RED_REJECT),
        ]
        bias_grp = VGroup()
        for i, (name, desc, color) in enumerate(rows):
            name_card = make_equation_card(name, color=color, scale=0.85)
            desc_lbl = Text(desc, font_size=20, color=WHITE)
            row = VGroup(name_card, desc_lbl).arrange(RIGHT, buff=0.4)
            row.move_to(BAND_CHART_CENTER + UP * 0.5 + DOWN * i * 0.85)
            bias_grp.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.2, run_time=0.7) for r in bias_grp],
                        lag_ratio=0.3),
        )
        self.wait(2.5)

        beat2 = beat_group(head, head_bg, bias_grp)
        self.play(FadeOut(beat2, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Concrete bias: voluntary online poll (~20 s)
        # ──────────────────────────────────────────────────────────────────
        head3 = Text("Worked example", font_size=26, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.7)
        head3_bg = BackgroundRectangle(head3, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head3_bg.move_to(head3.get_center())
        self.play(FadeIn(head3_bg, run_time=0.4), FadeIn(head3, run_time=1.0))
        self.wait(1.0)

        ex = make_equation_card(
            r"\text{``Should voting be compulsory?''}",
            color=ORANGE_TERM, scale=0.9,
        )
        ex.move_to(BAND_CHART_CENTER + UP * 0.5)
        self.play(FadeIn(ex, shift=UP * 0.2, run_time=1.3))
        self.wait(1.5)

        res = make_equation_card(
            r"\text{Yes: 89\%}",
            color=RED_REJECT, scale=1.0,
        )
        res.move_to(BAND_CHART_CENTER + DOWN * 0.4)
        self.play(FadeIn(res, shift=UP * 0.2, run_time=1.3))
        self.wait(1.5)

        why = Text("only politically-engaged users replied",
                   font_size=20, color=RED_REJECT)
        why.next_to(res, DOWN, buff=0.3)
        why_bg = BackgroundRectangle(why, color=BLACK,
                                     fill_opacity=0.95, buff=0.15)
        why_bg.move_to(why.get_center())
        self.play(FadeIn(why_bg, run_time=0.4), FadeIn(why, run_time=1.0))
        self.wait(2.5)

        beat3 = beat_group(head3, head3_bg, ex, res, why, why_bg)
        self.play(FadeOut(beat3, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Ethics checklist (~22 s)
        # ──────────────────────────────────────────────────────────────────
        head4 = Text("Ethics checklist", font_size=26, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.7)
        head4_bg = BackgroundRectangle(head4, color=BLACK,
                                       fill_opacity=0.95, buff=0.15)
        head4_bg.move_to(head4.get_center())
        self.play(FadeIn(head4_bg, run_time=0.4), FadeIn(head4, run_time=1.0))
        self.wait(1.0)

        ethics = VGroup()
        items = [
            r"\text{Informed consent}",
            r"\text{Anonymity of responses}",
            r"\text{No harm to participants}",
        ]
        for i, txt in enumerate(items):
            row = make_equation_card(txt, color=GREEN_OK, scale=0.9)
            row.move_to(BAND_CHART_CENTER + UP * 0.6 + DOWN * i * 0.85)
            ethics.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.2, run_time=0.7) for r in ethics],
                        lag_ratio=0.3),
        )
        self.wait(3.0)

        beat4 = beat_group(head4, head4_bg, ethics)
        self.play(FadeOut(beat4, run_time=1.0))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (held; total ≈ 95.7 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\text{Good study} = \text{unbiased sample} + \text{ethical practice}",
            "Watch for bias; respect participants' rights.",
            final_wait=43.0,
        )