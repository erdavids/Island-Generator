import PIL, random, sys, argparse, math
from PIL import Image, ImageDraw
import noise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", default=1500, type=int)
    parser.add_argument("--height", default=1500, type=int)
    parser.add_argument("-s", "--scale", default=200.0, type=float)
    parser.add_argument("-o", "--octaves", default=6, type=int)
    parser.add_argument("-p", "--persistence", default=.5, type=float)
    parser.add_argument("-l", "--lacunarity", default=2.0, type=float)
    parser.add_argument("-b", "--base", default=0, type=int)
    parser.add_argument("-md", "--max_distance", default=900.0, type=float)
    parser.add_argument("-a", "--alter", default=0, type=int)
    args = parser.parse_args()

    random.seed()
    offset = random.randint(1, 100) * random.randint(1, 1000)

    width, height = args.width, args.height
    octaves = args.octaves
    persistence = args.persistence
    lacunarity = args.lacunarity
    scale = args.scale
    base = args.base
    alter = args.alter
    max_distance = args.max_distance

    pil_image = Image.new('RGBA', (width, height))

    pixels = pil_image.load()

    cl = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]
    last_color = (0, 0, 0)

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):

            # Generates a value from -1 to 1
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

            if (int(pixel_value * 100.0) > 30):
                pixels[i, j] = cl[0]
            elif (int(pixel_value * 100.0) > 10):
                pixels[i, j] = cl[3]
            elif (int(pixel_value * 100.0) > -10):
                pixels[i, j] = cl[2]
            elif (int(pixel_value * 100.0) > -30):
                pixels[i, j] = cl[1]
            else:
                pixels[i, j] = cl[0]

    pil_image.save('Examples/Color-' + str(offset) + '-w-' + str(width) + '-h-' + str(height) + '.png')

if __name__ == "__main__":
    main()

    # 52 minutes - Definitely my maybe
    # -> 1:07

    # watch endsceen -> credits
