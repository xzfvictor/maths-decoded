import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class RelativeFrequencyScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Relative frequency", "Use repeated trials to estimate probability")

        beat = None
        count = MathTex(r"\text{relative frequency} = \frac{\text{event count}}{\text{number of trials}}", color=BLUE_TERM).scale(0.95)
        count.move_to(UP * 1.25)
        count_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.22)
        count_bg.move_to(count.get_center())
        beat = beat_group(beat, count_bg, count)
        self.play(FadeIn(count_bg), Write(count, run_time=1.8))
        self.wait(2)
        coin = VGroup(
            MathTex(r"5\text{ flips}", color=ORANGE_TERM),
            MathTex(r"\longrightarrow\text{ noisy result}", color=RED_REJECT),
            MathTex(r"500\text{ flips}", color=TEAL_TERM),
            MathTex(r"\longrightarrow\text{ clearer picture}", color=GREEN_OK),
        ).arrange(DOWN, buff=0.24).scale(0.82).move_to(DOWN * 0.35)
        coin_bg = BackgroundRectangle(coin, color=BLACK, fill_opacity=0.95, buff=0.2)
        coin_bg.move_to(coin.get_center())
        beat = beat_group(beat, coin_bg, coin)
        self.play(FadeIn(coin_bg), LaggedStart(*[Write(x) for x in coin], lag_ratio=0.15))
        self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        dots = VGroup(*[Dot(LEFT * 3.2 + RIGHT * i * 0.7 + UP * (0.25 * ((i % 3) - 1)), color=BLUE_TERM) for i in range(10)])
        dots.set_z_index(1)
        baseline = DashedLine(LEFT * 3.4 + UP * 0.2, RIGHT * 3.4 + UP * 0.2, color=GREEN_OK)
        baseline_lbl = Text("true probability", font_size=20, color=GREEN_OK).next_to(baseline, RIGHT, buff=0.2).scale(0.75)
        baseline_bg = BackgroundRectangle(baseline_lbl, color=BLACK, fill_opacity=0.95, buff=0.12)
        baseline_bg.move_to(baseline_lbl.get_center())
        label = Text("many trials: values cluster closer", font_size=22, color=TEAL_TERM).move_to(UP * 1.15)
        label_bg = BackgroundRectangle(label, color=BLACK, fill_opacity=1, buff=0.16)
        label_bg.move_to(label.get_center())
        beat = beat_group(beat, dots, baseline, baseline_bg, baseline_lbl, label_bg, label)
        self.play(FadeIn(label_bg), FadeIn(label), Create(baseline), FadeIn(baseline_bg), FadeIn(baseline_lbl), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08))
        self.wait(3)
        near = Text("few trials: big fluctuations", font_size=22, color=ORANGE_TERM).move_to(DOWN * 1.0)
        near_bg = BackgroundRectangle(near, color=BLACK, fill_opacity=1, buff=0.16)
        near_bg.move_to(near.get_center())
        beat = beat_group(beat, near_bg, near)
        self.play(FadeIn(near_bg), FadeIn(near))
        self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        bad = Text("\"A few trials should give the exact probability.\"", font_size=24).move_to(UP * 0.35)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2)
        bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        fix = Text("Not necessarily — run-to-run variability is normal.", font_size=22, color=RED_REJECT).move_to(DOWN * 0.65)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.18)
        fix_bg.move_to(fix.get_center())
        beat = beat_group(beat, bad_bg, bad, cross, fix_bg, fix)
        self.play(FadeIn(bad_bg), FadeIn(bad))
        self.wait(1.5)
        self.play(Create(cross))
        self.play(FadeIn(fix_bg), FadeIn(fix))
        self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"P(A) \approx \frac{\text{number of times }A\text{ occurs}}{n}", "More trials usually make the estimate settle.", final_wait=30.1)
