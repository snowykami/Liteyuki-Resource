import os.path

from PIL import Image, ImageDraw

folder = os.path.dirname(__file__)

for pic in os.listdir(folder):
    if pic.endswith(".png"):
        p = Image.open(pic)
        new_p = Image.new(mode="RGBA", size=p.size, color=(0, 0, 0, 0))
        for x in range(p.size[0]):

            for y in range(p.size[1]):
                pix = p.getpixel((x, y))
                if sum(pix) > 0:
                    ImageDraw.Draw(new_p).point((x, y), fill=(59, 66, 85, pix[3]))
        print(pic)
        new_p.save(fp="out/%s" % pic)
