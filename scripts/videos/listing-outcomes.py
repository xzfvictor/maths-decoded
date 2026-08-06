import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class ListingOutcomesScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Listing two-step outcomes", "Choose a representation, then count every leaf")

        # Beat 2: concrete ordered list for two coin tosses.
        beat = None
        heading = Text("Two coin tosses: ordered pairs", font_size=26, color=BLUE_TERM).move_to(UP * 0.95)
        heading_bg = BackgroundRectangle(heading, color=BLACK, fill_opacity=1, buff=0.18); heading_bg.move_to(heading.get_center())
        pairs = MathTex(r"(H,H)\quad (H,T)\quad (T,H)\quad (T,T)", color=TEAL_TERM).scale(1.0).move_to(UP * 0.1)
        pairs_bg = BackgroundRectangle(pairs, color=BLACK, fill_opacity=1, buff=0.22); pairs_bg.move_to(pairs.get_center())
        count = MathTex(r"2 \times 2 = 4\text{ outcomes}", color=GREEN_OK).scale(1.0).move_to(DOWN * 0.9)
        count_bg = BackgroundRectangle(count, color=BLACK, fill_opacity=1, buff=0.2); count_bg.move_to(count.get_center())
        beat = beat_group(beat, heading_bg, heading, pairs_bg, pairs, count_bg, count)
        self.play(FadeIn(heading_bg), FadeIn(heading), FadeIn(pairs_bg), Write(pairs, run_time=1.6)); self.wait(2)
        self.play(FadeIn(count_bg), Write(count)); self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 3: table and tree diagram representations.
        beat = None
        table_title = Text("Table / array", font_size=24, color=BLUE_TERM).move_to(LEFT * 2.6 + UP * 1.1)
        table = Table([["HH", "HT"], ["TH", "TT"]], row_labels=[Text("H"), Text("T")], col_labels=[Text("H"), Text("T")], include_outer_lines=True, element_to_mobject=Text, line_config={"stroke_width": 2}).scale(0.48).move_to(LEFT * 2.5 + DOWN * 0.05)
        tree_title = Text("Tree diagram", font_size=24, color=TEAL_TERM).move_to(RIGHT * 2.0 + UP * 1.5)
        root = Dot(RIGHT * 0.8 + DOWN * 0.1, color=WHITE)
        h1 = Dot(RIGHT * 2.0 + UP * 0.65, color=BLUE_TERM); t1 = Dot(RIGHT * 2.0 + DOWN * 0.75, color=BLUE_TERM)
        leaves = [Dot(RIGHT * 3.2 + UP * 1.1, color=GREEN_OK), Dot(RIGHT * 3.2 + UP * 0.2, color=GREEN_OK), Dot(RIGHT * 3.2 + DOWN * 0.3, color=GREEN_OK), Dot(RIGHT * 3.2 + DOWN * 1.15, color=GREEN_OK)]
        branches = VGroup(Line(root.get_center(), h1.get_center()), Line(root.get_center(), t1.get_center()), Line(h1.get_center(), leaves[0].get_center()), Line(h1.get_center(), leaves[1].get_center()), Line(t1.get_center(), leaves[2].get_center()), Line(t1.get_center(), leaves[3].get_center()))
        labels = VGroup(MathTex("H").scale(0.7).move_to(RIGHT * 1.42 + UP * 0.5), MathTex("T").scale(0.7).move_to(RIGHT * 1.42 + DOWN * 0.5), MathTex("H,H").scale(0.65).move_to(RIGHT * 3.65 + UP * 1.1), MathTex("H,T").scale(0.65).move_to(RIGHT * 3.65 + UP * 0.2), MathTex("T,H").scale(0.65).move_to(RIGHT * 3.65 + DOWN * 0.3), MathTex("T,T").scale(0.65).move_to(RIGHT * 3.65 + DOWN * 1.15))
        group = VGroup(table_title, table, tree_title, branches, root, h1, t1, *leaves, labels)
        bg = BackgroundRectangle(group, color=BLACK, fill_opacity=0.92, buff=0.2); bg.move_to(group.get_center())
        beat = beat_group(beat, bg, group)
        self.play(FadeIn(bg), FadeIn(table_title), Create(table), FadeIn(tree_title), Create(branches), FadeIn(root), FadeIn(h1), FadeIn(t1), LaggedStart(*[FadeIn(x) for x in leaves], lag_ratio=0.1), FadeIn(labels)); self.wait(6)
        self.play(FadeOut(beat, run_time=0.8))

        # Beat 4: multiplication principle and fair-tree probability.
        beat = None
        formula = MathTex(r"m\text{ outcomes} \times n\text{ outcomes} = mn\text{ total}", color=GREEN_OK).scale(0.95).move_to(UP * 1.25)
        formula_bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=1, buff=0.22); formula_bg.move_to(formula.get_center())
        examples = VGroup(MathTex(r"6\times6=36\text{ for two dice}"), MathTex(r"P(\text{one leaf})=\prod\text{ branch probabilities}"), MathTex(r"\sum\text{ leaf probabilities}=1")).arrange(DOWN, buff=0.35).scale(0.78).move_to(DOWN * 0.45)
        ex_bg = BackgroundRectangle(examples, color=BLACK, fill_opacity=0.95, buff=0.2); ex_bg.move_to(examples.get_center())
        beat = beat_group(beat, formula_bg, formula, ex_bg, examples)
        self.play(FadeIn(formula_bg), Write(formula)); self.wait(2); self.play(FadeIn(ex_bg), LaggedStart(*[Write(x) for x in examples], lag_ratio=0.2)); self.wait(6)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"\#\text{ outcomes}=m\times n", "List every leaf; products give fair-tree probabilities.", final_wait=20)
