"""Transcript-faithful Manim scene for axes-samples (m10-statistics-claims)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how the media can mislead you with statistics, and the two main spots to check. First up, the axes. Watch out for a truncated y-axis, where a bar chart starts at fifty instead of zero. That little trick makes a tiny change look like a huge jump. A broken axis or a non-zero baseline does the same thing. Asymmetric or logarithmic scales can be legitimate, but they need to be clearly labeled so you know what's going on. Then there's the sample. Ask yourself whether the sample was chosen fairly. For example, a poll of newspaper readers will lean toward a particular political view, so it's not representative. Also think about size, because a poll of thirty people is way less reliable than a poll of three thousand. And finally, watch out for population mismatches, like drawing conclusions about dogs from a study done on cats. Now let's see it in action."

class M10StatisticsClaimsAxesSamplesScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Claims Axes Samples', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how the media can mislead you with\nstatistics, and the two main spots to check. A broken axis or a non-zero\nbaseline does the same thing. For example, a poll of newspaper readers\nwill lean toward a particular political view, so it's not\nrepresentative.", "First up, the axes. Asymmetric or logarithmic scales can be legitimate,\nbut they need to be clearly labeled so you know what's going on. Also\nthink about size, because a poll of thirty people is way less reliable\nthan a poll of three thousand.", "Watch out for a truncated y-axis, where a bar chart starts at fifty\ninstead of zero. Then there's the sample. And finally, watch out for\npopulation mismatches, like drawing conclusions about dogs from a study\ndone on cats.", "That little trick makes a tiny change look like a huge jump. Ask\nyourself whether the sample was chosen fairly. Now let's see it in\naction."]
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
