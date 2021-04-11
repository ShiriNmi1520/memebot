from PIL import Image

if __name__ == '__main__':
    main()
def main():
    BIG_PIC_PATH = './img/big.png'
    SMALL_PIC_PATH = './img/o.png'

    bigPic = Image.open(BIG_PIC_PATH)
    smallPic = Image.open(SMALL_PIC_PATH)
    bigPic = bigPic.convert("RGB")
    smallPic = smallPic.convert("RGB")
    smallPic.thumbnail((40, 40))
    smallPic.load()

    # bg = Image.new('RGB',smallPic.size ,(255,255,255))
    # bg.paste(smallPic, mask=smallPic.split()[3])
    # bg.save('./img/save.jpg', 'JPEG', quality=80)
    
    # toPaste = Image.open('./img/save.jpg')
    x1 = 494 + smallPic.size[0]
    y1 = 75 + smallPic.size[1]
    box = (494, 75, x1, y1)

    bigPicChange = bigPic.paste(smallPic, box)
    bigPic.save('./img/big_change.png')
    smallPic.save('./img/small_save.png')