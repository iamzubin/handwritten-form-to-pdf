from PIL import Image, ImageDraw

def create_image(image_name, width, height):
    image = Image.new('RGB', (width, height), color = 'white')
    image.save(image_name)

def draw_lines(image_name, y_axis_list):
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)
    for y in y_axis_list:
        draw.line((100, y, 2380, y), fill="Black", width=3)
    del draw
    image.save("test1.png")

def get_lines_position(image_name, divisions_with_lines):
    list_of_y_axis = []
    current_line = 400
    draw_lines(image_name, [400])
    for values in divisions_with_lines:
        current_line = (values * 150) + current_line
        list_of_y_axis.append(current_line)
    return list_of_y_axis


def generate_form(form_name, fields):
    file_name = form_name + ".png"
    create_image(file_name, 2480, 3508)
    y_axis_lines = get_lines_position(file_name, [1, 1, 1, 2, 5])
    draw_lines(file_name, y_axis_lines)

generate_form("test", 69)
