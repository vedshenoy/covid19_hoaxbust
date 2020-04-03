#!/usr/bin/env python
#
# Code to insert text in poster jpg files.
#
# Copyright: Surhud More (IUCAA) 2020
#
# Bug reports/comments: Open github issues, or send pull requests

import textwrap
from PIL import Image, ImageDraw, ImageFont

class fill_poster:
    def __init__(self, image):
        self.imagename = image
        self.image = Image.open(image+".jpg")
        self.fullwidth = self.image.width

    def output_text(self, message, y, font=None, width=None, color='rgb(0, 0, 0)', margin=40, offsety=30):

        for line in textwrap.wrap(message, width):
            w, h = self.draw.textsize(line, font=font)
            self.draw.text(((self.image.width-w)/2, y + offsety), line, font=font, fill=color)
            offsety += font.getsize(line)[1]

    def convert(self, strings):
        self.draw = ImageDraw.Draw(self.image)
        font1 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Regular.ttf', size=30)
        font2 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=40)
        font3 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=30)
        font3 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=30)
        font4 = ImageFont.truetype('Noto/English/Montserrat-Bold.ttf', size=40)

        self.output_text("The Hoaxbusters", 40, font=font4,  width=30)

        self.output_text(strings["1"], 110, font=font1, width=30, color='rgb(94, 94, 94)')
        self.output_text(strings["2"], 150, font=font2, width=30)
        self.output_text(strings["3"], 250, font=font1, width=40, color='rgb(94, 94, 94)')
        self.output_text(strings["4"], 300, font=font2, width=45, color='rgb(189, 23, 23)')
        self.output_text(strings["5"], 850, font=font1, width=45, color='rgb(94, 94, 94)')
        self.output_text(strings["6"], 900, font=font3, width=45)
        self.image.save(self.imagename+"_modified.jpg")

if __name__ == "__main__":

    # These strings will have to be read from the appropriate files extracted
    # by `extract.sh`

    strings = {}
    strings["1"] = "दावा:"
    strings["2"] = "ह्या करोनाविषाणूची निर्मीती एखाद्या प्रयोगशाळेत झाली आहे."
    strings["3"] = "निर्णय:"
    strings["4"] = "खरं नाही."
    strings["5"] = "का?:"
    strings["6"] = "सर्व विषाणूंचे स्वरूप नैसर्गिकरित्या बदलत असते. संशोधकांनी हे दाखवून दिले आहे की, हा विषाणू देखील नैसर्गिकरित्याच एका दुसऱ्या करोनाविषाणूपासून उत्क्रांत झाला आहे. म्हणजेच तो मानवनिर्मित नाही."

    '''
    # Number 7
    strings["1"] = "दावा:"
    strings["2"] = "योगासने केल्याने माझे कोविड-१९ पासून संरक्षण होऊ शकते."
    strings["3"] = "निर्णय:"
    strings["4"] = "बहुतेक शक्य नाही (पुरेसा पुरावा नाही)"
    strings["5"] = "का?:"
    strings["6"] = "इतर व्यायाम पद्धतींप्रमाणेच योगासने केल्याने शरीर निरोगी व तणावमुक्त राहू शकते. निरोगी व्यक्ती कोणत्याही आजारापासून लवकर बऱ्या होऊ शकतात. पण “योगासने केल्याने कोविड-१९ पासून संरक्षण होते” यासाठी कोणताही पुरावा नाही."
    '''

    # Initiate a class
    a = fill_poster("Sample_images/00001")

    # Fill in the poster with strings, and save file
    a.convert(strings)
