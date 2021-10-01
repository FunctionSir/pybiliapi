# pybiliapi
用API获取B站上的视频信息等等。 <br>
她使用宽松的MIT许可证（见LICENSE文件）。 <br>
在遵守MIT许可证（见LICENSE文件）的前提下可以做任何更改等。比如裁剪不需要的部分使之更轻，更小。 <br>
## 使用方法
简单粗暴地扔到你的程序文件目录，import之即可。 <br>
要想裁剪她同样简单粗暴，删掉不用的函数即可。 <br>
把相关函数等拷贝至自己的程序也是可以的，只要遵守MIT许可证（见LICENSE文件）。 <br>
## 函数说明
bvid(aid) AV2BV str <br>
aid(bvid) BV2AV int <br>
cid(aid) 获取cid int <br>
cover(aid) 获取封面（URL）str <br>
view(aid) 获取观看量 int <br>
video_p(aid) 分P数 int <br>
like(aid) 获取赞数 int <br>
favorite(aid) 获取收藏数 int <br>
danmaku(aid) 获取弹幕数 int <br>
coin(aid) 获取硬币数 int <br>
share(aid) 获取分享数 int <br>
reply(aid) 获取评论数 int <br>
up_name(aid) 获取某视频的UP的名字 str <br>
up_uid(aid) 获取某视频的UP的UID int <br>
up_face(aid) 获取某视频的UP的头像（URL) str <br>
xml_danmaku_url(aid) 获取XML弹幕文件的URL str <br>
xml_danmaku_text(aid) 获取XML弹幕文件内容 str <br>
## 使用样例
````python
import biliapi as ba
ba.view(ba.aid('BV17x411w7KC')) 
````
