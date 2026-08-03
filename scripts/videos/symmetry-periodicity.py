import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class SymmetryPeriodicityScene(Scene):
    def construct(self) -> None:
        # ──────────────────────────────────────────────────────────────────
        # Beat 1 — Title (~5 s)
        # ──────────────────────────────────────────────────────────────────
        title = animate_intro(
            self,
            "Symmetry and periodicity of trig",
            "Sine and cosine are predictable — that is the whole point.",
        )

        # ──────────────────────────────────────────────────────────────────
        # Beat 2 — Periodicity: period is 2 pi (~26 s)
        # ──────────────────────────────────────────────────────────────────
        period = make_equation_card(
            r"\sin(x + 2\pi) \;=\; \sin(x)",
            color=BLUE_TERM,
            scale=1.1,
        )
        period.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(FadeIn(period, run_time=1.4))
        self.wait(3.0)

        # Equal to 360 degrees.
        deg = MathTex(r"2\pi \;\text{rad} \;=\; 360^{\circ}", color=BLUE_TERM).scale(0.95)
        deg.next_to(period, DOWN, buff=0.6)
        deg_bg = BackgroundRectangle(deg, color=BLACK, fill_opacity=0.95, buff=0.18)
        deg_bg.move_to(deg.get_center())
        self.play(FadeIn(deg_bg, run_time=0.4), FadeIn(deg, run_time=1.2))
        self.wait(3.0)

        # The "one cycle then forever" idea.
        note = Text(
            "One cycle, then the pattern repeats forever.",
            font_size=22,
            color=GREEN_OK,
        ).next_to(deg, DOWN, buff=0.5)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.15)
        note_bg.move_to(note.get_center())
        self.play(FadeIn(note_bg, run_time=0.4), FadeIn(note, run_time=1.2))
        self.wait(9.0)

        beat1 = beat_group(period, deg, deg_bg, note, note_bg)
        self.play(FadeOut(beat1, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 3 — Even vs odd symmetry (~30 s)
        # ──────────────────────────────────────────────────────────────────
        # A mirror identity for sine.
        cos_card = make_equation_card(
            r"\sin(\pi-x) \;=\; \sin(x)",
            color=TEAL_TERM,
            scale=1.05,
        )
        cos_card.move_to(BAND_CHART_CENTER + UP * 0.7)
        cos_tag = Text("mirror symmetry about x = pi/2", font_size=20, color=TEAL_TERM)
        cos_tag.next_to(cos_card, DOWN, buff=0.5)
        cos_tag_bg = BackgroundRectangle(cos_tag, color=BLACK, fill_opacity=0.95, buff=0.15)
        cos_tag_bg.move_to(cos_tag.get_center())
        self.play(FadeIn(cos_card, run_time=1.4))
        self.wait(2.0)
        self.play(FadeIn(cos_tag_bg, run_time=0.4), FadeIn(cos_tag, run_time=1.0))
        self.wait(5.0)

        beat_cos = beat_group(cos_card, cos_tag, cos_tag_bg)
        self.play(FadeOut(beat_cos, run_time=0.8))

        # The mirror axes repeat every pi.
        sin_card = make_equation_card(
            r"x=\dfrac{\pi}{2}+n\pi,\qquad n\in\mathbb Z",
            color=ORANGE_TERM,
            scale=1.05,
        )
        sin_card.move_to(BAND_CHART_CENTER + UP * 0.7)
        sin_tag = Text("maxima and minima are alternating mirror axes", font_size=20, color=ORANGE_TERM)
        sin_tag.next_to(sin_card, DOWN, buff=0.5)
        sin_tag_bg = BackgroundRectangle(sin_tag, color=BLACK, fill_opacity=0.95, buff=0.15)
        sin_tag_bg.move_to(sin_tag.get_center())
        self.play(FadeIn(sin_card, run_time=1.4))
        self.wait(2.0)
        self.play(FadeIn(sin_tag_bg, run_time=0.4), FadeIn(sin_tag, run_time=1.0))
        self.wait(8.0)

        beat_sin = beat_group(sin_card, sin_tag, sin_tag_bg)
        self.play(FadeOut(beat_sin, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 4 — Contrast: x squared has neither (~22 s)
        # ──────────────────────────────────────────────────────────────────
        x2 = make_equation_card(
            r"f(x) = \sin x + x",
            color=RED_REJECT,
            scale=1.1,
        )
        x2.move_to(BAND_CHART_CENTER + UP * 0.6)
        self.play(FadeIn(x2, run_time=1.4))
        self.wait(2.5)

        # Neither periodic nor odd.
        nope = Text(
            "Not periodic. The added x term destroys the repeating mirrors.",
            font_size=22,
            color=RED_REJECT,
        ).next_to(x2, DOWN, buff=0.6)
        nope_bg = BackgroundRectangle(nope, color=BLACK, fill_opacity=0.95, buff=0.15)
        nope_bg.move_to(nope.get_center())
        self.play(FadeIn(nope_bg, run_time=0.4), FadeIn(nope, run_time=1.2))
        self.wait(8.0)

        beat2 = beat_group(x2, nope, nope_bg)
        self.play(FadeOut(beat2, run_time=0.8))

        # ──────────────────────────────────────────────────────────────────
        # Beat 5 — Final takeaway (~43 s, total ≈ 95 s)
        # ──────────────────────────────────────────────────────────────────
        animate_final_definition(
            self,
            r"\sin(x+2\pi)=\sin x,\quad x_{\rm mirror}=\tfrac{\pi}{2}+n\pi",
            "Symmetry is why trig identities are shortcuts, not coincidences.",
            final_wait=43.0,
        )
