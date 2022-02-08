import time
from io import BytesIO
from Common.open_browser import RunBrowser
import cv2
import numpy as np
import requests
from PIL import Image
from Common.common import path_file


class Common(RunBrowser):

    def yzm(self):
        global result_value
        path = path_file()
        time.sleep(1)
        while self.page.query_selector('//*[contains(text(),"向右拖动滑块填充拼图")]') is not None:
            time.sleep(1)
            target_link = self.page.get_attribute("img.yidun_bg-img", 'src')
            template_link = self.page.get_attribute("img.yidun_jigsaw", 'src')
            target_img = Image.open(BytesIO(requests.get(target_link).content))
            template_img = Image.open(BytesIO(requests.get(template_link).content))
            target_img.save(path + '/Source/Image_yzm/target.jpg')  # 缺口图片
            template_img.save(path + '/Source/Image_yzm/template.png')  # 验证图片
            img_rgb = cv2.imread(path + '/Source/Image_yzm/target.jpg')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(path + '/Source/Image_yzm/template.png', 0)
            run = 1
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            # 使用二分法查找阈值的精确值
            L = 0
            R = 1
            while run < 20:
                run += 1
                threshold = (R + L) / 2
                if threshold < 0:
                    print('Error')
                    return None
                loc = np.where(res >= threshold)
                if len(loc[1]) > 1:
                    L += (R - L) / 2
                elif len(loc[1]) == 1:
                    result_value = loc[1][0]
                    break
                elif len(loc[1]) < 1:
                    R -= (R - L) / 2
            slider = self.page.query_selector("div.yidun_slider").bounding_box()
            self.page.mouse.move(slider['x'], slider['y'])
            self.page.mouse.down()
            self.page.mouse.move(int(slider['x'] + result_value + 10), slider['y'])
            self.page.mouse.up()
            time.sleep(1)
