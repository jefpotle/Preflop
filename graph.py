from PIL import Image

im = Image.open('LJ vs. SB.png')
final = []

pix = im.load()
def identify (rgb):
    colors = {'red':[235, 0, 0, 235], 'purple':[110, 0, 235, 235], "orange":[235, 110, 0, 235], "yellow":[235, 235, 0, 235], "green":[0, 235, 0, 235, 235], "pink":[235, 110, 235, 235], "blue":[0, 110, 235, 235], "white":[235, 235, 235, 235], "light_blue":[0, 235, 235, 235], "grey":[175, 175, 175, 235]}
    #if rgb == (245, 245, 245, 255):
    #    return 'ignore'
    for x in colors:
        tmp = colors[x]
        if abs(rgb[0] - tmp[0]) < 35 and abs(rgb[1] - tmp[1]) < 35 and abs(rgb[2] - tmp[2]) < 35 and abs(rgb[3] - tmp[3]) < 35:
            return x
    return rgb

for y in range(int(im.size[1]/13)-5, im.size[1], int(im.size[1]/13)):
    row = []
    for x in range(20, im.size[0], int(im.size[0]/13)):
        if identify(pix[x,y]) == 'ignore':
            row.append('ignore')
        row.append(identify(pix[x,y]))
        #row.append(pix[x,y])
        pix[x,y] = (0,0,0)
    final.append(row)
im.show()
card_range = []
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
for x in range(len(cards)):
    row = []
    switch = True
    for y in range(len(cards)):
        s = ""
        if x == y:
            s = cards[x] + cards[y]
            row.append(s)
            switch = False
        elif switch == True:
            if x < y:
                s = cards[x] + cards[y] +'o'
            else:
                s = cards[y] + cards[x] + 'o'
            row.append(s)
        else:
            if x < y:
                s = cards[x] + cards[y] + 's'
            else:
                s = cards[y] + cards[x] + 's'
            row.append(s)
    card_range.append(row)
dct = {}
for x in range(len(card_range)):
    for y in range(len(card_range[x])):
        if final[x][y] == 'white' and card_range[x][y] not in ['T9s', '77', '76s', '66', '65s', '55', '54s', '44', '33', '22']:
            pass
        else:
            dct[card_range[x][y]] = final[x][y]
print()
print(dct)
