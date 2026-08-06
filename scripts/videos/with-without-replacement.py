import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class WithWithoutReplacementScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "With vs without replacement", "One decision changes the second draw")

        # Beat 2: exact marble example from the narration.
        beat = None
        setup = Text("Bag: 3 red + 2 blue = 5 marbles", font_size=24).move_to(UP * 1.7)
        setup_bg = BackgroundRectangle(setup, color=BLACK, fill_opacity=1, buff=0.18); setup_bg.move_to(setup.get_center())
        first = MathTex(r"P(R_1)=\frac{3}{5}", color=BLUE_TERM).scale(1.0)
        first.next_to(setup, DOWN, buff=0.5)
        first_bg = BackgroundRectangle(first, color=BLACK, fill_opacity=1, buff=0.2); first_bg.move_to(first.get_center())
        second = MathTex(r"\text{without replacement: }2R+2B", color=ORANGE_TERM).scale(0.86)
        second.next_to(first, DOWN, buff=0.5)
        second_bg = BackgroundRectangle(second, color=BLACK, fill_opacity=1, buff=0.18); second_bg.move_to(second.get_center())
        cond = MathTex(r"P(R_2\mid R_1)=\frac{2}{4}=\frac12", color=TEAL_TERM).scale(1.0)
        cond.next_to(second, DOWN, buff=0.5)
        cond_bg = BackgroundRectangle(cond, color=BLACK, fill_opacity=1, buff=0.2); cond_bg.move_to(cond.get_center())
        beat = beat_group(beat, setup_bg, setup, first_bg, first, second_bg, second, cond_bg, cond)
        self.play(FadeIn(setup_bg, run_time=0.5), FadeIn(setup, run_time=1.0)); self.wait(2)
        self.wait(0.4)
        self.play(FadeIn(first_bg, run_time=0.5), Write(first, run_time=1.2)); self.wait(2)
        # Pause so the second statement doesn't flash over the setup row.
        self.wait(0.8)
        self.play(FadeIn(second_bg, run_time=0.5), Write(second, run_time=1.2)); self.wait(2)
        self.wait(0.4)
        self.play(FadeIn(cond_bg, run_time=0.5), Write(cond, run_time=1.2)); self.wait(3)
        product = MathTex(r"P(R_1\text{ and }R_2)=\frac35\times\frac12=\frac3{10}", color=GREEN_OK).scale(0.95)
        product.move_to(cond.get_center())
        product_bg = BackgroundRectangle(product, color=BLACK, fill_opacity=1, buff=0.2); product_bg.move_to(product.get_center())
        beat = beat_group(beat, product_bg, product)
        self.play(FadeOut(cond_bg), FadeOut(cond), FadeIn(product_bg), Write(product, run_time=1.5)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 3: general comparison.
        beat = None
        with_card = make_term_card(r"\text{with replacement}", r"\text{same probabilities; independent}", GREEN_OK).scale(0.78).move_to(LEFT * 2.7 + UP * 0.45)
        without_card = make_term_card(r"\text{without replacement}", r"\text{probabilities change; dependent}", RED_REJECT).scale(0.78).move_to(RIGHT * 2.7 + UP * 0.45)
        with_formula = MathTex(r"P(R_2)=P(R_1)", color=GREEN_OK).scale(0.8).move_to(LEFT * 2.7 + DOWN * 0.75)
        without_formula = MathTex(r"P(R_2\mid R_1)\ne P(R_1)", color=RED_REJECT).scale(0.8).move_to(RIGHT * 2.7 + DOWN * 0.75)
        wfb = BackgroundRectangle(with_formula, color=BLACK, fill_opacity=1, buff=0.18); wfb.move_to(with_formula.get_center())
        nfb = BackgroundRectangle(without_formula, color=BLACK, fill_opacity=1, buff=0.18); nfb.move_to(without_formula.get_center())
        beat = beat_group(beat, with_card, without_card, wfb, with_formula, nfb, without_formula)
        self.play(FadeIn(with_card), FadeIn(without_card)); self.wait(3); self.play(FadeIn(wfb), Write(with_formula), FadeIn(nfb), Write(without_formula)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 4: reject the claim that branches never change.
        beat = None
        bad = Text("\"The second branch always has the same probability.\"", font_size=21).move_to(UP * 0.4)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.18); bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        fix = Text("Only with replacement; without it, the bag shrinks.", font_size=21, color=RED_REJECT).move_to(DOWN * 0.7)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.17); fix_bg.move_to(fix.get_center())
        beat = beat_group(beat, bad_bg, bad, cross, fix_bg, fix)
        self.play(FadeIn(bad_bg), FadeIn(bad)); self.wait(1.5); self.play(Create(cross)); self.play(FadeIn(fix_bg), FadeIn(fix)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"\text{with: same branches}\quad\text{without: shifted branches}", "Without replacement makes the second draw depend on the first.", final_wait=87.8)
