from PIL import Image,ImageFilter,ImageFont,ImageDraw ##image lib
from matplotlib.pyplot import imshow 

filename = 'new.jpg'
im = Image.open(filename)
# imshow(im)

print(im.size)
print(im.format_description)
print(im.mode)

# # crop = (200,200,800,800)
# # croppped = im.crop(crop)
# # imshow(croppped)

# resized = im.resize((500,500))
# imshow(resized)

# grey_scale = im.convert
# im.show(grey_scale)

effect = im.filter(ImageFilter.GaussianBlur(radius=20))
im.show(effect)

draw = ImageDraw.Draw(im)
# font = ImageFont.truetype('arial.tff',200)
# draw.text((100,100), 'god of war',font=font)
# imshow(im)
