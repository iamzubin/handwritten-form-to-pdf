from PIL import Image, ImageDraw, ImageFont

'''
For using this file call the function generate_form and give it the fields of your form with number of lines you want in it.
fields = {"Name :": 1, "Age :": 1, "Sex :": 1, "Email :": 1, "Home Address :": 4}
generate_form("test", fields)
'''

def create_image(image_name, width, height):
    image = Image.new('RGB', (width, height), color = 'white')
    image.save(image_name)

def draw_lines(image_name, y_axis_list):
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)
    for y in y_axis_list:
        draw.line((100, y, 2380, y), fill="Black", width=3)
    del draw
    image.save(image_name)

def put_text_in_image(image_name, text_list, y_axis_list):
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))
    for y_axis, put_text in zip(y_axis_list[:-1], text_list):
        draw.text((140, y_axis + 50), put_text, (0,0,0), font=font)
    image.save(image_name)

def get_lines_position(image_name, divisions_with_lines):
    list_of_y_axis = []
    current_line = 250
    for values in divisions_with_lines:
        current_line = (values * 150) + current_line
        list_of_y_axis.append(current_line)
    return list_of_y_axis

def generate_form(form_name, fields):
    file_name = form_name + ".png"
    create_image(file_name, 2480, 3508)
    y_axis_lines = get_lines_position(file_name, list(fields.values()))
    draw_lines(file_name, y_axis_lines)
    put_text_in_image(file_name, list(fields.keys()), y_axis_lines)

    points_for_ocr = [] # These points are in pixals
    for y in y_axis_lines:
        points_for_ocr.append((100, y, 2380, y))
    
    return points_for_ocr