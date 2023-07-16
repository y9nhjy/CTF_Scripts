import zipfile, os

path = r'C:\Users\lENOVO\Downloads'  # 存放压缩包的目录


def x():  # 一次解压
    for i in os.listdir(path):
        if '.zip' in i:
            route = os.path.join(path, i)
            zip_file = zipfile.ZipFile(route)  # 压缩文件的路径与文件名
            for f in zip_file.namelist():  # 得到压缩包里所有文件名（循环）
                zip_file.extract(f, path)  # 循环解压文件到指定目录
            zip_file.close()  # 关闭文件，必须有，释放内存
            os.remove(route)


x()
while 1:
    x()
    zips = [m for m in os.listdir(path) if '.zip' in m]
    if not zips:  # 判断zips是否为空，为空则停止
        break
