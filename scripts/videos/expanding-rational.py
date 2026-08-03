"""Manim scene aligned to the expanding-rational narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_equation_card, animate_intro,
    animate_final_definition,
)


class ExpandingRationalScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "Expanding fractional and negative coefficients",
            "Distribute to every term, then check each sign.",
        )

        head = Text("A fraction multiplies every term", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.46)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        start = make_equation_card(r"\frac12(4x-6)", color=BLUE_TERM, scale=1.08)
        start.move_to(BAND_CHART_CENTER + UP * 0.48)
        distribute = MathTex(
            r"\frac12(4x)+\frac12(-6)=2x-3", color=GREEN_OK
        ).scale(0.92).move_to(BAND_CHART_CENTER + DOWN * 0.43)
        distribute_bg = BackgroundRectangle(distribute, color=BLACK, fill_opacity=1, buff=0.17)
        note = Text("Half of 4x is 2x; half of −6 is −3.", font_size=21, color=TEAL_TERM)
        note.move_to(BAND_CHART_CENTER + DOWN * 1.12)
        note_bg = BackgroundRectangle(note, color=BLACK, fill_opacity=0.96, buff=0.12)
        beat2 = beat_group(head_bg, head, start, distribute_bg, distribute, note_bg, note)
        self.play(FadeIn(head_bg), FadeIn(head))
        self.play(FadeIn(start, shift=UP * 0.15), run_time=1.2)
        self.play(FadeIn(distribute_bg), Write(distribute), run_time=1.4)
        self.play(FadeIn(note_bg), FadeIn(note))
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        head3 = Text("A minus outside flips every sign", font_size=26, color=ORANGE_TERM)
        head3.move_to(BAND_CHART_CENTER + UP * 1.46)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        before = make_equation_card(r"-(3x-5)", color=ORANGE_TERM, scale=1.15)
        before.move_to(BAND_CHART_CENTER + UP * 0.45)
        arrows = VGroup(
            MathTex(r"-(3x)=-3x", color=BLUE_TERM).scale(0.88),
            MathTex(r"-(-5)=+5", color=TEAL_TERM).scale(0.88),
        ).arrange(RIGHT, buff=1.0).move_to(BAND_CHART_CENTER + DOWN * 0.35)
        arrow_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=1, buff=0.13)
            for item in arrows
        ])
        result = MathTex(r"-(3x-5)=-3x+5", color=GREEN_OK).scale(1.0)
        result.move_to(BAND_CHART_CENTER + DOWN * 1.02)
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=1, buff=0.16)
        beat3 = beat_group(head3_bg, head3, before, arrow_bgs, arrows, result_bg, result)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        self.play(FadeIn(before))
        for bg, item in zip(arrow_bgs, arrows):
            self.play(FadeIn(bg), Write(item), run_time=0.8)
        self.play(FadeIn(result_bg), Write(result))
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Put the fraction and negative together", font_size=25, color=GREEN_OK)
        head4.move_to(BAND_CHART_CENTER + UP * 1.47)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        problem = make_equation_card(r"-\frac23(9x+12)", color=ORANGE_TERM, scale=1.12)
        problem.move_to(BAND_CHART_CENTER + UP * 0.52)
        products = MathTex(
            r"-\frac23(9x)-\frac23(12)", color=BLUE_TERM
        ).scale(0.93).move_to(BAND_CHART_CENTER + DOWN * 0.28)
        products_bg = BackgroundRectangle(products, color=BLACK, fill_opacity=1, buff=0.16)
        answer = make_equation_card(r"-6x-8", color=GREEN_OK, scale=1.15)
        answer.move_to(BAND_CHART_CENTER + DOWN * 1.0)
        beat4 = beat_group(head4_bg, head4, problem, products_bg, products, answer)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        self.play(FadeIn(problem))
        self.play(FadeIn(products_bg), Write(products))
        self.play(FadeIn(answer), run_time=1.1)
        self.play(Indicate(answer, color=GREEN_OK))
        self.wait(2.5)
        self.play(FadeOut(beat4, run_time=0.8))

        head5 = Text("Final sign-and-arithmetic check", font_size=25, color=RED_REJECT)
        head5.move_to(BAND_CHART_CENTER + UP * 1.43)
        head5_bg = BackgroundRectangle(head5, color=BLACK, fill_opacity=0.95, buff=0.15)
        checklist = VGroup(
            Text("Did I multiply every term?", font_size=22, color=BLUE_TERM),
            Text("Did the negative flip each sign?", font_size=22, color=ORANGE_TERM),
            MathTex(r"\frac12(12)=6\quad\text{not }5", color=GREEN_OK).scale(0.9),
        ).arrange(DOWN, buff=0.3).move_to(BAND_CHART_CENTER + DOWN * 0.08)
        checklist_bgs = VGroup(*[
            BackgroundRectangle(item, color=BLACK, fill_opacity=0.97, buff=0.12)
            for item in checklist
        ])
        beat5 = beat_group(head5_bg, head5, checklist_bgs, checklist)
        self.play(FadeIn(head5_bg), FadeIn(head5))
        for bg, item in zip(checklist_bgs, checklist):
            self.play(FadeIn(bg), FadeIn(item), run_time=0.75)
        self.wait(2.5)
        self.play(FadeOut(beat5, run_time=0.8))

        animate_final_definition(
            self,
            r"-\frac23(9x+12)=-6x-8",
            "Touch every term and keep the negative sign attached.",
            final_wait=65.0,
        )
