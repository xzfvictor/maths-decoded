"""Transcript-faithful Manim scene for proof-vs-demo (m10-space-proofs)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at the difference between demonstrating something and actually proving it. The big idea here is that showing one example isn't enough to call something true in geometry. Let's break it down. A geometric proof is basically a chain of statements that start with what you're given and end with what you want to show. Every step along the way has to be backed up by something solid, like a theorem, a definition, or a result you've already proven. Now here's where demonstration and proof part ways. A demonstration is when you do something like cut out shapes and slide them around on top of each other to show a result works in one specific case. That can be a great way to convince yourself the idea is probably true, and it might even help you spot the pattern. But it only covers the one situation you actually tested. A proof, on the other hand, has to cover every single case that fits the conditions you started with. It's not about showing it could happen, it's about showing it must happen, no exceptions. So remember, demonstrations suggest, but proofs confirm. Now let's see it in action."

class M10SpaceProofsProofVsDemoScene(Scene):
    def construct(self) -> None:
        title = Text('Space Proofs Proof Vs Demo', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at the difference between demonstrating\nsomething and actually proving it. Every step along the way has to be\nbacked up by something solid, like a theorem, a definition, or a result\nyou've already proven. But it only covers the one situation you actually\ntested. Now let's see it in action.", "The big idea here is that showing one example isn't enough to call\nsomething true in geometry. Now here's where demonstration and proof\npart ways. A proof, on the other hand, has to cover every single case\nthat fits the conditions you started with.", "Let's break it down. A demonstration is when you do something like cut\nout shapes and slide them around on top of each other to show a result\nworks in one specific case. It's not about showing it could happen, it's\nabout showing it must happen, no exceptions.", "A geometric proof is basically a chain of statements that start with\nwhat you're given and end with what you want to show. That can be a\ngreat way to convince yourself the idea is probably true, and it might\neven help you spot the pattern. So remember, demonstrations suggest, but\nproofs confirm."]
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
