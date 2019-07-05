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
    parser.add_argument("-pnw", "--planet_number_wide", default=1, type=int)
    parser.add_argument("-pnh", "--planet_number_high", default=1, type=int)
    parser.add_argument("-ps", "--planet_size", default=1500, type=int)
    parser.add_argument("-oc", "--other_color", default=0, type=int)
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
    planet_number_wide = args.planet_number_wide
    planet_number_high = args.planet_number_high
    planet_size = args.planet_size
    other_color = args.other_color

    pil_image = Image.new('RGBA', (planet_number_wide*planet_size, planet_number_high*planet_size))

    pixels = pil_image.load()
    #           var rand = myArray[Math.floor(Math.random() * myArray.length)];
         # document.getElementById("color-text").style.color = rand;
    colors_list = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]

    for col in range(pil_image.size[0]):
        for row in range(pil_image.size[1]):
            pixels[col, row] = (208, 200, 176)

    for col in range(0, pil_image.size[0], planet_size):
        for row in range(0, pil_image.size[1], planet_size):
            color_water = random.choice(colors_list)
            color_ground = random.choice(colors_list)
            while color_ground is color_water:
                color_ground = random.choice(colors_list)
            other_color = random.choice(colors_list)
            while other_color is color_water or other_color is color_ground:
                other_color = random.choice(colors_list)
            for i in range(col, col+planet_size):
                for j in range(row, row+planet_size):

                    # Generates a value from -1 to 1
                    pixel_value = noise.pnoise2((offset+i)/scale,
                                                (offset+j)/scale,
                                                octaves,
                                                persistence,
                                                lacunarity,
                                                width,
                                                height,
                                                base)
                    distance_from_center = math.sqrt(math.pow((i - (col+(col+planet_size))/2), 2) + math.pow((j - (row+(row+planet_size))/2), 2))


                    gradient_perc = distance_from_center/max_distance

                    #pixel_value -= math.pow(gradient_perc, 3)
                    #random.seed()

                    if (distance_from_center < max_distance):
                        if (other_color == 1 and int(pixel_value * 100.0) > 25):
                            pixels[i, j] = other_color
                        elif (int(pixel_value * 100.0) > 5):
                            pixels[i, j] = color_ground
                        else:
                            pixels[i, j] = color_water
                    elif (distance_from_center < (max_distance + .03 * max_distance)):
                        pixels[i, j] = (15, 15, 15)

    #region = pil_image.crop((500, 500, 1000, 1000))
    #pil_image.paste(region, (0, 0, 500, 500))
    pil_image.save('Examples/Planet-' + str(offset) + '-w-' + str(width) + '-h-' + str(height) + '.png')


if __name__ == "__main__":
    main()

    # 52 minutes - Definitely my maybe
    # -> 1:07

    # watch endsceen -> credits
