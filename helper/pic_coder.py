import base64 as b64

def encode(local_path, save_path):
    """
    将图片编码：Base64，并保存到 save_path 之中
    @param: local_path 需要编码的图片文件的路径
    @param: save_path 保存编码结果的文件路径
    """
    # 二进制方式打开文件
    pic = open(local_path, 'rb')
    pic_encode = b64.b64encode(pic.read())
    data = open(save_path, 'wb')
    data.write(pic_encode)
    pic.close()
    data.close()

def decode(code, path):
    """
    将Base64编码的图片还原为图片文件
    @param: code 图片的base64编码
    @param: path 要保存的路径
    """
    data = b64.b64decode(code)
    img = open(path, 'wb')
    img.write(data)
    img.close()

# encode('source/_posts/images/beauty.png', 'source/_posts/images/encode/beauty.txt');
decode(open('source/_posts/images/encode/beauty.txt').read(), 'source/_posts/images/beauty2.png')

