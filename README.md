# pybiliapi
用API获取B站上的视频信息等等。 <br>
她使用LGPL v3许可证（见LICENSE文件）。 <br>
在遵守LGPL v3许可证（见LICENSE文件）的前提下可以做任何更改等。比如裁剪不需要的部分使之更轻，更小。 <br>
## 使用方法
简单粗暴地扔到你的程序文件目录，import之即可。此模块无需使用pip获取，也无法使用pip获取。 <br>
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
import biliapi
biliapi.view(ba.aid('BV17x411w7KC')) 
````
## 关于LGPL不同版本间及与GPL许可证之间的不兼容问题的说明
特在此说明: 您可以视为此程序遵循LGPL v2.1及之后的任何版本, 或GPL v2及之后的任何版本.
