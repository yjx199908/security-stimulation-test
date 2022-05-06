from ast import Global
from PIL import Image,ImageDraw,ImageFont
from utils.global_constant import GlobalConstant
class ImgProvider:
    def __init__(self) -> None:
        pass

    @staticmethod
    def draw(content,img_name):
        font_size = 20
        font_len = len(content)
        font_img_len = font_len * font_size
        canvas_width = font_img_len + 2 * font_size
        canvas_height = 300
        im = Image.new("RGB",(canvas_width,canvas_height),(255,255,255))
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype(font=r"./assets/fonts/Ubuntu-B.ttf",size=font_size)
        dr.text((font_size,(canvas_height - font_size) / 2),content,fill="#000000",font=font)
        im.save('{}/{}'.format(GlobalConstant.IMAGES_FOLDER,img_name))