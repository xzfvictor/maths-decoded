"""Transcript-faithful Manim scene for causation-ethics (m10-statistics-claims)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = 'In this lesson we\'ll look at how to read statistical claims more carefully, especially when they could actually affect people\'s lives. First up, correlation versus causation. Just because two things move together doesn\'t mean one is causing the other, because there might be a hidden third factor, called a lurking variable, that\'s really driving both of them. For example, ice cream sales and drowning deaths both rise in summer, but that doesn\'t mean ice cream causes drowning, the heat is the lurking variable behind both. Next, cherry-picking, which is when someone only shows you the data that supports their point. A good habit is to ask, what data is missing here? Then watch out for loaded questions in surveys, where the wording nudges you toward a particular answer, like, "Don\'t you agree that we should…" which usually pushes people toward yes. Finally, ethics. When a statistic influences real decisions, like medical advice or government policy, the bar is higher, both the numbers and how they\'re interpreted should be open to scrutiny. Now let\'s see it in action.'

class M10StatisticsClaimsCausationEthicsScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Claims Causation Ethics', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to read statistical claims more\ncarefully, especially when they could actually affect people's lives.\nNext, cherry-picking, which is when someone only shows you the data that\nsupports their point. When a statistic influences real decisions, like\nmedical advice or government policy, the bar is higher, both the numbers\nand how they're interpreted should be open to scrutiny.", "First up, correlation versus causation. A good habit is to ask, what\ndata is missing here? Now let's see it in action.", 'Just because two things move together doesn\'t mean one is causing the\nother, because there might be a hidden third factor, called a lurking\nvariable, that\'s really driving both of them. Then watch out for loaded\nquestions in surveys, where the wording nudges you toward a particular\nanswer, like, "Don\'t you agree that we should…" which usually pushes\npeople toward yes.', "For example, ice cream sales and drowning deaths both rise in summer,\nbut that doesn't mean ice cream causes drowning, the heat is the lurking\nvariable behind both. Finally, ethics."]
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
