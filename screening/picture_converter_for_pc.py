# преобразует любое изображение в доступное для бейджика
from PIL import Image

image_path = "screening/image.png"  
img = Image.open(image_path)

img = img.resize((10, 10), Image.NEAREST)

img = img.convert("RGB")
img = img.transpose(Image.ROTATE_180) 

pixels = list(img.getdata())
matrix = [pixels[i * 10:(i + 1) * 10] for i in range(10)]

for row in matrix:
    print(row, ',')
