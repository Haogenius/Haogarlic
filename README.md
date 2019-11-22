# Haogarlic
json_to_dataset.py 适用于批量将文件夹中的json文件转成语义图片，方便你们检测自己的json有没有标好。
推荐使用命令行执行这点操作，因为labelme自带了一个exe可以直接执行
找到你的\Anaconda3\envs\labelme\Lib\site-packages\labelme\cli这个路径，将该路径下的json_to_dataset.py
换成这里的新代码
使用方法：进入到标注好的json文件路径下 在anaconda prompt（激活labelme环境） 输入 labelme_json_to_dataset ./（当前json文件所在路径）即可
