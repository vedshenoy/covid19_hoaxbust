# import required classes
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
        font1 = ImageFont.truetype('Noto/NotoSansDevanagari-Bold.ttf', size=40)
        font2 = ImageFont.truetype('Noto/NotoSansDevanagari-Bold.ttf', size=40)
        font3 = ImageFont.truetype('Noto/NotoSansDevanagari-Bold.ttf', size=30)

        self.output_text(strings["1"], 80, font=font1, width=30)
        self.output_text(strings["2"], 110, font=font2, width=30)
        self.output_text(strings["3"], 700, font=font1, width=40)
        self.output_text(strings["4"], 750, font=font3, width=45, color='rgb(255, 0, 0)')
        self.output_text(strings["5"], 850, font=font3, width=45)
        self.output_text(strings["6"], 900, font=font3, width=45)
        self.image.save(self.imagename+"_modified.jpg")

if __name__ == "__main__":
    strings = {}
    strings["1"] = "दावा:"
    strings["2"] = "योगासने केल्याने माझे कोविड-१९ पासून संरक्षण होऊ शकते."
    strings["3"] = "निर्णय:"
    strings["4"] = "बहुतेक शक्य नाही (पुरेसा पुरावा नाही)"
    strings["5"] = "का?:"
    strings["6"] = "इतर व्यायाम पद्धतींप्रमाणेच योगासने केल्याने शरीर निरोगी व तणावमुक्त राहू शकते. निरोगी व्यक्ती कोणत्याही आजारापासून लवकर बऱ्या होऊ शकतात. पण “योगासने केल्याने कोविड-१९ पासून संरक्षण होते” यासाठी कोणताही पुरावा नाही."

    a = fill_poster("Sample")
    a.convert(strings)
