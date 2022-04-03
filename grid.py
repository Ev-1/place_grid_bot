from PIL import Image, ImageDraw, ImageFont


def gen_grid(top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    top_left_x_offset = top_left_x
    top_left_y_offset = top_left_y

    pixel_magnifier = 30
    region_width = bottom_right_x-top_left_x_offset + 1
    region_height = bottom_right_y-top_left_y_offset + 1

    img = Image.new('RGBA', (region_width * pixel_magnifier, region_height * pixel_magnifier), color = (255, 255, 255, 0))

    fnt = ImageFont.truetype('./arial.ttf', 10)
    d = ImageDraw.Draw(img)
    for i in range(region_height):
        d.line((0, i * pixel_magnifier, pixel_magnifier * region_width, i * pixel_magnifier), fill=(0, 0, 0))

    for i in range(region_width):
        d.line((i * pixel_magnifier, 0, i * pixel_magnifier, pixel_magnifier * region_height), fill=(0, 0, 0))

    for x in range(region_width):
        for y in range(region_height):
            d.text((x * pixel_magnifier + 5, y * pixel_magnifier + 2), f"{x + top_left_x_offset}\n{y + top_left_y_offset}", font=fnt, fill=(0, 0, 0))

    img.save('grid_generator.png')
