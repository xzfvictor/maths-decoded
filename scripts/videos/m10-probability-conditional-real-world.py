"""Transcript-faithful Manim scene for real-world (m10-probability-conditional)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how probability simulation is used in the real world to make smart decisions when the future is uncertain. The core idea is simple: instead of trying to predict exactly what will happen, we build a model, run it thousands of times, and watch what patterns emerge. Let's walk through some classic examples. In insurance, companies don't know how big the next claim will be, so they simulate thousands of possible claim amounts to figure out a fair premium that covers most cases. In call centre queueing, they simulate random customer arrivals and service times to predict how long people will wait, and decide how many staff they need. For supply and demand, retailers simulate daily sales to forecast how much stock to order so they don't run out or overbuy. In public health, researchers simulate contact networks between people to estimate how a virus might spread. And in election forecasting, pollsters run thousands of simulated elections from their polling data to estimate each party's chance of winning. The pattern is the same every time: model the randomness, run the simulation many times, and use the results to plan. Now let's see it in action."

class M10ProbabilityConditionalRealWorldScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Conditional Real World', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how probability simulation is used in the\nreal world to make smart decisions when the future is uncertain. In call\ncentre queueing, they simulate random customer arrivals and service\ntimes to predict how long people will wait, and decide how many staff\nthey need. The pattern is the same every time: model the randomness, run\nthe simulation many times, and use the results to plan.", "The core idea is simple: instead of trying to predict exactly what will\nhappen, we build a model, run it thousands of times, and watch what\npatterns emerge. For supply and demand, retailers simulate daily sales\nto forecast how much stock to order so they don't run out or overbuy.\nNow let's see it in action.", "Let's walk through some classic examples. In public health, researchers\nsimulate contact networks between people to estimate how a virus might\nspread.", "In insurance, companies don't know how big the next claim will be, so\nthey simulate thousands of possible claim amounts to figure out a fair\npremium that covers most cases. And in election forecasting, pollsters\nrun thousands of simulated elections from their polling data to estimate\neach party's chance of winning."]
        for words in sections:
            beat = Text(words, font_size=24, line_spacing=0.8)
            if beat.width > 10.5:
                beat.set_width(10.5)
            beat.move_to(BAND_CHART_CENTER)
            bg = BackgroundRectangle(beat, color=BLACK, fill_opacity=1, buff=0.28)
            bg.move_to(beat.get_center())
            card = beat_group(bg, beat)
            self.add(card)
            self.wait(2.0)
            self.remove(card)
        final = Text("Key idea", font_size=32, color=GREEN_OK).move_to(DOWN * 1.7)
        final_bg = BackgroundRectangle(final, color=BLACK, fill_opacity=1, buff=0.25)
        final_bg.move_to(final.get_center())
        final_box = SurroundingRectangle(final, color=GREEN_OK, buff=0.3)
        self.add(final_bg, final, final_box)
        self.wait(95)
