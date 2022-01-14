def pngversjpg(image)->None:
    from PIL import Image

    im = Image.open(image)
    rgb_im = im.convert('RGB')
    rgb_im.save('convert.jpg')