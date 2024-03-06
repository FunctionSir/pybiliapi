# pybiliapi

用API获取B站上的视频信息等等.

## 使用方法

简单粗暴地扔到你的程序文件目录, import之即可. 此模块无需使用pip获取,也无法使用pip获取.  
要想裁剪她同样简单粗暴,删掉不用的函数即可.  
把相关函数等拷贝至自己的程序也是可以的, 只要遵守许可证要求 (见LICENSE文件及README.md文件最下方的说明) .  

## 函数说明

注: aid是不包含"av"两字母的AV号, bvid是包括"BV"两字母的BV号.  
bvid(aid) AV2BV str  
aid(bvid) BV2AV int  
cid(aid) 获取cid int  
cover(aid) 获取封面URL str  
view(aid) 获取观看量 int  
video_p(aid) 分P数 int  
like(aid) 获取赞数 int  
favorite(aid) 获取收藏数 int  
danmaku(aid) 获取弹幕数 int  
coin(aid) 获取硬币数 int  
share(aid) 获取分享数 int  
reply(aid) 获取评论数 int  
up_name(aid) 获取某视频的UP的名字 str  
up_uid(aid) 获取某视频的UP的UID int  
up_face(aid) 获取某视频的UP的头像（URL) str  
xml_danmaku_url(aid) 获取XML弹幕文件的URL str  
xml_danmaku_text(aid) 获取XML弹幕文件内容 str  

## 使用样例

````python
import biliapi
biliapi.view(ba.aid('BV17x411w7KC'))
````

## 关于LGPL不同版本间及与GPL许可证之间的不兼容问题的说明

特在此说明: 若您的项目使用LGPL v3, 或LGPL v2.1及之后的任何版本, 或GPL v2及之后的任何版本, 或AGPL v3及之后的任何版本时, 您可以视为此项目的许可证为LGPL v3, 或LGPL v2.1及之后的任何版本, 或GPL v2及之后的任何版本, 或AGPL v3及之后的任何版本(与您的项目的许可证相对应).
