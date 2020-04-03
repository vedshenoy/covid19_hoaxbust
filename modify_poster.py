#!/usr/bin/env python
#
# Code to insert text in poster jpg files.
#
# Copyright: Surhud More (IUCAA) 2020
#
# Bug reports/comments: Open github issues, or send pull requests

import textwrap
from PIL import Image, ImageDraw, ImageFont
from os import path
import numpy as np
import sys
import pandas

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

    def convert(self, strings, pl, language, fonts):
        self.draw = ImageDraw.Draw(self.image)

        self.output_text("The Hoaxbusters", 40, font=fonts["4"],  width=30)

        widthreduce = 0
        if language == "Malayalam": # or language == "Tamil":
           widthreduce = 5
        if language == "Urdu": # or language == "Tamil":
           widthreduce = -5
        self.output_text(strings["1"], pl["1"], font=fonts["1"], width=30-widthreduce, color='rgb(94, 94, 94)')
        self.output_text(strings["2"], pl["2"], font=fonts["2"], width=30-widthreduce)
        self.output_text(strings["3"], pl["3"], font=fonts["1"], width=40-widthreduce, color='rgb(94, 94, 94)')
        self.output_text(strings["4"], pl["4"], font=fonts["2"], width=45-widthreduce, color='rgb(189, 23, 23)')
        if pl["5"] != 0:
            self.output_text(strings["5"], pl["5"], font=fonts["5"], width=45-widthreduce, color='rgb(0, 0, 0)')
        self.output_text(strings["6"], pl["6"], font=fonts["1"], width=45-widthreduce, color='rgb(94, 94, 94)')
        self.output_text(strings["7"], pl["7"], font=fonts["3"], width=48-widthreduce)
        self.image.save(self.imagename+"_%s.jpg" % language)

if __name__ == "__main__":

    language = sys.argv[1]

    # Read the placements file
    placements = np.loadtxt("%s/placements_%s.txt" % (language, language))

    # Read the Fonts strings
    fonts_dict = {}
    fonts_file = open("Fonts.csv", "r")
    for line in fonts_file.readlines():
        lang, ttf = line.split(" ")[0], line.split(" ")[1].strip("\n")
        fonts_dict[lang] = ttf

    fonts = {}
    print ('%s-Regular.ttf' % fonts_dict[language])
    if language == "Malayalam" or language == "Tamil":
        fonts["1"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=20)
        fonts["2"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=30)
        fonts["3"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=20)
        fonts["5"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=15)
    elif language == "Urdu":
        fonts["1"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=18)
        fonts["2"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=25)
        fonts["3"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=18)
        fonts["5"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=15)
    else:
        fonts["1"] = ImageFont.truetype('%s-Regular.ttf' % (fonts_dict[language]), size=30)
        fonts["2"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=40)
        fonts["3"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=30)
        fonts["5"] = ImageFont.truetype('%s-Bold.ttf' % (fonts_dict[language]), size=20)

    fonts["4"] = ImageFont.truetype('Noto/English/Montserrat-Bold.ttf', size=40)

    df = pandas.read_csv("Hoaxbuster.csv")

    df.fillna("", inplace = True) 

    #for ii in range(1, 19):
    jj = 0
    for ii in range(1, 19):
        strings = {}
        pl = {}
        pl["1"] = placements[ii-1][1]
        pl["2"] = placements[ii-1][2]
        pl["3"] = placements[ii-1][3]
        pl["4"] = placements[ii-1][4]
        pl["5"] = placements[ii-1][5]
        pl["6"] = placements[ii-1][6]
        pl["7"] = placements[ii-1][7]
        strings["1"] = df[language].values[jj]
        jj = jj + 1
        strings["2"] = df[language].values[jj]
        jj = jj + 1
        strings["3"] = df[language].values[jj]
        jj = jj + 1
        strings["4"] = df[language].values[jj]
        jj = jj + 1
        strings["5"] = df[language].values[jj]
        jj = jj + 1
        strings["6"] = df[language].values[jj]
        jj = jj + 1
        strings["7"] = df[language].values[jj]
        jj = jj + 1
        
        if not path.exists("Sample_images/%05d.jpg" % ii) :
            print("could not find", ii)
            continue

        # Initiate a class
        a = fill_poster("Sample_images/%05d" % ii)
        # Fill in the poster with strings, and save file
        a.convert(strings, pl, language, fonts)
