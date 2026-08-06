import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RunningSimulationScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Running a simulation", "Turn many random trials into an estimate")

        beat = None
        run = MathTex(r"N \approx 1000\text{ trials}", color=BLUE_TERM).scale(1.15).move_to(UP * 0.75)
        run_bg = BackgroundRectangle(run, color=BLACK, fill_opacity=1, buff=0.22); run_bg.move_to(run.get_center())
        count = MathTex(r"k = \text{trials where the event occurred}", color=TEAL_TERM).scale(0.9).move_to(DOWN * 0.15)
        count_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.2); count_bg.move_to(count.get_center())
        estimate = MathTex(r"\text{estimate} = \frac{k}{N}", color=GREEN_OK).scale(1.0).move_to(DOWN * 1.05)
        est_bg = BackgroundRectangle(estimate, color=BLACK, fill_opacity=1, buff=0.2); est_bg.move_to(estimate.get_center())
        beat = beat_group(beat, run_bg, run, count_bg, count, est_bg, estimate)
        self.play(FadeIn(run_bg), Write(run)); self.wait(2)
        self.play(FadeIn(count_bg), Write(count)); self.wait(2)
        self.play(FadeIn(est_bg), Write(estimate)); self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        law = Text("Law of Large Numbers", font_size=28, color=TEAL_TERM).move_to(UP * 0.95)
        law_bg = BackgroundRectangle(law, color=BLACK, fill_opacity=1, buff=0.2); law_bg.move_to(law.get_center())
        arrow = Arrow(LEFT * 3.2 + DOWN * 0.15, RIGHT * 3.2 + DOWN * 0.15, color=GREEN_OK, buff=0)
        settle = Text("relative frequency settles closer to true probability", font_size=21, color=GREEN_OK).move_to(DOWN * 0.65)
        settle_bg = BackgroundRectangle(settle, color=BLACK, fill_opacity=0.95, buff=0.17); settle_bg.move_to(settle.get_center())
        beat = beat_group(beat, law_bg, law, arrow, settle_bg, settle)
        self.play(FadeIn(law_bg), FadeIn(law), Create(arrow)); self.wait(2)
        self.play(FadeIn(settle_bg), FadeIn(settle)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        error = MathTex(r"\text{error} \sim \frac{1}{\sqrt{N}}", color=ORANGE_TERM).scale(1.15).move_to(UP * 0.7)
        error_bg = BackgroundRectangle(error, color=BLACK, fill_opacity=1, buff=0.22); error_bg.move_to(error.get_center())
        more = Text("10 times more trials  →  about 3 times more accuracy", font_size=21, color=ORANGE_TERM).move_to(DOWN * 0.3)
        more_bg = BackgroundRectangle(more, color=BLACK, fill_opacity=0.95, buff=0.17); more_bg.move_to(more.get_center())
        apps = Text("birthday problem  •  Monty Hall  •  estimating pi", font_size=21, color=BLUE_TERM).move_to(DOWN * 1.05)
        apps_bg = BackgroundRectangle(apps, color=BLACK, fill_opacity=0.95, buff=0.17); apps_bg.move_to(apps.get_center())
        beat = beat_group(beat, error_bg, error, more_bg, more, apps_bg, apps)
        self.play(FadeIn(error_bg), Write(error)); self.wait(2)
        self.play(FadeIn(more_bg), FadeIn(more)); self.wait(3)
        self.play(FadeIn(apps_bg), FadeIn(apps)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"\widehat{P}(A) = \frac{k}{N}", "Repeat many trials; the estimate usually stabilises.", final_wait=20)
