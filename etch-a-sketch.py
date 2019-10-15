from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
import click
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


text = "Etch-a-sketch"


def displayText(text, x=20, y=18):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


displayText(text)

lcd.show()

x2 = 0
y2 = 0
char = getchar()
# right
while True:
    if x2 <= 127:
        char = getchar()
    if char == '\x1b[C':
        lcd.set_pixel(x2, y2, 1)
        lcd.show()
        x2 += 1
        lcd.set_pixel(x2, y2, 1)
    if x2 == 127:
        x2 = 0
        lcd.set_pixel(x2, y2, 1)
        lcd.show()
        x2 += 1
    if char == '\x1b[D':
        lcd.set_pixel(x2, y2, 1)
        lcd.show()
        x2 -= 1
        lcd.set_pixel(x2, y2, 1)
    if x2 == 0:
        x2 = 127
        lcd.set_pixel(x2, y2, 1)
        lcd.show()
        x2 += 1



     right()

     if abc == 128:

right()

 char = getchar()

 while True:
#     Down
     if y2 <= 63:
         char = getchar()
         if char == '\x1b[A':
             lcd.set_pixel(x2, y2, 1)
             lcd.show()
             y2 = y2 - 1
     # up
     if y2 <= 63:
         char = getchar()
         if char == '\x1b[B':
             lcd.set_pixel(x2, y2, 1)
             lcd.show()
             y2 = y2 + 1

     # Right
     if x2 <= 127:
         char = getchar()
         if char == '\x1b[C':
             lcd.set_pixel(x2, y2, 1)
             lcd.show()
             x2 = x2 + 1
     # Left
     if x2 <= 127:
         char = getchar()
         if char == '\x1b[D':
             lcd.set_pixel(x2, y2, 1)
             lcd.show()
             x2 = x2 - 1

     lcd.show()
