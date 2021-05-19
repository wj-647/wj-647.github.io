# -*- coding: UTF-8 -*-
#coding=utf-8
import matplotlib.pyplot as plt  #调用库
import numpy as np               #调用库
x = np.linspace(0, 3 * np.pi, 100)# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
y = np.sin(x)                     #写定函数

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)                       #两个图像的第一个
plt.title(r'$f(x)=sin(x)$')              #题目
plt.plot(x, y)                           #表示x，y坐标
#plt.show()

x1 = [t*0.375*np.pi for t in x]         #x=t*0.3750*π，t=x
y1 = np.sin(x1)                         #写定函数
plt.subplot(1,2,2)                      #两个图像的第二个
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')   #题目
plt.plot(x, y1)                                               #表示x1，y1坐标轴
plt.show()                                                     #打印图像