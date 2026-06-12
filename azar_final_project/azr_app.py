import flet as ft
import webbrowser
from dataclasses import dataclass

APP_TITLE = "Room 01: Azar — ZenX Academy"

ROOM_META = {
    "system_url": "https://zenx.academy/enter-the-system-the-internal-operating-system-zenx/",
}

MAX_WIDTH = 620
SCREEN_PAD = 28

COLORS = {
    "abyss": "#061019",
    "overlay_top": "#00000024",
    "overlay_mid": "#00000018",
    "overlay_bottom": "#08131d10",
    "panel_dark": "#00000018",
    "panel_border_light": "#FFFFFF2E",
    "text_light": "#EEF2F6",
    "text_light_soft": "#D6DEE7",
    "button_bg": "#101820",
    "button_text": "#EEF2F6",
}


@dataclass
class RoomState:
    page: int = 1
    reaction: str = ""
    hidden_rule: str = ""
    witness_note: str = ""


def space(h: int) -> ft.Container:
    return ft.Container(height=h)


def page_theme(page_number: int) -> dict:
    return {
        "text_main": COLORS["text_light"],
        "text_sub": COLORS["text_light_soft"],
        "panel_bg": COLORS["panel_dark"],
        "border": COLORS["panel_border_light"],
        "hint": "#CCD5DF",
        "input_bg": "#00000022",
        "input_border": COLORS["panel_border_light"],
        "input_focus": "#FFFFFF88",
    }


def room_text(
    value: str,
    size: float = 16,
    color: str = "#111111",
    weight: ft.FontWeight = ft.FontWeight.NORMAL,
    italic: bool = False,
    letter_spacing: float = 0,
    height: float = 1.45,
    font_family: str | None = None,
) -> ft.Text:
    return ft.Text(
        value=value,
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            size=size,
            color=color,
            weight=weight,
            italic=italic,
            letter_spacing=letter_spacing,
            height=height,
            font_family=font_family,
        ),
    )


def whisper(text: str, color: str, size: float = 12) -> ft.Text:
    return room_text(
        text.upper(),
        size=size,
        color=color,
        letter_spacing=2.0,
        weight=ft.FontWeight.W_500,
        font_family="Arial",
        height=1.2,
    )


def border_box(color: str) -> ft.Border:
    return ft.Border(
        top=ft.BorderSide(1, color),
        right=ft.BorderSide(1, color),
        bottom=ft.BorderSide(1, color),
        left=ft.BorderSide(1, color),
    )


def line(color: str, width_pct: float = 0.45) -> ft.Container:
    margin_h = int(MAX_WIDTH * (1 - width_pct) / 2)
    return ft.Container(
        height=1,
        bgcolor=color,
        margin=ft.Margin(margin_h, 0, margin_h, 0),
    )


def reading_panel(content, panel_bg: str, border_color: str, padding: int = 28) -> ft.Container:
    if not isinstance(content, ft.Column):
        content = ft.Column([content], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    return ft.Container(
        width=min(MAX_WIDTH + 120, 760),
        content=content,
        padding=padding,
        bgcolor=panel_bg,
        border_radius=8,
        border=border_box(border_color),
    )


def input_field(hint: str, theme: dict) -> ft.TextField:
    return ft.TextField(
        hint_text=hint,
        max_lines=4,
        min_lines=3,
        multiline=True,
        width=MAX_WIDTH,
        bgcolor=theme["input_bg"],
        border_color=theme["input_border"],
        focused_border_color=theme["input_focus"],
        color=theme["text_main"],
        hint_style=ft.TextStyle(color=theme["hint"], size=15),
        text_style=ft.TextStyle(size=17, color=theme["text_main"]),
        cursor_color=theme["text_main"],
        content_padding=ft.Padding(20, 18, 20, 18),
    )


def primary_button(label: str, on_click) -> ft.Container:
    return ft.Container(
        width=MAX_WIDTH,
        content=ft.FilledButton(
            content=room_text(
                label,
                size=16,
                color=COLORS["button_text"],
                weight=ft.FontWeight.W_600,
                font_family="Arial",
                letter_spacing=0.3,
                height=1.1,
            ),
            on_click=on_click,
            width=MAX_WIDTH,
            height=54,
            style=ft.ButtonStyle(
                bgcolor=COLORS["button_bg"],
                shape=ft.RoundedRectangleBorder(radius=4),
                padding=ft.Padding(24, 16, 24, 16),
            ),
        ),
    )


def build_background() -> ft.Container:
    return ft.Container(
        expand=True,
        image=ft.DecorationImage(
            src="bg.jpg",
            fit=ft.BoxFit.COVER,
        ),
        foreground_decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=[
                    COLORS["overlay_top"],
                    COLORS["overlay_mid"],
                    COLORS["overlay_bottom"],
                ],
                stops=[0.0, 0.55, 1.0],
            ),
        ),
    )


def build_shell(content: ft.Control) -> ft.Stack:
    return ft.Stack(
        expand=True,
        controls=[
            build_background(),
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    alignment=ft.Alignment(0, -1),
                    padding=ft.Padding(SCREEN_PAD, 56, SCREEN_PAD, SCREEN_PAD),
                    content=ft.Column(
                        [content],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                ),
            ),
        ],
    )


def build_page_hero(state: RoomState, on_begin) -> ft.Stack:
    t = page_theme(1)
    content = ft.Column(
        [
            space(110),
            whisper("Room 01", t["text_sub"], size=12),
            space(18),
            room_text(
                "AZAR",
                size=52,
                color=t["text_main"],
                weight=ft.FontWeight.W_500,
                letter_spacing=4,
                height=1.12,
                font_family="Georgia",
            ),
            space(14),
            room_text(
                "The Programming",
                size=22,
                color=t["text_sub"],
                italic=True,
                height=1.4,
                font_family="Georgia",
            ),
            space(32),
            room_text(
                "A room exists where something in you reacts before examination begins.",
                size=18,
                color=t["text_sub"],
                height=1.6,
                font_family="Arial",
            ),
            space(64),
            primary_button("BEGIN", on_begin),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_detection(state: RoomState, reaction_input, on_continue) -> ft.Stack:
    t = page_theme(2)
    content = ft.Column(
        [
            space(88),
            whisper("Detection", t["text_sub"], size=11),
            space(22),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            "Think of one response that happens before you think.",
                            size=24,
                            color=t["text_main"],
                            height=1.45,
                            font_family="Georgia",
                        ),
                        space(12),
                        room_text(
                            "A rejection. A tightening. A certainty. A defense.",
                            size=18,
                            color=t["text_sub"],
                            height=1.6,
                            font_family="Arial",
                        ),
                        space(22),
                        line(t["border"], 0.72),
                        space(20),
                        room_text(
                            "Name it briefly.",
                            size=18,
                            color=t["text_main"],
                            height=1.5,
                            font_family="Georgia",
                        ),
                        space(10),
                        room_text(
                            "Not the explanation. The automatic response itself.",
                            size=16,
                            color=t["text_sub"],
                            italic=True,
                            height=1.55,
                            font_family="Arial",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=30,
            ),
            space(28),
            reaction_input,
            space(34),
            primary_button("Continue", on_continue),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_hidden_rule(state: RoomState, hidden_input, on_continue) -> ft.Stack:
    t = page_theme(3)
    content = ft.Column(
        [
            space(88),
            whisper("Hidden Rule", t["text_sub"], size=11),
            space(22),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            "Under many reactions, a sentence is already running.",
                            size=23,
                            color=t["text_main"],
                            height=1.55,
                            font_family="Georgia",
                        ),
                        space(18),
                        room_text(
                            "What inner rule seems to operate beneath your reaction?",
                            size=17,
                            color=t["text_sub"],
                            height=1.5,
                            font_family="Arial",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=32,
            ),
            space(28),
            hidden_input,
            space(34),
            primary_button("Continue", on_continue),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_reveal(state: RoomState, on_continue) -> ft.Stack:
    t = page_theme(4)
    content = ft.Column(
        [
            space(88),
            whisper("Recognition", t["text_sub"], size=11),
            space(24),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            f"\"{state.reaction or '...'}\"",
                            size=24,
                            color=t["text_sub"],
                            italic=True,
                            height=1.45,
                            font_family="Georgia",
                        ),
                        space(18),
                        room_text(
                            "It feels immediate.",
                            size=26,
                            color=t["text_main"],
                            weight=ft.FontWeight.W_500,
                            height=1.35,
                            font_family="Georgia",
                        ),
                        space(10),
                        room_text(
                            "But immediacy is not proof.",
                            size=22,
                            color=t["text_sub"],
                            height=1.45,
                            font_family="Georgia",
                        ),
                        space(16),
                        room_text(
                            "A pattern can feel natural simply because it has repeated itself long enough.",
                            size=18,
                            color=t["text_sub"],
                            height=1.65,
                            font_family="Arial",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=34,
            ),
            space(44),
            primary_button("Continue", on_continue),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_structure(state: RoomState, on_continue) -> ft.Stack:
    t = page_theme(5)
    content = ft.Column(
        [
            space(88),
            whisper("Structure", t["text_sub"], size=11),
            space(22),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            "The pattern has structure.",
                            size=24,
                            color=t["text_main"],
                            height=1.5,
                            font_family="Georgia",
                        ),
                        space(18),
                        room_text(
                            "Trigger\n↓\nReaction\n↓\nJustification",
                            size=22,
                            color=t["text_sub"],
                            height=1.6,
                            font_family="Georgia",
                        ),
                        space(18),
                        room_text(
                            "What is explained last may be what happened first.",
                            size=17,
                            color=t["text_sub"],
                            height=1.55,
                            font_family="Arial",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=32,
            ),
            space(34),
            primary_button("Continue", on_continue),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_witness(state: RoomState, witness_input, on_continue) -> ft.Stack:
    t = page_theme(6)
    content = ft.Column(
        [
            space(88),
            whisper("Witness", t["text_sub"], size=11),
            space(22),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            "Name one pattern you can now observe more clearly.",
                            size=24,
                            color=t["text_main"],
                            height=1.5,
                            font_family="Georgia",
                        ),
                        space(16),
                        room_text(
                            "You do not need to solve it here. Only witness it.",
                            size=17,
                            color=t["text_sub"],
                            height=1.55,
                            font_family="Arial",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=32,
            ),
            space(28),
            witness_input,
            space(34),
            primary_button("Continue", on_continue),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def build_page_final(state: RoomState, on_enter) -> ft.Stack:
    t = page_theme(7)
    content = ft.Column(
        [
            space(92),
            whisper("The Threshold", t["text_sub"], size=11),
            space(24),
            reading_panel(
                ft.Column(
                    [
                        room_text(
                            "You identified the reaction.",
                            size=26,
                            color=t["text_main"],
                            weight=ft.FontWeight.W_500,
                            height=1.45,
                            font_family="Georgia",
                        ),
                        space(10),
                        room_text(
                            "You named the hidden rule beneath it.",
                            size=20,
                            color=t["text_sub"],
                            height=1.45,
                            font_family="Georgia",
                        ),
                        space(10),
                        room_text(
                            "You saw that something may be running before thought.",
                            size=18,
                            color=t["text_sub"],
                            height=1.55,
                            font_family="Arial",
                        ),
                        space(18),
                        line(t["border"], 0.42),
                        space(18),
                        room_text(
                            "Is this you — or is it running?",
                            size=20,
                            color=t["text_sub"],
                            italic=True,
                            height=1.5,
                            font_family="Georgia",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                t["panel_bg"],
                t["border"],
                padding=34,
            ),
            space(52),
            primary_button("ENTER THE SYSTEM", on_enter),
            space(18),
            whisper("The system waits beyond the threshold.", t["text_sub"], size=10),
            space(36),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return build_shell(content)


def main(page: ft.Page):
    state = RoomState()

    page.title = APP_TITLE
    page.bgcolor = COLORS["abyss"]
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 1280
    page.window_height = 720
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK

    reaction_input = input_field(
        "Write briefly — name the automatic reaction...",
        page_theme(2),
    )
    hidden_input = input_field(
        "Write one sentence, or even a few words...",
        page_theme(3),
    )
    witness_input = input_field(
        "Name the pattern briefly...",
        page_theme(6),
    )

    def next_page(e=None):
        state.page += 1
        update()

    def enter_system(e=None):
        webbrowser.open(ROOM_META["system_url"])

    def save_reaction(e=None):
        state.reaction = (reaction_input.value or "").strip()
        next_page()

    def save_hidden_rule(e=None):
        state.hidden_rule = (hidden_input.value or "").strip()
        next_page()

    def save_witness(e=None):
        state.witness_note = (witness_input.value or "").strip()
        next_page()

    def build_current_page():
        if state.page == 1:
            return build_page_hero(state, next_page)
        if state.page == 2:
            return build_page_detection(state, reaction_input, save_reaction)
        if state.page == 3:
            return build_page_hidden_rule(state, hidden_input, save_hidden_rule)
        if state.page == 4:
            return build_page_reveal(state, next_page)
        if state.page == 5:
            return build_page_structure(state, next_page)
        if state.page == 6:
            return build_page_witness(state, witness_input, save_witness)
        return build_page_final(state, enter_system)

    def update():
        page.clean()
        page.add(build_current_page())
        page.update()

    update()


import flet as ft
import os

app = ft.run(
    main,
    assets_dir="assets",
    export_asgi_app=True,
)

if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
    )
