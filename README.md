# python + OpenCV 分离红色目标并框选

## 本次目标

*对于以下图像实现对象提取，提取红色小球并框选出其范围*

![pic1](https://i.328888.xyz/2022/12/21/AEBvE.png)

*关键词：颜色通道过滤，区域最小外接矩形*

考虑到对颜色进行过滤，采用hsv格式进行处理，在此记录下[RGB、HSV和HSL的区别](https://zhuanlan.zhihu.com/p/67930839)
在查阅相关资料后发现，红色对应有两组不同h值，因此代码中叠加mask。详见[参考连接](https://wenku.baidu.com/link?url=TIfc4sxe_pj3n5hc4ZXEpDuHOdmkzV3KtOE0BspGtDa0BP1Hf3KeN8NLo__gDXvTpFybF2bvl43F35j0a1jL8DvKqH7sYJH419bBpjPo9-a&_wkts_=1671628900899)
![pic2](https://i.328888.xyz/2022/12/21/AEEut.png)
