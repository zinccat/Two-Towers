from PIL import Image


def touming(path, btmd):
    img = Image.open(path)
    img = img.convert('RGBA')
    x, y = img.size
    for i in range(x):
        for k in range(y):
            color = img.getpixel((i, k))
            if color[:3] == (255, 255, 255):
                color = (255, 255, 255, 0)
                # print('*',end='')#这句是我想试试到底有没有进这个条件
            else:
                color = color[:-1]+(btmd,)
            img.putpixel((i, k), color)
    img.save(path[:-4]+str(int(btmd*10/25))+'.png')

for i in range(1, 11):
    touming('images/archerE.png', i*25)
