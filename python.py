from PIL import Image
im = Image.open('SB vs. BB.png')
final = []

pix = im.load()
print(pix[550, 575])
pix[500,600] = (0,0,0)
im.show()
