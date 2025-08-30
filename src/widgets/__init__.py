class Widget:
    def render(self):
        raise NotImplementedError("Render method must be implemented by subclasses.")

class TextWidget(Widget):
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def render(self, display):
        display.draw_text(self.x, self.y, self.text)

class ImageWidget(Widget):
    def __init__(self, image_path, x, y):
        self.image_path = image_path
        self.x = x
        self.y = y

    def render(self, display):
        display.draw_image(self.x, self.y, self.image_path)

class ProgressBarWidget(Widget):
    def __init__(self, value, max_value, x, y, width, height):
        self.value = value
        self.max_value = max_value
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, display):
        percentage = self.value / self.max_value
        display.draw_rectangle(self.x, self.y, self.width * percentage, self.height)