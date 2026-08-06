"""Transcript-faithful Manim scene for euler-polyhedra (m10-space-networks)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at Euler's formula and a famous puzzle called the Königsberg bridges. First up, Euler's formula for polyhedra. A polyhedron is any solid with flat faces, like a cube or a pyramid. It has three things to count: faces, which are the flat surfaces, vertices, which are the corner points, and edges, which are the lines where two faces meet. Euler discovered a beautiful relationship: the number of faces plus the number of vertices equals the number of edges plus two. This works for every convex solid you can think of, from a simple tetrahedron to a dodecahedron. Next, the Königsberg bridges. Königsberg was a city with seven bridges, and the locals wondered if you could walk through town crossing every bridge exactly once without retracing your steps. Euler figured it out. You look at how many bridges meet at each land mass, which is called the degree of that point. His rule says a graph has an Eulerian trail, meaning you can walk every edge once, only if it has exactly zero or two odd-degree vertices. The Königsberg network had four, so it was impossible. Now let's see it in action."

class M10SpaceNetworksEulerPolyhedraScene(Scene):
    def construct(self) -> None:
        title = Text('Space Networks Euler Polyhedra', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at Euler's formula and a famous puzzle called\nthe Königsberg bridges. Euler discovered a beautiful relationship: the\nnumber of faces plus the number of vertices equals the number of edges\nplus two. Euler figured it out. Now let's see it in action.", "First up, Euler's formula for polyhedra. This works for every convex\nsolid you can think of, from a simple tetrahedron to a dodecahedron. You\nlook at how many bridges meet at each land mass, which is called the\ndegree of that point.", 'A polyhedron is any solid with flat faces, like a cube or a pyramid.\nNext, the Königsberg bridges. His rule says a graph has an Eulerian\ntrail, meaning you can walk every edge once, only if it has exactly zero\nor two odd-degree vertices.', 'It has three things to count: faces, which are the flat surfaces,\nvertices, which are the corner points, and edges, which are the lines\nwhere two faces meet. Königsberg was a city with seven bridges, and the\nlocals wondered if you could walk through town crossing every bridge\nexactly once without retracing your steps. The Königsberg network had\nfour, so it was impossible.']
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
