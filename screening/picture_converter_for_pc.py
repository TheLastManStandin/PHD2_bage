# преобразует любое изображение в доступное для бейджика
from PIL import Image
import os

set_folder_path_here = "screening\\x5x10_gifs"
set_int_resolution_here = [5, 10]

def img_to_list(img, resolution):
    x, y = resolution
    img_list = []

    img = img.resize((x, y), Image.NEAREST)

    img = img.convert("RGB")
    img = img.transpose(Image.ROTATE_180) 

    pixels = list(img.getdata())
    matrix = [pixels[i * x:(i + 1) * x] for i in range(y)]

    for row in matrix:
        img_list.append(row)

    return img_list

# def convert_pic(folder_path, resolution):
#     images = []

#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#         if os.path.isfile(file_path):
#             img = Image.open(os.getcwd() + f"\\{folder_path}\\" + file_name)
#             images.append([file_name, img_to_list(img, img.size)])

#     for file_name, pic in images:
#         print(f'"{file_name}":[')
#         for i in range(len(pic)):
#             if i % 2 == 1:
#                 print(pic[i], end="\n")
#             else:
#                 print(pic[i], end="")
        
#         print("],")

def convert_gif(folder_path, resolution):
    images = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            img = Image.open(os.getcwd() + f"\\{folder_path}\\" + file_name)
            gif_width, gif_height = img.size
            gif_list = img_to_list(img, img.size)
            x, y = resolution
            for i in range(gif_height // y):
                image = []
                for j in range(y):
                    image.append(gif_list[i * y + j])
                
                images.append([f"{file_name}_{i}", image])

    for file_name, pic in images:
        print(f'"{file_name}":[')
        for i in range(len(pic)):
                print(pic[i], end= ",\n")
        
        print("],")

if __name__ == "__main__":
    convert_gif(set_folder_path_here, set_int_resolution_here)