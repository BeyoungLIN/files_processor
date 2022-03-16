# -*- coding: utf-8 -*-
# @Time   : 2022/3/16 17:26
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : screenshot_web.py

class ScreenShotMerge():
    def __init__(self, page, over_flow_size):
        self.im_list = []
        self.page = page
        self.over_flow_size = over_flow_size
        self.get_path()

    def get_path(self):
        self.root_path = Path(__file__).parent.joinpath('temp')
        if not self.root_path.exists():
            self.root_path.mkdir(parents=True)
        self.save_path = self.root_path.joinpath('merge.png')

    def add_im(self, path):
        if len(self.im_list) == self.page:
            im = self.reedit_image(path)
        else:
            im = Image.open(path)
        im.save('{}/{}.png'.format(self.root_path, len(self.im_list) + 1))
        self.im_list.append(im)

    def get_new_size(self):
        max_width = 0
        total_height = 0
        # 计算合成后图片的宽度（以最宽的为准）和高度
        for img in self.im_list:
            width, height = img.size
            if width > max_width:
                max_width = width
            total_height += height
        return max_width, total_height

    def image_merge(self, ):
        if len(self.im_list) > 1:
            max_width, total_height = self.get_new_size()
            # 产生一张空白图
            new_img = Image.new('RGB', (max_width - 15, total_height), 255)
            x = y = 0
            for img in self.im_list:
                width, height = img.size
                new_img.paste(img, (x, y))
                y += height
            new_img.save(self.save_path)
            print('截图成功:', self.save_path)
        else:
            obj = self.im_list[0]
            width, height = obj.size
            left, top, right, bottom = 0, 0, width, height
            box = (left, top, right, bottom)
            region = obj.crop(box)
            new_img = Image.new('RGB', (width, height), 255)
            new_img.paste(region, box)
            new_img.save(self.save_path)
            print('截图成功:', self.save_path)

    def reedit_image(self, path):
        obj = Image.open(path)
        width, height = obj.size
        left, top, right, bottom = 0, height - self.over_flow_size, width, height
        box = (left, top, right, bottom)
        region = obj.crop(box)
        return region
