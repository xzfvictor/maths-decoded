"""
Shared style helpers for maths-decoded Manim scenes.

Every scene file should import this to get:
  - The safe-area frame constants (BAND_TITLE, BAND_BOTTOM, etc.)
  - The colour palette (BLUE_TERM, RED_REJECT, GREEN_OK, ...)
  - Generic card / definition helpers
  - Standard intro / outro animations

The safe-area rules are documented in the math-videos skill
(see ~/.claude/skills/math-videos/SKILL.md, "LAYOUT-SAFETY PATTERN 8"):
all content's outer edge must stay inside y ∈ [-3.5, +3.5].
"""

from manim import *


# ─── Safe-area frame constants ──────────────────────────────────────────────
# Frame y ∈ [-4, 4]. Keep all content's outer edge inside [-3.5, +3.5].
BAND_TITLE         = UP * 3.0
BAND_SUBTITLE      = UP * 2.4
BAND_CHART_CENTER  = ORIGIN
BAND_BOTTOM        = DOWN * 2.8


# ─── Colour palette ─────────────────────────────────────────────────────────
BLUE_TERM         = BLUE_C
TEAL_TERM         = TEAL_C
ORANGE_TERM       = ORANGE
RED_REJECT        = RED_C
GREEN_OK          = GREEN_C
PURPLE_ACCENT     = PURPLE_C
YELLOW_HIGHLIGHT  = YELLOW


# ─── Generic helpers ────────────────────────────────────────────────────────


def make_title_pair(title_tex: str, sub_tex: str) -> VGroup:
    """Build a (title, subtitle) pair, both with opaque backgrounds so
    they read against any chart content. The subtitle is auto-positioned
    below the title via next_to(...)."""
    title = Text(title_tex, font_size=38).move_to(BAND_TITLE)
    title_bg = BackgroundRectangle(title, color=BLACK, fill_opacity=1, buff=0.2)
    title_bg.move_to(title.get_center())
    sub = Text(sub_tex, font_size=22).next_to(title, DOWN, buff=0.35)
    sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.15)
    sub_bg.move_to(sub.get_center())
    return VGroup(title_bg, title, sub_bg, sub)


def make_term_card(term_tex: str, label_tex: str, color) -> VGroup:
    """A coloured term card with the term on top and a label below."""
    term = MathTex(term_tex, color=color).scale(1.1)
    label = MathTex(label_tex, color=color).scale(0.7)
    box = SurroundingRectangle(term, color=color, buff=0.18, stroke_width=2)
    bg = BackgroundRectangle(VGroup(term, box), color=BLACK, fill_opacity=0.85, buff=0.18)
    card = VGroup(bg, box, term)
    label.next_to(card, DOWN, buff=0.25)
    return VGroup(card, label)


def beat_group(*mobjects) -> VGroup:
    """Bundle a set of mobjects into a VGroup so the whole beat can be
    cleaned up with a single `FadeOut(beat_group(...))` at the end of
    the beat. **Never** list individual `FadeOut`s for each mobject —
    it's easy to forget the BackgroundRectangle or a `next_to`-anchored
    label, and the leftover mobject will overlap the next beat.

    Do NOT include the title/subtitle group (returned by `animate_intro`)
    or the final definition group (returned by `animate_final_definition`)
    — those are persistent across the whole animation.

    `None` values are silently dropped so callers can start a beat with
    `beat_N = None` and incrementally add to it:
        beat_N = beat_group(beat_N, new_mobject)
    """
    filtered = [m for m in mobjects if m is not None]
    if not filtered:
        return VGroup()
    if len(filtered) == 1:
        return filtered[0]
    return VGroup(*filtered)


def make_equation_card(
    eq_tex: str,
    color=WHITE,
    scale: float = 1.0,
    anchor: np.ndarray | None = None,
) -> VGroup:
    """A bordered equation card with an opaque background. If anchor is
    given, the card's center is placed at anchor; otherwise it stays at
    the chart center."""
    eq = MathTex(eq_tex, color=color).scale(scale)
    if anchor is not None:
        eq.move_to(anchor)
    bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.25)
    bg.move_to(eq.get_center())
    box = SurroundingRectangle(eq, color=color, buff=0.3, stroke_width=2)
    return VGroup(bg, eq, box)


def make_final_definition(
    eq_tex: str,
    sub_tex: str,
    eq_color=GREEN_OK,
) -> VGroup:
    """Standard final takeaway: boxed equation + sub-label, anchored so
    the sub has ≥0.5 unit margin from the bottom frame edge. Use with
    animate_final_definition()."""
    eq = MathTex(eq_tex).scale(1.0)
    # Place the equation's center high enough (y = -1.7) that the
    # SurroundingRectangle + sub-label both fit within the safe area.
    eq.move_to(DOWN * 1.7)
    eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.28)
    eq_bg.move_to(eq.get_center())
    box = SurroundingRectangle(eq, color=eq_color, buff=0.3, stroke_width=3)
    sub = Text(sub_tex, font_size=22, color=eq_color)
    sub.next_to(box, DOWN, buff=0.3)
    sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.18)
    sub_bg.move_to(sub.get_center())
    return VGroup(eq_bg, eq, box, sub_bg, sub)


# ─── Standard animations ────────────────────────────────────────────────────


def animate_intro(scene, title_tex: str, sub_tex: str, hold: float = 1.5) -> VGroup:
    """Animate the standard title + subtitle reveal. Returns the group
    so the caller can fade it out later."""
    group = make_title_pair(title_tex, sub_tex)
    scene.play(
        FadeIn(group[0], run_time=0.4),
        Write(group[1], run_time=1.4),
    )
    scene.play(
        FadeIn(group[2], run_time=0.4),
        FadeIn(group[3], shift=UP * 0.2, run_time=0.9),
    )
    scene.wait(hold)
    return group


def animate_final_definition(
    scene,
    eq_tex: str,
    sub_tex: str,
    final_wait: float,
) -> VGroup:
    """Animate the standard final takeaway: write eq, draw box, indicate,
    fade sub, then wait final_wait seconds so the video length matches
    the audio narration length."""
    group = make_final_definition(eq_tex, sub_tex)
    # group indices: 0=eq_bg, 1=eq, 2=box, 3=sub_bg, 4=sub
    scene.play(FadeIn(group[0], run_time=0.5), Write(group[1], run_time=2.0))
    scene.play(Create(group[2], run_time=1.0))
    scene.play(Indicate(group[1], color=GREEN_OK, scale_factor=1.05), run_time=1.5)
    scene.play(FadeIn(group[3], run_time=0.4), FadeIn(group[4], run_time=1.0))
    scene.wait(final_wait)
    return group