from PIL import Image, ImageDraw, ImageFont
import random
import pprint


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes  # store the dictionary

    def draw_circle(self, draw_context):
        x, y = self.attributes["position"]
        r = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.ellipse([(x - r, y - r), (x + r, y + r)], fill=color, outline="black", width = 2)

    def draw_rectangle(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.rectangle((x, y, x+size, y+size), fill=color, outline="black", width = 2)      

    def draw_rounded_rectangle(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.rounded_rectangle((x, y, x+size, y+size), random.randint(10,40),fill=color, outline="black", width = 2)    

    def draw_regular_polygon(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.regular_polygon((x, y, size), random.randint(4,10),fill=color, outline="black", width = 2)              

    def __str__(self):
        return self         

class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            num = random.randint(1,4)
            if num == 1:
                element.draw_circle(draw)
            elif num == 2:
                element.draw_rectangle(draw)
            elif num == 3:
                element.draw_rounded_rectangle(draw)                
            else:
                element.draw_regular_polygon(draw)
        draw.text((200, 200), 'ART', (0,0,0), font_size = 100)

        self.image.show()
        self.image.save("output2.png")

    def __str__(self):
       return pprint.pformat(f"{str(self.width)}, {str(self.height)}, {str(self.bg_color)}")


def main():
    canvas = Canvas(500, 500, (255, 255, 255))

    # circle = {
    #     "shape": "circle",
    #     "position": (100, 100),
    #     "radius": 50,
    #     "color": (255, 0, 0),
    # }
    # element = ArtElement(circle)
    # canvas.add_element(element)
    # canvas.render()

    for _ in range(random.randint(20, 40)):
        attrs = {
            "position": (random.randint(0, 500), random.randint(0, 500)),
            "size": random.randint(20, 80),
            "color": (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        }
        shape = ArtElement(attrs)
        canvas.add_element(shape)
    canvas.render()

main()

# canvas = Image.new("RGB", (500, 500), "#fff")
# rect = ImageDraw.Draw(canvas)
# rect.rectangle((10, 10, 200, 100), (255,0,0))
# canvas.show()x``

# im = Image.new("RGB", (500, 500), "#fff")
# d = ImageDraw.Draw(im)
# d.rectangle((10, 10, 200, 100), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
# im.save("output.png")
# im.show()
