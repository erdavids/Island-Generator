import PIL, random, sys, argparse, math
from PIL import Image, ImageDraw
import noise
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", default=1500, type=int)
    parser.add_argument("--height", default=1500, type=int)
    parser.add_argument("-s", "--scale", default=200.0, type=float)
    parser.add_argument("-o", "--octaves", default=6, type=int)
    parser.add_argument("-m", "--moisture", action="store_true")
    parser.add_argument("-p", "--persistence", default=.5, type=float)
    parser.add_argument("-l", "--lacunarity", default=2.0, type=float)
    parser.add_argument("-b", "--base", default=0, type=int)
    parser.add_argument("-md", "--max_distance", default=900.0, type=float)
    parser.add_argument("-d", "--detail", default="low", type=str)
    parser.add_argument("-a", "--alter", default=0, type=int)
    args = parser.parse_args()

    random.seed()

    offset = random.randint(1, 100) * random.randint(1, 1000)
    moisture_offset = random.randint(1, 100) * random.randint(1, 1000)


    width, height = args.width, args.height
    octaves = args.octaves
    persistence = args.persistence
    lacunarity = args.lacunarity
    scale = args.scale
    base = args.base
    detail = args.detail
    alter = args.alter
    moisture = args.moisture

    max_distance = args.max_distance
    pil_image = Image.new('RGBA', (width, height))

    pixels = pil_image.load()

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            pixels[i, j] = (153, 162, 157)

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            pixel_value = noise.pnoise2((offset+i)/scale,
                                        (offset+j)/scale,
                                        octaves,
                                        persistence,
                                        lacunarity,
                                        width,
                                        height,
                                        base)

            distance_from_center = math.sqrt(math.pow((i - width/2), 2) + math.pow((j - height/2), 2))

            gradient_perc = distance_from_center/max_distance


            pixel_value -= math.pow(gradient_perc, 3)

        #if (int(pixel_value * 100.0) == 90) or (int(pixel_value * 100.0) == 70) or (int(pixel_value * 100.0) == 40) or (int(pixel_value * 100.0) == 0):
            #if (int(pixel_value * 100.0) == 15):
            #    pixels[i, j] = (0, 0, 0)
            #if (int(pixel_value * 100.0) > 15):
            #    pixels[i, j] = (169, 166, 115)


            #elif (int(pixel_value * 100.0) == 7):
            #    pixels[i, j] = (0, 0, 0)
            if (int(pixel_value * 100.0) > 30 - alter):
                pixels[i, j] = (240, 240, 240)
            elif (int(pixel_value * 100.0) > 20 - alter):
                pixels[i, j] = (200, 200, 200)
            elif (int(pixel_value * 100.0) > 5 - alter):
                pixels[i, j] = (134, 164, 114)
            elif (int(pixel_value * 100.0) > 0 - alter):
                pixels[i, j] = (236, 212, 184)

            # if moisture == True:
            #     moisture_value = noise.pnoise2((offset+i)/(scale/5),
            #                                 (offset+j)/(scale/5),
            #                                 octaves,
            #                                 persistence,
            #                                 lacunarity,
            #                                 width,
            #                                 height,
            #                                 base)
            #
            #     if (int(pixel_value * 100.0) > 5 and int(pixel_value * 100.0) < 20):
            #         if int(moisture_value * 100.0) > 0:
            #             pixels[i, j] = (int(pixels[i, j][0] * 1.4), int(pixels[i, j][1] * 1.4), int(pixels[i, j][2] * 1.4))

    pil_image.save('Examples/Island-' + str(offset) + '-w-' + str(width) + '-h-' + str(height) + '.png')

if __name__ == "__main__":
    main()

    # 52 minutes - Definitely my maybe
    # -> 1:07

    # watch endsceen -> credits
