# iCalligraphy-Seg 项目



## 项目功能

该项目基于 $Python$ 库和 星火大模型 $API$ 开发，可以实现为一段没有符号的古诗文标号。

## 注意事项

使用之前要先自行下载 $langchain\_community$ 库和 $websocket-client$ 库。

由于官方库自带的 $bug$ ，使用之前要先 $Ctrl+$鼠标左键点击 $ChatSparkLLM$，进入 $sparkllm.py$ 文件后找到代码并注释，操作如下

![image-20241001204104131](.\imgs\image-20241001204104131.png)

![image-20241001204155920](.\imgs\image-20241001204155920.png)



## 功能实现

在使用之前要在 https://xinghuo.xfyun.cn/sparkapi 网站申请 $4.0ultra$ 的 $api$ ，再将相应的 $appid$ 填入代码部分，再点击运行即可，实现如下

![image-20241001204650232](.\imgs\image-20241001204650232.png)