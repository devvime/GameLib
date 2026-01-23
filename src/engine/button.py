from src.settings import * 

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = Rectangle(x, y, w, h)
        self.text = text

    def draw(self):
        mouse = get_mouse_position()
        hover = check_collision_point_rec(mouse, self.rect)

        draw_rectangle_rec(self.rect, GRAY if hover else LIGHTGRAY)
        draw_text(
            self.text,
            int(self.rect.x + 20),
            int(self.rect.y + 15),
            20,
            BLACK
        )

        return hover and is_mouse_button_pressed(MOUSE_BUTTON_LEFT)