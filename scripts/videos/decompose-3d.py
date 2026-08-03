import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class Decompose3dScene(Scene):
    def construct(self) -> None:
        # Beat 1 — title intro.
        animate_intro(
            self,
            "Angle from 3D direction vectors",
            "Decompose the directions, then use one dot product.",
        )

        # Beat 2 — concrete example.
        head2 = Text("Concrete pair of directions", font_size=25, color=BLUE_TERM)
        head2.move_to(BAND_CHART_CENTER + UP * 1.35)
        vectors = make_equation_card(
            r"\vec u=(1,2,2),\qquad \vec v=(2,1,-2)",
            color=BLUE_TERM,
            scale=0.9,
        ).move_to(BAND_CHART_CENTER + UP * 0.45)
        products = make_equation_card(
            r"\vec u\cdot\vec v=2+2-4=0,\quad |\vec u|=|\vec v|=3",
            color=TEAL_TERM,
            scale=0.8,
        ).move_to(BAND_CHART_CENTER + DOWN * 0.45)
        answer = make_equation_card(
            r"\cos\theta=0\quad\Longrightarrow\quad\theta=90^\circ",
            color=GREEN_OK,
            scale=0.85,
        ).move_to(BAND_CHART_CENTER + DOWN * 1.15)
        beat2 = beat_group(head2, vectors, products, answer)
        self.play(FadeIn(head2), FadeIn(vectors, shift=UP * 0.15), run_time=1.2)
        self.play(FadeIn(products, shift=UP * 0.15), run_time=1.1)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=1.1)
        self.wait(4.0)
        self.play(FadeOut(beat2, run_time=0.8))

        # Beat 3 — generalisation.
        head3 = Text("Any two 3D lines", font_size=25, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.35)
        general = make_equation_card(
            r"\cos\theta=\dfrac{|\vec u\cdot\vec v|}{|\vec u|\,|\vec v|}",
            color=GREEN_OK,
            scale=1.05,
        ).move_to(BAND_CHART_CENTER + UP * 0.25)
        note = Text(
            "The absolute value selects the smaller angle between the lines.",
            font_size=21,
            color=TEAL_TERM,
        ).move_to(BAND_CHART_CENTER + DOWN * 0.85)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.95, buff=0.14)
        beat3 = beat_group(head3, general, note_bg, note)
        self.play(FadeIn(head3), FadeIn(general, shift=UP * 0.15), run_time=1.3)
        self.play(FadeIn(note_bg), FadeIn(note), run_time=1.0)
        self.wait(5.0)
        self.play(FadeOut(beat3, run_time=0.8))

        # Beat 4 — contrast and reject.
        head4 = Text("Do not compare coordinates separately", font_size=24, color=RED_REJECT)
        head4.move_to(BAND_CHART_CENTER + UP * 1.35)
        wrong = make_equation_card(
            r"\theta\ne\arctan\!\left(\dfrac{v_y-u_y}{v_x-u_x}\right)",
            color=RED_REJECT,
            scale=0.9,
        ).move_to(BAND_CHART_CENTER + UP * 0.25)
        cross = Cross(wrong, color=RED_REJECT, stroke_width=5)
        correction = Text(
            "A 3D direction has three components: combine all three in the dot product.",
            font_size=20,
            color=ORANGE_TERM,
        ).move_to(BAND_CHART_CENTER + DOWN * 0.9)
        correction_bg = BackgroundRectangle(
            correction, color=BLACK, fill_opacity=0.95, buff=0.14
        )
        beat4 = beat_group(head4, wrong, cross, correction_bg, correction)
        self.play(FadeIn(head4), FadeIn(wrong), run_time=1.1)
        self.play(Create(cross), run_time=0.8)
        self.play(FadeIn(correction_bg), FadeIn(correction), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(beat4, run_time=0.8))

        # Beat 5 — final takeaway.
        animate_final_definition(
            self,
            r"\cos\theta=\dfrac{|\vec u\cdot\vec v|}{|\vec u|\,|\vec v|}",
            "Dot product, magnitudes, inverse cosine — one reliable process.",
            final_wait=46.0,
        )
