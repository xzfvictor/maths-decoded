"""Transcript-faithful Manim scene for network-basics (m10-space-networks)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how networks are described using vertices and edges, and what it means for a network to be connected. Think of a network, sometimes called a graph, as just a collection of dots joined by lines. The dots are called vertices, or nodes, and they represent things like cities, computers, or people. The lines joining them are called edges, or links, and they represent the connections, like roads, cables, or friendships. You'll see networks everywhere once you start looking, from a road map to a social media app to the internet itself. Now, connectedness is a really simple idea. A network is connected if you can get from any vertex to any other vertex just by following edges along. If you can't, then the network breaks apart into separate pieces called components. Finally, every vertex has a degree, which is simply how many edges meet at it. If a vertex has a degree of zero, it stands completely alone, and we call it isolated. Now let's see it in action."

class M10SpaceNetworksNetworkBasicsScene(Scene):
    def construct(self) -> None:
        title = Text('Space Networks Network Basics', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how networks are described using vertices\nand edges, and what it means for a network to be connected. You'll see\nnetworks everywhere once you start looking, from a road map to a social\nmedia app to the internet itself. Finally, every vertex has a degree,\nwhich is simply how many edges meet at it.", 'Think of a network, sometimes called a graph, as just a collection of\ndots joined by lines. Now, connectedness is a really simple idea. If a\nvertex has a degree of zero, it stands completely alone, and we call it\nisolated.', "The dots are called vertices, or nodes, and they represent things like\ncities, computers, or people. A network is connected if you can get from\nany vertex to any other vertex just by following edges along. Now let's\nsee it in action.", "The lines joining them are called edges, or links, and they represent\nthe connections, like roads, cables, or friendships. If you can't, then\nthe network breaks apart into separate pieces called components."]
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
