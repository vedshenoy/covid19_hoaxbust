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

    def convert(self, strings, pl, language):
        self.draw = ImageDraw.Draw(self.image)
        font1 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Regular.ttf', size=30)
        font2 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=40)
        font3 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=30)
        font3 = ImageFont.truetype('Noto/Devanagari/NotoSansDevanagari-Bold.ttf', size=30)
        font4 = ImageFont.truetype('Noto/English/Montserrat-Bold.ttf', size=40)

        self.output_text("The Hoaxbusters", 40, font=font4,  width=30)

        self.output_text(strings["1"], pl["1"], font=font1, width=30, color='rgb(94, 94, 94)')
        self.output_text(strings["2"], pl["2"], font=font2, width=30)
        self.output_text(strings["3"], pl["3"], font=font1, width=40, color='rgb(94, 94, 94)')
        self.output_text(strings["4"], pl["4"], font=font2, width=45, color='rgb(189, 23, 23)')
        self.output_text(strings["5"], pl["5"], font=font1, width=45, color='rgb(94, 94, 94)')
        self.output_text(strings["6"], pl["6"], font=font3, width=45)
        self.image.save(self.imagename+"_%s.jpg" % language)

if __name__ == "__main__":

    # Read the placements file
    placements = np.loadtxt("Marathi/placements_marathi.txt")

    # These strings will have to be read from the appropriate files extracted
    # by `extract.sh`
    fhandle = {}
    for ii in range(1, 7):
        fhandle["%d" % ii] = open("Marathi/string%d_marathi.txt" % ii, "r")

    #for ii in range(1, 19):
    for ii in range(1, 19):
        strings = {}
        pl = {}
        pl["1"] = placements[ii-1][1]
        pl["2"] = placements[ii-1][2]
        pl["3"] = placements[ii-1][3]
        pl["4"] = placements[ii-1][4]
        pl["5"] = placements[ii-1][5]
        pl["6"] = placements[ii-1][6]
        strings["1"] = fhandle["1"].readline()
        strings["2"] = fhandle["2"].readline()
        strings["3"] = fhandle["3"].readline() 
        strings["4"] = fhandle["4"].readline()
        strings["5"] = fhandle["5"].readline()
        strings["6"] = fhandle["6"].readline()
        
        if not path.exists("Sample_images/%05d.jpg" % ii) :
            print("could not find", ii)
            continue

        # Initiate a class
        a = fill_poster("Sample_images/%05d" % ii)
        # Fill in the poster with strings, and save file
        a.convert(strings, pl, "Marathi")

