from pyray import *
from raylib import *
from src.settings import * 

class Button:
    def __init__(
        self, x, y, w, h, text, 
        text_x = None, 
        text_y = None, 
        text_color = BLACK, 
        font_size = 20, 
        color = LIGHTGRAY, 
        hover_color = GRAY
    ):
        self.rect = Rectangle(x, y, w, h)
        self.text = text
        self.text_x = self.rect.x + 20 if text_x is None else self.rect.x + text_x
        self.text_y = self.rect.y + 15 if text_y is None else self.rect.y + text_y
        self.text_color = text_color
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color


    def draw(self):
        mouse = get_mouse_position()
        hover = check_collision_point_rec(mouse, self.rect)

        draw_rectangle_rec(self.rect, self.hover_color if hover else self.color)
        draw_text(
            self.text,
            int(self.text_x),
            int(self.text_y),
            self.font_size,
            self.text_color
        )

        return hover and is_mouse_button_pressed(MOUSE_BUTTON_LEFT)