from PIL import Image, ImageDraw, ImageFont

img = Image.open('green.background.png')
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
d.text((10, 10), "Hello World", fill=(255, 255, 255))
img.save('pil_text_font.png')