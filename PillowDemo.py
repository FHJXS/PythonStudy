import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def demo1():
    """
    缩小图片
    :return:
    """
    # 打开一个jpg图像文件,是当前文件
    im = Image.open("cha.jpg")
    # 获取图像尺寸
    w, h = im.size
    print("这个图片的大小为:%s x %s" % (w, h))
    # 缩放到50%
    im.thumbnail((w // 2, h // 2))
    print("重置后大小为：%s x %s" % (w // 2, h // 2))
    # 吧缩放的图片用jpeg格式保存
    im = im.convert('RGB')
    im.save('new.jpg', 'jpeg')


def demo2():
    """
    添加照片模糊效果
    :return:
    """
    # 先打开一个jpg图像文件
    img = Image.open("a.png")
    # 应用模糊滤镜
    img2 = img.filter(ImageFilter.BLUR)
    img2 = img2.convert('RGB')
    img2.save("blur.jpg", "jpeg")


def demo3():
    """
    使用绘图功能
    :return:
    """

    # 生成随机字母
    def rndChar():
        return chr(random.randint(65, 90))

    # 随机颜色
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
        # return (255,255,255)
    width = 60 * 4
    height = 60
    image = Image.new("RGB", (width, height), (255, 255, 255))
    # 创建Font对象：
    font = ImageFont.truetype("arial.ttf", 36)
    # font = ImageFont.load_default()
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    #模糊
    image = image.filter(ImageFilter.BLUR)
    image.save("code.jpg","jpeg")

def demo4():
    width = 500
    height = 500
    image = Image.new("RGB", (width, height), (255, 255, 255))
    font = ImageFont.truetype("STXINGKA.TTF", 500)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)))
    draw.text((0,0),"福", font=font, fill=(0,0,0))
    image = image.filter(ImageFilter.BLUR)
    image.save("福.jpg", "jpeg")
    pass

if __name__ == '__main__':
    demo4()
