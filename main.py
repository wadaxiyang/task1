# -*- coding: UTF-8 -*-
# 采用函数模块话以便于移植
# coding by wadaxiyang
import cv2
import numpy as np


def hsvDone(img_get):
    img_gs = cv2.GaussianBlur(img_get, (5, 5), 0)  # 先对图像进行高斯模糊处理
    img_hsv = cv2.cvtColor(img_gs, cv2.COLOR_BGR2HSV)
    img_hsv = cv2.erode(img_hsv, None, iterations=2)  # 腐蚀
    # 分别处理两组h值
    lower_red0 = np.array([0, 50, 50])
    upper_red0 = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red0, upper_red0)
    lower_red1 = np.array([156, 50, 50])
    upper_red1 = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    mask = mask0 + mask1
    output_hsv = img_hsv.copy()
    output_hsv = cv2.bitwise_and(output_hsv, output_hsv, mask=mask)  # 处理得出hsv图像
    return output_hsv


def boxSelection(img_hsv_get, img_get):
    img_gray = cv2.cvtColor(img_hsv_get, cv2.COLOR_BGR2GRAY)  # 转灰度
    retval, output = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)  # 填充，便于后续处理，其实前面已经可以算是已经完成一次填充
    # 寻找边界与矩形
    cnt = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    c = max(cnt, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    # 绘制矩形
    cv2.drawContours(img_get, [np.int0(box)], -1, (0, 255, 255), 2)
    # 中心坐标
    cv2.putText(img_get,
                str((box[2][0] - box[0][0]) / 2 + box[0][0]) + ',' + str((box[0][1] - box[1][1]) / 2 + box[1][1]),
                (int(box[2][0] - 10), int(box[2][1] - 25)),
                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
    return img_get


def main():
    img = cv2.imread("test.png")
    img_hsv = hsvDone(img)
    img_output = boxSelection(img_hsv, img)
    cv2.imshow('result', img_output)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
