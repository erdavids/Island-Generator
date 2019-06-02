import PIL, random, sys
from PIL import Image, ImageDraw
from opensimplex import OpenSimplex
from datetime import datetime

origDimension = 1500


def main():
    pil_image = Image.new('RGB', (origDimension, origDimension))

    pixels = pil_image.load()

    tmp = OpenSimplex(seed=1)
    tmp2 = OpenSimplex(seed=3)

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            pixels[i, j] = (0, 119, 190)

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            pixel_value = (tmp.noise2d(x=i/200.0, y=j/200.0) + tmp2.noise2d(x=i/200.0, y=j/200.0))/2

        #if (int(pixel_value * 100.0) == 90) or (int(pixel_value * 100.0) == 70) or (int(pixel_value * 100.0) == 40) or (int(pixel_value * 100.0) == 0):
            if (int(pixel_value * 100.0) == 15):
                pixels[i, j] = (0, 0, 0)
            elif (int(pixel_value * 100.0) > 15):
                pixels[i, j] = (107, 142, 35)
            elif (int(pixel_value * 100.0) > 0):
                pixels[i, j] = (214, 204, 169)
    pil_image.save('Generative-Space-Texture.png')
if __name__ == "__main__":
    main()
