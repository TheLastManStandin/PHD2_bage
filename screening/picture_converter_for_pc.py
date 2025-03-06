# преобразует любое изображение в доступное для бейджика
from PIL import Image
import os

set_folder_path_here = "screening\\4x4_images"
set_int_resolution_here = 4

def img_to_list(img, resolution):
    x = resolution
    img_list = []

    img = img.resize((x, x), Image.NEAREST)

    img = img.convert("RGB")
    img = img.transpose(Image.ROTATE_180) 

    pixels = list(img.getdata())
    matrix = [pixels[i * x:(i + 1) * x] for i in range(x)]

    for row in matrix:
        img_list.append(row)
        img_list.append(",")

    return img_list

def convert(folder_path, resolution):
    images = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            img = Image.open(os.getcwd() + f"\\{folder_path}\\" + file_name)
            images.append([file_name, img_to_list(img, resolution)])

    for file_name, pic in images:
        print(f'"{file_name}":[')
        for i in range(len(pic)):
            if i % 2 == 1:
                print(pic[i], end="\n")
            else:
                print(pic[i], end="")
        
        print("],")

if __name__ == "__main__":
    convert(set_folder_path_here, set_int_resolution_here)