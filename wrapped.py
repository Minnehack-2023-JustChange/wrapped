from PIL import Image, ImageDraw, ImageFont

def wrapped_text(dollar_total, type_donation, charity, month):
    img = Image.open('dominant_blue.jpg')
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('Arial.ttf', 45)
    fnt_2 = ImageFont.truetype('Arial.ttf', 35)
    fnt_3 = ImageFont.truetype('Arial.ttf', 30)
    fnt_4 = ImageFont.truetype('Arial.ttf', 25)

    draw.text((20, 10), "2023 JustChange Wrapped", font = fnt_2, fill = (255, 255, 255))

    draw.text((20, 375), "Dollars Donated", font = fnt_3, fill = (255, 255, 255))
    draw.text((20, 425), "$" + str(dollar_total), font = fnt, fill = (255, 255, 255))

    draw.text((20, 500), "Donation Type", font = fnt_3, fill = (255, 255, 255))
    draw.text((20, 550), str(type_donation), font = fnt_3, fill = (255, 255, 255))

    draw.text((275, 75), "Top Charities", font = fnt_3, fill = (255, 255, 255))
    for i in range(5):
        draw.text((275, 125 + i * 40), str(charity[i]), font = fnt_4, fill = (255, 255, 255))

    draw.text((275, 375), "Top Months", font = fnt_3, fill = (255, 255, 255))
    for k in range(5):
        draw.text((275, 425 + k * 40), str(month[k]), font = fnt_4, fill = (255, 255, 255))

    img.save('wrapped_finished.png')
